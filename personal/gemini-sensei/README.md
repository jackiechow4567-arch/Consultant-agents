# Gemini → Japanese teacher

Yes. For Jackie, **Gemini is the best AI teacher** of the three options:

| Tool | Text drill | Daily routine | Real listening / speaking |
|------|------------|---------------|---------------------------|
| Cursor Cloud Agent | Slow | No | No |
| xAI Grok Bot Sensei | Good on phone | Yes | No |
| **Gemini Gem + Gemini Live** | Good | Gem memory | **Yes** |

Use **personal Gemini** (gemini.google.com or the Gemini app). Do **not** put this in the six work consultant Gems, and do not upload `work-briefs/` or patient/KOL names.

## Setup (5 minutes)

Gemini **cannot see this Cursor repo**. You must upload a knowledge file into the Gem.

1. Open [Gemini Gems](https://gemini.google.com/gems/view) on your **personal** Google account.
2. **New Gem** → Name: `Sensei`.
3. Paste [gem-instructions.md](gem-instructions.md) into **Instructions**.
4. Under **Knowledge**, upload [knowledge-listening-lab.md](knowledge-listening-lab.md) (the 36 clips from the Cursor listening lab). Rebuild it anytime with `python export_knowledge.py`.
5. Save. Text lesson: send the line in [first-message.md](first-message.md).
6. Voice: open **this same Gem**, then **Live**. Say you want clip `n4-03` (or today's N4 track). Live follows Gem knowledge more reliably if you start from the Gem, not from a blank Gemini chat.

Do **not** upload the hematology PDFs in this repo to the Sensei Gem. Those are work papers, not Japanese lessons.

To add more of your own textbooks later: put Low-sensitivity files in `personal/japanese-lessons/` and ask Cursor to fold them into `knowledge-listening-lab.md`.

## Privacy

Personal language practice is **Low**. Keep clinic Japanese generic. If a sentence would identify a real physician, hospital, or product, stop and switch to Cursor local.
