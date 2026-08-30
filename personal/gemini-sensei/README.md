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
4. Under **Knowledge**, upload **all markdown files** in [upload-this/](upload-this/) (listening lab + generic clinic Japanese). Rebuild with `python pack_for_gemini.py`.
5. Save. Text lesson: send the line in [first-message.md](first-message.md).
6. Voice: open **this same Gem**, then **Live**. Say you want clip `n4-03` (or today's N4 track). Live follows Gem knowledge more reliably if you start from the Gem, not from a blank Gemini chat.

The repo has **no other Japanese textbooks**. The files added via GitHub upload are hematology PDFs and a clinic contact spreadsheet. Those do **not** go into personal Sensei.

| Repo upload | Gemini destination |
|-------------|--------------------|
| Listening lab + `knowledge-clinic-public-jp.md` | Personal Sensei Gem |
| `mba-notes/` + `gem-knowledge-pack/` | Six **work** Gems (already built) |
| Root `*.pdf` papers | Work Gem 04 / Gemini **Enterprise** only if you need them. Not Sensei. |
| `BESREMi_Clinic_Contact_Report_Jackie.xlsx` | **Nowhere.** High. Local only. |

To add real textbooks later: drop Low-sensitivity `.md` / `.txt` / `.pdf` into `personal/japanese-lessons/`, run `python pack_for_gemini.py`, then upload the new `upload-this/` files.

## Privacy

Personal language practice is **Low**. Keep clinic Japanese generic. If a sentence would identify a real physician, hospital, or product, stop and switch to Cursor local.
