# ISOM5020 — Frameworks reference

> Companion to [cheat-sheet.md](cheat-sheet.md). Agent 05 reads cheat-sheet first.

---

## 1. Course arc

```
MODULE 1: MANAGING IT (INTERNAL)              MODULE 2: MANAGING TECHNOLOGY (EXTERNAL)
────────────────────────────────              ─────────────────────────────────────
To IT? → Finance → Governance → Outsourcing    Disruptive vs sustaining
→ Implement → Secure → Projects                RPV + spin-off / acquire
         │                                              │
         └────────── "Business decision, not tech" ────┘
```

---

## 2. IT governance — alignment workflow

```
STEP 1: What decision category?
        Principles | Architecture | Infrastructure | Applications | Investment
        │
STEP 2: Who decides today? (Archetype)
        │
STEP 3: Company strategic focus?
        Profit → centralize | Growth → decentralize | ROA → IT in room
        │
STEP 4: Misalignment?
        YES → predict failure mode (cost, speed, integration)
        │
STEP 5: Fix = reassign authority + stakeholder management
        │
STEP 6: Link to business outcome metric
```

---

## 3. Governance matrix (template)

| Decision | Current archetype | Strategy fit? | Recommended | IT in room? |
|----------|-------------------|---------------|-------------|-------------|
| Architecture | | | | Required |
| Infrastructure | | | | Required |
| Investment | | | | Duopoly/Federal |
| Applications | | | | Context-dependent |

---

## 4. RPV — disruption diagnosis

```
New tech appears (worse on mainstream metrics, better for niche)
        │
        ▼
Can incumbent VALUES fund it? (market size, margin)
        │
        NO ──► Deprioritized / killed
        │
        YES
        │
        ▼
Can incumbent PROCESSES execute? (workflow, incentives)
        │
        NO ──► Spin-off or acquire (keep separate)
        │
        YES ──► Internal venture (still hard)
```

---

## 5. Cloud decision tree

```
What sensitivity tier?
        │
        ├── High / regulated ──► Private or hybrid slice; counsel on residency
        ├── Moderate ──► Hybrid or SaaS with DPA
        └── Low / generic ──► Public SaaS/IaaS
        │
        ▼
SaaS vs PaaS vs IaaS by control need and internal skill
        │
        ▼
Vendor lock-in + exit cost (pairs with SBMT6012G chokepoints)
```

---

## 6. ERP / CRM implementation checklist

| Phase | Gate |
|-------|------|
| Scope | One module / one process first |
| Process | Redesign before config |
| Integration | Legacy data mapping explicit |
| Governance | Sponsor + duopoly steering |
| Adoption | Training metrics, not go-live alone |
| ROI | Lagging indicators — set expectations |

---

## 7. Security — manager balance

```
Asset criticality ranking
        │
        ▼
Threat likelihood (phishing, ransomware, insider, supply chain)
        │
        ▼
Controls: patch cadence, access, training, IR plan
        │
        ▼
Residual risk accepted by leadership (documented)
```

---

## 8. Project methodology selector

| Signal | Lean toward |
|--------|-------------|
| Fixed regulatory spec | Waterfall phases |
| UI/requirements emerge in use | Agile iterations |
| Vendor package config | Hybrid (waterfall plan, agile config sprints) |
| Scope creep history | Change control board + executive sponsor |

---

## 9. Agent 05 crosswalk

| ISOM5020 framework | Agent section |
|--------------------|---------------|
| Governance alignment | Tech-strategy lens — internal capability |
| Cloud/ERP/CRM choice | Options table — ops burden |
| RPV / disruption | Recommendation — build/buy/partner |
| Security balance | Risks + monitoring triggers |
| SBMT6012G handoff | Geopolitical lens when supplier geography matters |
