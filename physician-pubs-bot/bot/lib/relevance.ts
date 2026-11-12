import type { PubMedArticle, RelevanceResult, RosterConfig } from "./types.js";

function norm(s: string): string {
  return s.toLowerCase().replace(/\s+/g, " ");
}

export function scoreRelevance(
  article: PubMedArticle,
  roster: RosterConfig
): RelevanceResult {
  const blob = norm(`${article.title} ${article.abstract}`);
  const { keywords, exclude } = roster.therapeutic_area;

  for (const ex of exclude) {
    if (blob.includes(norm(ex))) {
      return {
        score: 0,
        matchedKeywords: [],
        excluded: true,
        excludeReason: ex,
      };
    }
  }

  const matched = keywords.filter((k) => blob.includes(norm(k)));
  let score = 0;
  if (matched.length >= 3) score = 3;
  else if (matched.length === 2) score = 2;
  else if (matched.length === 1) score = 1;
  else score = 0;

  return {
    score,
    matchedKeywords: matched,
    excluded: false,
    excludeReason: null,
  };
}
