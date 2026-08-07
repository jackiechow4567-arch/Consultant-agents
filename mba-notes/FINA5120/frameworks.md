# FINA5120 — Frameworks reference

> Deeper structure for Finance agent. Prefer [cheat-sheet.md](cheat-sheet.md) for quick decisions.

---

## 1. Capital budgeting decision tree

```text
Define project & incremental scope
        ↓
Build unlevered FCFF timeline (incl. ΔNWC, CapEx, tax, salvage)
        ↓
Choose discount rate matched to project risk
        ↓
Compute NPV (+ IRR, PI, payback as diagnostics)
        ↓
If mutually exclusive or capital rationed → rank by NPV / PI
        ↓
Stress-test: r ±%, volume, price, delay, compliance cost
        ↓
Recommend Accept / Reject / Stage / Re-estimate
```

---

## 2. Incremental cash-flow checklist

Ask for each line item: *Occurs only if we accept?*

| Category | Treatment |
|----------|-----------|
| Sunk | Ignore |
| Opportunity cost | Include (forgone CF or market value) |
| Cannibalization | Subtract lost contribution after tax |
| Synergy / positive externality | Add incremental benefit |
| Overhead | Only the **incremental** portion |
| NWC | −ΔNWC at t; typically + recovery at end |
| Taxes | After-tax operating CF; tax on asset sale = t×(MV − book) |
| Interest / debt principal | Exclude from unlevered FCFF (in WACC) |

---

## 3. NPV vs IRR conflict resolution

| Situation | Prefer |
|-----------|--------|
| Stand-alone conventional project | NPV and IRR usually agree |
| Different scale / timing | **NPV** |
| Mutually exclusive | **NPV** (or incremental IRR carefully) |
| Capital rationing | **PI** then NPV of selected set |
| Nonconventional CF (sign changes) | Multiple IRRs → **NPV** |

**Reinvestment assumption:** IRR assumes intermediate CFs reinvested at IRR — often unrealistic → IRR may overstate.

---

## 4. Unlevered FCFF build

```text
Revenue
− Operating costs (ex interest)
− Depreciation
= EBIT
EBIT × (1 − t)          ← unlevered net income
+ Depreciation
− CapEx
− Increase in NWC
= Unlevered FCFF
```

Terminal / salvage: after-tax proceeds + NWC recovery.

---

## 5. Equity vs enterprise valuation

| Path | Discount rate | Output |
|------|---------------|--------|
| Dividends / total payout | r_equity | Equity value directly |
| FCFF | WACC | Enterprise value → subtract net debt → equity |

Gordon growth: P₀ = D₁/(r−g) only if **r > g** and g sustainable.

---

## 6. Risk → required return

```text
Historical / expected return
= Risk-free + Risk premium

Portfolio: diversify away idiosyncratic risk
CAPM: r_i = r_f + β_i × (E[R_m] − r_f)
```

**Managerial hook:** Riskier project CFs → higher r → lower NPV. Do not use a too-low “HQ hurdle” for a high-risk bet without stating it.

---

## 7. WACC build (Ch. 12)

**Available slides:** Ch. 9 (discount FCFF at r_wacc); Ch. 10–11 (CAPM, β). No separate Ch. 12 PDF in OneDrive — use Berk Ch. 12 for full procedure.

```text
Step 1: r_e = r_f + β × (E[R_m] − r_f)
Step 2: r_d = YTM on debt (pretax)
Step 3: WACC = (E/V) r_e + (D/V) r_d (1 − t)
Step 4: EV = Σ PV(FCFF) at WACC; Equity = EV + Cash − Debt
```

| Input | Typical source |
|-------|----------------|
| β | Regression vs market index; or unlevered β of comps + relever |
| r_f | T-bill / gov bond matching horizon |
| Market premium | Historical or forward estimate — state assumption |
| E, D | Market cap + market value of debt |
| t | Marginal corporate tax rate |

**Project hurdle:** if project risk ≠ firm average → adjust β or use divisional hurdle; document why.

---

## 8. Case pattern (P&G Whitestrips-style)

1. Clarify decision (launch / scale / kill)  
2. Map timeline (tree, not only single line — real options / stages)  
3. Build incremental FCFF vs status quo  
4. Choose r; compute NPV  
5. Sensitivity & qualitative risks (channel, cannibalization, execution)  
6. Recommendation with assumptions list  

---

## 9. Bond building blocks (for cost of debt)

Price = Σ PV(coupons) + PV(face) at YTM.  
Rising rates → falling prices.  
YTM ≈ pretax cost of debt input (adjust for tax shield in WACC).

---

## When NOT to over-apply

- Do not treat payback as the decision rule  
- Do not compare IRRs across vastly different project sizes  
- Do not mix levered CFs with WACC (or unlevered CFs with equity cost) inconsistently  
- Do not ignore compliance / PV / inspection costs as “non-financial” — put them in CF or as explicit risk adjustment
