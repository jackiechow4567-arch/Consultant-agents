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
