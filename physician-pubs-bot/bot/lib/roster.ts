import fs from "node:fs";
import path from "node:path";
import { parse as parseYaml } from "yaml";
import { projectRoot } from "./project-root.js";
import type { PhysicianEntry, RosterConfig } from "./types.js";

let cached: RosterConfig | null = null;

export function rosterPath(customPath?: string): string {
  if (customPath) {
    return path.resolve(customPath);
  }
  const envPath = process.env.PHYSICIAN_PUBS_ROSTER;
  if (envPath) {
    return path.resolve(envPath);
  }
  return path.join(projectRoot(), "roster.yaml");
}

export function loadRoster(customPath?: string): RosterConfig {
  const file = rosterPath(customPath);
  if (!customPath && cached && file === rosterPath()) {
    return cached;
  }
  const raw = fs.readFileSync(file, "utf8");
  const data = parseYaml(raw) as RosterConfig;
  if (!data?.physicians?.length) {
    throw new Error(`No physicians in roster: ${file}`);
  }
  if (!customPath) {
    cached = data;
  }
  return data;
}

export function getPhysician(
  roster: RosterConfig,
  physicianId: string
): PhysicianEntry | undefined {
  return roster.physicians.find((p) => p.id === physicianId);
}

/** PubMed author clauses from display name "Last, First Middle" → `Last F[Author]`. */
export function pubmedAuthorTerms(physician: PhysicianEntry): string[] {
  const terms: string[] = [];
  const display = physician.display_name.trim();
  const comma = display.indexOf(",");
  if (comma > 0) {
    const last = display.slice(0, comma).trim();
    const rest = display.slice(comma + 1).trim();
    const firstInitial = rest.charAt(0);
    if (last && firstInitial) {
      terms.push(`${last} ${firstInitial}[Author]`);
    }
    if (last) {
      terms.push(`${last}[Author]`);
    }
  } else {
    terms.push(`${display}[Author]`);
  }
  for (const v of physician.name_variants ?? []) {
    terms.push(`${v}[Author]`);
  }
  return [...new Set(terms)];
}
