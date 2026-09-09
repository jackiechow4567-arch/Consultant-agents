# Sign Grok Bot into your TradingView account

Yes. The Bot can use **your** TradingView session on its cloud computer. That is how it gets closer to a real JLaw screen (saved screener + live charts). The Python script in this repo does **not** log into your account.

Official: [Use the computer and apps](https://docs.x.ai/grok-bot/computer-and-apps), [troubleshooting sign-in](https://docs.x.ai/grok-bot/troubleshooting).

---

## What your login buys vs the public scanner

| | `daily_brief.py` (no login) | Logged-in TradingView |
|--|-----------------------------|------------------------|
| Data | Public scanner, often delayed | Your plan’s data (real-time on paid) |
| Filters | SMA / cap / liquidity / % from 52w high | Same **plus** saved screens, extra columns, your watchlists |
| Pivot / pocket pivot / RS line / volume dry-up | **Not** in the scanner — script cannot see the chart | Bot opens **your** daily layout and scores the buy checklist |
| Breakout distance | 52-week high is only a proxy | Actual pivot high on the chart (the 5% chase rule) |
| Alerts / lists | None | Watchlist **JLaw Watch**, optional alerts |

The account does **not** magically compute Train-the-Trader pivots. Accuracy comes from: **your saved screener → your chart layout → the buy checklist**. The Bot is the operator.

---

## 1. Sign in once (you type the password)

All Grok Bots share **one** computer and **one** browser. A TradingView login is visible to every Bot on your account.

In the **JLaw Daily** thread:

```text
Open Agent Computer. Go to https://www.tradingview.com and check if we
are signed in. If a password, 2FA, or CAPTCHA appears, pause and ask
me to take over. Do not guess credentials. Do not ask me to paste a
password or SMS code into this chat.
```

Then:

1. Open **Agent Computer** in Grok Bot.
2. **Take over** when the login wall appears.
3. Sign in yourself. Finish 2FA / CAPTCHA.
4. Confirm you see your avatar / saved screens.
5. Tell the Bot: `Continue. Confirm the TradingView username shown in the UI (not the password).`

If TradingView is listed under **Settings → Plugins**, add it and prefer that connector. There is often **no** official TradingView plugin — the browser session is the supported path.

Never put `TV_USERNAME` / `TV_PASSWORD` in git, MCP env files, or chat.

---

## 2. Save the JLaw screen **on TradingView** (once)

Do this while signed in (you or the Bot with you watching). Recipe: [`../playbooks/tradingview-logged-in-screen.md`](../playbooks/tradingview-logged-in-screen.md).

Create and **Save** these on the account:

| Name | Type | Purpose |
|------|------|---------|
| **JLaw Stage 2** | Stock Screener | Daily universe |
| **JLaw Near-high** | Stock Screener | Tighter, within ~5% of 52-week high |
| **JLaw Daily** | Chart layout | 50/200 (and 10/21), volume, 52-week high |
| **JLaw Watch** | Watchlist | Short list the Bot maintains |

Optional (usually **Premium**): Pine Screener + [`../tradingview/jlaw-stage2-flags.pine`](../tradingview/jlaw-stage2-flags.pine) on a US-stock watchlist for tightness (`range10_pct`) and MA stack.

---

## 3. Teach the weekday click-path (≤10 min)

When **Teach a task** is available:

1. Open the Bot computer view.
2. Describe: `Load saved Stock Screener "JLaw Stage 2", copy the visible table, then open the top 5 names on layout "JLaw Daily".`
3. Do that once. Stop recording.
4. Paste the decision rules from [`../grok-bot/skills/tradingview-logged-in-screen.md`](../grok-bot/skills/tradingview-logged-in-screen.md) — a recording has no 5% chase rule until you add it.

If Teach a task is missing, send that skill as written instructions after one successful manual run.

---

## 4. Daily order of sources (mandatory)

1. **Logged-in TradingView** — saved screener + charts  
2. `daily_brief.py` — only if the session expired or the screener UI failed  
3. Say **which** source was used. Never mix yesterday’s TV table with today’s script as if they were one scan.

---

## Session hygiene

| Event | What to do |
|-------|------------|
| TV asks for login again | Take over; re-auth; then `Continue` |
| CAPTCHA / 2FA | You complete it. Bot waits |
| You shared the Bot link | Login is **not** copied to recipients, but do not put account hints in the public profile |
| Stop using TV on the Bot | Sign out on the computer; pause the routine |

---

## What stays inaccurate even when logged in

- Pocket pivot and RS-line **unless** you add a script you already use and run Pine Screener or inspect the chart
- “Perfect” base count — still a human/Bot visual on daily bars
- Fundamentals / 催化劑 — still filings and news, not the TV chat room
