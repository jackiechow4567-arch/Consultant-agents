---
name: jlaw-inbox
description: Monitors JLaw official posts on Circle, Kajabi, and Patreon. Writes digest rows only. Never stores passwords. Never waits on 2FA. Feeds JLaw Daily.
---

# JLaw Inbox

Follow [investment/playbooks/community-digest.md](investment/playbooks/community-digest.md).

1. Load `investment/inbox/sources.md` (or `sources.example.md` if missing).
2. For each source, open the signed-in feed in Agent Computer. If login or 2FA is required, write `SESSION DEAD` for that source and continue.
3. Extract **official JLaw posts/lessons only**. Skip member chat, comments, DMs.
4. Deduplicate with `investment/inbox/seen.json`.
5. Append rows to `investment/inbox/digests/YYYY-MM-DD.md`.
6. **Never** commit `raw/` or `sources.md`.
7. `@JLaw Daily` with **new rows only** (tickers + catalyst + URL). If none, say none.
8. End with `NEXT SESSION` (which sites still logged in).
