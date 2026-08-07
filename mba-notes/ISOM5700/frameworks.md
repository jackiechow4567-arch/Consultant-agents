# ISOM5700 — Frameworks reference

> Companion to [cheat-sheet.md](cheat-sheet.md). Agent reads cheat-sheet first.

---

## 1. Course arc (process view)

```
STRATEGY LINK          FLOW & CAPACITY           MATCH UNCERTAINTY        QUALITY & LEAN          SUPPLY CHAIN
────────────────       ───────────────           ─────────────────        ─────────────           ────────────
P,Q,T,V positioning    Little's Law              Newsvendor (Cu, Co)       Common vs special       Material / info /
→ C,Q,T,Flex           Bottleneck                EOQ + reorder point       cause (SPC)             financial flows
Business model         Queueing (var + u)        Inventory pooling         7 wastes, JIT/Jidoka    Co-opetition, VMI
Resource/process       Pool vs specialize        Revenue management        Service lines           Bullwhip
```

---

## 2. Strategic alignment framework

```
BUSINESS STRATEGY (product positioning)
        │
        ▼
Priority among P, Q, T, V  (price, quality, response time, variety)
        │
        ▼
PROCESS CAPABILITIES: Cost C, Quality Q, Lead time T, Flexibility Flex
        │
        ├── Resource strategy: type, sizing, location (people, assets, IP, data)
        └── Process strategy: outsource, demand mgmt, risk, improvement/innovation
```

**Alignment test:** Every ops initiative should trace to a **positioning priority** and move a **process capability** metric.

---

## 3. Little's Law — diagnostic workflow

```
Pick flow unit (patient, $, SKU, job)
        │
        ▼
Measure or estimate any TWO of:  I (inventory)  R (flow rate)  T (flow time)
        │
        ▼
Compute third:  I = R × T
        │
        ▼
Compare inventory turn / holding cost vs benchmark
        │
        ▼
Hypothesis: reduce T (speed) vs reduce I (WIP/cash) vs increase R (throughput)
```

**AR example:** If sales = R and AR = I → collection cycle T = I/R.

---

## 4. Process capacity — analysis checklist

| Step | Action |
|------|--------|
| 1 | Draw process flow diagram (activities, buffers, resources) |
| 2 | List activity times per resource |
| 3 | Compute resource capacity (jobs/hour or min work/hour) |
| 4 | If multiple job types → convert to **minutes of work** |
| 5 | Compute utilization at target throughput |
| 6 | Identify **bottleneck** (highest utilization) |
| 7 | Apply bottleneck principles (don't starve, subordinate others) |

**Output table template:**

| Resource | # workers | Total cap | Workload | Utilization | Bottleneck? |
|----------|-----------|-----------|----------|-------------|-------------|
| | | | | | |

---

## 5. Queueing — structure and levers

```
Arrivals → [Queue Iq, wait Tq] → Servers (m) → [In service Ip] → Departures
                              Flow time T = Tq + p
```

**Performance drivers:**

| Lever | Effect on wait |
|-------|----------------|
| ↑ servers m | ↓ wait (but adds cost) |
| ↓ utilization u | ↓ wait (non-linear) |
| ↓ CVa, CVp (reduce variability) | ↓ wait |
| Pooling | ↓ wait (flexibility) but may ↑ non-value time |
| Priority rules | ↓ wait for priority class; ↑ for others |

**Time–cost tradeoff curve:** Plot wait vs utilization — steep near u → 1. Adding capacity at high u yields diminishing wait reduction.

**Capacity pooling vs specialization matrix:**

| | Low specialization benefit | High specialization benefit (learning curve) |
|---|---------------------------|---------------------------------------------|
| **High arrival variability** | Favor pooling | Hybrid (pooled simple, specialized complex) |
| **Low variability** | Either works | Favor specialization |

---

## 6. Newsvendor — decision checklist

```
Define single ordering / capacity commitment opportunity
        │
        ▼
Estimate demand distribution (mean, SD)
        │
        ▼
Compute Cu (cost of too little) and Co (cost of too much)
        │
        ▼
Optimal service level = Cu / (Cu + Co)
        │
        ▼
Find Q* from distribution (Normal → z × σ + μ)
        │
        ▼
Report: avg sales, lost sales, leftover inventory
```

**Revenue management variant:** Fixed capacity → protect Q seats/slots for high-fare segment; Cu/Co from fare classes.

**Applications beyond retail:** Therapist staffing (Williamsport), travel buffer to meeting, catalog wine order, airline seat protection.

---

## 7. Inventory policy — EOQ + reorder point

### EOQ (deterministic R)

```
Annual cost = KR/Q + hQ/2
Q* = √(2KR/h)
```

Check: truck fill constraints, supplier MOQ, cash limits.

### Reorder point (stochastic demand)

```
Order qty Q = EOQ
Lead-time demand ~ Normal( L·μ_w , √L·σ_w )
Safety stock = z × √L × σ_w   (for target cycle service level)
Reorder point = L·μ_w + safety stock
Average inventory ≈ Q/2 + SS
```

### Pooling economics (4 → 1 warehouse sketch)

| | 4 regional DCs | 1 central DC |
|---|----------------|--------------|
| Cycle stock | 4 × (Q/2) | Q/2 (larger EOQ) |
| Safety stock | 4 × SS(σ) | SS(√4·σ) < 4×SS |
| Ordering cost | 4× fixed | 1× fixed |
| Delivery lead time | Shorter | Longer |

**Decision:** Quantify service-level vs inventory vs shipping tradeoff.

---

## 8. Quality — SPC workflow

```
Define conformance spec
        │
        ▼
Sample regularly → compute defect rate p
        │
        ▼
Plot on p-chart with control limits
        │
        ├── In limits → process in control (common cause only)
        └── Out of limits → hunt special cause → remove → restore control
        │
        ▼
Long-term: reduce common cause (process improvement)
```

**Fishbone categories:** Materials, Methods, Machines, People, Environment.

**Inspection vs control:**

| | Inspection | Process control |
|---|------------|-----------------|
| Focus | Output | Process capability |
| Timing | After defect | Before / during |
| Cost | Higher (scrap, rework) | Lower (prevention) |

---

## 9. Lean — waste scan checklist

| Waste | Manufacturing signal | Service / clinical signal |
|-------|---------------------|---------------------------|
| Waiting | WIP queues | Patient/site idle time |
| Overproduction | Make-to-stock excess | Reports nobody reads |
| Defects | Rework, scrap | Protocol deviations, query rates |
| Motion | Unnecessary handling | Staff walking for supplies |
| Inventory | Raw/WIP/finished | Excess drug depots, batch files pending |
| Transport | Inter-facility moves | Sample shipment delays |
| Overprocessing | Extra steps | Duplicate data entry |

**JIT levers:** Product layout · setup reduction · pull/Kanban  
**Jidoka levers:** Stop line · five whys · poka-yoke

---

## 10. Supply chain — collaboration checklist

| Question | Tool |
|----------|------|
| Is margin fought over a fixed pie? | Co-opetition — design win-win contracts |
| Demand signal distorted upstream? | Bullwhip diagnosis (batch orders, promos, lead time) |
| Can vendor see downstream inventory/sales? | VMI / CPFR |
| Insource vs outsource? | Core competency + partnership vs market buy |
| Info sharing blocked? | Incentive alignment, confidentiality, KPI sharing |

**Three flows to optimize jointly:** Material (when/where), Information (visibility), Financial (terms, risk sharing).

---

## 11. Integration with other MBA agents

| Agent / course | Handoff |
|----------------|---------|
| **01 Strategy (MGMT5410)** | Positioning sets P,Q,T,V priority → OM chooses C,Q,T,Flex |
| **01 Econ (ECON5110)** | Pricing / capacity constraints; game theory in SC contracts |
| **02 Finance (FINA5120)** | Holding cost = cost of capital; NPV of automation/capex |
| **04 GM (MGMT6501T/W)** | Service-line org design; innovation in healthcare delivery |

---

## Source

Distilled from OneDrive `Spring 2026\ISOM5700 Operations Management`: syllabus, course summary, Quick Reference Equation, Lecture Notes 1–8, presentation PDFs. **Excluded:** personal homework drafts/answers, exam practice solutions, group evaluation.
