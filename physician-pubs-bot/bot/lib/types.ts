export type RosterConfig = {
  lookback_months: number;
  therapeutic_area: {
    keywords: string[];
    exclude: string[];
  };
  ncbi: {
    tool: string;
    email: string;
  };
  physicians: PhysicianEntry[];
};

export type PhysicianEntry = {
  id: string;
  display_name: string;
  affiliations?: string[];
  name_variants?: string[];
  orcid?: string;
};

export type PubMedArticle = {
  pmid: string;
  title: string;
  journal: string;
  pubDate: string;
  doi: string | null;
  abstract: string;
  authors: string[];
};

export type RelevanceResult = {
  score: number;
  matchedKeywords: string[];
  excluded: boolean;
  excludeReason: string | null;
};

export type OpenAlexAuthor = {
  id: string;
  displayName: string;
  orcid: string | null;
  worksCount: number;
  lastKnownInstitutions: string[];
};
