# Playbook — Portfolio / watchlist review (Grot Bot)

Monthly or post-screen review. Combines equity and fixed-income sleeves.

---

## Input template

```markdown
## Meta
- Date:
- Review type: watchlist only / live positions
- Sensitivity: Low / Mid / High
- Benchmark: (e.g. SPY + AGG blend)

## Holdings or watchlist
| Ticker | Sleeve | Weight % | Entry thesis (1 line) | Still valid? |
|--------|--------|----------|----------------------|--------------|

## Constraints
- Max single-name %:
- Cash target %:
- Sectors to avoid:
```

## Review steps

1. **Re-run screens** — equities: `jlaw_stage2_screen.py`; bonds: `bond_screen_ib.py` (or `bond_screen.py` if TWS offline) if >30 days stale  
2. **Thesis audit** — mark each line Valid / Weakened / Invalid  
3. **Risk dashboard** — beta blend, sector/factor concentration, FI duration bucket  
4. **ACCT5100 pass** — any new red flags on held names?  
5. **Actions** — add / trim / hold / research further (user decides execution)

## Output sections

```markdown
## Executive summary (3 bullets)

## Sleeve health
| Sleeve | Target % | Actual % | Drift | Action |
|--------|----------|----------|-------|--------|

## Names to drop from watchlist
-

## Names for FA deep dive
-

## Macro / rates note (1 paragraph)
```
