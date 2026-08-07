# Playbook: Distill a Perplexity Space into Cursor role memory

Use this when moving history from Perplexity Spaces (Product Manager, General Manager, Clinical PM / FDA) into the local consultant vault.

## Goal

Produce a **1–3 page role card** agents can load — not a dump of chat transcripts.

## Sensitivity first

| If the Space contains… | Do this |
|------------------------|---------|
| Public research, frameworks, generic PM practice | Distill into `industry/role-*.md` (low/mid) |
| Internal roadmap, names, money, clinical detail | Draft in `work-briefs/` → run `deidentify-brief` → then merge safe parts into `industry/` |
| Patient / inspection raw evidence | Keep high; **never** paste back into Perplexity to “summarize” |

## Steps (Product Manager Space — start here)

1. In Perplexity, open Space **Product Manager**.
2. Pick the **10–20 highest-value threads** (decisions, playbooks, recurring advice — skip one-off trivia).
3. For each thread, copy title + your key conclusions (or Save/PDF), paste into a scratch file under `work-briefs/` if sensitive, else into chat with Cursor.
4. Ask Cursor:

```text
Distill the following Perplexity Product Manager Space excerpts into
consultant-agents/industry/role-pm.md using the existing sections.
De-identify names, exact money, and unpublished roadmap detail.
Keep decision criteria, do/don't rules, stakeholders-by-role, and lessons.
```

5. Review the updated `role-pm.md`. Delete scratch exports you no longer need.
6. Spot-check: ask `consultant-router` a PM question and confirm it cites role memory.

## What to extract

- Role definition and success metrics  
- Recurring decisions and criteria  
- Do / don’t rules  
- Preferred output formats  
- Stakeholders by **role**  
- Hard-won lessons  
- Frameworks you repeatedly used  

## What to drop

- Full Q&A transcripts  
- Long web-paraphrase answers you can re-research  
- PII, clinical identifiers, contract text, exact unreleased numbers  

## File targets

| Space | Role memory file | Primary agents |
|-------|------------------|----------------|
| Product Manager | `industry/role-pm.md` | 01, 04 |
| General Manager | `industry/role-gm.md` | 04, 00 |
| Clinical PM / FDA | `industry/role-clinical-pm.md` | 03 |

## After distillation

- Keep using Perplexity Spaces for **new low-sensitivity research** only.  
- Put durable role memory in Cursor so it survives tool/account changes.  
- Re-distill quarterly or after major role shifts.
