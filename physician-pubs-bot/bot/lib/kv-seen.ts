const SEEN_PREFIX = "seen_pmids:";

export type HostKv = {
  get: (key: string) => Promise<unknown>;
  put: (key: string, value: string | string[]) => Promise<void>;
};

export async function getSeenPmids(
  kv: HostKv,
  physicianId: string
): Promise<Set<string>> {
  const raw = await kv.get(`${SEEN_PREFIX}${physicianId}`);
  if (!Array.isArray(raw)) return new Set();
  return new Set(raw.filter((x) => typeof x === "string"));
}

export async function markSeenPmids(
  kv: HostKv,
  physicianId: string,
  pmids: string[]
): Promise<void> {
  const existing = await getSeenPmids(kv, physicianId);
  for (const id of pmids) existing.add(id);
  await kv.put(`${SEEN_PREFIX}${physicianId}`, [...existing]);
}

export async function filterNewPmids(
  kv: HostKv,
  physicianId: string,
  pmids: string[],
  includeSeen: boolean
): Promise<string[]> {
  if (includeSeen) return pmids;
  const seen = await getSeenPmids(kv, physicianId);
  return pmids.filter((id) => !seen.has(id));
}
