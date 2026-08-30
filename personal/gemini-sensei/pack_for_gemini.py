#!/usr/bin/env python3
"""Build a Gemini-upload folder from repo materials that are safe for Sensei."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
DROP = REPO / "personal" / "japanese-lessons"
OUT = ROOT / "upload-this"
SAFE_NAME = "knowledge-clinic-public-jp.md"

EXCLUDED = [
    ("Root hematology PDFs (published papers)", "Work library, not Japanese lessons. Use work Gem 04 + Gemini Enterprise if needed — not personal Sensei."),
    ("industry/pm-reference/BESREMi_Clinic_Contact_Report_Jackie.xlsx", "High. Real clinic contacts. Never upload to Gemini."),
    ("work-briefs/", "High. Local only."),
]


def main() -> None:
    if (ROOT / "export_knowledge.py").exists():
        subprocess.check_call(["python3", str(ROOT / "export_knowledge.py")])
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    copied: list[str] = []
    for src in (
        ROOT / "knowledge-listening-lab.md",
        ROOT / SAFE_NAME,
        ROOT / "gem-instructions.md",
    ):
        if src.exists():
            shutil.copy2(src, OUT / src.name)
            copied.append(src.name)

    DROP.mkdir(parents=True, exist_ok=True)
    for path in sorted(DROP.iterdir()):
        if path.name.startswith(".") or path.suffix.lower() not in {".md", ".txt", ".pdf"}:
            continue
        shutil.copy2(path, OUT / path.name)
        copied.append(f"japanese-lessons/{path.name}")

    manifest = [
        "# Gemini Sensei upload pack",
        "",
        "Upload every `*.md` in this folder to the **personal** Sensei Gem → Knowledge.",
        "Do not upload the excluded files below.",
        "",
        "## Included",
        "",
        *[f"- `{name}`" for name in copied],
        "",
        "## Excluded (still in the repo, not for personal Gemini)",
        "",
    ]
    for item, why in EXCLUDED:
        manifest += [f"- **{item}** — {why}", ""]
    manifest += [
        "## Work materials (already a Gemini pack)",
        "",
        "MBA + industry notes are already in `gem-knowledge-pack/*-knowledge.md`.",
        "Those go to the six **work** Gems, not Sensei.",
        "",
        "## Add more Japanese files later",
        "",
        "Put Low-sensitivity textbooks in `personal/japanese-lessons/`, then run:",
        "",
        "```",
        "python pack_for_gemini.py",
        "```",
        "",
    ]
    (OUT / "MANIFEST.md").write_text("\n".join(manifest), encoding="utf-8")
    print(f"wrote {OUT} ({len(copied)} lesson files)")


if __name__ == "__main__":
    main()
