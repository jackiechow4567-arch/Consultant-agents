# Routine — weekday morning brief (Hong Kong)

Paste this to **JLaw Daily** after the skills work on a one-off run.

```text
Every weekday at 07:30 Asia/Hong_Kong, run Daily JLaw screen, then News & 催化劑,
then Position / watchlist review.

Inputs:
- python investment/scripts/daily_brief.py --limit 25 --markdown
- investment/watchlist.md if it exists, else investment/templates/watchlist.example.md
- public web / X for catalysts on the shortlist and watchlist

Output: one markdown brief in this conversation, format from
investment/playbooks/daily-brief.md. Actionable table ≤10 names.

If scanner or web data is unavailable, report the failure in the thread.
Do not treat yesterday’s prices as live. Never place trades or send
external messages. Research support only.
```

After the Bot creates it: **Test run** → then enable.

Owner: JLaw Daily  
Timezone: Asia/Hong_Kong  
Approval: draft only  
Missing data: fail visibly
