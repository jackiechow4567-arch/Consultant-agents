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
