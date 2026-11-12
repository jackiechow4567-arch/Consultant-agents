# physician-pubs-bot

Medical Affairs agent: monitor target physicians’ **PubMed** publications, score relevance to your TA (default MPN/PV), dedupe by PMID, and produce MSL-ready briefs.

## Quick start

```bash
cd physician-pubs-bot
# Edit roster.yaml (physicians only — no NCBI signup)
npm run check
npx @grok/agent-sdk validate --dir .
npx @grok/agent-sdk dev
```

Model turns need `npx @grok/agent-sdk login` or `CURSOR_API_KEY`.

## Configuration

| File | Purpose |
|------|---------|
| [`roster.yaml`](roster.yaml) | Physicians, TA keywords, `lookback_months` |
| [`SCOPE.md`](SCOPE.md) | Default scope decisions |
| `PHYSICIAN_PUBS_ROSTER` | Optional env override path to roster file |

**No NCBI account or API application.** See [`docs/self-service-research.md`](docs/self-service-research.md).

## Tier A (optional alerts — skip if not wanted)

PubMed email/RSS alerts need a My NCBI login: [`docs/tier-a-pubmed-setup.md`](docs/tier-a-pubmed-setup.md).

## HKUST full-text workflow (human step)

The bot **does not** use institutional login or scrape paywalls.

1. Copy **DOI** (or PMID) from tool output.
2. Connect via **HKUST VPN** if your library requires it.
3. Use **Find@HKUST** or the [library ejournals portal](https://library.hkust.edu.hk/) to open the publisher copy.
4. Save PDFs to your local evidence library (e.g. repo `industry/pm-reference/` index).
5. For external LLM summarization, de-identify per your privacy policy first.

## Schedule

No built-in weekly cron — run `fetch_publications` / `scan_roster` when you need an update. To automate later, add a file under `bot/schedules/` only if your org allows it.

## Tools

- `fetch_publications` — one physician from PubMed
- `scan_roster` — all physicians + `host.kv` PMID dedupe
- `resolve_author` — OpenAlex disambiguation

## Tests

```bash
npx @grok/agent-sdk tool call fetch_publications --dir . --input '{"physician_id":"dr_gisslinger"}'
npx @grok/agent-sdk eval --dir . --tag smoke
```

## Sensitivity

Use public metadata only in roster files. Do not commit internal target-tiering or employer strategy notes.
