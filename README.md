# YouTube AI Chatbot

Production-ready AI chatbot for generating YouTube content using FastAPI and OpenAI.

## Features

- Horror stories
- Educational scripts
- YouTube Shorts scripts
- Hooks and titles
- SEO descriptions

## Setup

```bash
pip install -r backend/requirements.txt
```

Create `.env` file:

```env
OPENROUTER_API_KEY=your_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

OPENROUTER_MODEL=inclusionai/ring-2.6-1t:free

FRONTEND_URL=http://127.0.0.1:8000
```

Run app:

```bash
python run.py
```

Open frontend:

```text
frontend/index.html
```
