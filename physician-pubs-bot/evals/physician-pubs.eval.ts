import { defineEval, includes } from "@grok/agent-sdk/evals";

export default defineEval({
  tags: ["smoke", "pubmed"],
  description: "fetch_publications returns verifiable PMIDs for a known haematology author.",
  async test(t) {
    await t.send(
      'Call fetch_publications for physician_id "dr_gisslinger" only. Reply with a one-line count and the top PMID; do not invent papers.'
    );
    t.succeeded();
    t.calledTool("fetch_publications", {
      input: { physician_id: "dr_gisslinger" },
    });
    t.check(t.reply, includes(/PMID|\d{6,8}/));
  },
});
