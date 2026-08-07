# ISOM5700 → career hooks (Clinical PM / PM / GM · HK healthcare)

Pair with [MGMT5410 career-hooks](../MGMT5410/career-hooks.md) (strategy fit) and clinical PM playbooks in `consultant-agents/industry/`.

---

## Clinical Project Manager

| ISOM5700 tool | Work application |
|---------------|------------------|
| **Little's Law** | Triage enrollment pipeline: if many subjects in screening (I) and fixed activation rate (R), time-in-process (T) explains site frustration |
| **Bottleneck analysis** | Identify constraint stage (IRB, import license, site initiation, monitoring) — subordinate other tasks to protect bottleneck |
| **Queueing / utilization** | Adding CRAs near u→100% yields diminishing wait reduction; fix variability (protocol ambiguity, missing docs) first |
| **Newsvendor** | One-shot decisions: how many sites to activate, kits to ship, backup slots for enrollment before deadline |
| **Reorder point + SS** | IMP/ancillary supply replenishment — balance stockout risk vs expiry/write-off (Co/Cu framing) |
| **SPC / special cause** | Spike in protocol deviations or query rate → special cause investigation before blaming "site performance" |
| **Lean / poka-yoke** | eTMF checklist gates, mandatory fields, duplicate detection — mistake-proof submission packages |
| **Service lines (Williamsport)** | Therapeutic-area squads improve coordination but reduce cross-pooling — use floaters for cross-trial surge |

---

## Product Manager

| ISOM5700 tool | Work application |
|---------------|------------------|
| **Strategic framework (P,Q,T,V)** | Launch positioning drives ops priority: rare disease → flexibility + quality; commodity → cost + availability |
| **Lead time / flow time** | Time-to-access metrics (registration → first dose) as product KPI tied to process design |
| **Inventory pooling** | Central vs regional drug depots for HK+GBA — quantify service level vs working capital for HQ business case |
| **Postponement** | Delay pack/label differentiation until closer to market authorization or payer decision |
| **Quality dimensions** | Separate **conformance** (SOP/regulatory) from **perceived** quality (HCP experience) in launch readiness |
| **Digital SC** | Track-and-trace, cold chain IoT — ops innovation as product differentiator vs competitor |

---

## General Manager

| ISOM5700 tool | Work application |
|---------------|------------------|
| **Process capabilities C,Q,T,Flex** | Subsidiary operating model must match HQ positioning — don't run "low cost" ops for "premium intimacy" brand |
| **Capacity pooling vs specialization** | Shared medical/regulatory pool vs dedicated brand teams — explicit tradeoff in org design |
| **Centralization economics** | Consolidate HK warehousing vs local responsiveness for hospital tenders |
| **Co-opetition / VMI** | 3PL/distributor partnerships — share POS/hospital consumption data to cut bullwhip on key SKUs |
| **Revenue management** | Allocate scarce medical affairs / KOL access across brands by margin/strategic priority |
| **Costs of quality** | Prevention spend (training, systems) vs cost of inspection failures (audit findings, recalls) |
| **Bottleneck at GM level** | Escalate when constraint is regulatory bandwidth, not headcount — capacity is not always "hire more" |

---

## HK subsidiary-specific

- **Public vs private channel:** Different arrival variability → different pooling; HA tender cycles create **batch demand** and bullwhip upstream.  
- **Cross-border GBA:** Lead-time demand for imports — safety stock driven by customs/regulatory **L** and **σ**, not only sales forecast.  
- **Hospital access programs:** Patient flow in clinics mirrors queueing — prioritize high-value segments without breaking compliance fairness rules.  
- **Pharma cold chain:** Inventory hiding problems — reduce buffer only when monitoring (Jidoka) catches excursions in real time.  
- **Clinical ops hub HK:** High-flow cataract / day-surgery pilots (local) = product layout + setup reduction pattern for site networks.  

---

## RAID mapping (ops lens)

| RAID type | ISOM5700 hook |
|-----------|---------------|
| **Risk** | High utilization + high variability → queue blow-up |
| **Assumption** | Demand distribution (Normal?) and lead time stable |
| **Issue** | Active bottleneck starving downstream milestones |
| **Dependency** | Supplier/3PL info flow — bullwhip if batch ordering |

---

## Forward distillation

Append one bullet after useful ops decisions:

```markdown
- YYYY-MM-DD [role]: [lesson] (ISOM5700: [framework])
```
