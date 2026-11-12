# Self-service research (no NCBI signup, no alerts)

You do **not** need to register with NCBI, apply for API access, or turn on email/RSS alerts.

## What “NCBI” meant in the bot

The bot reads **public** PubMed metadata (same as searching in a browser). There is:

- No employer authorization step  
- No NCBI account  
- No notifications unless you host a schedule yourself (this project ships **without** a weekly cron)

Optional `ncbi.email` in `roster.yaml` is only a courtesy label on API requests. Leave it out entirely.

## Recommended workflow (on demand)

1. Edit [`roster.yaml`](../roster.yaml) with your target physicians (name + affiliation).
2. Run a search when **you** want an update:

   ```bash
   cd physician-pubs-bot
   npx @grok/agent-sdk tool call fetch_publications --dir . --input '{"physician_id":"YOUR_ID"}'
   ```

   Or chat in `npx @grok/agent-sdk dev`: e.g. “scan dr_template”.

3. Open each **PMID** link in the output in your browser (no login required for abstracts).
4. For full text, use **HKUST Find@HKUST** + VPN with the DOI from the tool output.

## Manual browser-only alternative

No bot at all:

1. Go to [PubMed](https://pubmed.ncbi.nlm.nih.gov/).
2. Search: `Last F[Author]` and add affiliation or disease keywords.
3. Sort by **Date** and note PMIDs/DOIs.
4. Pull PDFs via HKUST library.

## Tier A alerts (skip)

[`tier-a-pubmed-setup.md`](tier-a-pubmed-setup.md) is for people who **want** PubMed email alerts (requires a free My NCBI login). Ignore it if you research manually.
