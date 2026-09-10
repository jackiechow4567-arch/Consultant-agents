# Automatic weekday screening (this is the daily job)

Setup messages (sign-in, create screener) are **once**. They are not the daily loop.

**Automatic** = a Grok Bot **Routine**. After it exists, it runs at 07:30 Hong Kong even if your laptop is closed. You read the brief; you do not press Screen.

Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations).

---

## What can be fully unattended

| Every weekday, no one at the keyboard | Needs you (rare) |
|----------------------------------------|------------------|
| `daily_brief.py` Stage 2 scan + sector rank | First TradingView sign-in / 2FA |
| Web/X 催化劑 on the shortlist | TV session expired (CAPTCHA) — brief still posts |
| Markdown brief in the JLaw Daily thread | You execute broker orders |
| Recommended adds/drops for `JLaw Watch` | Optional: click TV watchlist if session was dead |
| Read latest `investment/inbox/digests/` as 催化劑 hints | Circle/Kajabi/Patreon login — that is **JLaw Inbox**, not this Bot |

TradingView charts stay **best-effort**. If the site asks for login at 07:30, the Bot **must not wait**. It posts the script brief and one line: `TV session expired`. That is how screening stays automatic.

100% unattended **and** logged-in TradingView every day is not possible: TV will re-ask 2FA/CAPTCHA. Do not try to store the password in the Bot.

---

## Turn it on (one paste)

In **Grok Bot** → **JLaw Daily** (after a one-off screen has worked once):

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
4) If investment/inbox/digests/ has a file, fold those rows into
   News & 催化劑 as hints (not buys). Chart gate still required.
5) News & 催化劑 on the shortlist. Post one brief in this conversation,
   ≤10 names. Never place trades. Never touch other watchlists.

If the Python scanner fails, say SCANNER FAILED in the thread.
Do not reuse yesterday’s prices.
```

Then:

1. Confirm timezone **Asia/Hong_Kong** (Settings → General → Agent).
2. **View conversation details** → **Routines** → **Test run** (this run is real).
3. **Enable**.
4. Turn on **notifications** for this Bot so the brief pings you.

That is the automation. Messages 1–3 in [`HANDOFF-TRADINGVIEW.md`](HANDOFF-TRADINGVIEW.md) only make TV *richer* when the cookie is still valid.

---

## How to know it is actually automatic

| Check | Pass |
|-------|------|
| Routines list shows next run ~07:30 HKT | Enabled, not paused |
| Test run posted a brief **without** you clicking Screen | Script table present |
| Next weekday, brief is in the thread before you open the app | Laptop was closed |
| A later morning says `TV session expired` but still has a table | Correct degrade |

If there is **no** routine, nothing will run by itself.

---

## Optional second automatic pass

Pre-US-open card: [`routines/pre-us-open.md`](routines/pre-us-open.md) at 20:30 HKT. Same rule: never wait on login.

---

## JLaw Inbox (separate Bot)

Community polls are **not** this Bot. Create **JLaw Inbox**, then:

1. [`HANDOFF-INBOX.md`](HANDOFF-INBOX.md) — you sign in to Circle, Kajabi, Patreon once (take over).
2. [`routines/community-poll.md`](routines/community-poll.md) — weekday **08:15** and **21:00** HKT.

That Bot writes digest rows; this Bot reads them at 07:30. No Gmail.
