# JLaw community inbox (digest only)

Official JLaw posts from **Circle, Kajabi, Patreon** (in-app). Grok Bot **JLaw Inbox** polls signed-in tabs and writes rows here.

**In git:** ticker / catalyst digest only.  
**Not in git:** full lesson text, other members’ chat, passwords. Put accidental pastes in `raw/` (gitignored).

Setup: [`../grok-bot/HANDOFF-INBOX.md`](../grok-bot/HANDOFF-INBOX.md)  
Playbook: [`../playbooks/community-digest.md`](../playbooks/community-digest.md)

Copy [`sources.example.md`](sources.example.md) to `sources.md` and paste your three member URLs (`sources.md` is gitignored).

`seen.json` keys are stable IDs (source + URL or title+date). Empty `{ "version": 1, "items": {} }` is the start state.

This Cursor cloud checkout **cannot** sign into your Circle, Kajabi, or Patreon. Polling happens in the **Grok Bot** Agent Computer after you take over once.
