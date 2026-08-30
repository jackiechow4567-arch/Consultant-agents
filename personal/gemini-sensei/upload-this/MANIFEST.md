# Gemini Sensei upload pack

Upload every `*.md` in this folder to the **personal** Sensei Gem → Knowledge.
Do not upload the excluded files below.

## Included

- `knowledge-listening-lab.md`
- `knowledge-clinic-public-jp.md`
- `gem-instructions.md`

## Excluded (still in the repo, not for personal Gemini)

- **Root hematology PDFs (published papers)** — Work library, not Japanese lessons. Use work Gem 04 + Gemini Enterprise if needed — not personal Sensei.

- **industry/pm-reference/BESREMi_Clinic_Contact_Report_Jackie.xlsx** — High. Real clinic contacts. Never upload to Gemini.

- **work-briefs/** — High. Local only.

## Work materials (already a Gemini pack)

MBA + industry notes are already in `gem-knowledge-pack/*-knowledge.md`.
Those go to the six **work** Gems, not Sensei.

## Add more Japanese files later

Put Low-sensitivity textbooks in `personal/japanese-lessons/`, then run:

```
python pack_for_gemini.py
```
