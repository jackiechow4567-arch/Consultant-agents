# Grot Bot — Investment Assistant Setup

Personal stock and bond screening assistant, wired to your **MBA finance agents** and local tools.

> **Disclaimer:** Grot Bot is research support only — not investment, tax, or legal advice.

---

## What you get

| Component | Purpose |
|-----------|---------|
| [`agents/grot-bot.md`](agents/grot-bot.md) | System prompt (Cursor skill or Gemini Gem) |
| [`.cursor/skills/grot-bot-investor`](../.cursor/skills/grot-bot-investor/SKILL.md) | Cursor skill — invoke with `Use grot-bot-investor.` |
| [`playbooks/stock-screen.md`](playbooks/stock-screen.md) | JLaw Stage 2 equity workflow |
| [`playbooks/bond-screen.md`](playbooks/bond-screen.md) | Fixed-income sleeve workflow (FINA5120) |
| [`playbooks/portfolio-review.md`](playbooks/portfolio-review.md) | Monthly watchlist / position review |
| [`scripts/jlaw_stage2_screen.py`](scripts/jlaw_stage2_screen.py) | US equity trend screen (TradingView, no key) |
| [`scripts/bond_screen.py`](scripts/bond_screen.py) | Bond ETF yield / duration map (yfinance) |
| TradingView MCP | Live quotes, movers, technicals in Cursor |

**Knowledge backend:** `mba-notes/FINA5120`, `ACCT5100`, `MGMT6501W` + `finance-accounting-consultant` for finalist valuation.

---

## Quick start (Cursor)

### 1. Open the repo root

Open the **repository root** (`Consultant-agents/`), not only the `investment/` subfolder — skills live under `.cursor/skills/`.

### 2. Install dependencies

**Windows (one-click):**

```bat
SETUP-TRADINGVIEW.bat
```

**macOS / Linux:**

```bash
bash scripts/install-tradingview-mcp.sh
pip install -r investment/scripts/requirements-tradingview.txt
```

Restart Cursor fully after install. Check **Settings → Tools & MCP → tradingview** (green).

### 3. Talk to Grot Bot

Examples:

```text
Use grot-bot-investor. Run a Stage 2 US equity screen and give me a top-10 watchlist.

Use grot-bot-investor. Map my bond sleeve options for a 5-year horizon, defensive rate view.

Use grot-bot-investor. Review my watchlist — growth sleeve, max 8% per name.
```

### 4. Deep dive on finalists

```text
Use finance-accounting-consultant. Sanity-check NPV / assumptions for <TICKER> from today's Grot screen.
```

---

## Manual script usage

```bash
# Equities — JLaw Stage 2
python investment/scripts/jlaw_stage2_screen.py --limit 40
python investment/scripts/jlaw_stage2_screen.py --hard-only --json

# Fixed income — ETF sleeve map
python investment/scripts/bond_screen.py
python investment/scripts/bond_screen.py --symbols TLT,IEF,SHY,AGG,LQD,HYG,TIP --json
```

---

## Gemini Enterprise (optional)

1. Create a Gem named **Grot Bot**.  
2. Paste the contents of [`agents/grot-bot.md`](agents/grot-bot.md) as the system instruction.  
3. Upload distilled `mba-notes/FINA5120/cheat-sheet.md` (Low sensitivity).  
4. For live prices, prefer Cursor + TradingView MCP; use Gemini for memo writing on de-identified shortlists.

---

## Sensitivity rules

| Data | Tier | Tool |
|------|------|------|
| Public tickers, ETF yields | Low | Cursor + MCP / scripts |
| Portfolio weights (rounded) | Mid | Cursor; de-ID before Gemini |
| Exact balances, tax lots | High | `work-briefs/` only |

See [privacy-policy.md](../privacy-policy.md).

---

## Architecture

```mermaid
flowchart LR
  You[You] --> Grot[Grot Bot]
  Grot --> Stock[jlaw_stage2_screen.py]
  Grot --> Bond[bond_screen.py]
  Grot --> TV[TradingView MCP]
  Grot --> MBA[FINA5120 / ACCT5100 notes]
  Grot --> FA[finance-accounting-consultant]
  FA --> Memo[Valuation / assumptions memo]
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `tradingview` MCP red | Re-run install script; restart Cursor; try `mcp.python-fallback.json` |
| `uvx` not found | Install [uv](https://github.com/astral-sh/uv); or use Python fallback config |
| Empty bond ETF on TV scanner | Use `bond_screen.py` (yfinance) — TV free scanner is equity-heavy |
| Screen too narrow | `jlaw_stage2_screen.py --hard-only` |

---

## Related

- [Main vault README](../README.md)  
- [Finance agent](../agents/02-finance-accounting.md)  
- [FINA5120 cheat sheet](../mba-notes/FINA5120/cheat-sheet.md)
