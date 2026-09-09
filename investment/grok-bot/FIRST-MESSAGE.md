# First message to JLaw Daily (after profile is saved)

```text
Read investment/knowledge/jlaw-operating-system.md,
investment/playbooks/daily-brief.md,
investment/playbooks/tradingview-logged-in-screen.md, and
investment/grok-bot/SETUP-TRADINGVIEW-LOGIN.md.

If TradingView is not signed in on this computer, open Agent Computer
and go to tradingview.com. If a password / 2FA / CAPTCHA appears, pause
so I can take over. Do not ask me to paste a password into chat.

When signed in, run the TradingView logged-in screen: saved screener
"JLaw Stage 2" (create it from the playbook if missing) and layout
"JLaw Daily". Open at most 8 daily charts. Score the real pivot and
the 5% chase rule. Source = TradingView account.

Only if the session cannot be used, run:
python investment/scripts/daily_brief.py --limit 25 --markdown
and label the brief DEGRADED.

Then check news and 催化劑 on the top names plus investment/watchlist.md
or templates/watchlist.example.md.

Post today's brief. Actionable list ≤10. No average-down. No broker orders.
```

When that run looks right, save skills, then paste [`AUTO.md`](AUTO.md) / [`routines/weekday-morning.md`](routines/weekday-morning.md) so screening runs **without you**. Until a Routine exists, nothing is automatic.
