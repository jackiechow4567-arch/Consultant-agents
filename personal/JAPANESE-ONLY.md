# Japanese agents stay separate from work agents

Jackie: these two stacks must not share files.

| Stack | Agents | Allowed files |
|-------|--------|----------------|
| Work consulting | `consultant-router` and SM / FA / OC / PG / TG | `agents/`, `industry/`, `mba-notes/`, `gem-knowledge-pack/`, `work-briefs/` |
| Japanese teaching | `@japanese-teacher`, Gemini Gem **Sensei**, Grok Bot **Sensei**, listening lab | `personal/japanese-listening-lab/` and `personal/japanese-lessons/` only |

## Never upload to Sensei

- Root hematology / MPN PDFs
- `industry/pm-reference/` (including clinic contact xlsx)
- `gem-knowledge-pack/*-knowledge.md` (those are the six **work** Gems)
- MBA notes, investment tools, Grot Bot

## Add your own Japanese textbooks

Drop them in `personal/japanese-lessons/`, then rebuild `personal/gemini-sensei/upload-this/`.
