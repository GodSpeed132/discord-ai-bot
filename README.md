# AI Discord Chat Bot

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python\&logoColor=white)
![Discord.py](https://img.shields.io/badge/Discord.py-2.x-5865F2?logo=discord\&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite\&logoColor=white)

An AI-powered Discord bot built with **discord.py** that integrates Google's **Gemini API** to answer user questions while storing conversation history in SQLite. Users can review or clear their previous conversations through Discord commands.

---

# Features

* Chat with Google's Gemini AI directly from Discord
* Store conversation history in SQLite
* View your five most recent conversations
* Clear your conversation history
* Per-user conversation storage
* Modular bot architecture using Discord Cogs
* Environment variable configuration using `python-dotenv`

---

# Commands

| Command            | Description                                 |
| ------------------ | ------------------------------------------- |
| `!chat <question>` | Ask Gemini a question                       |
| `!history`         | Display your five most recent conversations |
| `!clear_history`   | Delete your stored conversation history     |

---

# Architecture

```text
              User
                │
                ▼
      Discord Message (!chat)
                │
                ▼
        discord.py Command
                │
                ▼
        Google Gemini API
                │
                ▼
        Generate Response
                │
        ┌───────┴────────┐
        ▼                ▼
 Save Question      Send Reply
 & Answer to DB      to Discord
        │
        ▼
      SQLite
```

---

# Tech Stack

## Backend

* Python
* discord.py

## AI

* Google Gemini API

## Database

* SQLite

## Other

* python-dotenv

---

# Project Structure

```text
.
├── bot.py
├── cogs/
│   └── convo.py
├── discdb.db
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

# Database

The bot stores conversation history in SQLite.

| Column     | Description     |
| ---------- | --------------- |
| `id`       | Primary Key     |
| `user_id`  | Discord User ID |
| `question` | User prompt     |
| `answer`   | Gemini response |

---

# Running Locally

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/discord-ai-bot.git

cd discord-ai-bot
```

---

## Create a virtual environment

```bash
python -m venv .venv
```

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

---

## Install dependencies

### Using uv (Recommended)

```bash
uv sync
```

### Using pip

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
DISCORD_TOKEN=your_discord_bot_token
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## Run the bot

```bash
python bot.py
```

---

# Example Usage

```text
User
│
├── !chat What is FastAPI?
│
▼
Gemini generates a response
│
▼
Bot replies in Discord
│
▼
Question and answer are saved to SQLite
```

---

# Design Decisions

## Discord Cogs

Commands are organized into Discord Cogs to separate command logic from the bot's startup code. This structure improves maintainability and makes it easier to add new features.

## SQLite Storage

SQLite was chosen as a lightweight database for storing conversation history. It provides persistent storage without requiring a separate database server.

## Per-User Conversation History

Each conversation is stored using the user's Discord ID, allowing every user to retrieve or delete only their own conversation history.

## Environment Variables

Sensitive information such as the Discord bot token and Gemini API key is stored using environment variables instead of being hardcoded into the application.

---

# Future Improvements

* Multi-turn conversation context
* Streaming AI responses
* Slash command support
* PostgreSQL support
* Docker support
* Unit tests
* Rate limiting
* Conversation export

---

# What I Learned

This project gave me practical experience with:

* Building Discord bots using `discord.py`
* Integrating external AI APIs
* SQLite database operations
* CRUD operations
* Environment variable management
* Organizing Python applications using Discord Cogs
* Error handling for database and API interactions
