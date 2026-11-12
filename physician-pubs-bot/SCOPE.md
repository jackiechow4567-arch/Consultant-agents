# Scope decisions (defaults)

Confirmed implementation choices for Medical Affairs physician publication monitoring:

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Roster size | **Up to ~30 physicians** | Tier A + bot design tuned for small KOL lists; scale via batching in schedule |
| Therapeutic area | **MPN / PV / haematology-oncology** | Aligns with `industry/pm-reference/pv-clinical-evidence.md` in this repo |
| Delivery | **Agent SDK (Tier C)** + Tier A spreadsheet | Scheduled scan + deterministic PubMed tools; Grok system prompt in `bot/instructions.md` |
| Geography | **Global authors, HK affiliation hints optional** | PubMed + OpenAlex disambiguation via affiliation strings on roster |
| Sensitivity | **Low/Mid** — public metadata only | No paywall scraping; roster is name + affiliation + optional ORCID |

Override TA keywords and physicians in [`roster.yaml`](roster.yaml).
