---
name: consultant-router
description: >-
  Routes MBA and industry consulting questions to the right specialist agent,
  sensitivity tier, and tool (Cursor, Gemini Enterprise, Perplexity). Use when
  the user asks for a consultant, chief of staff routing, which agent to use,
  privacy/sensitivity tier, or starts a strategy, finance, operations, clinical
  PM, product, GM, tech strategy, or geopolitics decision task. Do not use for
  Japanese teaching — that is `@japanese-teacher` / Gemini Sensei only.
---

# Consultant Router

## Japanese teaching is out of scope

If the user asks for Japanese, JLPT, 日本語, Sensei, listening practice, or language drills:

- Stop. Do **not** route to SM / FA / OC / PG / TG.
- Tell them to use `@japanese-teacher`, the personal Gemini Gem **Sensei**, or `personal/japanese-listening-lab/`.
- Do not load `personal/japanese-*` into a work consultant.
- Do not load work files (`industry/`, `mba-notes/`, `gem-knowledge-pack/`, root PDFs, clinic contacts) into a Japanese agent.

## Instructions

1. Read and follow:
   - `consultant-agents/agents/00-router.md`
   - `consultant-agents/privacy-policy.md`
2. If missing, ask at most 4 questions: decision goal, sensitivity (Low/Mid/High), constraints, role lens (CPM/PM/GM).
3. If sensitivity is unclear, default one tier higher and say why.
4. Pick **one primary** and at most one support:
   - SM → `agents/01-strategy-marketing.md`
   - FA → `agents/02-finance-accounting.md`
   - OC → `agents/03-operations-clinical-pm.md`
   - PG → `agents/04-product-gm.md`
   - TG → `agents/05-tech-geopolitics.md`
5. Attach playbooks when needed (`exec-comms`, `data-story-brief`, `decision-one-pager`, etc.).
6. Point to role memory: `industry/role-pm.md` / `role-gm.md` / `role-clinical-pm.md`.
7. Output in the router’s fixed format. Do not deep-analyze before sensitivity is set.

## After routing

Offer to continue as the primary specialist (read that agent file and proceed), or tell the user which Cursor skill to invoke next.
