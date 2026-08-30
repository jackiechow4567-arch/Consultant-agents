#!/usr/bin/env python3
"""Turn the listening-lab clips into a Gemini Gem knowledge file."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LAB = ROOT.parent / "japanese-listening-lab"
OUT = ROOT / "knowledge-listening-lab.md"
TRACKS = {
    "n5": "N5 daily",
    "n4": "N4 daily",
    "n3": "N3 work",
    "med": "Clinic / healthcare (generic only)",
}


def main() -> None:
    raw = (LAB / "lessons.js").read_text(encoding="utf-8")
    lessons = json.loads(raw.split("=", 1)[1].strip().rstrip(";"))
    lines = [
        "# Jackie Japanese curriculum (from Cursor listening lab)",
        "",
        "Source: Consultant-agents `personal/japanese-listening-lab/`.",
        "Sensitivity: Low. Original learner sentences. No real patient, physician, hospital, or product names.",
        "",
        "How to teach from this file:",
        "- Recycle these sentences. Do not invent a parallel textbook.",
        "- One sitting = 2–4 clips from the same track.",
        "- For dictation, hide the English until he answers.",
        "- Clinic track is generic medical Japanese only.",
        "",
    ]
    current = None
    for item in lessons:
        if item["track"] != current:
            current = item["track"]
            lines += [f"## {TRACKS.get(current, current)}", ""]
        q = item["quiz"]
        answer = q["choices"][q["answer"]]
        lines += [
            f"### {item['id']} — {item['title']}",
            f"- Japanese: {item['jp']}",
            f"- Kana: {item['kana']}",
            f"- English: {item['en']}",
            f"- Check: {q['q']}",
            f"- Answer: {answer}",
            "",
        ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes, {len(lessons)} clips)")


if __name__ == "__main__":
    main()
