# Skill — Daily JLaw screen

Save in Grok Bot as **Daily JLaw screen**.

```text
When to use: weekday idea generation and the first half of the morning brief.

Required inputs:
- investment/knowledge/jlaw-operating-system.md
- investment/playbooks/stock-screen.md
- Prefer TradingView logged-in screen when a session exists
  (see skills/tradingview-logged-in-screen.md).
- Fallback: python investment/scripts/daily_brief.py

Sequence:
1. State tape regime first (easy / grind / late-stage caution). If grind, keep the list tiny.
2. If TradingView is signed in: load saved screener "JLaw Stage 2" and
   open charts on "JLaw Daily". That is the accurate path.
3. Else run: python investment/scripts/daily_brief.py --limit 25 --markdown
   and label DEGRADED. On script failure, say the feed degraded.
4. Rank sectors by how many leaders printed and by 1-month performance. Prefer names in the strongest groups.
5. Drop cheap names, thin names, and laggards. Drop anything that would require chasing >5% above a breakout (chart pivot, not only 52-week high).
6. Keep ≤10 names in the actionable table. Put extras in an appendix.
7. Do not invent OHLC. If you did not pull a number, write TBD.

Validate:
- Hard filters visible: US primary listing, liquid, >$2B, above 200-day, quality 50/200 stacked.
- Each row has % from 52-week high and a one-line thesis hook.
- No buy order language.

Return: markdown matching investment/playbooks/daily-brief.md (screening sections only).

Approval: none for research. Any broker action is blocked.
```
