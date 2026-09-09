# Set up Grok Bot for daily JLaw work

**Lost?** [`WHERE-TO-CLICK.md`](WHERE-TO-CLICK.md) maps every label (New, Edit Profile, Agent Computer, Plugins, Routines) to the actual button. Those live in the **Grok Bot desktop app**, not in Cursor.

You already have the screen in this repo (`investment/scripts/`). This page is the **Grok Bot app** path: one named Bot, a few skills, one weekday routine.

Official product docs: [Grok Bot overview](https://docs.x.ai/grok-bot/overview), [create a Bot](https://docs.x.ai/grok-bot/bots), [skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations).

Cursor users can skip to [../README.md](../README.md) and invoke `jlaw-investor` instead. Same doctrine, different surface.

---

## 0. What you will have when this is done

| Piece | Lives where | Does what |
|-------|-------------|-----------|
| Bot **JLaw Daily** | Grok Bot sidebar | Owns the job and the routine |
| **Your TradingView login** | Shared Agent Computer browser | Accurate screen + charts — [`SETUP-TRADINGVIEW-LOGIN.md`](SETUP-TRADINGVIEW-LOGIN.md) |
| Skills (`/` menu) | Settings → Plugins → Yours | How to screen, check 催化劑, review positions, run buy/sell checks |
| Weekday routine | That Bot → Conversation details → Routines | 07:30 Asia/Hong_Kong brief (change if you prefer pre-US-open) |
| This git repo | Bot computer **or** Cursor workspace | Scripts + knowledge files |

The Bot **drafts**. You **execute** in the broker.

---

## 1. Create the Bot

1. Open the Grok Bot app.
2. Sidebar **New** (or `Ctrl/Cmd+N`) → **Create new agent**.
3. **Bot actions → Edit Profile**:
   - Name: `JLaw Daily`
   - Title: `Personal US-equity screen and catalyst desk`
   - Description: paste the block in [`PROFILE.md`](PROFILE.md)
4. Pin the Bot.

Do **not** share the Bot link until you have removed any personal account detail from the description (share links are public).

---

## 2. Put this repo on the Bot’s computer

All of your Grok Bots share **one** cloud computer. Treat logins as visible to every Bot.

In the JLaw Daily thread:

```text
Clone or pull https://github.com/jackiechow4567-arch/Consultant-agents.git
into the workspace. Confirm these paths exist:
- investment/knowledge/jlaw-operating-system.md
- investment/playbooks/daily-brief.md
- investment/scripts/daily_brief.py
Then install: pip install -r investment/scripts/requirements-tradingview.txt
Run a one-off: python investment/scripts/daily_brief.py --limit 25 --markdown
```

If clone is awkward, attach the `investment/` folder (or at least `knowledge/` + `playbooks/` + `scripts/`) as files the Bot can read.

**Then sign TradingView in on the Bot computer** — this is what makes screening accurate. Follow [`SETUP-TRADINGVIEW-LOGIN.md`](SETUP-TRADINGVIEW-LOGIN.md). You take over for password / 2FA; never paste the password into chat.

On Windows in **Cursor** (parallel setup, not Grok Bot):

```bat
SETUP-TRADINGVIEW.bat
```

---

## 3. Save the four skills

Open the Bot and send **one skill at a time**. After a skill works once, say: “Save that as a skill named …”

Paste-ready text:

| Skill | File | When |
|-------|------|------|
| TradingView logged-in screen | [`skills/tradingview-logged-in-screen.md`](skills/tradingview-logged-in-screen.md) | **Primary** screen (your TV account) |
| Daily JLaw screen | [`skills/daily-screen.md`](skills/daily-screen.md) | Fallback if TV session is down |
| News & 催化劑 | [`skills/news-catalyst.md`](skills/news-catalyst.md) | Shortlist + holdings |
| Position / watchlist review | [`skills/position-review.md`](skills/position-review.md) | After the screen |
| Buy / sell gate | [`skills/buy-sell-gate.md`](skills/buy-sell-gate.md) | Before any order discussion |

Enable each skill for **this** Bot under **Settings → Plugins → Yours** if it does not show in `/`.

**Teach a task** (browser, ≤10 min) after TradingView is signed in: load saved screener `JLaw Stage 2`, then open the top names on layout `JLaw Daily`. Add the written rules from `skills/tradingview-logged-in-screen.md` — a recording is only a draft.

---

## 4. First live task (do this before automating)

Paste:

```text
Read investment/knowledge/jlaw-operating-system.md and
investment/playbooks/daily-brief.md.

If TradingView is signed in on this computer, run the TradingView
logged-in screen (saved screener "JLaw Stage 2" + layout "JLaw Daily").
Only if the session is down, run python investment/scripts/daily_brief.py
--limit 25 --markdown and label the brief DEGRADED.

Then run the News & 催化劑 skill on the top 8 names plus any tickers
in investment/templates/watchlist.example.md.

Post today's brief. Do not recommend averaging down. Do not chase
names more than 5% above a breakout. No broker orders.
```

Correct the output once (too many names, missed earnings, wrong regime). Only then schedule it.

---

## 5. Create the weekday routine

Ask **this** Bot (not a different one):

```text
Every weekday at 07:30 Asia/Hong_Kong, run TradingView logged-in screen
(saved "JLaw Stage 2" + charts). If TradingView asks for login, pause
for take-over. Only if the session is dead, fall back to Daily JLaw screen
/ daily_brief.py and label DEGRADED.

Then News & 催化劑, then Position / watchlist review.

Inputs: TradingView saved screener; watchlist file if present;
public web/X for catalysts.

Output: one markdown brief in this conversation, ≤10 actionable names.

If the scanner or web data is down, report the failure. Do not reuse
stale prices as live. Never place trades or send messages outside
this thread. Research support only.
```

Confirm: owner, time zone, inputs, output, approval boundary, missing-data behaviour.

Then **Test run** (a test run does real work). Check:

- Regime is stated first
- Table is sourced (script or TradingView)
- Earnings dates are dated
- It stopped at “draft brief,” no orders

Optional second routine (pre-US cash session): see [`routines/pre-us-open.md`](routines/pre-us-open.md).

Manage later: Bot → **View conversation details** → **Routines**.

---

## 6. Daily habit (you)

| Time (HKT) | You do |
|------------|--------|
| ~07:30 | Read the brief; mark 0–2 names for charts |
| Before any buy | Run `/buy-sell-gate` on that one ticker |
| After US close / next morning | Check whether stops need moving; never average down |

Keep the live watchlist short. Copy [`templates/watchlist.example.md`](../templates/watchlist.example.md) to `investment/watchlist.md` (gitignored) and point the Bot at it.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Routine did not fire | Conversation details → Routines: enabled? time zone Hong Kong? |
| Empty / stale screen | Re-run logged-in TV screener; if session expired, take over and sign in; `daily_brief.py` is degraded fallback |
| TV login / 2FA loop | Take over Agent Computer; never paste the password into chat — see `SETUP-TRADINGVIEW-LOGIN.md` |
| 40-name dump | Remind the Bot: actionable list ≤10; rest is appendix |
| Chasing extended names | Enforce the 5% breakout rule in the profile; fail those rows |
| Bot wants to buy a tip | Kill — low-quality source |
| High-sensitivity paste | Stop; move to `work-briefs/` in Cursor |

---

## What this Bot will not do

- Broker execution, algos, or “set the order for me”
- Tax, visa, or licensed advice
- Averaging down, cheap-stock fishing, or style-hopping into options day-trading because the tape is quiet
