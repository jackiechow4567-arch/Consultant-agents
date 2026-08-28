#!/usr/bin/env python3
"""Pack the listening lab into one HTML file with embedded MP3s."""

from __future__ import annotations

import base64
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "japanese-listening-lab.html"


def main() -> None:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    raw = (ROOT / "lessons.js").read_text(encoding="utf-8")
    payload = json.loads(raw.split("=", 1)[1].strip().rstrip(";"))
    for item in payload:
        mp3 = (ROOT / item["audio"]).read_bytes()
        item["audio"] = "data:audio/mpeg;base64," + base64.b64encode(mp3).decode("ascii")
    inline = "window.LESSONS = " + json.dumps(payload, ensure_ascii=False) + ";\n"
    html = html.replace(
        '<script src="lessons.js"></script>',
        "<script>\n" + inline + "</script>",
    )
    html = html.replace(
        "Neural Japanese audio is already in the folder.",
        "This is a single file: audio is embedded. Double-click it in Chrome or Edge.",
    )
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
