# Gem 05 — Tech & Geopolitics Knowledge Pack

> Generated 2026-07-28 12:02 for Gemini Gem Knowledge upload.
> Rebuilt: 2026-07-28 12:02 · Run `python build.py` after vault or gm-reference updates.
> Paste the matching system instruction from `gem-system-prompts.md`.

Tech strategy + geopolitics; includes exec comms and data-viz cheat sheets for HQ narratives.

---

## Source: ISOM5020 Technology Strategy & Management

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


---

## Source: SBMT6012G Geopolitics of Emerging Tech

# SBMT6012G — Geopolitics of Emerging Tech cheat sheet

> HKUST Spring 2026 · Julien de Troullioud de Lanversin · Distilled for Agent **05 Tech/Geopolitics** · **Done 2026-07-27**  
> Pairs with [ISOM5020](../ISOM5020/cheat-sheet.md) (internal IT strategy) — use **6012G for export controls, supply-chain chokepoints, US–China tech rivalry**

---

## Core premise

**Techno-geopolitics:** Technology is not neutral geography — polities *choose* how tech enters geopolitics. Tech can **emancipate from geography** (telecom, cloud) or create a **new virtual geography** (platforms, AI ecosystems).

**Agent rule:** Distinguish **publicly known control regimes** (cite need for counsel) from speculation. Map **parent jurisdiction, HK ops, supplier geography** explicitly.

---

## When to use what (agent quick map)

| Question | Start with |
|----------|------------|
| Why does US–China fight over a technology? | **Techno-geopolitical dynamics** table + **state toolkit** |
| Can we depend on this vendor/node? | **Chokepoints** + **weaponization of dependencies** |
| Semiconductor / GPU / lithography exposure? | **Semi supply chain** anatomy |
| AI adoption with geopolitical risk? | **AI race dimensions** (capabilities, resources, ecosystem) |
| Corporate response under controls? | **Nvidia case pattern** — comply, localize, diversify, lobby |
| Long-horizon emerging risk? | **Quantum** — computation, comms, sensors (early-stage) |

---

## Key dynamics: technology ↔ geopolitics

| Category | What it means |
|----------|---------------|
| **Power projection & military advantage** | Tech extends influence, deterrence, new domains (cyber, autonomous weapons) |
| **Violence & systemic risk** | Escalation, WMD-adjacent tech, existential risk debates |
| **Dependencies & vulnerabilities** | Chokepoints, digital sovereignty, resource-intensive supply chains |
| **Cooperation & governance** | Standards, alliances, multilateral rules (when states allow) |
| **Connectivity & societal integration** | Bridges or divides societies; empowers non-state actors |
| **Security & safety** | Defense against attack; also new attack surfaces |
| **Competition, prestige, economic dominance** | Innovation races, monopolies, critical materials, sanctions |
| **Hybrid & asymmetric threats** | Disinformation, cyber, blurred peace/war lines |

**Individual vs state interests:** Same technology (telecom, crypto, AI, semiconductors) serves **consumer convenience** and **state power projection** simultaneously — corporate decisions sit in the overlap.

---

## Where dynamics operate (stack)

```
Applications/Impacts ←→ Capabilities ←→ Resources (data, hardware, energy, rare earth)
         ↑                      ↑                    ↑
    Knowledge/Know-how ←→ Ecosystem ←→ Power, Risks, Cooperation/Governance
```

Use this stack to locate **where** a subsidiary decision creates exposure (e.g., GPU supply = Resources + Chokepoints; cloud region = Ecosystem + Governance).

---

## State toolkit (geopolitics of technology)

| Bucket | Tools |
|--------|-------|
| **Economic & investment** | Subsidies, tax credits, industrial policy, tariffs, procurement, nationalization |
| **Regulatory & legal** | Export controls, investment screening, tech transfer, IP, antitrust, data rules, standards |
| **R&D** | National programs, frontier research funding |
| **Alliances & diplomacy** | Tech alliances, denial coalitions, sanctions |
| **Espionage & cyber** | Tech theft, attacks, counter-espionage |
| **Military & coercion** | Deterrence, embargo, degradation |
| **Narrative** | Prestige competition, ideological framing |

**US–China AI race uses all buckets** — not only export controls.

---

## AI geopolitics (SBMT6012G Week 1–2 arc)

### Race dimensions

1. **Capabilities** — frontier models, weights, engineering vs theory  
2. **Resources** — data, hardware (GPUs), energy  
3. **Ecosystem** — policy, institutions, cultural enablers  

**Scaling law (policy relevance):** More compute + data + weights → better performance → **energy and chip demand** are strategic, not incidental.

### Applications & risks (governance hooks)

| Domain | Issue |
|--------|-------|
| **Military** | Autonomous weapons, faster targeting, electronic warfare, war-planning AI |
| **Law enforcement** | AI surveillance, predictive policing |
| **Information** | World-building on platforms, cyberpsychology, disinformation at scale |
| **Security** | Society dependent on AI → vulnerable to training-data / model attacks |
| **Ethics** | Black-box interpretability, autonomous harm, targeted ads & mental health |
| **Existential (tail risk)** | Debated; keep separate from near-term ops decisions |

### Two metaphors for the “AI race”

| Metaphor | Implication |
|----------|-------------|
| **Sprint to AGI (winner-take-all)** | First to AGI may create insurmountable lead |
| **Marathon + dependency weaponization** | Keep rivals dependent on your tech/standards; control innovation path |

**Chokepoints (top ~1%):** Advanced GPUs, EUV lithography, rare earths, elite talent, frontier models, agentic AI — competition often **not** in the “99%” commodity layer.

---

## Semiconductors — “the new oil”

### Supply chain anatomy

```
Design software → Fabless design → Wafer fab equipment → Foundries/Fabs → Assembly → End users
   (US trio)        (US-heavy)      (US + NL/ASML)         (TW/KR/US; SMIC rising)  (CN/TW)   (states + hyperscalers)
```

**Chokepoints:** EDA (Synopsys, Cadence, Mentor); **ASML EUV** (only advanced lithography); **TSMC/Samsung/Intel** advanced fab concentration; **Taiwan geography risk**.

### China position (circa course materials)

- Largest **importer** of semiconductors (~$350B, 2020 — exceeds crude oil)  
- Lag on **most advanced** nodes; Huawei/SMIC **5 nm** milestone noted as catch-up signal  
- High-end chips matter for **military, smartphones, AI training**; mid-tier OK for many data-center/auto uses  

### China policy tools

Subsidies, tax credits, R&D, foreign talent recruitment, licensing JVs, technology transfer.

### US counter-measures (Biden-era framework in course)

| **CHIPS Act (~$280B)** | **Export controls** |
|------------------------|---------------------|
| Domestic fab incentives, R&D, workforce | Ban advanced chips, EDA, fab equipment to China |
| Deny funding if facilities in China | Nvidia GPU restrictions; Huawei entity list |
| Tax credits for manufacturers | Unverified/Entity lists; extraterritorial reach (allies stop equipment sales) |

**Case pattern — Fujian Jinhua:** Entity list → cut from US tech → bankruptcy (illustrates **legal/export lever**, not a prediction for every firm).

**Corporate dilemma — Nvidia “Balancing Act”:** China ~25% → ~9% datacenter revenue under controls; **de-contented chips** still draw Commerce scrutiny; **no substitute market** for China scale; compliance vs loophole perception vs Chinese local substitution risk.

---

## Quantum (second revolution — conceptual)

| Pillar | Geopolitical relevance |
|--------|------------------------|
| **Quantum computing** | Break certain crypto; accelerate simulation/ML (future, uncertain timeline) |
| **Quantum simulation** | Materials, drug discovery |
| **Quantum communication** | Eavesdropping detectable via measurement disturbance |
| **Quantum sensors** | Detection, navigation, defense |

**Reality check:** Qubits decohere; results probabilistic; isolation extremely hard — **monitor, don’t over-weight in 12-month vendor decisions**.

---

## Corporate response checklist (subsidiary GM/PM)

1. **Map the stack** — which layer(s) does this decision touch?  
2. **Identify chokepoints** — single-source EDA, fab, cloud region, model API?  
3. **Classify control exposure** — dual-use, entity list, data residency (counsel)  
4. **Scenario plan** — denial, degraded SKU, local alternative, timeline to switch  
5. **Align narrative** — HQ, regulators, customers (see [exec-comms playbook](../../playbooks/exec-comms.md))  
6. **Monitoring triggers** — rule changes, supplier M&A, fab disruption, new entity listings  

---

## Exclusions (not in vault)

Team project guidance, personal presentations, role-play scripts, exam answers. Raw HBR case PDF remains in OneDrive.

---

## Source

OneDrive: `Spring 2026\SBMT6012 Geopolictics of Emerging Tech` — lectures 0–3, syllabus, Nvidia HBR case (`_725009-PDF-ENG`), mini-case company/gov briefs.


---

## Source: MGMT6501Q Communication (exec comms)

# MGMT6501Q — Communication for Business Leaders cheat sheet

> HKUST Spring 2026 · Pass/Fail · Distilled for **exec-comms playbook** · **Done 2026-07-27**  
> Attach when audience is HQ, board, C-suite, crisis comms, or difficult 1:1

---

## Core premise

**Business communication = sharing** thoughts so the audience **remembers, feels, and acts** as you intend.

**Success measures:**
- **Content:** Substantial + Consequential  
- **Delivery:** Efficient + Effective  

**Mindset:** Communication starts with **clear thinking and active listening**, not the mouth.

---

## Universal prep — three questions (always)

Before any message (email, speech, meeting, Q&A):

| # | Question | Label |
|---|----------|-------|
| 1 | What do I want them to **remember**? | Substantial |
| 2 | How do I want them to **feel**? | Effective |
| 3 | What do I want them to **do**? | Consequential |

After delivery: ask the audience the same three — **gap = improvement target**.

**Also confirm:** Audience · Channel (1:many / 1:1 / many:many) · Communication style · Success metric.

---

## Munter communication strategy (four lenses)

1. **Communicator strategy** — credibility, goals  
2. **Audience strategy** — knowledge, expectations, bias, resistance  
3. **Message strategy** — structure, tell/sell/consult/join  
4. **Channel choice** — medium fit  

**Styles:**

| Style | When |
|-------|------|
| **Tell** | Inform; low resistance |
| **Sell** | Persuade; need buy-in |
| **Consult** | Input before decision |
| **Join** | Co-create; high engagement |

---

## Session map (course arc)

| Session | Mode | Skill |
|---------|------|-------|
| **1** | One-to-many | 90-sec speech; feedback ABCD |
| **2** | One-on-one | Investigative/persuasive interview; appraisal |
| **3** | Many-to-many (I) | HBR summarization/elaboration + Q&A |
| **4** | Many-to-many (II) | Crisis meeting + press conference (Tylenol) |

---

## Feedback — ABCD model (giving)

- **Acceptable** · **Balanced** · **Constructive** · **Direct**  
- Substantial · Consequential  
- Describe **facts + impact** — not character attacks  
- Three conversions: Past→Future · Problem→Opportunity · Opinion→Suggestion  

**Receiving:** Feedback is a gift; clarify; don't defend; keep own judgment.

**Peer feedback triad:** (1) What do you remember? (2) How do you feel? (3) What will you do?

---

## One-to-one interviews — prep checklist

1. Objective?  
2. Style (tell/sell/consult/join)?  
3. Credibility with counterpart?  
4. What do they know/expect?  
5. Current situation & bias?  
6. Interest level in your message?  
7. Difficulty of requested action?  
8. What will persuade them?  
9. Message structure?  

**Observer role:** Manager's manager — escalation path visible.

**Appraisal pattern:** Hidden rating expectations → negotiate agreement → summarize next steps.

---

## Many-to-many — HBR presentation (2 min + Q&A)

**Summarization:** Distill article to **professional lessons** — not article replay.  
**Elaboration:** Deep-dive one concept (e.g., Chinese negotiation element) with examples.

**Roles:** Presenter · Q&A responder · Closer (90 sec)  
**Visual aids:** Support message — don't compete.

---

## Crisis comms — Tylenol simulation framework

### Internal crisis meeting

- Assign chair, timekeeper, minutes  
- Round 1: **What should we do?** (recall scope, tampering hypothesis, credo)  
- Round 2: **What do we say? Who speaks?**  
- Debrief meeting effectiveness  

### Press conference objectives (same three questions)

1. What should the world **remember**?  
2. How should people **feel**?  
3. What should they **do**?  

**Deliverables:** ≤90 sec prepared statement · named spokespeople · impromptu Q&A prep  

### Stakeholder tensions (generic crisis pattern)

| Role | Typical pull |
|------|--------------|
| CEO | Long-term trust, credo |
| Finance | Minimize liability, stock |
| Legal | Say little |
| PR/Comms | Fast public guidance |
| Medical | Public safety first |
| Marketing | Brand survival |
| Plant/Ops | Exonerate operations |

**J&J Credo anchor:** Patients/customers first — decision filter under conflict.

**Lesson:** Responsible leadership = **align words and actions** under multi-stakeholder stress; Q&A discipline matters as much as opening statement.

---

## Q&A and listening (Session 3 readings — concepts)

- **Five kinds of listening** (HBR): discriminate content, understand, remember, evaluate, respond — match mode to question type  
- **Promise-based management:** Execution via explicit commitments between parties  
- **Communication that blocks learning:** Defensive routines, mixed messages — diagnose before persuading  

---

## Upward brief pattern (HQ / board)

```markdown
## Ask (one sentence)
## Why now
## Recommendation
## Options considered (2–3 lines)
## Risks / asks of HQ
## Decision needed by (date)
```

---

## Quality bar (playbook checklist)

- [ ] Ask / recommendation in first 5 lines  
- [ ] No unexplained jargon  
- [ ] High-sensitivity detail stripped from forwardable draft  
- [ ] Clear owner and date for next step  

---

## Exclusions

Role-play personal scenarios (Jamie/Bobby, Chris/Sandy), peer evaluation forms, personal Tylenol Q&A prep docs, videos. HBR PDFs with empty OCR — frameworks taken from **Student Notes** and course structure.

---

## Source

OneDrive: `Spring 2026\MGMT6501Q Communication for Business Leaders` — Student Notes PDF, session structure, Tylenol case materials (generic crisis framework only).


---

## Source: ISOM5120 Visualizing Data (data story)

# ISOM5120 — Visualizing Data for Business Decisions cheat sheet

> HKUST Spring 2026 · Jean Wang · Distilled for **data-story-brief playbook** · **Done 2026-07-27**  
> Attach when user needs chart choice, dashboard brief, or executive data story

---

## Core premise

**Data visualization** turns granular data into **understandable, decision-oriented** views — static or interactive.  
Goal is not "show all data" but **support a business decision** with the right encoding, story flow, and audience takeaway.

**Tools in course:** Tableau (primary), Power BI (comparison lab) — principles are tool-agnostic.

---

## When to use what (agent quick map)

| Question | Start with |
|----------|------------|
| What am I trying to do? | **Purpose:** Exploration · Communication · Cognition · Decision |
| Who is looking? | **Define before design** — purpose, viewers, data, message |
| Which chart? | **Insight type → chart type** (ranking, change, part-to-whole, etc.) |
| Is this dashboard or slide? | **Strategic vs operational** dashboard |
| Is the viz honest? | **Effectiveness criteria** — especially truthfulness & perceptibility |
| Symbolic vs pattern question? | Table may beat chart for **precise lookup** |

---

## Four purposes of visualization

| Purpose | Use when |
|---------|----------|
| **Exploration** | Unknown patterns; analyst drills |
| **Communication** | Fixed narrative for audience |
| **Cognition** | Understand complexity (e.g., market shift) |
| **Decision making** | Choice requires comparison to target/baseline |

**Explanatory vs exploratory:** Executives usually need **explanatory** — one primary message per view.

---

## Define before you design

| Step | Questions |
|------|-----------|
| **Purpose** | Why this viz? Goals? Polish level? Format? Interactivity? |
| **Viewers** | Who? Prior knowledge? Expectations? Detail need? |
| **Data** | Relevant fields? Raw vs aggregated? Groupings? Outliers? |
| **Message** | Takeaway? Emotion? Leftover questions? |
| **Design** | How many views? Marks/channels? Reading order? |

---

## Effectiveness criteria (check all)

| Criterion | Test |
|-----------|------|
| **Usefulness** | Shows decision-relevant information |
| **Engagement** | Connects; yields insight |
| **Aesthetics** | Clean; no decoration |
| **Perceptibility** | Eye/brain decode with minimal effort |
| **Truthfulness** | No skewed axes or misleading ratios |
| **Intuitiveness** | Easy to read |
| **Completeness** | Covers question scope — not clutter |

**5-second rule:** Key insight visible in ~5 seconds.

---

## Visual encoding — marks & channels

**Mark:** Point, line, area, bar (geometric item)  
**Channel:** Position, size, color, shape, orientation  

**Encoding = Marks + Channels** mapped to data attributes (qualitative vs quantitative).

**Channel choice rules:**
- **Quantitative magnitude** → position on common scale (best accuracy)  
- **Identity / categories** → color hue, shape (limited classes)  
- Prefer **accurate channels** for critical comparisons  

**Anscombe's quartet lesson:** Same summary stats, different stories — **always plot**.

---

## When NOT to visualize

**Symbolic questions** — precise single values ("total cases Tuesday?") → **table** often better.  
**Pattern questions** — trends, outliers, distributions → **chart**.

---

## Dashboard types

| Type | Audience | Update | Focus |
|------|----------|--------|-------|
| **Strategic / KPI** | Executives, board | Daily–quarterly | Goals vs strategy |
| **Operational** | Operators, supervisors | Real-time/near-real | Act on exceptions |

**Components:** Data source · metrics · charts · filters · navigation · interactivity tying views.

---

## Design principles (course checklist)

1. **5-second rule** — insight fast  
2. **Right chart type** for the analytical question  
3. **Less is more** — remove non-informative ink  
4. **Color wisely** — 5–8 distinct colors; meaning not decoration  
5. **Alignment** — related elements aligned; diverging bars when appropriate  
6. **Clear captions** — title states insight; annotate key points  
7. **White space** — guides eye; reduces cognitive load  

---

## Insight → chart type guide

| Analytical need | Common chart forms |
|-----------------|-------------------|
| **Ranking** | Ordered bar, slope graph |
| **Change over time** | Line, area, slope |
| **Part-to-whole** | Stacked bar (careful), treemap, waffle |
| **Distribution** | Histogram, box plot, violin |
| **Correlation** | Scatter, bubble |
| **Deviation from target** | Bar + reference line, bullet chart |
| **Magnitude comparison** | Bar (start at zero) |
| **Flow / process** | Sankey (when justified) |
| **Spatial** | Map (only if geography is the insight) |

**Re-chart same data** when question changes (e.g., yearly trend vs cumulative return vs range).

---

## Visual analytics (exploration layer)

Techniques in course labs:
- **Calculated fields** · **table calculations** (% of total, period change)  
- **Reference lines / parameters** — adjustable goals (e.g., profit margin threshold)  
- **Trend lines & forecast** — describe model; show confidence when useful  
- **Cluster analysis** — segment profiling after clustering  

Use when audience must **drill** — pair with guardrails so they don't drown.

---

## Story flow (executive brief)

1. **Context** — what decision, what data  
2. **So what** — primary insight (one sentence)  
3. **Options / variance** — vs target, baseline, or scenario B  
4. **Ask / next step** — owner, date  

---

## Data caveats block (always include)

- Metric definitions · aggregation level · time window  
- Missing data / sample bias  
- **What NOT to show** — clutter, raw rows, sensitive identifiers  

**Sensitivity:** Aggregate, index, or delay if High tier — per playbook.

---

## Exclusions

Personal final project submission, `.twbx` workbooks, lab CSV/XLS datasets. Lecture 4 slides not separately filed — Week 3–4 lab PDFs cover dashboard + visual analytics techniques.

---

## Source

OneDrive: `Spring 2026\ISOM5120 Visualizaing Data for Business Decisions` — syllabus, lec1–3 PDFs, lab1–5 PDFs, project brief.

## References

Munzner *Visualization Analysis & Design* · Wilke *Fundamentals of Data Visualization* · Wexler et al. *Big Book of Dashboards*


---
