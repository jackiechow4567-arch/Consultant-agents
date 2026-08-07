"""Generate gem-system-prompts.md from agent markdown files."""

from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
AGENTS = VAULT / "agents"
OUT = Path(__file__).resolve().parent / "gem-system-prompts.md"

NAMES = [
    ("00", "Router / Chief of Staff", "00-router.md"),
    ("01", "Strategy & Marketing", "01-strategy-marketing.md"),
    ("02", "Finance & Accounting", "02-finance-accounting.md"),
    ("03", "Operations & Clinical PM", "03-operations-clinical-pm.md"),
    ("04", "Product / GM", "04-product-gm.md"),
    ("05", "Tech & Geopolitics", "05-tech-geopolitics.md"),
]

REPLACEMENTS = [
    ("consultant-agents/mba-notes/", ""),
    ("consultant-agents/industry/", ""),
    ("If `mba-notes/<CODE>/cheat-sheet.md` exists, prefer citing it over generic textbook recall.",
     "Prefer uploaded MBA cheat sheets in your knowledge pack over generic textbook recall."),
    ("If `mba-notes/FINA5120/cheat-sheet.md` or `mba-notes/ACCT5100/cheat-sheet.md` exists, prefer citing it.",
     "Prefer uploaded FINA5120 and ACCT5100 cheat sheets in your knowledge pack."),
    ("If `mba-notes/ISOM5700/cheat-sheet.md` exists, prefer citing it.",
     "Prefer uploaded ISOM5700 cheat sheet in your knowledge pack."),
    ("If matching `mba-notes/<CODE>/cheat-sheet.md` exists, prefer citing it.",
     "Prefer uploaded MBA cheat sheets in your knowledge pack."),
    ("`playbooks/exec-comms.md`", "exec-comms patterns (MGMT6501Q in knowledge pack)"),
    ("`playbooks/data-story-brief.md`", "data-story patterns (ISOM5120 in knowledge pack)"),
    ("`playbooks/decision-one-pager.md`", "decision one-pager structure"),
    ("`playbooks/project-risk-resource.md`", "RAID / project-risk structure"),
    ("`playbooks/finance-qa-brief.md`", "finance Q&A brief structure"),
    ("`industry/role-pm.md`", "role-pm section in knowledge pack"),
    ("`industry/role-gm.md`", "role-gm section in knowledge pack"),
    ("`industry/role-clinical-pm.md`", "role-clinical-pm section in knowledge pack"),
    ("`consultant-agents/industry/role-pm.md`", "role-pm section in knowledge pack"),
    ("`consultant-agents/industry/role-gm.md`", "role-gm section in knowledge pack"),
    ("`consultant-agents/industry/role-clinical-pm.md`", "role-clinical-pm section in knowledge pack"),
    ("`consultant-agents/industry/pm-reference/_index.md`", "pm-reference topics in role-pm"),
    ("`consultant-agents/industry/cpm-reference/_index.md`", "cpm-reference topics in role-clinical-pm"),
    ("`01-strategy-marketing.md`", "Gem 01"),
    ("`02-finance-accounting.md`", "Gem 02"),
    ("`03-operations-clinical-pm.md`", "Gem 03"),
    ("`04-product-gm.md`", "Gem 04"),
    ("`05-tech-geopolitics.md`", "Gem 05"),
    ("Always read `", "Refer to knowledge pack: "),
    ("read `", "refer to knowledge pack: "),
    ("Use `frameworks.md`", "Use deeper frameworks sections in knowledge pack if present"),
    ("Use `career-hooks.md`", "Use career-hooks sections in knowledge pack if present"),
    ("sources `mba-notes/MGMT6501Q/cheat-sheet.md`", "MGMT6501Q section in knowledge pack"),
    ("sources `mba-notes/ISOM5120/cheat-sheet.md`", "ISOM5120 section in knowledge pack"),
    ("→ `frameworks.md` → `career-hooks.md`", "sections in knowledge pack"),
    ("cheat-sheet.md` → `frameworks.md` → `career-hooks.md`", "cheat-sheet sections in knowledge pack"),
]


def main() -> None:
    parts = [
        "# Gemini Gem System Prompts",
        "",
        "Copy each fenced block into the matching Gem **Instructions** field.",
        "Upload the matching `*-knowledge.md` file as Gem **Knowledge**.",
        "",
        "---",
        "",
    ]
    for num, title, fname in NAMES:
        text = (AGENTS / fname).read_text(encoding="utf-8")
        if "---" in text:
            text = text.split("---", 1)[1].lstrip()
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        parts.extend([
            f"## Gem {num} — {title}",
            "",
            "```",
            text.strip(),
            "```",
            "",
            "---",
            "",
        ])
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUT.name} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
