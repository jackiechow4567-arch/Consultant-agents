#!/usr/bin/env python3
"""Rebuild Gemini knowledge pack files from vault cheat-sheets and role memory."""

from datetime import date, datetime
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
MBA = VAULT / "mba-notes"
IND = VAULT / "industry"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else f"*(missing: {p})*"


def pack(filename: str, title: str, intro: str, sections: list[tuple[str, Path]]) -> None:
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    parts = [
        f"# {title}",
        "",
        f"> Generated {date.today().isoformat()} {datetime.now().strftime('%H:%M')} for Gemini Gem Knowledge upload.",
        f"> Rebuilt: {stamp} · Run `python build.py` after vault or gm-reference updates.",
        "> Paste the matching system instruction from `gem-system-prompts.md`.",
        "",
        intro.strip(),
        "",
        "---",
        "",
    ]
    for label, path in sections:
        parts.extend([f"## Source: {label}", "", read(path), "", "---", ""])
    dest = OUT / filename
    dest.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {dest.name} ({dest.stat().st_size // 1024} KB)")


def main() -> None:
    pack(
        "00-router-knowledge.md",
        "Gem 00 — Router Knowledge Pack",
        "Use with Gem 00 Router. Supports communication framing and ethics/sensitivity before specialist handoff.",
        [
            ("MGMT6501Q Communication", MBA / "MGMT6501Q" / "cheat-sheet.md"),
            ("MGMT5590 Responsible Leadership", MBA / "MGMT5590" / "cheat-sheet.md"),
        ],
    )
    pack(
        "01-strategy-marketing-knowledge.md",
        "Gem 01 — Strategy & Marketing Knowledge Pack",
        "Prefer these MBA cheat sheets over generic recall. Role memory when lens = PM.",
        [
            ("Role: Product Manager", IND / "role-pm.md"),
            ("MGMT5410 Strategic Management", MBA / "MGMT5410" / "cheat-sheet.md"),
            ("MARK5120 Marketing Strategy", MBA / "MARK5120" / "cheat-sheet.md"),
            ("ECON5110 Managerial Microeconomics", MBA / "ECON5110" / "cheat-sheet.md"),
        ],
    )
    pack(
        "02-finance-accounting-knowledge.md",
        "Gem 02 — Finance & Accounting Knowledge Pack",
        "Use with Gem 02 Finance & Accounting.",
        [
            ("FINA5120 Corporate Finance", MBA / "FINA5120" / "cheat-sheet.md"),
            ("ACCT5100 Corporate Reporting", MBA / "ACCT5100" / "cheat-sheet.md"),
        ],
    )
    pack(
        "03-ops-clinical-pm-knowledge.md",
        "Gem 03 — Ops & Clinical PM Knowledge Pack",
        "ISOM5700 ops frameworks + role-clinical-pm criteria.",
        [
            ("Role: Clinical Project Manager", IND / "role-clinical-pm.md"),
            ("ISOM5700 Operations Management", MBA / "ISOM5700" / "cheat-sheet.md"),
        ],
    )
    gm = IND / "gm-reference"
    pack(
        "04-product-gm-knowledge.md",
        "Gem 04 — Product / GM Knowledge Pack",
        "CEO / healthcare innovation / ethics / strategy + GM and PM role memory + HK GM reference.",
        [
            ("Role: General Manager", IND / "role-gm.md"),
            ("Role: Product Manager", IND / "role-pm.md"),
            ("GM ref: HK Employment Ordinance", gm / "hk-employment-ordinance.md"),
            ("GM ref: HK employment contracts", gm / "hk-employment-contracts.md"),
            ("GM ref: Employee handbook patterns", gm / "employee-handbook-hk-patterns.md"),
            ("GM ref: Leadership (Global Immersion)", gm / "leadership-global-immersion.md"),
            ("GM ref: Creativity & systems thinking", gm / "creativity-systems-thinking.md"),
            ("MGMT6501T Effective CEO", MBA / "MGMT6501T" / "cheat-sheet.md"),
            ("MGMT6501W Innovation in Healthcare", MBA / "MGMT6501W" / "cheat-sheet.md"),
            ("MGMT5590 Responsible Leadership", MBA / "MGMT5590" / "cheat-sheet.md"),
            ("MGMT5410 Strategic Management", MBA / "MGMT5410" / "cheat-sheet.md"),
        ],
    )
    pack(
        "05-tech-geopolitics-knowledge.md",
        "Gem 05 — Tech & Geopolitics Knowledge Pack",
        "Tech strategy + geopolitics; includes exec comms and data-viz cheat sheets for HQ narratives.",
        [
            ("ISOM5020 Technology Strategy & Management", MBA / "ISOM5020" / "cheat-sheet.md"),
            ("SBMT6012G Geopolitics of Emerging Tech", MBA / "SBMT6012G" / "cheat-sheet.md"),
            ("MGMT6501Q Communication (exec comms)", MBA / "MGMT6501Q" / "cheat-sheet.md"),
            ("ISOM5120 Visualizing Data (data story)", MBA / "ISOM5120" / "cheat-sheet.md"),
        ],
    )


if __name__ == "__main__":
    main()
