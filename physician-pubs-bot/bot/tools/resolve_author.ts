import { defineTool } from "@grok/agent-sdk/tools";
import * as z from "zod/v4";
import { searchOpenAlexAuthors } from "../lib/openalex.js";
import { getPhysician, loadRoster } from "../lib/roster.js";

export default defineTool({
  description:
    "Disambiguate a target physician using OpenAlex (public metadata). Use before citing works if the name is ambiguous.",
  effect: "read",
  inputSchema: z.object({
    physician_id: z
      .string()
      .optional()
      .describe("Roster id from roster.yaml"),
    name: z
      .string()
      .optional()
      .describe("Display name if not using roster id"),
    affiliation_hint: z.string().optional(),
  }),
  async execute({ physician_id, name, affiliation_hint }) {
    let displayName = name;
    let hint = affiliation_hint;
    if (physician_id) {
      const roster = loadRoster();
      const p = getPhysician(roster, physician_id);
      if (!p) {
        return { error: `Unknown physician_id: ${physician_id}` };
      }
      displayName = p.display_name;
      hint = hint ?? p.affiliations?.[0];
    }
    if (!displayName) {
      return { error: "Provide physician_id or name" };
    }
    const candidates = await searchOpenAlexAuthors(displayName, hint);
    return {
      query_name: displayName,
      affiliation_hint: hint ?? null,
      candidates: candidates.slice(0, 5),
      note: "Confirm the correct author with affiliation and ORCID before MSL prep.",
    };
  },
});
