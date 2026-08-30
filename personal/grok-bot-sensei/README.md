# Grok Bot → Japanese teacher (Sensei)

This is **xAI Grok Bot** (`x.ai/bot`), not Cursor Cloud Agents and not **Grot Bot** (investing).

Grok Bot is the right daily tutor: it stays on your phone, keeps memory, and can post a weekday lesson. It still **cannot play audio**. Keep the [listening lab](../japanese-listening-lab/README.md) for ears.

## 4-minute setup

1. Open the **Grok Bot** app (Windows / Mac / iPhone). Sign in with Cursor if asked.
2. Sidebar → **New** (`Ctrl+N` / `Cmd+N`) → **Create new agent**.
3. **Bot actions → Edit Profile**. Paste [bot-profile.md](bot-profile.md) (Name `Sensei`, Job `Japanese teacher`, Description).
4. Send the message in [first-message.md](first-message.md).
5. If the lesson looks right, paste [skill-daily-lesson.md](skill-daily-lesson.md), then [routine.md](routine.md).
6. Optional: [skill-check-dictation.md](skill-check-dictation.md) for sentences you type from the listening lab.

Do **not** give Sensei work email, Salesforce, or IB TWS. Those stay on Grot Bot / consultant agents.

## Split of tools

| Need | Tool |
|------|------|
| Daily text lesson on the phone | **Grok Bot Sensei** |
| Fast desktop grammar drill | Cursor Desktop + `japanese-teacher` skill |
| Listening / shadowing | `japanese-listening-lab.html` |
| Live speaking | ChatGPT Advanced Voice or Gemini Live |
| Stock/bond screens | Grot Bot (`grot-bot-investor`) |

## Docs

- [Create a Bot](https://docs.x.ai/grok-bot/bots)
- [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations)
