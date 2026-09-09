# Playbook — Daily JLaw brief

Weekday operating cadence for Grok Bot **JLaw Daily** (or Cursor skill `jlaw-investor`).

Sensitivity: default **Low** (public prices and news).

---

## Cadence

| Step | Skill / script | Output |
|------|----------------|--------|
| 0 | Regime call | Easy / grind / late-stage caution |
| 1 | `daily_brief.py` or Daily JLaw screen | Leaders + sector rank |
| 2 | News & 催化劑 | Calendar + IGNORE vs USE |
| 3 | Position / watchlist review | Stops, trims, drops |
| 4 | (On demand) Buy / sell gate | PASS / FAIL / WAIT on one ticker |

Cap the **actionable** list at **10**. Everything else is appendix.

---

## Output template

```markdown
# Daily brief — <YYYY-MM-DD> (Asia/Hong_Kong)

## Disclaimer
Research support only — not investment advice. No orders placed.

## Tape
- Regime: easy / grind / late-stage caution
- Evidence: (index location vs 50/200, leadership breadth — cite source)
- Implication: screen aggressively / hibernate / raise cash language

## Sector leadership
| Sector | # leaders | 1M tape | Note |
|--------|-----------|---------|------|
| | | | |

## Actionable shortlist (≤10)
| Ticker | Sector | Close | % from 52w high | % vs 50d | 1M | Thesis hook | Catalyst (date) | Buy-zone? | Flags |
|--------|--------|-------|-----------------|----------|----|-------------|-----------------|-----------|-------|
| | | | | | | | | | |

## Catalyst calendar (next 10 sessions)
| Date | Ticker | Event | USE or IGNORE | Source |
|------|--------|-------|---------------|--------|
| | | | | |

## Watchlist / positions
| Ticker | Thesis still valid? | Stop | Action (user) |
|--------|---------------------|------|----------------|
| | | | |

## Explicitly not doing
- Averaging down:
- Chase >5% above breakout:
- Tips / cheap names:

## Next 3
1.
2.
3.
```

## Quality bar

- [ ] Regime first
- [ ] Script or TradingView cited
- [ ] ≤10 actionable names
- [ ] Each catalyst has a date + source
- [ ] Earnings inside 10 days tagged HOLD-SIZE-RISK
- [ ] Disclaimer present
