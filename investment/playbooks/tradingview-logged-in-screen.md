# Playbook — Logged-in TradingView screen (accurate JLaw path)

Use this when Grok Bot is signed into **your** TradingView account. Public `daily_brief.py` is only a fallback.

Sensitivity: **Low** (public prices). Do not type passwords into chat.

---

## A. Stock Screener “JLaw Stage 2” (save on the account)

Open [Stock Screener](https://www.tradingview.com/screener/). Market **USA**, type **Stock**.

### Filters

| Filter | Setting |
|--------|---------|
| Exchange | NYSE, NASDAQ, AMEX (primary listings) |
| Market cap | ≥ 2B |
| Last | ≥ 10 |
| Average Volume (30) | ≥ 400K (raise toward 1M if too many thin names) |
| Beta 1 year | ≥ 1 (drop this row for a defensive sleeve — separate saved screen) |
| Price vs SMA | Close ≥ SMA 50 **and** Close ≥ SMA 200 |
| SMA vs SMA | SMA 50 ≥ SMA 200 |
| Optional tightness | SMA 20 ≥ SMA 50 (stricter Stage 2) |
| 52-week high | Close ≥ 75% of 52-week high (Quality) |
| 52-week low | Close ≥ 130% of 52-week low |

Add columns: Name, Sector, Close, SMA 50, SMA 200, % from 52-week high (or High all / 52w), Perf 1W, Perf 1M, Relative Volume, Average Volume, Market cap, Beta.

Sort: **Perf 1M** descending, or **% from 52-week high** descending for leaders hugging highs.

Click **Save** → name **`JLaw Stage 2`**.

### Second saved screen “JLaw Near-high”

Duplicate, then tighten 52-week high to **within 5%** (close ≥ 95% of 52-week high). This is still a **proxy** for “near breakout.” The 5% chase rule is measured from the **pivot high on the chart**, not only this column.

---

## B. Chart layout “JLaw Daily”

On a daily Superchart, save a layout:

- Timeframe: **1D**
- SMA 10, SMA 21, **SMA 50**, **SMA 200** (50 and 200 must be obvious)
- Volume pane
- Horizontal line or built-in **52-week high**
- Optional: any RS / relative-strength indicator **you already use** (do not paste third-party script source into git)

Save as **`JLaw Daily`**. The Bot must load this layout before scoring the buy checklist.

---

## C. Watchlist “JLaw Watch”

Create an empty list. Hard cap **8–12** symbols. The Bot may add/remove **after** the brief, not dump 40 names into it.

---

## D. Daily operator sequence (Bot)

1. Confirm the TradingView UI shows a signed-in account. If login wall → pause for take-over.
2. Open SPX (or NQ) on **JLaw Daily**. Call regime (easy / grind / late-stage). Cite 50/200 location.
3. Load screener **JLaw Stage 2**. Note row count. If >80, also load **JLaw Near-high**.
4. Take the top names by sector clustering (several leaders in one group beat a lone laggard).
5. Open **at most 8** charts on **JLaw Daily**. For each, fill:

| Chart check | Pass? |
|-------------|-------|
| 50d and 200d sloping up; price above 50d (or ≤8% below) | |
| Base / pivot visible; ≥3 days; looks tight (range not sloppy; ~&lt;10% if measurable) | |
| Volume dried up in the base vs prior | |
| Distance from **actual breakout / pivot high** ≤5% (prefer 3%, best 2%) | |
| Not a cheap/thin leftover that slipped the filter | |
| Sector chart also strong | |
| Technical stop ≤8% and 2:1 still holds | |

One hard fail = not today. Visual pivot/RS/volume is why the login exists.

6. Write the daily-brief table. Mark `Source: TradingView saved screener JLaw Stage 2 + charts`.
7. Fallback: if the session is dead and you cannot wait, run `daily_brief.py` and label it **degraded / no account**.

---

## E. Optional Pine Screener (Premium)

1. Add [`../tradingview/jlaw-stage2-flags.pine`](../tradingview/jlaw-stage2-flags.pine) to your indicators.
2. Build a US-stock watchlist (e.g. from the Stage 2 result, or a large-cap index list).
3. Pine Screener → that list → this script → filter `ma_stack = 1` and `range10_pct ≤ 10` and `pct_from_high ≥ -25`.

Pine Screener scans a **list**, not the whole market, and typically one script at a time. Use it to **tighten** Stage 2, not replace it.

---

## Quality bar

- [ ] Signed-in confirmed
- [ ] Named saved screener used (not a one-off anonymous filter)
- [ ] Regime from the index chart
- [ ] ≤8 charts actually opened
- [ ] Breakout % from the **pivot**, not only 52-week high
- [ ] Actionable table ≤10
