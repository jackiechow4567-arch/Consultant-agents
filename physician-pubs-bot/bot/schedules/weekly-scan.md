---
cron: "0 8 * * 1"
---

Run a weekly publication scan for Medical Affairs:

1. Call **scan_roster** with default options (`min_relevance` 1, mark seen in kv).
2. For each physician with **new_publications** where **relevance ≥ 2**, call **fetch_publications** for that `physician_id` and draft the MSL brief using the output template in your instructions.
3. Summarize in one message: table of new hits (PMID required), plus per-physician hooks for scientific exchange (no promotional claims).
4. Remind the user to pull full text via HKUST Find@HKUST using DOI/PMID — do not attempt paywall access.
