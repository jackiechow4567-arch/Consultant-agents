#!/usr/bin/env python3
"""Offline bond ETF sleeve map via yfinance (fallback when IB TWS is not running).

For individual bond screening, use bond_screen_ib.py + TWS.
See investment/SETUP-IB-TWS.md and investment/playbooks/bond-screen.md.
"""

from __future__ import annotations

import argparse
import json
import sys

DEFAULT_SYMBOLS = [
    "SHY",  # short Treasury
    "IEF",  # 7-10y Treasury
    "TLT",  # long Treasury
    "AGG",  # US aggregate
    "BND",  # Vanguard aggregate
    "LQD",  # investment grade credit
    "HYG",  # high yield
    "TIP",  # inflation-linked
]

SLEEVE_MAP = {
    "SHY": "Short government / cash-like",
    "IEF": "Intermediate government",
    "TLT": "Long government",
    "AGG": "Core aggregate",
    "BND": "Core aggregate",
    "LQD": "Investment grade credit",
    "HYG": "High yield credit",
    "TIP": "Inflation-linked",
}


def fetch_row(symbol: str) -> dict:
    import yfinance as yf

    t = yf.Ticker(symbol)
    info = t.info or {}
    hist = t.history(period="1mo")
    last_close = float(hist["Close"].iloc[-1]) if len(hist) else None
    return {
        "symbol": symbol,
        "name": info.get("shortName") or info.get("longName") or symbol,
        "sleeve": SLEEVE_MAP.get(symbol, info.get("category", "Other")),
        "category": info.get("category"),
        "yield": info.get("yield") or info.get("dividendYield"),
        "beta_3y": info.get("beta3Year"),
        "expense_ratio": info.get("annualReportExpenseRatio"),
        "close": last_close,
        "currency": info.get("currency", "USD"),
    }


def run_screen(symbols: list[str]) -> list[dict]:
    rows = []
    for sym in symbols:
        try:
            rows.append(fetch_row(sym.upper()))
        except Exception as exc:  # noqa: BLE001
            rows.append({"symbol": sym.upper(), "error": str(exc)})
    return rows


def print_table(rows: list[dict]) -> None:
    headers = ["symbol", "sleeve", "yield", "beta_3y", "close", "category"]
    print(f"{'Symbol':<8} {'Sleeve':<28} {'Yield':>8} {'Beta3y':>8} {'Close':>10}")
    print("-" * 70)
    for r in rows:
        if "error" in r:
            print(f"{r['symbol']:<8} ERROR: {r['error']}")
            continue
        yld = r.get("yield")
        yld_s = f"{yld*100:.2f}%" if isinstance(yld, (int, float)) else "n/a"
        beta = r.get("beta_3y")
        beta_s = f"{beta:.2f}" if isinstance(beta, (int, float)) else "n/a"
        close = r.get("close")
        close_s = f"{close:.2f}" if isinstance(close, (int, float)) else "n/a"
        print(f"{r['symbol']:<8} {r.get('sleeve','')[:28]:<28} {yld_s:>8} {beta_s:>8} {close_s:>10}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Bond ETF sleeve map (yfinance)")
    parser.add_argument(
        "--symbols",
        default=",".join(DEFAULT_SYMBOLS),
        help="Comma-separated ETF symbols (default: core FI map)",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    symbols = [s.strip() for s in args.symbols.split(",") if s.strip()]
    rows = run_screen(symbols)

    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        print("# Bond / FI ETF sleeve map (yfinance)", file=sys.stderr)
        print_table(rows)
        print(
            "\n# Use with investment/playbooks/bond-screen.md for FINA5120 framing.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
