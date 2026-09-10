# Playbook — Community digest (in-app, no Gmail)

JLaw Inbox polls **signed-in** Circle → Kajabi → Patreon. Distill only. A post is not a buy.

---

## Allow

- Official JLaw posts, lessons, course drops, creator broadcasts
- Tickers, dates, setup vs noise, one-line idea, URL

## Never

- Full body / screenshots of paid lessons into git
- Other members’ comments, group chat, DMs
- Gmail as a substitute for the site
- Posting, liking, replying
- Passwords in chat

## Sequence

1. Read `investment/inbox/sources.md` (or `sources.example.md` if missing).
2. For each URL: if login wall → `SESSION DEAD`, next site.
3. List items newer than `investment/inbox/seen.json`.
4. For each new official item, one row:

| time_hkt | source | title | tickers | catalyst | idea | ref |
|----------|--------|-------|---------|----------|------|-----|

`catalyst`: setup / sector / earnings / ignore  

5. Append to `investment/inbox/digests/YYYY-MM-DD.md` (create from `inbox/digests/README.md` shape).
6. Add keys to `seen.json`.
7. `@JLaw Daily` with **new rows only**. Chart gate still required.

## Quality

- [ ] Three session statuses recorded  
- [ ] No full lesson paste  
- [ ] No other members  
- [ ] Daily ping has tickers or explicit `none`
