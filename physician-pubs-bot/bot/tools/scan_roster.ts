import { defineTool } from "@grok/agent-sdk/tools";
import * as z from "zod/v4";
import {
  buildPubmedQuery,
  pubmedFetchArticles,
  pubmedSearchIds,
} from "../lib/pubmed.js";
import { filterNewPmids, markSeenPmids } from "../lib/kv-seen.js";
import { scoreRelevance } from "../lib/relevance.js";
import {
  getPhysician,
  loadRoster,
  pubmedAuthorTerms,
} from "../lib/roster.js";

export default defineTool({
  description:
    "Scan all physicians on the roster via PubMed, score relevance, dedupe by PMID in host.kv, and return new hits since last scan.",
  effect: "idempotent",
  inputSchema: z.object({
    physician_ids: z
      .array(z.string())
      .optional()
      .describe("Subset to scan; default all roster physicians"),
    include_seen: z
      .boolean()
      .optional()
      .describe("Return previously seen PMIDs too"),
    mark_seen: z
      .boolean()
      .optional()
      .describe("Record returned PMIDs in kv (default true)"),
    min_relevance: z
      .number()
      .int()
      .min(0)
      .max(3)
      .optional()
      .describe("Only return rows at or above this score (default 1)"),
  }),
  async execute(
    { physician_ids, include_seen, mark_seen, min_relevance },
    ctx
  ) {
    const roster = loadRoster();
    const ids =
      physician_ids?.length ? physician_ids : roster.physicians.map((p) => p.id);
    const minRel = min_relevance ?? 1;
    const shouldMark = mark_seen !== false;
    type PubRow = {
      pmid: string;
      title: string;
      journal: string;
      pub_date: string;
      doi: string | null;
      relevance: number;
      matched_keywords: string[];
      excluded: boolean;
    };
    const results: Array<{
      physician_id: string;
      display_name: string;
      new_publications: PubRow[];
      pubmed_query: string;
    }> = [];

    for (const physicianId of ids) {
      const physician = getPhysician(roster, physicianId);
      if (!physician) {
        results.push({
          physician_id: physicianId,
          display_name: "(unknown)",
          new_publications: [],
          pubmed_query: "",
        });
        continue;
      }
      const authorTerms = pubmedAuthorTerms(physician);
      const term = buildPubmedQuery(
        authorTerms,
        physician.affiliations,
        undefined
      );
      const pmids = await pubmedSearchIds(
        term,
        roster.ncbi,
        roster.lookback_months,
        40
      );
      const newIds = await filterNewPmids(
        ctx.host.kv,
        physicianId,
        pmids,
        include_seen === true
      );
      const articles = await pubmedFetchArticles(newIds, roster.ncbi);
      const pubs = articles
        .map((a) => {
          const rel = scoreRelevance(a, roster);
          return {
            pmid: a.pmid,
            title: a.title,
            journal: a.journal,
            pub_date: a.pubDate,
            doi: a.doi,
            relevance: rel.score,
            matched_keywords: rel.matchedKeywords,
            excluded: rel.excluded,
          };
        })
        .filter((p) => !p.excluded && p.relevance >= minRel);

      if (shouldMark && articles.length > 0) {
        await markSeenPmids(
          ctx.host.kv,
          physicianId,
          articles.map((a) => a.pmid)
        );
      }

      results.push({
        physician_id: physicianId,
        display_name: physician.display_name,
        pubmed_query: term,
        new_publications: pubs,
      });
    }

    await ctx.host.kv.put("last_scan_at", new Date().toISOString());

    return {
      last_scan_at: new Date().toISOString(),
      physicians_scanned: results.length,
      results,
      instructions:
        "Format MSL briefs from this JSON using bot/instructions.md. Fetch abstracts with fetch_publications for detail.",
    };
  },
});
