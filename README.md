# Gitagent

A small, local-first productivity assistant with practical tools for organizing files, finding files, reviewing cleanup candidates, drafting replies, summarizing call transcripts, creating calendar events, and asking a configured AI model general questions.

## Quick start

Requires Python 3.10+ and has no third-party package dependencies.

```bash
python gitagent.py --help
```

AI-generated summaries, reply drafts, and general questions require an OpenAI-compatible API key. Configure it in your shell (never put secrets in source code):

```bash
export OPENAI_API_KEY="your-key"
# Optional, for compatible services:
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_MODEL="gpt-4o-mini"
```

On Windows PowerShell, use `$env:OPENAI_API_KEY="your-key"`.

## Features

### Organize a folder

Preview the proposed moves first; no files are changed by default:

```bash
python gitagent.py organize ~/Downloads
```

Apply the moves only after reviewing the preview:

```bash
python gitagent.py organize ~/Downloads --apply
```

Files are grouped by common type into Documents, Images, Audio, Video, Archives, Code, and Other. Existing names are not overwritten. This works only on files directly inside the selected folder; it does not reorganize nested folders.

### Find files by name

```bash
python gitagent.py find ~/Documents invoice
```

### Review cleanup candidates

```bash
python gitagent.py cleanup ~/Downloads
```

This only reports common temporary files and metadata files. It never deletes files. Review candidates yourself before removing anything.

### Summarize a call transcript

Save or export a transcript as a UTF-8 text file, then run:

```bash
python gitagent.py summarize-call call-transcript.txt
```

The assistant returns an overview, decisions, action items, and unresolved questions, and is instructed not to invent missing details.

### Draft a reply

```bash
python gitagent.py reply incoming-message.txt --tone "warm and concise"
```

The generated text is only a draft; Gitagent does not send messages.

### Create a calendar event

```bash
python gitagent.py calendar-add "Project check-in" \
  --start "2026-06-05T14:00:00-04:00" \
  --end "2026-06-05T14:30:00-04:00" \
  --description "Review milestones" \
  --location "Video call" \
  --output project-check-in.ics
```

Import the `.ics` file into Google Calendar, Outlook, Apple Calendar, or another compatible calendar. The tool does not connect to or modify an online calendar account.

### Ask a general question

```bash
python gitagent.py ask "Help me plan a focused workday"
```

## Safety and scope

Gitagent is a starter assistant, not an unrestricted autonomous computer controller. It does not record calls, access email or online calendars, send messages, delete files, run shell commands, or operate other applications. File organization is preview-only unless you explicitly add `--apply`; cleanup is report-only. Review AI-generated content before relying on or sharing it. Transcripts and prompts are sent to the API endpoint you configure when using AI features, so do not submit sensitive content unless you have permission and understand that provider's data practices.
