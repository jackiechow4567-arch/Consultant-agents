# Gemini Gems — Knowledge Pack & System Prompts

> Generated for HKUST MBA × industry consultant agents (PharmaEssentia HK subsidiary).  
> **2026-07-27**

## Quick setup (6 Gems)

1. In [Google AI Studio → Gems](https://aistudio.google.com/), create **6 custom Gems**.
2. For each Gem, paste the **system instruction** from [`gem-system-prompts.md`](gem-system-prompts.md) (section matching the Gem number).
3. Upload **one** knowledge file per Gem (this folder):

| Gem | Name | Knowledge file | Size |
|-----|------|----------------|------|
| **00** | Router / Chief of Staff | [`00-router-knowledge.md`](00-router-knowledge.md) | ~15 KB |
| **01** | Strategy & Marketing | [`01-strategy-marketing-knowledge.md`](01-strategy-marketing-knowledge.md) | ~67 KB |
| **02** | Finance & Accounting | [`02-finance-accounting-knowledge.md`](02-finance-accounting-knowledge.md) | ~14 KB |
| **03** | Ops & Clinical PM | [`03-ops-clinical-pm-knowledge.md`](03-ops-clinical-pm-knowledge.md) | ~29 KB |
| **04** | Product / GM | [`04-product-gm-knowledge.md`](04-product-gm-knowledge.md) | ~100 KB (includes GM reference + HK NDA / “1+”) |
| **05** | Tech & Geopolitics | [`05-tech-geopolitics-knowledge.md`](05-tech-geopolitics-knowledge.md) | ~30 KB |

4. **Workflow:** Open Gem **00** first → paste your question + any context → follow routing to Gem 01–05.

## Tool & sensitivity rules (all Gems)

| Tier | Tool |
|------|------|
| **Low** | Gemini / Perplexity (public research) |
| **Mid** | Gemini only after de-identifying internal details |
| **High** | Cursor + local vault only — export de-identified conclusions to Gemini |

**Never** upload to Gemini: raw trial data, unpublished dossiers, contract annexes, patient identifiers, or full financial models with sensitive subsidiary numbers.

## What each knowledge pack contains

| Pack | MBA courses | Role memory |
|------|-------------|-------------|
| 00 | MGMT6501Q, MGMT5590 | — |
| 01 | MGMT5410, MARK5120, ECON5110 | role-pm.md |
| 02 | FINA5120, ACCT5100 | — |
| 03 | ISOM5700 | role-clinical-pm.md |
| 04 | MGMT6501T, MGMT6501W, MGMT5590, MGMT5410 | role-gm.md, role-pm.md, gm-reference, hk-nda-registration |
| 05 | ISOM5020, SBMT6012G, MGMT6501Q, ISOM5120 | — |

## Refreshing after vault updates

Re-run from vault root (or ask Cursor):

```powershell
python consultant-agents/gem-knowledge-pack/build.py
python consultant-agents/gem-knowledge-pack/gen-prompts.py
```

Then re-upload changed `*-knowledge.md` files to the matching Gem.

## Cursor parity

Same agent logic lives in:

- `consultant-agents/agents/00-router.md` … `05-tech-geopolitics.md`
- Cursor skills: `/consultant-router`, `/strategy-marketing`, `/finance-accounting`, `/ops-clinical-pm`, `/product-gm`, `/tech-geopolitics`

Gemini Gems = same prompts + this knowledge pack. Cursor also reads live vault paths and `work-briefs/` for High sensitivity.
