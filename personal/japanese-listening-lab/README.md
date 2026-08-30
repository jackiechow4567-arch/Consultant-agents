# Japanese Listening Lab

Cursor Cloud Agents are a bad Japanese teacher: they boot slowly, answer in text, and **cannot play audio**. This folder is the listening replacement.

## Open it (no GitHub login needed)

**Easiest:** double-click `japanese-listening-lab.html` (single file, audio already inside). Use Chrome or Edge.

That one-file copy is built with:

```powershell
python generate_standalone.py
```

If you only have the folder: double-click `index.html` and keep `lessons.js` plus `audio/` next to it.

If scripts are blocked:

```powershell
python -m http.server 8765
```

Then open `http://localhost:8765`.

Do **not** use a `localhost` address from a Cursor Cloud Agent chat — that server is on the remote machine, not your PC.

## What is here

## What is here

36 original clips with Microsoft neural Japanese TTS (Nanami / Keita):

| Track | Use for |
|-------|---------|
| N5 daily | Greetings, time, shopping, commute |
| N4 daily | Appointments, directions, bookings |
| N3 work | Meetings, email follow-up, trips |
| Clinic / healthcare | Generic clinic Japanese (no real names or products) |

Modes: **Shadow** (script hidden) → **Dictation** → **Quiz**. Speed 0.7x–1.15x. Progress is stored in the browser only.

## Daily stack (15 minutes)

1. 8 minutes in this lab (shadow, then dictation)
2. 5 minutes **spoken** Japanese: ChatGPT Advanced Voice or Gemini Live
3. Optional: one story on [NHK News Web Easy](https://www3.nhk.or.jp/news/easy/)

For daily **phone** text lessons, use xAI Grok Bot **Sensei** — paste the profile in `personal/grok-bot-sensei/`. For desktop grammar, use Cursor **Desktop** chat with the `japanese-teacher` skill. Do not launch a Cloud Agent for tutoring.

## Regenerate audio

Needs `edge-tts` (already used to build `audio/`):

```powershell
pip install edge-tts
python generate_audio.py
```
