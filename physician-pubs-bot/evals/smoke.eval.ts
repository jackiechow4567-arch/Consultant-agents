import { defineEval } from "@grok/agent-sdk/evals";

export default defineEval({
  tags: ["smoke"],
  description: "scan_roster calls PubMed for roster physicians.",
  async test(t) {
    await t.send(
      'Call scan_roster with physician_ids ["dr_gisslinger"] and min_relevance 0. Summarize how many publications were returned.'
    );
    t.succeeded();
    t.calledTool("scan_roster");
  },
});
