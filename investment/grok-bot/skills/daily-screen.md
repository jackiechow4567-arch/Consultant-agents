# Skill — Daily JLaw screen

Save in Grok Bot as **Daily JLaw screen**.

```text
When to use: weekday idea generation and the first half of the morning brief.

Required inputs:
- investment/knowledge/jlaw-operating-system.md
- investment/playbooks/stock-screen.md
- ability to run python investment/scripts/daily_brief.py
  (fallback: jlaw_stage2_screen.py or TradingView browser)

Sequence:
1. State tape regime first (easy / grind / late-stage caution). If grind, keep the list tiny.
2. Run: python investment/scripts/daily_brief.py --limit 25 --markdown
   On failure, run jlaw_stage2_screen.py --limit 40 and say the feed degraded.
3. Rank sectors by how many leaders printed and by 1-month performance. Prefer names in the strongest groups.
4. Drop cheap names, thin names, and laggards. Drop anything that would require chasing >5% above a breakout.
5. Keep ≤10 names in the actionable table. Put extras in an appendix.
6. Do not invent OHLC. If you did not pull a number, write TBD.

Validate:
- Hard filters visible: US primary listing, liquid, >$2B, above 200-day, quality 50/200 stacked.
- Each row has % from 52-week high and a one-line thesis hook.
- No buy order language.

Return: markdown matching investment/playbooks/daily-brief.md (screening sections only).

Approval: none for research. Any broker action is blocked.
```
