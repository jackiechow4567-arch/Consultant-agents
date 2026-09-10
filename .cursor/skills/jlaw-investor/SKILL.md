---
name: jlaw-investor
description: >-
  Personal US-equity JLaw desk: Stage 2 screen, news/catalysts (催化劑),
  daily watchlist review, buy/sell gate. Use when the user asks for Grok Bot
  investing, stock screening, catalysts, or invokes jlaw-investor.
---

# JLaw Daily (personal investing)

This is **not** the MBA Finance consultant. Screen and risk-check public US names. Hand off 1–3 finalists to `finance-accounting-consultant` only for statement / DCF work.

1. Read and follow:
   - `investment/knowledge/jlaw-operating-system.md`
   - `investment/playbooks/daily-brief.md`
2. For screens: prefer logged-in TradingView (`investment/playbooks/tradingview-logged-in-screen.md`). Fallback: `python investment/scripts/daily_brief.py --limit 25 --markdown` and label DEGRADED.
3. For news / 催化劑: `investment/playbooks/news-catalyst.md`. Cite source + date. Tips = IGNORE. Fold in the latest `investment/inbox/digests/` file as community hints (not buys).
4. For positions: `investment/playbooks/position-review.md` and the buy/sell checklists under `investment/knowledge/`.
5. Regime first. Actionable list ≤10. Never average down. Never chase >5% above a breakout. Never place broker orders.
6. Default sensitivity **Low**. Account dumps → stop; `work-briefs/` only.
7. Output the daily-brief template. Research support only — not investment advice.
