# Interactive Brokers TWS — API setup for Grot Bot bond screening

Grot Bot uses **IB Trader Workstation (TWS)** or **IB Gateway** to screen individual bonds (corporate, government, municipal, agency) with the same filters you would use in the TWS Bond Scanner.

> **Disclaimer:** Research support only — not investment advice. Bond market data and scanner filters may require appropriate IB market data subscriptions.

---

## 1. Install TWS or IB Gateway

Download from [Interactive Brokers](https://www.interactivebrokers.com/en/trading/tws.php):

| App | Best for |
|-----|----------|
| **TWS** | Full UI + Bond Scanner + API (recommended while learning) |
| **IB Gateway** | Lightweight headless API connection |

Log in with your IB account (paper or live).

---

## 2. Enable the API (one-time)

In **TWS** (or Gateway):

1. **File → Global Configuration → API → Settings**
2. Check **Enable ActiveX and Socket Clients**
3. Set **Socket port**:
   - `7497` — paper trading (default in `bond-screens.yaml`)
   - `7496` — live trading
4. Under **Trusted IPs**, add `127.0.0.1`
5. (Recommended) Uncheck **Read-Only API** if you later want order placement from scripts — Grot Bot screening is read-only by default.
6. Click **Apply** → **OK**
7. **Fully restart TWS** after changing API settings.

### Verify in TWS

Open **New Window → Scanners → Bond Scanner** and confirm you can run a manual corporate-bond search. If the GUI scanner works, the API path is usually configured correctly.

---

## 3. Install Python dependencies

From the **repo root**:

```bash
pip install -r investment/scripts/requirements-tradingview.txt
```

This installs `ib_insync`, `pyyaml`, and other Grot Bot dependencies.

---

## 4. Test the connection

With **TWS running and logged in**:

```bash
# Discover valid scanner codes for your TWS version (run once)
python investment/scripts/bond_screen_ib.py --dump-scanner-params

# US corporate bonds — IG sleeve (BBB–AAA), sorted by yield-to-worst
python investment/scripts/bond_screen_ib.py --preset corp-us

# US Treasuries / government
python investment/scripts/bond_screen_ib.py --preset govt-us

# Maturity window example (corporate)
python investment/scripts/bond_screen_ib.py --preset corp-us \
  --maturity-above 202801 \
  --maturity-below 203512 \
  --json

# Single bond lookup by CUSIP
python investment/scripts/bond_screen_ib.py --cusip 459200KZ3 --json
```

If connection fails, check port, trusted IP, and that TWS is not showing an API warning dialog.

---

## 5. Configure presets

Edit [`config/bond-screens.yaml`](config/bond-screens.yaml):

| Field | Purpose |
|-------|---------|
| `defaults.port` | `7497` paper / `7496` live |
| `defaults.client_id` | Unique per concurrent API client |
| `presets.*.location_code` | Bond universe (e.g. `BOND.US`, `BOND.GOVT.US`) |
| `presets.*.scan_code` | Sort/ranking (e.g. yield, maturity) |

After `--dump-scanner-params`, open `investment/config/scanner-params.xml` and search for `BOND` to confirm `location_code` and `scan_code` values for your TWS build. Update the YAML if IB changes naming.

---

## 6. Use with Grot Bot in Cursor

```text
Use grot-bot-investor. Run an IB TWS corporate bond screen, BBB–AAA, maturity 2028–2035.

Use grot-bot-investor. Screen US government bonds for a 3-year ladder sleeve.
```

Grot Bot will run `bond_screen_ib.py`, apply the **FINA5120** checklist from [`playbooks/bond-screen.md`](playbooks/bond-screen.md), and shortlist candidates.

---

## 7. Market data notes

| Topic | Detail |
|-------|--------|
| **Scanner vs quotes** | `reqScannerData` returns **contracts**, not live bid/ask/yield. Request snapshots separately in TWS or extend the script. |
| **Filters** | Rating / yield filters may require bond market data subscriptions on your IB account. |
| **Paper account** | Paper TWS uses port `7497`; scanner universes may differ from live. |
| **Offline fallback** | `python investment/scripts/bond_screen.py` — ETF proxy map via yfinance when TWS is not running |

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Cannot connect to IB TWS` | TWS not running, wrong port, or API not enabled |
| API connects but no results | Try `--dump-scanner-params`; update `scan_code` in YAML |
| `Error 162` / scanner rejected | Invalid `location_code` or `scan_code` for your TWS version |
| Rating filter ignored | Bond rating data subscription may be required |
| Client id in use | Change `defaults.client_id` in YAML or pass `--client-id` |

---

## Security

- Keep API on **localhost only** (`127.0.0.1`).
- Do not expose ports `7496`/`7497` to the internet.
- Account balances and positions are **High** sensitivity — keep in `work-briefs/`, not external LLMs.
