# Getting a free AI API key

A practical starting point for the current Gitagent code is [GroqCloud](https://console.groq.com/), which offers an OpenAI-compatible API and has offered a free developer tier. Create an account, generate an API key from the Groq console, then check the console for the current model name and usage limits. Free quotas and eligibility can change.

Set these environment variables in the same terminal where you run Gitagent. Replace the placeholder values with your key and a chat model currently available in your Groq console:

### macOS / Linux

```bash
export OPENAI_API_KEY="your-groq-api-key"
export OPENAI_BASE_URL="https://api.groq.com/openai/v1"
export OPENAI_MODEL="model-name-from-your-groq-console"
python gitagent.py ask "Help me plan my day"
```

### Windows PowerShell

```powershell
$env:OPENAI_API_KEY = "your-groq-api-key"
$env:OPENAI_BASE_URL = "https://api.groq.com/openai/v1"
$env:OPENAI_MODEL = "model-name-from-your-groq-console"
python gitagent.py ask "Help me plan my day"
```

The same configuration powers `summarize-call` and `reply`. Do not paste your key into GitHub, source files, screenshots, or chat. Environment variables set this way last only for the current terminal session. Treat transcripts and messages as potentially sensitive: using a hosted API sends their text to that provider. Check the provider's privacy terms and current free-tier limits before use.

Gitagent uses OpenAI-compatible Chat Completions. Other compatible providers may work by changing the base URL, key, and model, but support and free quotas vary. Google AI Studio also offers a Gemini API with a free tier in eligible regions, but its API format differs from the OpenAI-compatible endpoint currently used by Gitagent.
