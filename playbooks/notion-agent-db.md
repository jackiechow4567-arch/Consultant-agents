# Playbook: Notion databases for consultant agents

Purpose: store durable outputs and knowledge from Cursor / Gemini / Perplexity agents in Notion — without dumping high-sensitivity raw material.

**Privacy rule (same as vault):** High sensitivity → de-identify first → then log Mid/Low summary only.

---

## Recommended design (two databases)

Do **not** put everything in one mega-table. Use two linked DBs.

### DB A — `Agent Outputs` (decision / memo log)

One row = one agent deliverable you want to keep.

| Property | Type | Options / notes |
|----------|------|-----------------|
| Name | Title | Short decision title |
| Date | Date | When produced |
| Agent | Select | Router, Strategy-Marketing, Finance-Accounting, Ops-ClinicalPM, Product-GM, Tech-Geopolitics |
| Role lens | Select | CPM, PM, GM |
| Sensitivity | Select | Low, Mid, High (High rows should only contain de-identified text) |
| Output type | Select | Decision one-pager, RAID, Finance Q&A, Exec brief, Tech risk memo, Routing brief, Other |
| Status | Select | Draft, Final, Shared with HQ, Archived |
| Recommendation | Text | One-line “Do X; don’t Y” |
| Audience | Select | Self, Team, HQ, Board, Partner |
| Tools used | Multi-select | Cursor, Gemini, Perplexity |
| MBA frameworks | Multi-select | Free tags e.g. Five Forces, NPV, RAID, STP |
| Tags | Multi-select | Product, Clinical, Finance, Geopolitics, HK, etc. |
| Related knowledge | Relation | → DB B |
| Source vault path | URL / Text | Optional local path or Gemini link |
| Body | Page content | Full memo (markdown pasted into page) |

### DB B — `Agent Knowledge` (reusable memory)

One row = a durable note (role rule, industry fact, MBA cheat point).

| Property | Type | Options / notes |
|----------|------|-----------------|
| Name | Title | e.g. “PM: do/don’t on claims” |
| Type | Select | Role memory, MBA note, Industry, Playbook lesson, Glossary |
| Agent affinity | Multi-select | Same agent list as DB A |
| Role lens | Multi-select | CPM, PM, GM |
| Sensitivity | Select | Low, Mid |
| Course code | Select | ACCT5100, ECON5110, … (optional) |
| Last reviewed | Date | |
| Related outputs | Relation | → DB A |
| Body | Page content | Distilled bullets only |

---

## Prompt 1 — Create the databases in Notion

Paste into Notion AI, or ask Cursor after Notion is connected:

```text
Create two Notion databases for my MBA consultant-agent system.

Database 1 title: Agent Outputs
Properties:
- Name (title)
- Date (date)
- Agent (select): Router, Strategy-Marketing, Finance-Accounting, Ops-ClinicalPM, Product-GM, Tech-Geopolitics
- Role lens (select): CPM, PM, GM
- Sensitivity (select): Low, Mid, High
- Output type (select): Decision one-pager, RAID, Finance Q&A, Exec brief, Tech risk memo, Routing brief, Other
- Status (select): Draft, Final, Shared with HQ, Archived
- Recommendation (text)
- Audience (select): Self, Team, HQ, Board, Partner
- Tools used (multi-select): Cursor, Gemini, Perplexity
- MBA frameworks (multi-select)
- Tags (multi-select)
- Source vault path (text)

Database 2 title: Agent Knowledge
Properties:
- Name (title)
- Type (select): Role memory, MBA note, Industry, Playbook lesson, Glossary
- Agent affinity (multi-select): Router, Strategy-Marketing, Finance-Accounting, Ops-ClinicalPM, Product-GM, Tech-Geopolitics
- Role lens (multi-select): CPM, PM, GM
- Sensitivity (select): Low, Mid
- Course code (select): ACCT5100, ECON5110, ISOM5020, MARK5120, FINA5120, ISOM5120, ISOM5700, MGMT5410, MGMT6501Q, MGMT6501T, SBMT6012G, MGMT6501W, MGMT5590
- Last reviewed (date)

Then create a two-way relation:
- Agent Outputs ↔ Agent Knowledge
  (Outputs property: Related knowledge; Knowledge property: Related outputs)

Add three views on Agent Outputs:
1. Board — table, sorted by Date descending
2. By Agent — board grouped by Agent
3. HQ-ready — filter Status = Final OR Shared with HQ, Sensitivity ≠ High

Put both databases under a page titled: Consultant Agents Hub
```

---

## Prompt 2 — After any agent run: format a Notion row (Cursor / Gemini)

Append this to the end of an agent conversation:

```text
Format your final answer for my Notion database "Agent Outputs".

1) Give a property block I can paste (or that an automation can map):

Name:
Date: YYYY-MM-DD
Agent: [Router | Strategy-Marketing | Finance-Accounting | Ops-ClinicalPM | Product-GM | Tech-Geopolitics]
Role lens: [CPM | PM | GM]
Sensitivity: [Low | Mid | High]
Output type: [Decision one-pager | RAID | Finance Q&A | Exec brief | Tech risk memo | Routing brief | Other]
Status: Draft
Recommendation: [one sentence Do X / don't Y]
Audience: [Self | Team | HQ | Board | Partner]
Tools used: [Cursor and/or Gemini and/or Perplexity]
MBA frameworks: [comma-separated]
Tags: [comma-separated]
Source vault path: [if any]

2) Then give PAGE BODY in clean Markdown (max ~800 words) with:
- Conclusion / recommendation first
- Assumptions
- Options (if any)
- Risks
- Next actions

Rules:
- If Sensitivity would be High, REWRITE the body to Mid (de-identified) and set Sensitivity: Mid.
- Never include patient identifiers, exact contract clauses, or precise confidential amounts.
- Do not invent property values; use UNKNOWN if missing.
```

---

## Prompt 3 — Distill durable knowledge into DB B

Use when something should become reusable memory (not a one-off memo):

```text
From this conversation, extract 1–5 durable knowledge items for my Notion database "Agent Knowledge".

For each item provide:
Name:
Type: [Role memory | MBA note | Industry | Playbook lesson | Glossary]
Agent affinity:
Role lens:
Sensitivity: [Low | Mid only]
Course code: [if applicable, else none]
Last reviewed: YYYY-MM-DD
Body: (5–10 bullets max, actionable, de-identified)

Skip one-off project trivia. Prefer decision rules, do/don't, frameworks, and stakeholder patterns.
If nothing is durable, say: NO_KNOWLEDGE_ROWS
```

---

## Prompt 4 — Router: always end with Notion logging block

Add to Router (`00`) conversations or Gem instructions:

```text
At the end of every routing or specialist deliverable, append a section:

## Notion log (Agent Outputs)
[fill Prompt 2 property block + short body]

If the user said "save to knowledge", also append:

## Notion knowledge candidates
[Prompt 3 items]
```

---

## Prompt 5 — Weekly review in Notion AI

```text
Using my "Agent Outputs" database from the last 14 days:
1) List decisions still Status = Draft that need Final
2) Cluster by Agent and Role lens
3) Extract 5 lessons worth promoting into "Agent Knowledge"
4) Flag any row that looks too sensitive for Notion (names, money, clinical IDs) and suggest a redacted rewrite
```

---

## Prompt 6 — Cursor skill-style one-liner (daily habit)

```text
Use product-gm-consultant (or whichever agent). When done, also output a Notion Agent Outputs property block + page body per my playbook notion-agent-db.md. De-identify if needed.
```

---

## What not to store in Notion

| Keep out | Where instead |
|----------|----------------|
| Patient / subject identifiers | Local `work-briefs/` only |
| Contract full text, exact unreleased financials | Local vault |
| Raw Perplexity thread dumps | Distill first |
| High-sensitivity originals | De-identify → Mid summary in Notion |

Notion is for **searchable Mid/Low decision memory**, not your confidential source archive.

---

## Optional views & automations later

- Filter: Role lens = GM + Output type = Decision one-pager  
- Template button: “New decision memo” with Prompt 2 checklist  
- Relation: link each Output to 1–3 Knowledge rows after weekly review  
