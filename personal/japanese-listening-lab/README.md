# Japanese Listening Lab

Cursor Cloud Agents are a bad Japanese teacher: they boot slowly, answer in text, and **cannot play audio**. This folder is the listening replacement.

## Open it

Double-click `index.html` in Chrome or Edge (Windows: the file should open in the browser). Keep `lessons.js` and `audio/` next to it.

If scripts are blocked, from this folder:

```powershell
python -m http.server 8765
```

Then open `http://localhost:8765`.

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

For grammar and text correction, use Cursor **Desktop** chat with the `japanese-teacher` skill. Do not launch a Cloud Agent for that.

## Regenerate audio

Needs `edge-tts` (already used to build `audio/`):

```powershell
pip install edge-tts
python generate_audio.py
```
