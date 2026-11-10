#!/usr/bin/env python3
"""Fail if the Medical Affairs library drops a figure the agent is expected to cite."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "industry" / "ma-reference" / "evidence-ropeg.md"
RULES = ROOT / "industry" / "ma-reference" / "response-rules.md"
CATALOG = ROOT / "industry" / "ma-reference" / "library-catalog.md"

REQUIRED = {
    EVIDENCE: [
        "0.94 versus 0.82",
        "0.34",
        "5/95 (5.3%)",
        "12/74 (16.2%)",
        "62/94 (66.0%)",
        "14/72 (19.4%)",
        "54.5%",
        "34.9%",
        "p = 0.0974",
        "52/64 (81%)",
        "32/63 (51%)",
        "2.91 versus 4.17",
        "8/29 (27.6%)",
        "NCT04285086",
        "250 µg",
        "n=20",
        "Eight cycles",
    ],
    RULES: [
        "without symptomatic splenomegaly",
        "Not a proactive topic",
        "pegylated interferon alfa-2a",
        "treating physician decides",
        "pregnancy",
    ],
    CATALOG: [
        "2023 Gisslinger.pdf",
        "2022 Kiladjian.pdf",
        "2023 Barbui.pdf",
        "2022 Edahiro.pdf",
        "2025 Pei.pdf",
        "20230508162013_1_slideshow.pdf",
        "43.1%",
    ],
}


def main() -> None:
    missing = []
    for path, needles in REQUIRED.items():
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                missing.append(f"{path.name}: missing {needle!r}")
    if missing:
        raise SystemExit("\n".join(missing))
    print(f"Medical Affairs library check passed ({sum(len(v) for v in REQUIRED.values())} anchors).")


if __name__ == "__main__":
    main()
