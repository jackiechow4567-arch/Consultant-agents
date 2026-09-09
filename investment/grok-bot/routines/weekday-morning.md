# Routine — weekday morning brief (Hong Kong)

This is the **automatic** job. Paste it only after one manual screen has looked right.

**Rule:** weekday runs never wait for you. TradingView is extra, not a gate.

```text
Create a routine. Do not wait for me on weekday runs.

Every weekday at 07:30 Asia/Hong_Kong:
1) ALWAYS run: python investment/scripts/daily_brief.py --limit 25 --markdown
   This is the automatic screen. It must finish even if I am asleep.
2) If TradingView is already signed in (no login wall), ALSO load
   saved screener "JLaw Stage 2", open up to 8 charts on "JLaw Daily",
   and sync watchlist "JLaw Watch" (≤12). Label source: TradingView+.
3) If TradingView shows login, 2FA, or CAPTCHA: do NOT pause and do
   NOT type passwords. Skip TV. Label source: automatic (no TV session).
   Add one line: TV session expired — take over when convenient.
4) News & 催化劑 on the shortlist. Post one brief in this conversation,
   ≤10 names. Never place trades. Never touch other watchlists.

If the Python scanner fails, say SCANNER FAILED in the thread.
Do not reuse yesterday’s prices.
```

Then: **View conversation details** → **Routines** → **Test run** → **Enable**.  
Timezone: Settings → General → Agent → **Asia/Hong_Kong**.  
Turn on notifications for this Bot.

Owner: JLaw Daily  
Missing data: post failure, do not block  
Approval: draft only — no orders
