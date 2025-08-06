# 💰 Telegram Expenses Bot

Um bot no Telegram para registrar e consultar gastos pessoais de forma simples, rápida e totalmente gratuita.

## 🧠 Motivação

A ideia surgiu da necessidade de registrar meus próprios gastos sem depender de planilhas ou aplicativos complicados. Busquei criar uma solução prática, com comandos simples e de fácil acesso. Cogitei usar a API do WhatsApp, mas os custos e a burocracia inviabilizaram. Por isso, optei por uma arquitetura gratuita usando o Telegram.

---

## ⚙️ Tecnologias Utilizadas

- **Python** com **Flask** – para criação da API
- **Supabase** – banco de dados em nuvem (PostgreSQL + autenticação + RLS)
- **Gunicorn** – servidor WSGI para produção
- **Railway** – plataforma de deploy gratuito
- **Telegram Bot API** – interação com o usuário

---

## 📦 Funcionalidades

### ✅ Registrar despesas
Envie uma mensagem no seguinte formato:

`` expense 25 groceries ``


O bot irá registrar a despesa de R$25,00 na categoria “groceries” associada ao seu ID de usuário do Telegram.

### 📊 Consultar total de gastos

Envie:

`` total ``

O bot irá retornar a soma total de todos os seus gastos registrados.

### 🆘 Ver comandos disponíveis
Envie qualquer outro texto ou comando desconhecido e o bot responderá com a lista de comandos disponíveis.

---

## 🔐 Segurança

A tabela `expenses` no Supabase possui políticas de RLS (Row-Level Security) que garantem que cada usuário só tenha acesso às suas próprias despesas.

---

## 🚀 Deploy

O projeto está hospedado na **Railway**, com Webhook ativado no Telegram apontando para:

`` https://<seu-subdominio>.up.railway.app/webhook ``


O deploy está automatizado com uso de `Procfile` e variáveis de ambiente via `.env`.

---

## 📁 Estrutura do Projeto


## expenses-bot/
### │
### ├── app.py # Código principal com a lógica do bot e rotas Flask
### ├── Procfile # Define o comando de execução no Railway
### ├── requirements.txt # Dependências do projeto
### ├── .env # Variáveis de ambiente (não subir no Git!)
### └── README.md # Este arquivo ``


---

## 📎 Comandos úteis

### Ativar Webhook no Telegram:
 
 `` https://api.telegram.org/bot<SEU_TOKEN>/setWebhook? ``
 `` url=https://<SEU_SUBDOMINIO>.up.railway.app/webhook ``

---

## 🧪 Exemplos

**Registro:**


**Consulta:**
 total
→ 📊 Total expenses: $45.00


---

## 🧩 Contribuições

Sinta-se à vontade para clonar, adaptar ou propor melhorias ao projeto. Feedbacks são sempre bem-vindos!

---

## 🔗 Repositório

[🔗 GitHub - Clique aqui para acessar o código](https://github.com/VinyProgramador/expenses_bot)

---

## 👨‍💻 Autor

Desenvolvido por [VinyProgramador] – focado em soluções práticas, acessíveis e de aprendizado contínuo.





