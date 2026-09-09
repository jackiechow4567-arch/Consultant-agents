# Skill — TradingView logged-in screen

Save in Grok Bot as **TradingView logged-in screen**.

On a **live chat** (user present): use TradingView charts.  
On a **routine / 07:30 run**: never wait for login. Script first.

```text
When to use: enrich a Stage 2 list with the user's signed-in TradingView.

Required inputs:
- investment/playbooks/tradingview-logged-in-screen.md
- investment/knowledge/buy-checklist.md
- Saved screener "JLaw Stage 2" and layout "JLaw Daily" when session is live

Scheduled / routine sequence (unattended):
1. ALWAYS run python investment/scripts/daily_brief.py --limit 25 --markdown
   first. This is the automatic screen.
2. Open tradingview.com. If already signed in, load "JLaw Stage 2",
   open up to 8 charts on "JLaw Daily", score the real pivot / 5% rule,
   sync "JLaw Watch" (≤12). Label source TradingView+.
3. If login, 2FA, or CAPTCHA: do not pause, do not type secrets.
   Post the script brief. Label automatic (no TV session).
   One line: TV session expired — take over when convenient.
4. Never block the weekday post on a human. No orders.

Live chat sequence (user is here):
1. If login wall, ask them to take over (no passwords in chat).
2. Then screener + charts as in the playbook.

Validate: no invented OHLC; ≤10 actionable names; no average-down.
```
