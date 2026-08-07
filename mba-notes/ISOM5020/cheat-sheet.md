# ISOM5020 — Technology Strategy & Management cheat sheet

> HKUST Fall 2025 · Distilled for Agent **05 Tech/Geopolitics** · **Done 2026-07-27**  
> Pairs with [SBMT6012G](../SBMT6012G/cheat-sheet.md) (external geopolitics) — use **5020 for internal IT decisions, governance, and digital transformation**

---

## Core premise

**"Critical IT decisions are business decisions, not technology decisions."**  
Develop a **process for strategizing about technology** — specific products change; decision logic endures.

**Paradox:** ~80% of IT projects fail (Gartner) yet winners (FedEx, Starbucks mobile, IKEA AR) gain durable advantage — **management quality** separates outcomes.

**Scale:** Global IT spend ~$5T (2024); ~50% of Fortune 500 capex; projected >$6T by 2026.

---

## When to use what (agent quick map)

| Question | Start with |
|----------|------------|
| Who should decide this IT call? | **IT governance** — 5 categories × 5 archetypes |
| Build vs buy vs outsource? | **Cloud/ERP/CRM** module + organizational fit |
| Will incumbents miss this tech? | **Disruptive vs sustaining** + **RPV** |
| Is this project spiraling? | **Scope creep**, estimation, Waterfall vs Agile |
| Security investment level? | **No perfect security** — balance + patch priority |
| Vendor/geopolitics overlay? | Hand off external lens to [SBMT6012G](../SBMT6012G/cheat-sheet.md) |

---

## Course structure: two modules

### Module 1 — Managing IT (internal)

| Topic | Manager focus |
|-------|---------------|
| **To IT or not** | Business case, opportunity cost |
| **Financial planning** | ROI, TCO, portfolio trade-offs |
| **IT governance** | Who decides what — align to strategy |
| **Outsourcing** | In-house vs vendor — control vs speed |
| **Implementation** | Change management, adoption |
| **Security** | Policy + technology; breach readiness |
| **Projects** | Scope, estimation, methodology |

### Module 2 — Managing technology (external)

| Topic | Manager focus |
|-------|---------------|
| **Disruptive technologies** | RPV, spin-off vs integrate |
| **Emerging opportunities** | IoT, digital twins, GenAI — timing and fit |

**Cases teach:** "What would you do?" — not latest gadget specs.

---

## IT governance (5 decisions × 5 archetypes)

### Five decision categories

1. **IT principles** — role of IT in strategy (sets direction)  
2. **IT architecture** — standards, integration (needs IT expertise)  
3. **IT infrastructure** — cloud, network, data centers (shared backbone)  
4. **Business applications** — CRM, ERP, custom systems  
5. **IT investment & funding** — project prioritization, budgets  

### Five governance archetypes (centralized → decentralized)

| Archetype | Who decides | Fit |
|-----------|-------------|-----|
| **Business monarchy** | CEO/CFO, no IT | Fast, business-only — risks bad tech choices |
| **IT monarchy** | CIO/IT only | Standards — risks ignoring business |
| **Federal** | Corp + BU + IT jointly | Buy-in — slow, can deadlock |
| **IT duopoly** | IT + business leader | Balance — can deadlock |
| **Feudal** | Each BU alone | Fast local — duplication, inconsistency |

### Strategy–governance alignment

| Company focus | Governance bias | Risk if wrong |
|---------------|-----------------|---------------|
| **Profit / cost** | Centralized (monarchy) | Feudal → duplicated systems, higher cost |
| **Growth / speed** | Decentralized (feudal/federal) | Over-centralized → missed windows |
| **Asset utilization / ROA** | **IT always in room** (duopoly/monarchy) | Business-only → failed implementations |

**Exam-grade insight:** Architecture & infrastructure **require IT specialist** — business monarchy here predicts failure (e.g., Rich-Con Steel pattern).

### VWoA pattern (investment governance)

- 40 projects, $210M need, $60M budget → need **transparent prioritization**  
- **IT Steering Committee + Digital Business Council** (federal)  
- Link projects to **Next Round of Growth** strategy  
- **Good governance creates losers** — political pressure on CIO is expected  

### SYSCO pattern

- Pre-1993 **feudal** → inconsistent CRM, high cost  
- Post-1993 **centralized** → aligned with profit focus  

---

## CRM — customer intimacy at scale

**Definition:** Replicate mom-and-pop customer knowledge across enterprise.

**Three modules:** Sales Force Automation · Customer Service · Marketing (pick modules; don't boil ocean).

**Failure driver:** **"Plug & play" myth** — CRM requires **process redesign**, not install-only.

**Best practices:** Narrow initial scope · integrate with legacy · change management · measure adoption · executive sponsor.

**Enterprise stack:** ERP (internal) + CRM (customer) + SCM (supplier) — vendors increasingly bundle.

---

## Cloud computing

**Business lens:** Elastic capacity, pay-as-you-go, agility — **and** compliance/residency trade-offs.

| Model | What vendor manages | Control |
|-------|---------------------|---------|
| **SaaS** | Full application | Least control, fastest |
| **PaaS** | Infra/OS; you build apps | Moderate |
| **IaaS** | VMs/storage; you stack rest | Most control, most burden |

| Deployment | Use when |
|------------|----------|
| **Public** | Generic, non-sensitive |
| **Private** | Regulated, legacy, performance-sensitive |
| **Hybrid** | Split by sensitivity (e.g., gov confidential vs generic) |

**Manager takeaway:** Match **data sensitivity** to deployment — not "cloud yes/no."

---

## ERP — integrated processes

**Value:** Single database across sales, finance, HR, materials, SCM — real-time visibility.  
**Failure rate:** 50–75% — usually **organizational**, not technical.

| Approach | Trade-off |
|----------|-----------|
| **Single vendor** (SAP, Oracle) | Integration vs flexibility |
| **Best-of-breed patchwork** | Flexibility vs integration cost |

**Evolution:** Traditional monolith → postmodern APIs → cloud-native + AI modules.

**Key decisions:** Vendor selection · configuration vs customization · phased rollout · **who owns change**.

---

## Disruptive technologies (Christensen pattern)

| | Sustaining | Disruptive |
|---|-----------|------------|
| **Performance** | Better on mainstream metrics | Worse initially; valued by niche |
| **Incumbent response** | Invest and win | Ignore until too late |
| **Example arc** | Faster HDD | Smaller cheaper HDD → mainstream |

### RPV — why incumbents can't pivot

| | Resources | Processes | Values |
|---|-----------|-----------|--------|
| **Nature** | Assets, people, brand | How work gets done | Margin/size thresholds for yes/no |
| **Flexibility** | Most flexible | Rigid | Most rigid |
| **Disruption failure** | Rarely root cause | Rejects new workflow | Kills small markets |

### Three response strategies

1. **Force internally** — fight processes/values (high fail rate)  
2. **Spin-off subsidiary** — new RPV (often best)  
3. **Acquire** — **keep separate** or kill acquired RPV by integration  

---

## IT security

**Truths:** No perfect security · new tech = new attack surface · **balance** cost vs inconvenience.

| Threat | Manager note |
|--------|--------------|
| Ransomware | Ops halt + reputation |
| DDoS | Availability |
| Phishing | Human factor |
| Insider | Access control |
| Supply chain | Vendor compromise |

**Priority:** Most breaches exploit **known** vulnerabilities — **patching** beats perfect walls.

**Policy = technology + people + process** (training, incident response, asset prioritization).

---

## IT project management

**Failure drivers:** Scope creep · bad estimation · wrong methodology · weak change control.

| Method | When |
|--------|------|
| **Waterfall** | Stable requirements, regulatory validation |
| **Agile** | Evolving requirements, iterative discovery |

**Estimation tools:** Delphi · Function Point Analysis · expert judgment (each has bias).

**Scope discipline:** "Essential vs nice-to-have?" · formal change board.

**Cases:** Netdynamic (ERP implementation), iPremier (security incident response), GenAI salesbot (adoption/risk).

---

## Emerging tech themes (Week 7 wrap)

| Tech | Business angle |
|------|----------------|
| **IoT / Agentic AI** | Operations data, automation — governance + security surface |
| **Digital twins** | Simulation for ops/clinical — integration with legacy |
| **GenAI** | Productivity vs hallucination, data leakage, vendor terms |

Treat as **decision cases** — apply governance, security, and disruption lenses.

---

## Exclusions

Personal case cheat sheets, group executive summaries, Assignment 2 personal digital-twin research, exam templates, `.pptx` decks. Raw cases stay in OneDrive.

---

## Source

OneDrive: `Fall 2025\ISOM5020 Technology Strategy and Management` — course description, exam study guide, week case PDFs, module exam-summary docx files (CRM, cloud, ERP, governance, security, projects, disruption).
