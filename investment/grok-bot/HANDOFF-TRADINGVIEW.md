# Let Grok Bot run TradingView (screen + watchlist)

“Control TradingView” means the Bot uses the **Agent Computer browser** while **you** stay signed in. It is not an official TradingView API. You type the password; the Bot clicks screener, charts, and **one** watchlist.

Do **not** turn on “run on my local computer” for this. The cloud Agent Computer is enough.

---

## Allow vs never

| Allow (this Bot) | Never without asking you |
|------------------|--------------------------|
| Open Stock Screener, load **JLaw Stage 2** / **JLaw Near-high** | Delete or rename your other saved screens |
| Open charts on layout **JLaw Daily** | Place / cancel broker or TV trading panel orders |
| Create and edit watchlist **JLaw Watch** only (≤12 names) | Wipe **JLaw Watch** without listing what was removed |
| Add/remove symbols on **JLaw Watch** after the brief | Touch any other watchlist (personal, broker sync, etc.) |
| Optional: price alerts **only** on JLaw Watch names | Email, tweet, or message from your TV account |
| Screenshot tables/charts into the Grok thread | Change billing, password, or connected brokers |

All of your Grok Bots share this login. Do not sign into TradingView on the Agent Computer if another Bot should not see it.

---

## Message 1 — sign in (you take over)

In **Grok Bot app** → Bot **JLaw Daily** → open **Agent Computer**, then paste:

```text
Open https://www.tradingview.com in Agent Computer.
If you see a login wall, 2FA, or CAPTCHA, stop and ask me to take over.
Do not type or ask for my password or SMS code in this chat.
After I finish sign-in, confirm the username shown in the UI and wait.
```

You: **Take over** → sign in on that preview → 2FA → then:

```text
Continue. You are signed in. Do not store the password.
```

---

## Message 2 — create screener, layout, watchlist (once)

```text
Follow investment/playbooks/tradingview-logged-in-screen.md.

On THIS TradingView account, create if missing (do not overwrite
unrelated saved items):

1) Stock Screener saved as "JLaw Stage 2" with the filters in that playbook.
2) Duplicate tightened to "JLaw Near-high" (within 5% of 52-week high).
3) Daily chart layout "JLaw Daily": SMA 10, 21, 50, 200, volume, 52-week high.
4) Empty watchlist "JLaw Watch". Hard cap 12 symbols. Never edit any
   other watchlist.

Then screenshot: screener filter list, layout, empty JLaw Watch.
Stop for my OK before adding symbols.
```

Watch the Agent Computer while it clicks. If it drifts, take over and finish that one control, then `Continue from this page`.

---

## Message 3 — first real screen + fill the watchlist

```text
Run TradingView logged-in screen:
- Load "JLaw Stage 2"
- Regime from SPX/NQ on "JLaw Daily"
- Open at most 8 daily charts
- 5% chase rule = distance from the PIVOT, not only 52-week high
- Post the daily brief (≤10 names)

Then update watchlist "JLaw Watch" only:
- Add names that passed the chart gate
- Remove names that failed (list them in the brief)
- Keep ≤12. Do not average down. No orders.

Save this process as a skill named "TradingView logged-in screen".
```

Skill text to merge if the saved skill is thin: [`skills/tradingview-logged-in-screen.md`](skills/tradingview-logged-in-screen.md).

Optional: **Teach a task** (Agent Computer open) while you load the screener and open 3 charts once, then add the rules above.

---

## Message 4 — turn on automatic screening (required)

Messages 1–3 do **not** run tomorrow by themselves. Automation is a **Routine**.

Paste this (also in [`AUTO.md`](AUTO.md) and [`routines/weekday-morning.md`](routines/weekday-morning.md)):

```text
Create a routine. Do not wait for me on weekday runs.

Every weekday at 07:30 Asia/Hong_Kong:
1) ALWAYS run: python investment/scripts/daily_brief.py --limit 25 --markdown
   This is the automatic screen. It must finish even if I am asleep.
2) If TradingView is already signed in (no login wall), ALSO load
   saved screener "JLaw Stage 2", open up to 8 charts on "JLaw Daily",
   and sync watchlist "JLaw Watch" (≤12). Label source: TradingView+.
3) If TradingView shows login, 2FA, or CAPTCHA: do NOT pause and do
   NOT type passwords. Skip TV. Label source: automatic (no TV session).
   Add one line: TV session expired — take over when convenient.
4) News & 催化劑 on the shortlist. Post one brief in this conversation,
   ≤10 names. Never place trades. Never touch other watchlists.

If the Python scanner fails, say SCANNER FAILED in the thread.
Do not reuse yesterday’s prices.
```

Then **View conversation details** → **Routines** → **Test run** → **Enable**.  
Laptop can be closed. If there is no routine, nothing is automatic.

---

## If something feels too loose

Tighten with one line:

```text
From now on: you may only change watchlist "JLaw Watch".
Ask before creating alerts. Never use the Trading panel.
```

To stop: pause the routine, Agent Computer → sign out of TradingView. Deleting the Bot does **not** sign out by itself.
