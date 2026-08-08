#!/usr/bin/env python3
"""JLaw-style Stage 2 screen via TradingView scanner (no API key)."""

from __future__ import annotations

import argparse
import sys

from tradingview_screener import Column, Query


def run_screen(limit: int = 50, quality: bool = True) -> tuple[int, object]:
    """Return (total_matches, dataframe) for Stage 2 hard filters."""
    filters = [
        Column("is_primary") == True,  # noqa: E712
        Column("type") == "stock",
        Column("exchange").isin(["NYSE", "NASDAQ", "AMEX"]),
        Column("close") > Column("SMA200"),
        Column("market_cap_basic") > 2_000_000_000,
        Column("Value.Traded") > 30_000_000,  # ~$30M daily dollar volume proxy
        Column("beta_1_year") >= 1.0,
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
    if quality and len(df):
        df = df[
            (df["close"] >= df["price_52_week_high"] * 0.75)
            & (df["close"] >= df["price_52_week_low"] * 1.30)
        ].copy()
        df["pct_from_high"] = (df["close"] / df["price_52_week_high"] - 1.0) * 100.0
        df = df.head(limit)
    return total, df


def main() -> int:
    parser = argparse.ArgumentParser(description="JLaw Stage 2 TradingView screen")
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--hard-only", action="store_true", help="Skip quality MA/near-high filters")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of table")
    args = parser.parse_args()

    total, df = run_screen(limit=args.limit, quality=not args.hard_only)
    print(f"# Stage2 scanner total (hard filters): {total}", file=sys.stderr)
    print(f"# Returned rows: {len(df)}", file=sys.stderr)

    if args.json:
        print(df.to_json(orient="records"))
    else:
        cols = [
            c
            for c in [
                "ticker",
                "name",
                "close",
                "sector",
                "beta_1_year",
                "Perf.W",
                "Perf.1M",
                "Perf.3M",
                "pct_from_high",
                "Value.Traded",
                "market_cap_basic",
            ]
            if c in df.columns
        ]
        print(df[cols].to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
