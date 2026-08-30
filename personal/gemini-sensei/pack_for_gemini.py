#!/usr/bin/env python3
"""Pack Japanese-lesson files only. Ignores the rest of the repo."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
DROP = REPO / "personal" / "japanese-lessons"
OUT = ROOT / "upload-this"
OK_SUFFIX = {".md", ".txt", ".pdf"}


def main() -> None:
    subprocess.check_call(["python3", str(ROOT / "export_knowledge.py")])
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    copied: list[str] = []
    src = ROOT / "knowledge-listening-lab.md"
    shutil.copy2(src, OUT / src.name)
    copied.append(src.name)

    DROP.mkdir(parents=True, exist_ok=True)
    for path in sorted(DROP.iterdir()):
        if path.name.startswith(".") or path.name.lower() == "readme.md":
            continue
        if path.suffix.lower() not in OK_SUFFIX:
            continue
        shutil.copy2(path, OUT / path.name)
        copied.append(f"japanese-lessons/{path.name}")

    (OUT / "MANIFEST.md").write_text(
        "\n".join(
            [
                "# Japanese-only Gemini pack",
                "",
                "Upload the `knowledge-*.md` files (and any lesson PDFs) to the personal Sensei Gem.",
                "This pack does not include work agents, MBA notes, or product files.",
                "",
                "## Included",
                "",
                *[f"- `{name}`" for name in copied],
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"wrote {OUT} ({len(copied)} Japanese files)")


if __name__ == "__main__":
    main()
