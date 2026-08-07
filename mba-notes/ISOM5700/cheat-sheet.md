# ISOM5700 — Operations Management cheat sheet

> HKUST Spring 2026 · Albert Ha · Distilled for Operations & Clinical PM agent (`03`) · **Replenished 2026-07-27**  
> Textbook: *Matching Supply with Demand* (Cachon & Terwiesch, 5th ed.) · Pairs with [MGMT5410](../MGMT5410/cheat-sheet.md) (strategy positioning) — use **5700 for process/capacity/inventory/quality/SCM execution**

---

## What OM is (and is not)

**Operations management** = design, plan, execute, improve, and innovate **business processes** that produce goods or services.

A **process** has two functions:
1. **Conversion** — deploy resources to convert inputs → outputs (goods/services)
2. **Flow** — match **supply with demand**

**Not** strategy alone — OM translates business positioning into resource/process choices. **Not** "efficiency everywhere" — align process capabilities to strategic priorities.

---

## When to use what (agent quick map)

| Question | Start with |
|----------|------------|
| How fast/slow is this process? Where is inventory stuck? | **Little's Law** (I = R × T) |
| What limits throughput? | **Process capacity / bottleneck** analysis |
| Why are customers waiting? | **Queueing** — variability + utilization |
| Pool vs specialize resources? | **Capacity pooling** vs **specialization** tradeoff |
| One-shot order under uncertain demand? | **Newsvendor** (Cu, Co, service level) |
| Steady replenishment, fixed demand rate? | **EOQ** |
| Random demand + lead time? | **Reorder point** + safety stock |
| Centralize vs regional warehouses? | **Inventory pooling** economics |
| Defects / process drift? | **SPC** — common vs special cause |
| Eliminate waste, shorten flow? | **Lean** — 7 wastes, JIT, Jidoka |
| SC partners fighting over margin? | **Co-opetition**, **VMI**, bullwhip diagnosis |

---

## Operations & strategy link

**Four product/service attributes (customer view):** Price **P**, Quality **Q**, Response time **T**, Variety **V**.

**Four process capabilities (ops view):** Cost **C**, Quality **Q**, Lead time **T**, Flexibility **Flex**.

| Process capability | Competitive advantage |
|--------------------|----------------------|
| Low cost (C) | Low price (P) |
| High process quality (Q) | High product/service quality (Q) |
| Short lead time (T) | Fast/reliable delivery, time-to-market (T) |
| Flexibility (Flex) | Variety, customization (V) |

**Strategic framework:** Business strategy (product positioning) → **priority of P,Q,T,V** → **process capabilities C,Q,T,Flex** → resource & process strategies.

**Business model:** Value proposition + revenue model + **resources** + **process model** (how resources create value). Process innovation (e.g. order-to-ship → ship-to-order) can enable new business models.

**Zara pattern (case):** Fast/flexible supply chain supports speed + variety positioning; coherent resource/process choices (proximity manufacturing, multi-functional teams, limited batches).

---

## Process flow measures

**Flow unit** = whatever moves through the process (patient, dollar, SKU, job).

| Measure | Definition |
|---------|------------|
| **Flow rate R** (throughput) | Flow units per unit time |
| **Flow time T** | Time a flow unit spends in process |
| **Inventory I** | Flow units in the process |

### Little's Law (long-run averages)

**I = R × T**

Also: **Inventory turn = COGS / Inventory = 1 / T** (when using COGS-based turn).

**Uses:** Diagnose bottlenecks in cash, AR, WIP, rental fleet — knowing any two of I, R, T gives the third.

**Inventory holding cost:** If holding cost rate = h per unit per year and flow time = T years → cost per unit of sales ≈ h × T.

---

## Process capacity analysis

1. Draw **process flow diagram** — activities, buffers, resources, flows.
2. **Resource capacity** = max output rate of each resource.
3. **Process capacity** = capacity of the **bottleneck** (constraint resource).
4. **Utilization** = flow rate / resource capacity (fraction of time busy).

**Multiple job types:** Use **one minute of work** as common unit (not flow units).

**Principles of bottleneck management:**
- Bottleneck **dictates** process performance
- Avoid **idling** the bottleneck
- **Subordinate** non-bottlenecks to support bottleneck
- Shift work to non-bottlenecks when possible

**Trap:** Higher utilization ≠ higher productivity if non-value-adding time rises (e.g. travel in pooled field service).

---

## Waiting time management

**Flow time T = waiting time in queue Tq + activity time p**

**Root causes of waiting:**
- **Arrival variability** (bursts of demand)
- **Service variability** (job size, inexperience)
- **High utilization** (little safety capacity) — relationship is **non-linear**

### Queue model inputs

| Input | Symbol |
|-------|--------|
| Servers | m |
| Avg interarrival time | a (rate R = 1/a) |
| Avg activity time | p (service rate = 1/p) |
| CV of interarrival | CVa = sa/a |
| CV of activity | CVp = sp/p |

**Utilization:** u = R / (m × service rate per server)

**Approximate Tq** (King's formula variant used in course):

Tq ≈ (p/m) × [u/(1−u)] × [(CVa² + CVp²)/2] × utilization/activity factors

Use course **Queue.xls / Queue Model** spreadsheet for numeric analysis.

### Four principles

| Principle | Idea |
|-----------|------|
| **Capacity pooling** | Shared servers flex to random demand → shorter waits (but may add travel/non-value time) |
| **Specialization** | Learning curve → faster, more consistent service for repeated task types |
| **Time–cost tradeoff** | Wait ↑ sharply as u → 100%; adding capacity has **diminishing** wait reduction (ER problem) |
| **Service priority** | Priority rules improve wait for some customers, worsen for others (check system-wide metrics) |

**NOP case pattern:** Pooling reduces queue but adds travel; optimize team size with quantified tradeoff.

**Managing perception:** Occupied time feels shorter than empty wait; anxiety, unfairness, unexplained waits hurt experience (virtual queues / WTI).

---

## Capacity management — uncertain demand

### Newsvendor model (one ordering opportunity)

Match order quantity Q to random demand D.

| Term | Meaning |
|------|---------|
| **Cu** | Unit **underage** cost (stockout / too little) |
| **Co** | Unit **overage** cost (leftover / too much) |
| **Service level** | P(D ≤ Q*) |

**Optimal service level:**

**Cu / (Cu + Co)**

Then find Q* from demand distribution (Normal: use safety factor × σ).

**General matching:** Same logic for seat protection (RM), therapist capacity, travel-time buffer to appointment.

### Revenue management (fixed capacity)

When supply is fixed (seats, rooms, slots): **segment by willingness to pay**, protect capacity for high-fare/high-value segments.

**Airline pattern:** Cu = full fare − discount fare; Co = discount fare (unsold seat); protect seats for business travelers.

---

## Inventory management

### Cost components

- **K** — fixed ordering cost ($/order)
- **h** — holding cost ($/unit/time)
- **Stockout cost** — lost sales, goodwill, expediting

**Cycle service level** = P(all demand in cycle met from on-hand inventory).

### EOQ (constant demand rate R)

**Total cost = hQ/2 + KR/Q**

**Optimal order quantity: Q* = √(2KR/h)**

Balances fixed ordering vs holding. Check truck-capacity constraints (may accept slightly suboptimal Q).

### Reorder point (random demand, Normal weekly demand)

- Order quantity: **EOQ**
- Lead-time demand: mean = **L × mean_weekly**, SD = **√L × SD_weekly**
- **Reorder point = lead-time demand at target service level**
- **Safety stock = reorder point − expected lead-time demand**

**Drivers of safety stock:** ↑ service level, ↑ lead time, ↑ demand variability.

### Inventory pooling

**Principle:** Pooled safety stock achieves same service level with **less** total inventory (σ of sum grows slower than sum of σ's when demands independent).

| Form | Example |
|------|---------|
| **Location pooling** | Consolidate warehouses |
| **Virtual pooling** | Transshipment + info sharing across sites |
| **Product pooling** | Common platform/components (auto mega-platform) |
| **Postponement** | Delay differentiation (Benetton: knit then dye) |

**Centralize vs decentralize:**
- Central: lower total inventory & ops cost (economies of scale)
- Decentral: shorter delivery lead time, lower outbound shipping cost

---

## Quality management

**Dimensions:** Performance, features, reliability, durability, serviceability, aesthetics, perceived quality, **conformance** (meets spec).

**Inspection** = detect defects at output. **Process control** = prevent — **cheaper and better**.

### Variability types

| Type | Cause | Response |
|------|-------|----------|
| **Common cause** | Inherent in process design | Long-term improvement |
| **Special cause** | Assignable event (bad batch, wrong setting) | Find and remove quickly |

**In control** = only common cause. **Out of control** = special cause present → defect rate elevated.

### Control chart (p-chart for attributes)

- Plot sample defect rate vs control limits
- **Inside limits** → no action (or false negative if actually out of control)
- **Outside limits** → investigate special cause
- Balance **false positive** vs **false negative** costs

**Tools:** Pareto (vital few defects), **Fishbone/Ishikawa** (cause–effect), control charts.

**Six Sigma:** SPC tools + continuous improvement philosophy; ≈ 3.4 DPMO target.

**Costs of quality:** Prevention, appraisal, internal failure, external failure — economics favor prevention.

---

## Lean operations (TPS)

**Philosophy:** Continuous improvement (Kaizen); eliminate **waste**, not just cut cost.

### Seven wastes (TIMWOOD+)

Transportation, Inventory, Motion, Waiting, Overproduction, Overprocessing, Defects (+ unused talent).

**Inventory hides problems** — Toyota reduces inventory to **expose** problems; buffers mask root causes.

### Two objectives

| Objective | Tactics |
|-----------|---------|
| **Just-in-time (JIT)** | Product layout, setup reduction, demand pull (Kanban) |
| **Jidoka (autonomation)** | Stop at defect; **five whys**; **poka-yoke** (mistake-proof) |

**Product layout vs functional layout:**
- Product: shorter flow, less WIP, faster quality feedback
- Functional: higher utilization via pooling but more handling/inventory

**Williamsport pattern:** Service lines = product layout for rehab → better coordination & satisfaction but lower therapist utilization (loss of pooling). Refinements: floaters, merge small lines, flexible spillover line.

---

## Supply chain management

**Supply chain** = network of processes (design → manufacture → deliver → service → recycle) often owned by different firms.

**Three flows:** Material, **information**, financial.

**Objectives:** Low cost, short response, high quality, flexibility; minimize supply/demand/financial risk; CSR expectations.

### Co-opetition

Collaborate to **grow the pie**; compete for fair share. Pure competition → win-lose and bullwhip.

**Outsourcing:**
- **Market buy** — short-term, many suppliers, min purchase price
- **Partnership** — long-term, few suppliers, joint design, capability investment (Cisco model)

### Bullwhip effect

Demand variability **amplifies upstream**. Causes: forecast error, batch ordering, lead times, promotions, lack of info sharing.

**VMI (vendor managed inventory):** Vendor sees downstream data, centralizes replenishment decisions (Barilla pattern) → lower inventory + fewer stockouts.

### Digital SCM

IoT, blockchain, 3D printing, smart replenishment, omni-channel — improve info/material flow coordination.

---

## 8 questions before an ops recommendation

1. What is the **strategic positioning** (P,Q,T,V priority)?
2. What are **I, R, T** — does Little's Law reveal a hidden bottleneck?
3. Where is the **capacity constraint** and its utilization?
4. Is waiting driven by **variability**, **utilization**, or **design** (pool vs specialize)?
5. Is demand **one-shot** (Newsvendor) or **repeating** (EOQ/ROP)?
6. What **service level** is required vs cost of inventory/capacity?
7. Are defects from **special** or **common** causes?
8. What is the **supply chain info/material** flow — any bullwhip or misaligned incentives?

---

## Do / don't for this agent

**Do:** Quantify bottlenecks; separate capacity vs demand variability; tie ops levers to strategic priorities; use pooling/specialization tradeoff explicitly.  
**Don't:** Maximize utilization blindly; ignore compliance/safety gates; treat all demand as Normal without checking; recommend centralization without service-level impact.

---

## Course map (Spring 2026 · Albert Ha → tools)

| Class | Topic | Tools / cases |
|-------|-------|---------------|
| 1 | Operations & strategy | Strategic framework, Zara, business model |
| 2 | Process analysis | Little's Law, capacity, bottlenecks |
| 3 | Waiting time | Queue model, NOP case |
| 4 | Inventory | EOQ, reorder point, pooling |
| 5 | Simulation game | Sailboat — lean flow |
| 6 | Capacity + quality | Newsvendor, Williamsport, SPC |
| 7 | Lean + SCM | TPS, Barilla/VMI, digital SC |
| 8 | Final exam | Open-book; MCQ + quantitative |

**Cases (course):** Zara · National Office Products · Williamsport Hospital — pattern recognition only; personal HW/exam answers not in vault.

**GenAI policy (course):** Prohibited for homework unless allowed; use AI as tutor for concepts, not submitted work.
