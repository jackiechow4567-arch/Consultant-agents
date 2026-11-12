import { defineTool } from "@grok/agent-sdk/tools";
import * as z from "zod/v4";
import {
  buildPubmedQuery,
  hkustFindAtHint,
  pubmedFetchArticles,
  pubmedLink,
  pubmedSearchIds,
} from "../lib/pubmed.js";
import { scoreRelevance } from "../lib/relevance.js";
import {
  getPhysician,
  loadRoster,
  pubmedAuthorTerms,
} from "../lib/roster.js";

export default defineTool({
  description:
    "Fetch recent PubMed publications for a roster physician. Returns PMIDs, abstracts, relevance scores, and HKUST full-text hints.",
  effect: "read",
  inputSchema: z.object({
    physician_id: z.string(),
    use_ta_filter_in_query: z
      .boolean()
      .optional()
      .describe(
        "If true, AND the PubMed query with TA keywords (may miss papers). Default false."
      ),
    retmax: z.number().int().min(1).max(100).optional(),
  }),
  async execute({ physician_id, use_ta_filter_in_query, retmax }) {
    const roster = loadRoster();
    const physician = getPhysician(roster, physician_id);
    if (!physician) {
      return { error: `Unknown physician_id: ${physician_id}` };
    }
    const authorTerms = pubmedAuthorTerms(physician);
    const term = buildPubmedQuery(
      authorTerms,
      physician.affiliations,
      use_ta_filter_in_query ? roster.therapeutic_area.keywords : undefined
    );
    const ids = await pubmedSearchIds(
      term,
      roster.ncbi,
      roster.lookback_months,
      retmax ?? 30
    );
    const articles = await pubmedFetchArticles(ids, roster.ncbi);
    const rows = articles.map((a) => {
      const rel = scoreRelevance(a, roster);
      return {
        pmid: a.pmid,
        pubmed_url: pubmedLink(a.pmid),
        title: a.title,
        journal: a.journal,
        pub_date: a.pubDate,
        doi: a.doi,
        relevance: rel.score,
        matched_keywords: rel.matchedKeywords,
        excluded: rel.excluded,
        abstract_preview: a.abstract.slice(0, 400),
        full_text_hint: hkustFindAtHint(a.doi, a.pmid),
      };
    });
    return {
      physician: {
        id: physician.id,
        display_name: physician.display_name,
      },
      pubmed_query: term,
      lookback_months: roster.lookback_months,
      count: rows.length,
      publications: rows,
    };
  },
});
