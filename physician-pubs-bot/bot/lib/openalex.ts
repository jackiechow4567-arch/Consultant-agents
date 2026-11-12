import type { OpenAlexAuthor } from "./types.js";

const BASE = "https://api.openalex.org";

export async function searchOpenAlexAuthors(
  name: string,
  affiliationHint?: string
): Promise<OpenAlexAuthor[]> {
  const url =
    `${BASE}/authors?search=${encodeURIComponent(name)}&per_page=10&mailto=physician-pubs-bot@example.com`;
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`OpenAlex author search failed: ${res.status}`);
  }
  const json = (await res.json()) as {
    results?: Array<{
      id: string;
      display_name: string;
      orcid: string | null;
      works_count: number;
      last_known_institutions?: Array<{ display_name?: string }>;
    }>;
  };
  let results =
    json.results?.map((r) => ({
      id: r.id,
      displayName: r.display_name,
      orcid: r.orcid,
      worksCount: r.works_count,
      lastKnownInstitutions:
        r.last_known_institutions?.map((i) => i.display_name ?? "") ?? [],
    })) ?? [];

  if (affiliationHint) {
    const hint = affiliationHint.toLowerCase();
    results = [...results].sort((a, b) => {
      const score = (auth: OpenAlexAuthor) =>
        auth.lastKnownInstitutions.some((i) =>
          i.toLowerCase().includes(hint)
        )
          ? 1
          : 0;
      return score(b) - score(a);
    });
  }
  return results;
}
