#!/usr/bin/env python3
"""Build a weekday JLaw brief: Stage 2 screen + sector rank + optional earnings dates."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from jlaw_stage2_screen import dataframe_to_markdown, default_columns, run_screen


def sector_rank(df, top_n: int = 8):
    if df is None or "sector" not in df.columns:
        return []
    buckets: dict[str, list] = defaultdict(list)
    for _, row in df.iterrows():
        sector = row.get("sector") or "Unknown"
        buckets[str(sector)].append(row)
    ranked = []
    for sector, rows in buckets.items():
        perfs = [r.get("Perf.1M") for r in rows if r.get("Perf.1M") == r.get("Perf.1M")]
        avg = sum(float(p) for p in perfs) / len(perfs) if perfs else 0.0
        ranked.append((sector, len(rows), avg))
    ranked.sort(key=lambda x: (x[1], x[2]), reverse=True)
    return ranked[:top_n]


def _yf_symbol(symbol: str) -> str:
    return str(symbol).strip().split(":")[-1]


def _earnings_from_ticker(symbol: str):
    import io
    from contextlib import redirect_stderr, redirect_stdout

    import yfinance as yf  # type: ignore

    sink = io.StringIO()
    raw = None
    try:
        with redirect_stderr(sink), redirect_stdout(sink):
            t = yf.Ticker(_yf_symbol(symbol))
            for attr in ("calendar", "earnings_dates"):
                try:
                    raw = getattr(t, attr)
                    if callable(raw):
                        raw = raw()
                    if raw is not None:
                        break
                except Exception:
                    continue
    except Exception:
        return None
    if raw is None:
        return None
    # DataFrame indexed by datetime
    try:
        import pandas as pd

        if isinstance(raw, pd.DataFrame) and len(raw):
            idx = raw.index
            next_dt = None
            now = datetime.now(timezone.utc)
            for ts in idx:
                ts_dt = ts.to_pydatetime() if hasattr(ts, "to_pydatetime") else ts
                if getattr(ts_dt, "tzinfo", None) is None:
                    ts_dt = ts_dt.replace(tzinfo=timezone.utc)
                if ts_dt >= now - timedelta(days=1):
                    next_dt = ts_dt
                    break
            if next_dt is None:
                next_dt = idx[0].to_pydatetime() if hasattr(idx[0], "to_pydatetime") else idx[0]
            return next_dt
        if isinstance(raw, dict):
            for key in ("Earnings Date", "earningsDate"):
                if key in raw:
                    val = raw[key]
                    if isinstance(val, (list, tuple)) and val:
                        return val[0]
                    return val
    except Exception:
        return None
    return None


def fetch_earnings(tickers: list[str], max_names: int = 10) -> dict[str, str]:
    out: dict[str, str] = {}
    try:
        import yfinance  # noqa: F401
    except ImportError:
        return out
    for symbol in tickers[:max_names]:
        yf_symbol = str(symbol).split(":")[-1]
        try:
            dt = _earnings_from_ticker(yf_symbol)
            if dt is None:
                continue
            if hasattr(dt, "date"):
                out[symbol] = dt.date().isoformat()
            else:
                out[symbol] = str(dt)[:10]
        except Exception:
            continue
    return out


def render_brief(df, total: int, earnings: dict[str, str], quality: bool) -> str:
    today = date.today().isoformat()
    lines = [
        f"# Daily brief — {today} (scanner)",
        "",
        "## Disclaimer",
        "Research support only — not investment advice. No orders placed.",
        "",
        "## Tape",
        "- Regime: TBD (Bot fills from index vs 50/200 and breadth — do not invent)",
        "- Scanner: TradingView Stage 2"
        + (" quality filters on" if quality else " hard filters only"),
        f"- Scanner matches (hard filters): {total}",
        f"- Rows returned: {0 if df is None else len(df)}",
        "",
        "## Sector leadership",
    ]
    ranked = sector_rank(df)
    if not ranked:
        lines.append("_no sector data_")
    else:
        lines.append("| Sector | # leaders | 1M avg % |")
        lines.append("| --- | --- | --- |")
        for sector, n, avg in ranked:
            lines.append(f"| {sector} | {n} | {avg:.1f} |")

    lines.extend(["", "## Actionable shortlist (≤10)"])
    if df is None or len(df) == 0:
        lines.append("_no rows — say the feed failed; do not reuse stale prices_")
        return "\n".join(lines) + "\n"

    top = df.head(10).copy()
    if earnings and "ticker" in top.columns:
        top["earnings"] = top["ticker"].map(lambda x: earnings.get(str(x), ""))
    cols = default_columns(top)
    if "earnings" in top.columns:
        cols = cols + ["earnings"]
    lines.append(dataframe_to_markdown(top, cols))
    lines.extend(
        [
            "",
            "## Appendix (remaining scanner rows)",
            dataframe_to_markdown(df.iloc[10:25], default_columns(df))
            if len(df) > 10
            else "_none_",
            "",
            "## Catalyst calendar",
            "_Bot: run News & 催化劑 on the shortlist. Earnings dates above are yfinance hints only._",
            "",
            "## Explicitly not doing",
            "- Averaging down",
            "- Buying cheap / thin / laggard names",
            "- Treating this table as a breakout list (pivot / RS still need a chart)",
            "",
            "## Next 3",
            "1. Classify tape regime before acting",
            "2. Chart the top 2 names against investment/knowledge/buy-checklist.md",
            "3. Tag earnings <10 sessions as HOLD-SIZE-RISK",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="JLaw daily brief (Stage 2 + sectors)")
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--hard-only", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--markdown", action="store_true", default=True)
    parser.add_argument("--out", type=Path, help="Write markdown to this path")
    parser.add_argument(
        "--earnings",
        action="store_true",
        help="Optional yfinance earnings dates (Bot web search is preferred)",
    )
    args = parser.parse_args()

    quality = not args.hard_only
    total, df = run_screen(limit=args.limit, quality=quality)
    print(f"# Stage2 scanner total (hard filters): {total}", file=sys.stderr)
    print(f"# Returned rows: {0 if df is None else len(df)}", file=sys.stderr)

    if args.json:
        if df is None:
            print("[]")
        else:
            print(df.to_json(orient="records"))
        return 0

    tickers = []
    if df is not None and "ticker" in df.columns:
        tickers = [str(x) for x in df["ticker"].head(10).tolist()]
    earnings = fetch_earnings(tickers) if args.earnings else {}

    text = render_brief(df, total, earnings, quality=quality)
    print(text)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        print(f"# wrote {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
