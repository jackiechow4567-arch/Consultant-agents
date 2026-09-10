#!/usr/bin/env python3
"""JLaw-style Stage 2 screen via TradingView scanner (no API key)."""

from __future__ import annotations

import argparse
import sys

from tradingview_screener import Column, Query

MIN_PRICE = 10.0
MIN_MARKET_CAP = 2_000_000_000
MIN_VALUE_TRADED = 30_000_000


def run_screen(limit: int = 50, quality: bool = True) -> tuple[int, object]:
    """Return (total_matches, dataframe) for Stage 2 hard filters."""
    filters = [
        Column("is_primary") == True,  # noqa: E712
        Column("type") == "stock",
        Column("exchange").isin(["NYSE", "NASDAQ", "AMEX"]),
        Column("close") > Column("SMA200"),
        Column("market_cap_basic") > MIN_MARKET_CAP,
        Column("Value.Traded") > MIN_VALUE_TRADED,
        Column("beta_1_year") >= 1.0,
        Column("close") >= MIN_PRICE,
    ]
    if quality:
        filters.extend(
            [
                Column("close") > Column("SMA50"),
                Column("SMA50") > Column("SMA200"),
            ]
        )

    # Pull a wider set, then apply near-high / off-low quality cuts in pandas.
    fetch_n = max(limit * 4, 200) if quality else limit
    query = (
        Query()
        .select(
            "name",
            "close",
            "market_cap_basic",
            "Value.Traded",
            "average_volume_30d_calc",
            "price_52_week_high",
            "price_52_week_low",
            "SMA50",
            "SMA200",
            "beta_1_year",
            "Perf.W",
            "Perf.1M",
            "Perf.3M",
            "sector",
            "industry",
            "relative_volume_10d_calc",
        )
        .where(*filters)
        .order_by("Perf.1M", ascending=False)
        .limit(fetch_n)
    )
    total, df = query.get_scanner_data()
    if df is None or len(df) == 0:
        return total, df
    df = enrich_screen(df)
    if quality:
        df = df[
            (df["close"] >= df["price_52_week_high"] * 0.75)
            & (df["close"] >= df["price_52_week_low"] * 1.30)
        ].copy()
        df = df.head(limit)
    else:
        df = df.head(limit)
    return total, df


def enrich_screen(df):
    """Add % distances and simple flags used by the daily brief."""
    out = df.copy()
    if "ticker" not in out.columns and out.index.name in {"ticker", "symbol"}:
        out = out.reset_index()
    elif "ticker" not in out.columns:
        out = out.reset_index()
        if "index" in out.columns and "ticker" not in out.columns:
            out = out.rename(columns={"index": "ticker"})

    close = out["close"]
    if "price_52_week_high" in out.columns:
        out["pct_from_high"] = (close / out["price_52_week_high"] - 1.0) * 100.0
    if "SMA50" in out.columns:
        out["pct_from_sma50"] = (close / out["SMA50"] - 1.0) * 100.0
    if "SMA200" in out.columns:
        out["pct_from_sma200"] = (close / out["SMA200"] - 1.0) * 100.0

    flags = []
    for _, row in out.iterrows():
        bits = []
        pct_high = row.get("pct_from_high")
        pct_50 = row.get("pct_from_sma50")
        if pct_high == pct_high and pct_high >= -5:
            bits.append("near_high")
        if pct_50 == pct_50 and pct_50 < -8:
            bits.append("gt_8pct_below_50d")
        if row.get("close", 0) < MIN_PRICE:
            bits.append("cheap")
        flags.append(",".join(bits) if bits else "")
    out["flags"] = flags
    return out


def dataframe_to_markdown(df, columns: list[str]) -> str:
    cols = [c for c in columns if c in df.columns]
    if not cols:
        return "_no columns_"
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join("---" for _ in cols) + " |"
    lines = [header, sep]
    for _, row in df.iterrows():
        cells = []
        for c in cols:
            val = row[c]
            cells.append(_fmt_cell(c, val))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def _fmt_cell(col: str, val) -> str:
    if val is None:
        return ""
    try:
        if val != val:  # NaN
            return ""
    except Exception:
        pass
    if col in {"close", "SMA50", "SMA200", "beta_1_year"}:
        try:
            return f"{float(val):.2f}"
        except (TypeError, ValueError):
            return str(val)
    if col.startswith("pct_") or col.startswith("Perf") or col == "relative_volume_10d_calc":
        try:
            return f"{float(val):.1f}" if col.startswith("pct_") or col.startswith("Perf") else f"{float(val):.2f}"
        except (TypeError, ValueError):
            return str(val)
    if col in {"Value.Traded", "market_cap_basic", "average_volume_30d_calc"}:
        try:
            num = float(val)
            if num >= 1_000_000_000:
                return f"{num / 1_000_000_000:.1f}B"
            if num >= 1_000_000:
                return f"{num / 1_000_000:.1f}M"
            return f"{num:.0f}"
        except (TypeError, ValueError):
            return str(val)
    return str(val)


def default_columns(df) -> list[str]:
    preferred = [
        "ticker",
        "name",
        "close",
        "sector",
        "beta_1_year",
        "Perf.W",
        "Perf.1M",
        "Perf.3M",
        "pct_from_high",
        "pct_from_sma50",
        "Value.Traded",
        "market_cap_basic",
        "relative_volume_10d_calc",
        "flags",
    ]
    return [c for c in preferred if c in df.columns]


def main() -> int:
    parser = argparse.ArgumentParser(description="JLaw Stage 2 TradingView screen")
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--hard-only", action="store_true", help="Skip quality MA/near-high filters")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of table")
    parser.add_argument("--markdown", action="store_true", help="Emit a markdown table")
    args = parser.parse_args()

    total, df = run_screen(limit=args.limit, quality=not args.hard_only)
    print(f"# Stage2 scanner total (hard filters): {total}", file=sys.stderr)
    print(f"# Returned rows: {0 if df is None else len(df)}", file=sys.stderr)

    if df is None or len(df) == 0:
        print("No rows.")
        return 0

    if args.json:
        print(df.to_json(orient="records"))
    elif args.markdown:
        print(dataframe_to_markdown(df, default_columns(df)))
    else:
        cols = default_columns(df)
        print(df[cols].to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
