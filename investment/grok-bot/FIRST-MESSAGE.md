# First message to JLaw Daily (after profile is saved)

```text
Read investment/knowledge/jlaw-operating-system.md,
investment/playbooks/daily-brief.md, and investment/playbooks/news-catalyst.md.

Install deps if needed: pip install -r investment/scripts/requirements-tradingview.txt

Run: python investment/scripts/daily_brief.py --limit 25 --markdown
If that fails, say the scanner failed and use TradingView in the browser.
Do not reuse stale prices.

Then check news and 催化劑 on the top 8 names plus any tickers in
investment/templates/watchlist.example.md (or investment/watchlist.md if present).

Post today's brief in the daily-brief template. Actionable list ≤10.
Never average down. Never chase >5% above a breakout. No broker orders.
Research support only.
```

When that run looks right, save the four skills in `grok-bot/skills/` and create the routine in `grok-bot/routines/weekday-morning.md`.
