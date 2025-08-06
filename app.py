import os
import requests
from flask import Flask, request
from datetime import datetime
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

bot_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Expenses Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" not in data:
        return "ok"

    message = data["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text", "").lower().strip()

    if text.startswith("expense"):
        try:
            parts = text.split(maxsplit=2)
            if len(parts) < 3:
                raise ValueError("Invalid format")
            _, amount_str, category = parts
            amount = float(amount_str)

            supabase.table("expenses").insert({
                "type": "expense",
                "amount": amount,
                "category": category,
                "date": datetime.now().isoformat(),
                "user_id": str(chat_id),
            }).execute()

            send_message(chat_id, f"💸 Expense of ${amount:.2f} for '{category}' recorded.")
        except Exception as e:
            print(f"❌ Error inserting expense: {e}")
            send_message(chat_id, "⚠️ Use format: expense 25 groceries")

    elif text.startswith("total"):
        try:
            result = supabase.table("expenses") \
                .select("amount") \
                .eq("user_id", str(chat_id)) \
                .eq("type", "expense") \
                .execute()

            total = sum(item["amount"] for item in result.data)
            send_message(chat_id, f"📊 Total expenses: ${total:.2f}")
        except Exception as e:
            print(f"❌ Error fetching total: {e}")
            send_message(chat_id, "⚠️ Could not retrieve total.")
    else:
        send_message(chat_id,
            "💬 Available commands:\n• expense 25 groceries\n• total"
        )

    return "ok"

def send_message(chat_id, text):
    url = f"{bot_url}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    import sys
    port = int(os.environ.get("PORT", 5000))
    print(f"Running on port: {port}", file=sys.stderr)
    app.run(host="0.0.0.0", port=port)
