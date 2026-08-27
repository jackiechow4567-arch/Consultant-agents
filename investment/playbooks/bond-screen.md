# Playbook — Bond & fixed-income screening (Grot Bot)

Applies: personal fixed-income allocation; aligns with **FINA5120 Ch. 6** (bond pricing, YTM, rate risk).  
Sensitivity: default **Low**.

---

## Scope

Grot Bot screens **fixed-income exposure**, not individual bond picking, unless you supply CUSIPs/ISINs.

**Default approach:** liquid **ETF proxies** + duration ladder map.  
Individual corporates/munis → manual checklist below + professional confirmation for illiquid issues.

## Step 1 — Clarify fixed-income goal

| Goal | Sleeve proxies | Key risk |
|------|----------------|----------|
| **Cash / liquidity** | SHY, BIL, money-market funds | Reinvestment rate |
| **Core aggregate** | AGG, BND | Duration ~6–7y; rate sensitive |
| **Government ladder** | SHY → IEF → TLT | Curve shape / Fed path |
| **Investment grade credit** | LQD | Spread widening |
| **High yield** | HYG | Default cycle |
| **Inflation-linked** | TIP | Real yield level |

## Step 2 — Run ETF map script

```bash
python investment/scripts/bond_screen.py

# JSON output
python investment/scripts/bond_screen.py --json

# Custom symbol list
python investment/scripts/bond_screen.py --symbols TLT,IEF,SHY,AGG,LQD,HYG,TIP
```

Review: **yield**, **category**, **beta (3y)** as duration/risk proxy.

## Step 3 — FINA5120 bond checklist

For each sleeve you are considering:

| Concept | Question |
|---------|----------|
| **Price vs YTM** | If rates rise 100bp, approximate price hit (duration) |
| **Credit spread** | Is compensation vs Treasuries adequate for the risk? |
| **Liquidity** | Can you exit at tight spread in stress? (ETF ≠ underlying) |
| **Tax** | US withholding / HK local tax — flag TBD for user's wrapper |
| **Real return** | Nominal yield minus expected inflation |

**Decision rule:** match **duration to holding period**; do not reach for yield without naming the credit risk.

## Step 4 — Macro context (Low sensitivity)

Use Perplexity or public news for:

- Fed / central bank path  
- IG vs HY spread levels vs history  
- Inflation prints vs breakevens  

Keep conclusions qualitative unless you have a verified data source.

## Step 5 — Individual bond checklist (optional)

If screening a **specific bond** (user-provided):

```markdown
| Field | Value |
|-------|-------|
| Issuer | |
| Coupon / maturity | |
| Price / YTM | |
| Rating (Moody's/S&P/Fitch) | |
| Callable? | |
| Liquidity (avg daily volume) | |
| Covenants / secured? | |
```

**Red flags:** rating on negative watch, PIK toggles, covenant-lite without spread premium, concentrated sector (e.g. single EM country).

## Output template

```markdown
# Bond / FI screen — <date>

## Objective
- Horizon:
- Rate view: (higher / lower / neutral)
- Credit appetite: (gov only / IG / HY)

## Sleeve map
| Symbol | Category | Yield | Beta(3y) | Role | Notes |
|--------|----------|-------|----------|------|-------|

## Recommended allocation sketch (illustrative %)
- Short gov:
- Core agg:
- Credit / other:

## Risks to monitor
1.
2.

## Disclaimer
Research support only — not investment, tax, or legal advice.
```

## Handoff

For **issuer-level** work on a corporate bond finalist → `finance-accounting-consultant` with ACCT5100 statement read on the issuer's equity (if listed).
