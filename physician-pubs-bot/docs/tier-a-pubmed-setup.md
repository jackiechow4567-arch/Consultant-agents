# Tier A — PubMed alerts (no code)

Use this while the Agent SDK bot is in dev, or as a permanent backstop.

## Spreadsheet

Maintain [`tier-a-pubmed-roster.csv`](tier-a-pubmed-roster.csv) with one row per target physician.

| Column | Purpose |
|--------|---------|
| `pubmed_author_query` | Paste into PubMed Advanced Search (Author field) |
| `pubmed_saved_search_url` | Link after you save the search |
| `alert_email_notes` | How you set email/RSS frequency |

## Per-physician setup

1. Open [PubMed Advanced Search](https://pubmed.ncbi.nlm.nih.gov/advanced/).
2. Author: `LastInitial[Author]` e.g. `Gisslinger H[Author]`.
3. Optional **Affiliation** filter if the name is common.
4. Optional **Title/Abstract** filter with TA keywords (MPN, polycythemia vera, etc.).
5. **Search** → **Create RSS** or **Save search** → **Email alerts** (requires free NCBI account).
6. Copy the query string into the CSV.

## Tips

- Add ORCID to the row when known; use ORCID in PubMed if indexed.
- For very common surnames, always combine author + affiliation + one TA keyword.
- Alerts cover **new PubMed records**; the bot still helps with **relevance scoring** and **MSL briefs**.
