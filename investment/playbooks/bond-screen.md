# Playbook — Bond & fixed-income screening (Grot Bot)

Applies: personal fixed-income allocation; aligns with **FINA5120 Ch. 6** (bond pricing, YTM, rate risk).  
**Primary data source:** **Interactive Brokers TWS** (Bond Scanner API).  
Sensitivity: default **Low** for public bond descriptors; **High** for account positions.

---

## Prerequisites

1. **TWS or IB Gateway** running locally with API enabled  
2. Python deps installed: `pip install -r investment/scripts/requirements-tradingview.txt`  
3. One-time setup: [`SETUP-IB-TWS.md`](../SETUP-IB-TWS.md)

---

## Scope

Grot Bot screens **individual bonds** (corporate, government, municipal, agency) via IB — the same universes as the TWS **Bond Scanner**.

| Mode | Tool | When |
|------|------|------|
| **Primary** | `bond_screen_ib.py` | TWS running — individual bonds |
| **CUSIP lookup** | `bond_screen_ib.py --cusip` | Verify a specific issue |
| **Offline fallback** | `bond_screen.py` | TWS not available — ETF sleeve map only |

---

## Step 1 — Clarify fixed-income goal

| Goal | IB preset | Typical filters |
|------|-----------|-----------------|
| **IG corporate ladder** | `corp-us` | S&P BBB–AAA; maturity window |
| **US Treasuries / gov** | `govt-us` | Maturity near-to-far |
| **Municipal (tax-aware)** | `muni-us` | Rating + maturity; flag tax advice TBD |
| **Agency** | `agency-us` | Maturity sort |
| **FI ETF sleeve (TWS)** | `fi-etf-us` | Advanced scanner — liquid ETF proxies |

Ask the user: horizon, credit appetite (gov / IG / HY), currency, and whether they need **individual bonds** or **ETF sleeves**.

## Step 2 — Run IB TWS screen

```bash
# Corporate IG (default preset in bond-screens.yaml)
python investment/scripts/bond_screen_ib.py --preset corp-us

# Government / Treasury universe
python investment/scripts/bond_screen_ib.py --preset govt-us

# Maturity window + JSON for agent parsing
python investment/scripts/bond_screen_ib.py --preset corp-us \
  --maturity-above 202801 \
  --maturity-below 203512 \
  --sp-rating-above BBB \
  --sp-rating-below AAA \
  --json

# Single bond by CUSIP
python investment/scripts/bond_screen_ib.py --cusip 459200KZ3 --json

# First-time: dump scanner codes for your TWS version
python investment/scripts/bond_screen_ib.py --dump-scanner-params
```

**Review fields:** CUSIP, maturity, coupon, currency, exchange.  
For **live bid/ask/yield**, open the contract in TWS or extend the script with `reqMktData` snapshots (requires bond data subscriptions).

### Preset reference

Configured in [`config/bond-screens.yaml`](../config/bond-screens.yaml).  
Adjust `location_code`, `scan_code`, and default ratings there after running `--dump-scanner-params`.

## Step 3 — FINA5120 bond checklist

For each finalist:

| Concept | Question |
|---------|----------|
| **Price vs YTM** | At quoted price, is YTM adequate vs your hurdle? Duration if rates +100bp? |
| **Credit spread** | Spread vs comparable Treasury — compensation for issuer risk? |
| **Liquidity** | Size, issue amount, typical IB availability — can you exit? |
| **Callable / structure** | Yield-to-worst vs yield-to-maturity; call dates |
| **Tax** | US withholding / HK local — flag TBD for user's wrapper |
| **Real return** | Nominal yield minus expected inflation |

**Decision rule:** match **duration to holding period**; do not reach for yield without naming credit risk.

## Step 4 — ACCT5100 issuer pass (corporates)

If the issuer has listed equity:

| Flag | Question |
|------|----------|
| Leverage | Net debt / EBITDA rising? |
| Coverage | Interest coverage tightening? |
| Governance | Restatement, auditor change? |
| Cash flow | OCF vs net income divergence? |

Downgrade or drop names with multiple unresolved flags.

## Step 5 — Macro context (Low sensitivity)

Use Perplexity or public news for Fed path, IG/HY spread levels, inflation.  
Keep qualitative unless sourced.

## Step 6 — Offline ETF fallback (optional)

When TWS is not running:

```bash
python investment/scripts/bond_screen.py --fallback-etf
# or explicitly:
python investment/scripts/bond_screen_ib.py --preset corp-us --fallback-etf
```

Use for **sleeve mapping only** — not individual bond selection.

## Output template

```markdown
# Bond / FI screen — <date>

## Source
- IB TWS preset: corp-us / govt-us / …
- Filters: maturity, rating, coupon
- TWS port: 7497 paper / 7496 live

## Objective
- Horizon:
- Rate view:
- Credit appetite:

## Shortlist (≤10)
| Rank | CUSIP | Issuer | Maturity | Coupon | YTM/YTW | Thesis | Flags |
|------|-------|--------|----------|--------|---------|--------|-------|

## Sleeve / ladder sketch
- 

## Risks to monitor
1.
2.

## Disclaimer
Research support only — not investment, tax, or legal advice.
```

## Handoff

Corporate finalists → `finance-accounting-consultant` with ACCT5100 read on the issuer (if listed).

## Troubleshooting

See [`SETUP-IB-TWS.md`](../SETUP-IB-TWS.md).
