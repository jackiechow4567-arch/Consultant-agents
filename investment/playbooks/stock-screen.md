# Playbook — Equity screening (Stage 2)

Personal US-equity idea list. Aligns with the JLaw operating system and FINA5120 risk-return thinking. Default sensitivity **Low**.

---

## When to use

- Weekday idea generation
- Stage 2 **uptrend** candidates (not bottom-fishing)
- Pre-filter before a one-name buy gate or `finance-accounting-consultant` deep dive

## Step 1 — Sleeve (do not mix)

| Sleeve | Screen bias |
|--------|-------------|
| Growth / momentum (default) | Stage 2 + beta ≥ 1 |
| Quality compounder | Same, but demand closer to 52-week high |
| Defensive | Relax beta; do **not** mix into the growth table |
| Spec / event | Separate list only |

## Step 2 — Quant screen

```bash
python investment/scripts/daily_brief.py --limit 25 --markdown
python investment/scripts/jlaw_stage2_screen.py --limit 40
python investment/scripts/jlaw_stage2_screen.py --hard-only --limit 60 --json
```

**Hard filters (script):**

- Primary listing; stock; NYSE / NASDAQ / AMEX
- Close > SMA200; market cap > $2B
- Dollar volume proxy ≳ $30M
- Beta (1y) ≥ 1.0 (growth sleeve)

**Quality filters (default on):**

- Close > SMA50 > SMA200
- Close ≥ 75% of 52-week high **and** ≥ 130% of 52-week low
- Close ≥ $10 (reject cheap names)

**Derived flags:**

- `% from 52-week high` — leaders hug highs; still apply the **5% above breakout** chase rule on the actual pivot, not only the 52-week print
- `% vs 50-day` — >8% below 50-day is usually a pass

True pivot / pocket-pivot / RS-line checks are **chart work** on the shortlist, not scanner columns.

## Step 3 — Sector cut

Prefer names in groups that already show several leaders. Do not buy the laggard in a hot group.

## Step 4 — Chart gate (finalists only)

Open TradingView. Walk `investment/knowledge/buy-checklist.md`. One hard fail = not today.

## Step 5 — Red-flag pass (public filings)

| Flag | Question |
|------|----------|
| Earnings quality | NI vs operating cash persistently diverging? |
| Leverage | Net debt rising with no investment story? |
| Governance | Restatement, auditor change, related-party spikes? |
| Dilution | ATM / offering overhang into the breakout? |

Kill or downgrade multiple unresolved flags.

## Output

Use the shortlist table in `daily-brief.md`. Appendix is fine; the actionable table is not.
