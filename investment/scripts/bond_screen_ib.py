#!/usr/bin/env python3
"""Bond screening via Interactive Brokers TWS / IB Gateway (ib_insync).

Requires TWS or IB Gateway running locally with API enabled.
See investment/SETUP-IB-TWS.md for one-time setup.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "bond-screens.yaml"


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def connect_ib(host: str, port: int, client_id: int, timeout: float):
    from ib_insync import IB

    ib = IB()
    ib.connect(host, port, clientId=client_id, timeout=timeout)
    return ib


def build_subscription(preset: dict[str, Any], args: argparse.Namespace):
    from ib_insync import ScannerSubscription

    sub = ScannerSubscription(
        numberOfRows=args.rows,
        instrument=preset["instrument"],
        locationCode=preset["location_code"],
        scanCode=preset["scan_code"],
    )

    if preset.get("exclude_convertible"):
        sub.excludeConvertible = True

    sp_above = args.sp_rating_above or preset.get("sp_rating_above")
    sp_below = args.sp_rating_below or preset.get("sp_rating_below")
    if sp_above:
        sub.spRatingAbove = sp_above
    if sp_below:
        sub.spRatingBelow = sp_below

    moody_above = args.moody_rating_above or preset.get("moody_rating_above")
    moody_below = args.moody_rating_below or preset.get("moody_rating_below")
    if moody_above:
        sub.moodyRatingAbove = moody_above
    if moody_below:
        sub.moodyRatingBelow = moody_below

    if args.maturity_above:
        sub.maturityDateAbove = args.maturity_above
    elif preset.get("maturity_date_above"):
        sub.maturityDateAbove = preset["maturity_date_above"]

    if args.maturity_below:
        sub.maturityDateBelow = args.maturity_below
    elif preset.get("maturity_date_below"):
        sub.maturityDateBelow = preset["maturity_date_below"]

    if args.coupon_above is not None:
        sub.couponRateAbove = args.coupon_above
    if args.coupon_below is not None:
        sub.couponRateBelow = args.coupon_below

    if args.above_price is not None:
        sub.abovePrice = args.above_price
    if args.below_price is not None:
        sub.belowPrice = args.below_price

    return sub


def contract_to_row(contract, rank: int, distance: str, benchmark: str, projection: str) -> dict:
    return {
        "rank": rank,
        "symbol": getattr(contract, "symbol", "") or "",
        "local_symbol": getattr(contract, "localSymbol", "") or "",
        "sec_type": getattr(contract, "secType", "") or "",
        "currency": getattr(contract, "currency", "") or "",
        "exchange": getattr(contract, "exchange", "") or "",
        "cusip": getattr(contract, "cusip", "") or "",
        "issuer_id": getattr(contract, "issuerId", "") or "",
        "maturity": getattr(contract, "lastTradeDateOrContractMonth", "") or "",
        "coupon": getattr(contract, "coupon", None),
        "distance": distance,
        "benchmark": benchmark,
        "projection": projection,
    }


def run_scanner(ib, sub) -> list[dict]:
    scan_data = ib.reqScannerData(sub)
    rows = []
    for idx, item in enumerate(scan_data, start=1):
        rows.append(
            contract_to_row(
                item.contractDetails.contract,
                rank=idx,
                distance=item.distance,
                benchmark=item.benchmark,
                projection=item.projection,
            )
        )
    return rows


def lookup_cusip(ib, cusip: str) -> list[dict]:
    from ib_insync import Bond

    contract = Bond(cusip=cusip)
    details = ib.reqContractDetails(contract)
    rows = []
    for idx, detail in enumerate(details, start=1):
        rows.append(contract_to_row(detail.contract, rank=idx, distance="", benchmark="", projection=""))
    return rows


def dump_scanner_params(ib, out_path: Path | None) -> str:
    xml = ib.reqScannerParameters()
    if out_path:
        out_path.write_text(xml, encoding="utf-8")
    return xml


def print_table(rows: list[dict], preset_label: str) -> None:
    print(f"# IB TWS bond screen — {preset_label}", file=sys.stderr)
    print(f"# Matches: {len(rows)}", file=sys.stderr)
    print(
        f"{'Rank':<5} {'Symbol':<12} {'CUSIP':<12} {'Maturity':<10} {'Coupon':>8} {'Currency':<8} {'Exchange'}"
    )
    print("-" * 80)
    for r in rows:
        coupon = r.get("coupon")
        coupon_s = f"{coupon:.3f}" if isinstance(coupon, (int, float)) else (coupon or "n/a")
        print(
            f"{r.get('rank', ''):<5} "
            f"{r.get('symbol', '')[:12]:<12} "
            f"{r.get('cusip', '')[:12]:<12} "
            f"{str(r.get('maturity', ''))[:10]:<10} "
            f"{coupon_s:>8} "
            f"{r.get('currency', ''):<8} "
            f"{r.get('exchange', '')}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Bond screen via IB TWS / IB Gateway")
    parser.add_argument(
        "--preset",
        default="corp-us",
        help="Preset from investment/config/bond-screens.yaml (corp-us, govt-us, muni-us, agency-us, fi-etf-us)",
    )
    parser.add_argument("--host", help="TWS host (default from config)")
    parser.add_argument("--port", type=int, help="TWS API port (7497 paper, 7496 live)")
    parser.add_argument("--client-id", type=int, help="API client id")
    parser.add_argument("--rows", type=int, help="Max rows to return")
    parser.add_argument("--maturity-above", help="Min maturity (YYYYMMDD or YYYYMM per TWS)")
    parser.add_argument("--maturity-below", help="Max maturity (YYYYMMDD or YYYYMM)")
    parser.add_argument("--sp-rating-above", help="Min S&P rating (e.g. BBB)")
    parser.add_argument("--sp-rating-below", help="Max S&P rating (e.g. AAA)")
    parser.add_argument("--moody-rating-above", help="Min Moody's rating")
    parser.add_argument("--moody-rating-below", help="Max Moody's rating")
    parser.add_argument("--coupon-above", type=float, help="Min coupon rate")
    parser.add_argument("--coupon-below", type=float, help="Max coupon rate")
    parser.add_argument("--above-price", type=float, help="Min price filter")
    parser.add_argument("--below-price", type=float, help="Max price filter")
    parser.add_argument("--cusip", help="Lookup a single bond by CUSIP instead of scanning")
    parser.add_argument(
        "--dump-scanner-params",
        metavar="FILE",
        nargs="?",
        const="investment/config/scanner-params.xml",
        help="Save TWS scanner parameter XML (run once to discover valid scan codes)",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    parser.add_argument(
        "--fallback-etf",
        action="store_true",
        help="If TWS is unreachable, run yfinance ETF map (bond_screen.py)",
    )
    args = parser.parse_args()

    cfg = load_config()
    defaults = cfg.get("defaults", {})
    presets = cfg.get("presets", {})

    if args.preset not in presets and not args.cusip and not args.dump_scanner_params:
        print(f"Unknown preset '{args.preset}'. Options: {', '.join(presets)}", file=sys.stderr)
        return 2

    host = args.host or defaults.get("host", "127.0.0.1")
    port = args.port or defaults.get("port", 7497)
    client_id = args.client_id or defaults.get("client_id", 71)
    timeout = defaults.get("timeout", 15)
    args.rows = args.rows or defaults.get("rows", 40)

    try:
        ib = connect_ib(host, port, client_id, timeout)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: Cannot connect to IB TWS at {host}:{port} — {exc}", file=sys.stderr)
        print("See investment/SETUP-IB-TWS.md to enable the API.", file=sys.stderr)
        if args.fallback_etf:
            print("Falling back to ETF map (yfinance)...", file=sys.stderr)
            import subprocess

            script = Path(__file__).parent / "bond_screen.py"
            return subprocess.call([sys.executable, str(script)])
        return 1

    try:
        if args.dump_scanner_params:
            out = Path(args.dump_scanner_params)
            xml = dump_scanner_params(ib, out)
            print(f"Saved scanner parameters to {out} ({len(xml)} bytes)", file=sys.stderr)
            print("Search the XML for instrument='BOND' to verify location_code / scan_code.", file=sys.stderr)
            if args.json:
                print(json.dumps({"path": str(out), "bytes": len(xml)}))
            return 0

        if args.cusip:
            rows = lookup_cusip(ib, args.cusip)
            preset_label = f"CUSIP lookup {args.cusip}"
        else:
            preset = presets[args.preset]
            sub = build_subscription(preset, args)
            rows = run_scanner(ib, sub)
            preset_label = preset.get("label", args.preset)

        payload = {
            "source": "ib-tws",
            "preset": args.preset if not args.cusip else None,
            "cusip": args.cusip,
            "host": host,
            "port": port,
            "count": len(rows),
            "results": rows,
        }

        if args.json:
            print(json.dumps(payload, indent=2, default=str))
        else:
            print_table(rows, preset_label)
    finally:
        ib.disconnect()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
