# Gem 02 — Finance & Accounting Knowledge Pack

> Generated 2026-07-28 12:02 for Gemini Gem Knowledge upload.
> Rebuilt: 2026-07-28 12:02 · Run `python build.py` after vault or gm-reference updates.
> Paste the matching system instruction from `gem-system-prompts.md`.

Use with Gem 02 Finance & Accounting.

---

## Source: FINA5120 Corporate Finance

# FINA5120 — Corporate Finance cheat sheet

> HKUST Spring 2026 · Prof. Ekkachai Saenyasiri, CFA · Berk & DeMarzo *Corporate Finance* (6e)  
> Distilled for Finance & Accounting agent (`02`) · Companion: [ACCT5100](../ACCT5100/) (statements) when available

---

## Course spine

**Primary goal of corporate finance:** maximize shareholder value via good **investment (capital budgeting)** and **financing** decisions.

**Core pipeline for any project:**

1. Estimate **incremental** cash flows  
2. Choose / estimate **discount rate** (opportunity cost of capital)  
3. Compute **NPV** (and cross-check IRR / PI / payback)  
4. Decide: **follow NPV** when rules conflict

---

## When to use what (agent quick map)

| Question | Tool |
|----------|------|
| Should we invest in this project / PSP expansion / launch spend? | **NPV** first; state r and CF assumptions |
| How attractive is the rate of return? | **IRR** (vs cost of capital) — watch size & reinvestment pitfalls |
| Capital rationing / rank projects under budget? | **Profitability index (PI)** |
| Rough liquidity / risk screen? | **Payback** (secondary only) |
| What cash flows belong in the model? | **Incremental CF** test; ignore **sunk**; include **opportunity cost**, **externalities**, **ΔNWC**, **taxes** |
| How to build project CFs? | **Unlevered FCFF** = EBIT(1−t) + Dep − CapEx − ΔNWC |
| What is the stock / enterprise worth? | **DDM / Gordon** or **FCFF → EV → equity** |
| What return do investors require? | **Risk premium**, diversification, **CAPM / beta** → cost of equity |
| Firm-wide discount rate? | **WACC** (Ch. 12 — see below; no separate Ch.12 PDF in course folder) |
| Bond / fixed income side? | Bond pricing, YTM, interest-rate risk (Ch. 6) |

---

## Time value of money (Ch. 3–5)

- **PV / FV** of single sums and streams; **annuities** and **growing annuities**  
- Match **rate** to **period** (monthly vs annual)  
- **EAR vs APR:** convert when compounding frequency differs  
- Law of one price / no-arbitrage intuition (Ch. 1, 3): same cash flows → same value  

---

## Investment decision rules (Ch. 7)

| Rule | Decision | Caveats |
|------|----------|---------|
| **NPV** | Accept if NPV > 0 | **Course default** — size & timing handled correctly |
| **IRR** | Accept if IRR > cost of capital | Misleading for **scale**, **timing**, **nonconventional CFs**, **mutually exclusive** projects; assumes reinvestment at IRR |
| **Payback** | Accept if recovers within cutoff | Ignores TVM and CFs after cutoff — use as screen only |
| **Profitability index** | PI = PV(inflows)/PV(outflows) or NPV/investment | Useful under **capital rationing** |

**Practice note (Graham & Harvey):** NPV and IRR most used; payback still common; PI less so.  
**Class rule:** when NPV and IRR conflict → **follow NPV**.

---

## Cash flow estimation (Ch. 8)

**Only incremental CFs** — “Will this CF occur ONLY if we accept the project?”

| Include | Exclude / careful |
|---------|-------------------|
| Opportunity cost of assets used | **Sunk costs** (past consultant fees, etc.) |
| Cannibalization / positive externalities | Allocated overhead that doesn’t change |
| CapEx, salvage (after-tax) | Financing side effects if using unlevered FCFF + WACC |
| ΔNWC (recover at end typically) | Interest expense in unlevered FCFF (financing in WACC) |
| After-tax operating effects | Accounting profit alone |

**Unlevered FCFF (as if no debt):**

```text
FCFF = EBIT × (1 − t) + Depreciation − CapEx − ΔNWC
```

Equivalent rearrangements with tax shield on depreciation appear in slides.  
**MACRS / tax depreciation** matters for after-tax CF timing.

---

## Bonds (Ch. 6)

- Bond price = PV of coupons + PV of face at YTM  
- Price vs YTM inverse; interest-rate risk rises with duration/maturity  
- Use for understanding **cost of debt** inputs later  

---

## Stocks & enterprise valuation (Ch. 9)

| Method | Idea |
|--------|------|
| **Constant-growth DDM (Gordon)** | P₀ = D₁ / (r − g) — requires **r > g** |
| Multi-stage DDM | High growth then terminal Gordon |
| **Total payout** | Dividends + repurchases |
| **FCFF valuation** | EV₀ = PV(FCFF) at **r_wacc**; Equity = EV − net debt |

**FCFF valuation steps:** forecast FCFF → terminal value (growing FCFF) → discount at WACC → subtract net debt → per share.

---

## Risk, return, portfolio (Ch. 10–11)

- **Risk premium** = expected return − risk-free rate (e.g. small stocks ~15% historical premium over T-bills)  
- Risk measured by **variance / SD** of returns  
- **Diversification:** idiosyncratic risk falls in a portfolio; **systematic** risk remains  
- **Beta (β):** slope of stock return vs market — β=1 average; β>1 more volatile; β<1 defensive  
- **Portfolio beta:** β_p = Σ w_i × β_i  
- **Portfolio return:** E[R_p] = Σ w_i × E[R_i]  

**CAPM (cost of equity / required return):**

```text
r_i = r_f + β_i × (E[R_m] − r_f)
```

- In equilibrium, **required return = expected return = cost of capital**  
- **Market risk premium** = E[R_m] − r_f — rises when overall market risk perceived higher  
- Unsystematic risk → **zero risk premium** (diversified away)  

**Efficient frontier intuition:** combine assets to reduce SD without giving up return; avoid dominated portfolios.

---

## Cost of capital & WACC (Ch. 12 · CLO5)

**Source note:** Syllabus lists Ch. 12 Week 4, but **no dedicated Ch. 12 lecture PDF** exists in OneDrive — only Weeks 1–3 slide PDFs. WACC **application** is in **Ch. 9 FCFF slides**; **CAPM / β** in **Ch. 10–11**. Complete WACC build follows **Berk & DeMarzo Ch. 12** + in-class coverage.

### WACC formula

```text
WACC = (E/V) × r_e  +  (D/V) × r_d × (1 − t)
```

- **V = E + D** (use **market** values where possible)  
- **r_e** = cost of equity (CAPM or DDM implied)  
- **r_d** = pretax cost of debt (typically **YTM** on existing debt / borrowing rate)  
- **(1 − t)** = tax shield on interest  

### Steps to estimate WACC

1. **Cost of equity r_e** — CAPM: r_f + β × market risk premium (β from regression or comps)  
2. **Cost of debt r_d** — bond YTM or new borrowing rate (Ch. 6)  
3. **Weights E/V, D/V** — target or current capital structure  
4. **Plug into WACC** — discount **unlevered FCFF** at WACC → **EV**  
5. **Equity value** = EV + Cash − Debt; **P₀** = Equity / shares outstanding  

### FCFF valuation with WACC (Ch. 9 slides)

```text
EV₀ = PV(FCFF₁…FCFF_n) + PV(TV)
TV_n = FCFF_{n+1} / (r_wacc − g)     ← constant g forever after year n
P₀ = (EV₀ + Cash − Debt) / shares
```

**Nike-style pattern:** forecast sales growth → EBIT margin → FCFF = EBIT(1−t) + Dep − CapEx − ΔNWC; when CapEx = Dep they net to zero.

### Project vs firm WACC

| Situation | Discount rate |
|-----------|---------------|
| Average-risk project, same business | **Firm WACC** |
| Different business / geography / leverage | **Project-specific r** — match β to comparables or adjust for risk |
| ROIC > WACC | Value creation; ROIC < WACC → destroys value |

**Consistency rule:** unlevered FCFF + WACC **or** levered FCF to equity + r_e — never mix.

---

## Financial statements bridge (Ch. 2)

Statements feed CapEx, NWC, EBIT, tax — link to ACCT5100 for deep statement reading.  
For capital budgeting, convert accounting items into **cash** correctly.

---

## Agent output discipline

- Always state **currency, horizon, r, tax rate, and key CF assumptions**  
- Mark **TBD** rather than inventing precision  
- High-sensitivity subsidiary numbers → ranges / indices only outside Cursor  
- Recommendation: **Accept / Reject / Re-estimate** with NPV sensitivity to r  

---

## Source map (OneDrive)

`...\Spring 2026\FINA5120 Corporate Finance\` — Lecture Slides **Weeks 1–3 only** (no Week 4 / Ch. 12 PDF uploaded), L5 bi-weekly syllabus, P&G Whitestrips case, Berk–DeMarzo solutions. **Ch. 12 WACC:** textbook + Ch. 9 FCFF + Ch. 10–11 CAPM slides.


---

## Source: ACCT5100 Corporate Reporting

# ACCT5100 — Corporate Reporting cheat sheet

> HKUST Fall 2025 · Prof. Charles Hsu · Distilled for Finance & Accounting agent (`02`)  
> Companion: [FINA5120](../FINA5120/cheat-sheet.md) (NPV / FCFF) · Educated **user** of statements, not bookkeeper

---

## Course spine

Become an **educated user** of financial accounting: infer economics from statements, adjust for comparability, assess health/performance, spot fraud/governance red flags, and understand basic **ESG** reporting.

**Three roles of financial accounting:** decision-making (value) · contracting (debt covenants, comp) · stewardship.

**Why earnings matter:** Markets react to earnings; for growth firms, missing EPS by ~1¢ can move price sharply → **earnings management incentives**.

---

## When to use what (agent quick map)

| Question | Tool |
|----------|------|
| What happened economically this period? | **IS + BS + SCF** together |
| Is the firm liquid / going concern risk? | **CFO**, working capital, SCF quality |
| How profitable vs peers? | **ROA / ROE**, common-size IS |
| Why is ROE high/low? | **DuPont** decomposition |
| Are peers comparable? | Adjust **inventory (FIFO/LIFO)**, leases, impairment, IFRS vs US GAAP |
| Are receivables / inventory healthy? | Turnover + days outstanding |
| Is PPE aggressive? | Useful life, impairment, revaluation (IFRS) |
| Hidden leverage / risk? | Contingent liabilities, provisions, leases, pension |
| When is revenue real? | **IFRS 15 / ASC 606** 5-step |
| ESG / climate claims? | Scopes, standards, green financing — separate from GAAP P&L |

---

## Four primary statements (Week 1)

| Statement | Purpose |
|-----------|---------|
| **Balance sheet** | Assets = Liabilities + Equity at a point in time |
| **Income statement** | Accrual performance over a period |
| **Statement of cash flows** | Cash sources/uses — O / I / F |
| **Statement of changes in equity** | Links NI, OCI, dividends, capital |

**Common-size:** IS items ÷ net sales; BS items ÷ total assets — peer comparison.

**Bridge to cash:** Compare operating income (IS) with **CFO** (SCF). Large non-operating cash items — rank by absolute size.

---

## Accounting mechanics (Week 2)

- **Accrual** basis; **matching** principle  
- **Prepaid** ≠ expense until consumed  
- Expense vs **capitalize** decision drives future depreciation/amortization  
- Non-monetary PPE: often **historical cost** (US GAAP); IFRS may allow **fair value / revaluation**  
- Contra-assets (e.g. accumulated depreciation, allowance for doubtful accounts)

---

## Cash flow statement & analysis (Week 3)

**Sections:** Operating · Investing · Financing  

| Method | Idea |
|--------|------|
| **Indirect CFO** | Start NI → + non-cash expenses → ± WC changes (US common) |
| **Direct** | Cash receipts − cash payments (rare in US) |

**IFRS flexibility:** Interest/dividends received or paid may classify O vs I/F differently than US GAAP — **adjust for comparability**.

**DuPont (ROE drivers)** — from course cheat notes:

```text
ROE ≈ Leverage × Asset turnover × Operating margin × Interest efficiency
```

(Exact factor labels vary by teaching version — interpret as: how much debt, how much sales per asset, how much profit per sales, cost of debt.)

Also compute **ROA** (as %). High leverage amplifies ROE but raises financial risk.

---

## Current assets (Week 4)

| Topic | Manager takeaway |
|-------|------------------|
| A/R + allowance | Bad-debt expense / impairment of receivables |
| Inventory cost flow | **FIFO vs LIFO** — LIFO often ↑COGS ↓tax in inflation (US); **IFRS bans LIFO**; US may disclose **LIFO reserve** |
| LCM / impairment | Write-downs |
| Turnover | High inventory turnover ≈ efficiency; also compute **days inventory** |

Earnings management: LIFO layers can be used to manage COGS when prices change.

---

## Non-current assets (Week 5)

- **PPE:** depreciation methods (course focus: straight-line); revise estimates  
- **Impairment:** US GAAP — once impaired, **no reversal** (except limited cases); IFRS — **can reverse** (not goodwill)  
- **Revaluation:** IFRS can revalue PPE/intangibles; not US GAAP  
- **Intangibles / goodwill:** goodwill not amortized — **impairment test**  
- **Disposal:** gain/loss hits IS; check SCF investing  

---

## Liabilities (Week 6)

- Current vs long-term; **bonds** at premium/discount; retirement / buyback  
- **Contingent liabilities / provisions** — disclosure vs recognition  
- **Leases**, pensions — leverage and risk analysis  
- Interest-bearing debt ≈ financial leverage input  
- Green financing / carbon topics linked to ESG  

---

## Revenue, financial assets, ESG (Week 7)

### Revenue — IFRS 15 / ASC 606 (5 steps)

1. Identify contract  
2. Identify performance obligations  
3. Determine transaction price  
4. Allocate price to obligations  
5. Recognize when obligation satisfied (**control** transfers)

Control indicators: right to payment, legal title, physical possession, risks/rewards, acceptance.

### Financial assets (simplified)

| Category | Measurement |
|----------|--------------|
| Trading | **FVTPL** (P&L) |
| Non-trading equity (IFRS) | Often **FVTOCI**; US GAAP often FVTPL for equity |
| Held-to-maturity debt | **Amortized cost** |

### ESG reporting

- Scopes, standards, regulations (~3 hours in course)  
- Link to net-zero / green financing narratives  
- Agent: separate **ESG claims** from audited financial performance; flag greenwashing risk  

---

## Fraud & governance (throughout)

Course repeatedly uses fraud cases. Agent checklist:

- Aggressive revenue timing  
- Channel stuffing / bill-and-hold without control transfer  
- Cookie-jar reserves / big baths  
- Related-party / off-balance risks  
- Tone at the top / audit committee weakness  

Not a legal conclusion — flag for **professional confirmation**.

---

## Link to FINA5120

| ACCT5100 | Feeds FINA5120 |
|----------|----------------|
| EBIT, tax, Dep, CapEx, ΔNWC | **Unlevered FCFF** |
| Interest-bearing debt | Net debt in EV → equity |
| Comparability adjustments | Peer multiples / ratios |

---

## Agent discipline

- Prefer **ranges** for High-sensitivity subsidiary numbers  
- Always note **IFRS vs US GAAP** when comparing peers  
- Mark TBD; no fake precision  
- Not tax, audit, or legal advice  

---

## Source map

`...\Fall 2025\ACCT 5100 Corprate Reporting\` — Weeks 1–7 lecture posts, syllabus, personal cheat sheet, cases (Apple, UST Bakery, Inditex/Adidas–Puma, Hershey/Deere, SHKP, BASF).


---
