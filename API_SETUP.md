# Groq API setup

Gitagent calls Groq's OpenAI-compatible Chat Completions API at `https://api.groq.com/openai/v1/chat/completions` when `GROQ_API_KEY` is set. Create a key in the [Groq Console](https://console.groq.com/keys). Check [Groq's current model list](https://console.groq.com/docs/models) and your console for models available to your account and their usage limits. Free-tier eligibility and quotas may change.

The current default model in Gitagent is `llama-3.3-70b-versatile`, matching the example in the supplied Groq API reference. Override it with `GROQ_MODEL` if Groq's model list or your account requires another model.

## macOS / Linux

```bash
export GROQ_API_KEY="your-groq-api-key"
export GROQ_MODEL="llama-3.3-70b-versatile"
python gitagent.py ask "Explain the importance of fast language models"
```

## Windows PowerShell

```powershell
$env:GROQ_API_KEY = "your-groq-api-key"
$env:GROQ_MODEL = "llama-3.3-70b-versatile"
python gitagent.py ask "Explain the importance of fast language models"
```

The same settings are used by `summarize-call` and `reply`. Do not paste the key into source code, GitHub, screenshots, or chat. These shell environment variables are temporary and last only for the current terminal session. Hosted API requests send prompt/transcript text to Groq; avoid submitting sensitive content unless you have permission and have reviewed the provider's data practices.

Gitagent also retains support for other OpenAI-compatible providers: set `OPENAI_API_KEY`, and optionally `OPENAI_BASE_URL` and `OPENAI_MODEL`. For Groq, `GROQ_BASE_URL` can override the default endpoint; otherwise Gitagent uses the official Groq base URL. `GROQ_MODEL` takes precedence over `OPENAI_MODEL` when `GROQ_API_KEY` is set.
