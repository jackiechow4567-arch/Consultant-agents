import type { PubMedArticle } from "./types.js";

const BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils";
const MIN_INTERVAL_MS = 340;

let lastFetchAt = 0;

async function throttle(): Promise<void> {
  const now = Date.now();
  const wait = MIN_INTERVAL_MS - (now - lastFetchAt);
  if (wait > 0) {
    await new Promise((r) => setTimeout(r, wait));
  }
  lastFetchAt = Date.now();
}

function ncbiQuery(ncbi: NcbiConfig): string {
  return `tool=${encodeURIComponent(ncbi.tool)}&email=${encodeURIComponent(ncbi.email)}`;
}

export type NcbiConfig = { tool: string; email: string };

function mindateFromMonths(months: number): string {
  const d = new Date();
  d.setMonth(d.getMonth() - months);
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${y}/${m}/${day}`;
}

export function buildPubmedQuery(
  authorTerms: string[],
  affiliations: string[] | undefined,
  taKeywords: string[] | undefined
): string {
  const authorClause =
    authorTerms.length === 1
      ? authorTerms[0]
      : `(${authorTerms.join(" OR ")})`;
  const parts = [authorClause];
  if (affiliations?.length) {
    const aff = affiliations
      .map((a) => `${a}[Affiliation]`)
      .join(" OR ");
    parts.push(`(${aff})`);
  }
  if (taKeywords?.length) {
    const kw = taKeywords
      .slice(0, 8)
      .map((k) => `"${k}"[Title/Abstract]`)
      .join(" OR ");
    parts.push(`(${kw})`);
  }
  return parts.join(" AND ");
}

export async function pubmedSearchIds(
  term: string,
  ncbi: NcbiConfig,
  lookbackMonths: number,
  retmax = 50
): Promise<string[]> {
  await throttle();
  const mindate = mindateFromMonths(lookbackMonths);
  const url =
    `${BASE}/esearch.fcgi?db=pubmed&retmode=json&retmax=${retmax}` +
    `&sort=date&datetype=edat&mindate=${encodeURIComponent(mindate)}` +
    `&term=${encodeURIComponent(term)}&${ncbiQuery(ncbi)}`;
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`PubMed esearch failed: ${res.status}`);
  }
  const json = (await res.json()) as {
    esearchresult?: { idlist?: string[] };
  };
  return json.esearchresult?.idlist ?? [];
}

function textOf(el: Element | null): string {
  return el?.textContent?.trim() ?? "";
}

function parsePubmedXml(xml: string): PubMedArticle[] {
  const articles: PubMedArticle[] = [];
  const blocks = xml.split(/<PubmedArticle>/);
  for (const block of blocks.slice(1)) {
    const pmid = block.match(/<PMID[^>]*>(\d+)<\/PMID>/)?.[1];
    if (!pmid) continue;
    const title = textFromTag(block, "ArticleTitle");
    const journal = textFromTag(block, "Title");
    const year =
      block.match(/<PubDate>[\s\S]*?<Year>(\d+)<\/Year>/)?.[1] ?? "";
    const month =
      block.match(/<PubDate>[\s\S]*?<Month>(\w+)<\/Month>/)?.[1] ?? "";
    const day =
      block.match(/<PubDate>[\s\S]*?<Day>(\d+)<\/Day>/)?.[1] ?? "";
    const pubDate = [year, month, day].filter(Boolean).join(" ");
    const abstractParts = [
      ...block.matchAll(
        /<AbstractText[^>]*>([\s\S]*?)<\/AbstractText>/g
      ),
    ].map((m) => stripTags(m[1]));
    const abstract = abstractParts.join(" ").trim();
    const doi =
      block.match(/<ArticleId IdType="doi">([^<]+)<\/ArticleId>/)?.[1] ??
      null;
    const authors = [
      ...block.matchAll(/<LastName>([^<]+)<\/LastName>/g),
    ].map((m) => m[1]);
    articles.push({
      pmid,
      title,
      journal,
      pubDate,
      doi,
      abstract,
      authors,
    });
  }
  return articles;
}

function textFromTag(block: string, tag: string): string {
  const m = block.match(new RegExp(`<${tag}[^>]*>([\\s\\S]*?)<\\/${tag}>`));
  return m ? stripTags(m[1]) : "";
}

function stripTags(s: string): string {
  return s.replace(/<[^>]+>/g, "").trim();
}

export async function pubmedFetchArticles(
  ids: string[],
  ncbi: NcbiConfig
): Promise<PubMedArticle[]> {
  if (ids.length === 0) return [];
  await throttle();
  const url =
    `${BASE}/efetch.fcgi?db=pubmed&retmode=xml&id=${ids.join(",")}` +
    `&${ncbiQuery(ncbi)}`;
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`PubMed efetch failed: ${res.status}`);
  }
  const xml = await res.text();
  return parsePubmedXml(xml);
}

export function pubmedLink(pmid: string): string {
  return `https://pubmed.ncbi.nlm.nih.gov/${pmid}/`;
}

export function hkustFindAtHint(doi: string | null, pmid: string): string {
  if (doi) {
    return `HKUST Library: search DOI "${doi}" via Find@HKUST / ejournals (VPN if required).`;
  }
  return `HKUST Library: open PubMed ${pubmedLink(pmid)} and use Find@HKUST for full text.`;
}
