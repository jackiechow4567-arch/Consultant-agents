# Skill — TradingView logged-in screen

Save in Grok Bot as **TradingView logged-in screen**. This is the **primary** daily screen when a TradingView session exists.

```text
When to use: weekday idea generation whenever TradingView is signed in
on the Agent Computer. Prefer this over daily_brief.py.

Required inputs:
- Signed-in TradingView (user completes password / 2FA via take-over;
  never ask for a password in chat)
- Saved Stock Screener named "JLaw Stage 2"
- Chart layout named "JLaw Daily"
- investment/playbooks/tradingview-logged-in-screen.md
- investment/knowledge/buy-checklist.md

Sequence:
1. Open tradingview.com. If a login wall, CAPTCHA, or 2FA appears:
   pause, ask the user to take over, then continue. Do not type secrets.
2. Open SPX or NQ on layout "JLaw Daily". State tape regime with
   evidence (price vs 50/200). If grind, keep the list tiny.
3. Open Products → Stock Screener → load "JLaw Stage 2".
   Record how many rows. If huge, also load "JLaw Near-high".
4. Cluster by sector. Prefer groups with several leaders.
5. Open at most 8 daily charts on "JLaw Daily". Score pivot tightness,
   volume dry-up, RS if an RS pane exists, and % above the ACTUAL
   breakout/pivot (fail if >5%). 52-week high is only a location hint.
6. Build ≤10 actionable rows. Source line must say
   "TradingView JLaw Stage 2 + charts".
7. If the session is expired and the user is not available, run
   python investment/scripts/daily_brief.py --limit 25 --markdown
   and label the brief DEGRADED (no TradingView account).

Validate:
- You actually opened charts for the actionable names (not scanner-only).
- No invented OHLC. No average-down. No broker orders.

Approval: none for research. Stop for login/2FA.
```
