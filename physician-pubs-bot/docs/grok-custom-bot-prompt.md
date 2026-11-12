# Tier B — Grok custom bot system prompt

If you are not running the Agent SDK host, create a **custom Grok bot** and paste the prompt below. Fill bracketed sections once.

```markdown
# Identity
You are a Medical Affairs publication intelligence assistant...

(full prompt lives in the implementation plan; use bot/instructions.md in this repo as the maintained source of truth)
```

**Source of truth:** [`../bot/instructions.md`](../bot/instructions.md) — copy into Grok when it changes.

**Limitation:** Without `fetch_publications` / `scan_roster` tools, require **PMID on every row** and prefer the user pastes `scan_roster` JSON from:

```bash
npx @grok/agent-sdk tool call scan_roster --dir physician-pubs-bot --input '{"physician_ids":["YOUR_ID"]}'
```
