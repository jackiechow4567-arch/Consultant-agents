# Playbook — Equity screening (Grot Bot)

Applies: personal US equity watchlists; aligns with **FINA5120** (risk-return) and **JLaw Stage 2** trend filters.  
Sensitivity: default **Low** (public market data).

---

## When to use

- Weekly / monthly **idea generation**
- **Stage 2** uptrend candidates (not bottom-fishing)
- Pre-filter before fundamental work with `finance-accounting-consultant`

## Step 1 — Clarify sleeve

| Sleeve | Typical profile | Screen bias |
|--------|-----------------|-------------|
| **Growth / momentum** | 3–10y horizon; tolerates volatility | JLaw Stage 2 default (beta ≥ 1) |
| **Quality compounder** | Large cap, steady margins | Stage 2 + tighten near-high (≥85% of 52w high) |
| **Defensive** | Lower beta, dividends | Relax beta; add dividend yield filter via TradingView MCP |
| **Spec / watch only** | Small cap, event-driven | Separate list — do **not** mix with core Stage 2 output |

## Step 2 — Run quant screen

```bash
# Default Stage 2 (quality filters on)
python investment/scripts/jlaw_stage2_screen.py --limit 40

# Hard filters only (wider net)
python investment/scripts/jlaw_stage2_screen.py --hard-only --limit 60

# JSON for agent parsing
python investment/scripts/jlaw_stage2_screen.py --limit 30 --json
```

**Hard filters (built into script):**

- Primary listing; type = stock; NYSE / NASDAQ / AMEX  
- Close > SMA200; market cap > $2B  
- Value.Traded > ~$30M; beta (1y) ≥ 1.0  

**Quality filters (default on):**

- Close > SMA50 > SMA200  
- Close ≥ 75% of 52-week high **and** ≥ 130% of 52-week low  

## Step 3 — TradingView MCP (optional enrichment)

Ask the agent to pull via MCP:

- Sector / industry breakdown of shortlist  
- Relative volume, recent performance vs SPX  
- Key levels (support / resistance) for entry discipline  

## Step 4 — Fundamental red-flag pass (ACCT5100)

For each finalist, check (public sources only):

| Flag | Question |
|------|----------|
| Earnings quality | Large gap between net income and operating cash flow? |
| Leverage | Net debt / EBITDA trending up without clear reinvestment story? |
| Governance | Auditor change, restatement, related-party spikes? |
| Revenue recognition | Bill-and-hold, channel stuffing signals in MD&A? |

**Kill or downgrade** names with multiple unresolved flags.

## Step 5 — FINA5120 framing (before buying)

| Check | Action |
|-------|--------|
| Required return | Implied growth vs your hurdle (CAPM sanity) |
| Downside | What breaks the thesis (rates, regulation, competition)? |
| Position size | Risk budget — single name % cap |
| Correlation | Not 5 names in the same factor bucket |

## Output template

```markdown
# Equity screen — <date>

## Parameters
- Sleeve:
- Script: jlaw_stage2_screen.py (--flags)
- Universe:

## Shortlist (≤10)
| Ticker | Sector | 1M perf | % from 52w high | Beta | Thesis hook | Flags |
|--------|--------|---------|-----------------|------|-------------|-------|

## Excluded (notable)
- 

## Next
- [ ] FA deep dive on:
- [ ] Set alerts / levels:
```

## Quality checklist

- [ ] Sleeve stated  
- [ ] Script or MCP source cited  
- [ ] ≤10 names on shortlist  
- [ ] ACCT5100 pass documented  
- [ ] Disclaimer present  
