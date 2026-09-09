# Where to click (Grok Bot setup)

The setup steps mix **three products**. If a label is missing, you are probably in the wrong one.

| You are here | What it looks like | Use it for |
|--------------|--------------------|------------|
| **Grok Bot app** | Separate desktop app named Grok Bot (not Cursor, not grok.com chat) | Create **JLaw Daily**, Agent Computer, skills, routines |
| **This git repo** | Cursor window, or GitHub folder `investment/grok-bot/` | Copy-paste PROFILE, skills, playbooks |
| **TradingView website** | tradingview.com in a **browser** (on the Bot computer or yours) | Saved screener **JLaw Stage 2**, layout **JLaw Daily** |

Install the app: [Get started](https://docs.x.ai/grok-bot/get-started) → download from [x.ai/bot](https://x.ai/bot). Sign in with the **same Cursor account**. Eligible plans: SuperGrok Plus/Heavy, or Cursor Pro+ / Ultra / Teams.

---

## A. Inside the Grok Bot app

Imagine the window: **left sidebar** (list of Bots) + **center chat** + **composer** (text box at the bottom).

| I said | Where it actually is |
|--------|----------------------|
| **New → Create new agent** | Left sidebar, button **New** (or `Ctrl+N` / `Cmd+N`). In the New chat screen, click **Create new agent**. |
| **Bot actions → Edit Profile** | Open the Bot in the sidebar (it may still be named “New Agent”). Top of the conversation: **Bot actions** (⋯ or the Bot name). Click **Edit Profile**. Alternate: **View conversation details** → **Agent settings** (name, title, description). |
| Paste the **description** | That Edit Profile / Agent settings **Description** box. Copy the fenced block from [`PROFILE.md`](PROFILE.md) in the repo. |
| **Pin** | Same Bot menu → Pin (keeps it at the top of the sidebar). |
| **Agent Computer** | Inside **that Bot’s conversation**, a control named **Agent Computer** (computer / desktop preview). This is a **cloud** desktop, not your laptop. |
| **Take over** | After Agent Computer is open, the takeover control on that preview. Use it for TradingView password / 2FA. |
| **Teach a task** | One-to-one chat **with Agent Computer open**. If you do not see it, skip — paste the skill text instead (rollout is gradual). |
| **Settings → Plugins** | Account menu (your avatar, usually bottom-left) → **Settings**, or `Ctrl+,` / `Cmd+,`. Section **Plugins**. **Marketplace** = catalog; **Yours** = what this Bot can use. Plugins also appear as **Plugins** in the sidebar. |
| **`/` skills** | Click the **composer** (bottom text box) and type `/`. If a skill is missing: Settings → Plugins → **Yours** → enable it for **JLaw Daily**. |
| **`@` mentions** | Same composer, type `@` for Bots, routines, plugins. |
| **Routines** | Open **JLaw Daily** → **View conversation details** → **Routines**. Enable, pause, **Test run**, edit schedule. |
| **Timezone** | Settings → **General** → **Agent** → Timezone (routines use this). Set **Hong Kong** if you want 07:30 HKT. |

You will **not** find Edit Profile, Agent Computer, or Routines inside **Cursor** chat or on **grok.com**.

---

## B. Inside this repo (the markdown files)

Those paths are **files**, not Grok Bot buttons.

**In Cursor:** File → Open Folder → this `Consultant-agents` repo. Left file tree:

```text
investment/
  grok-bot/
    WHERE-TO-CLICK.md     ← you are here
    SETUP.md
    PROFILE.md            ← copy Description from here
    FIRST-MESSAGE.md
    SETUP-TRADINGVIEW-LOGIN.md
    skills/               ← paste these into the Bot
    routines/
  playbooks/
  knowledge/
```

**On GitHub:** open the PR or repo → folder `investment/grok-bot/` → click the file → copy.

| I said | File to open |
|--------|----------------|
| Profile text | `investment/grok-bot/PROFILE.md` |
| First message | `investment/grok-bot/FIRST-MESSAGE.md` |
| TV login steps | `investment/grok-bot/SETUP-TRADINGVIEW-LOGIN.md` |
| Saved-screener recipe | `investment/playbooks/tradingview-logged-in-screen.md` |
| Skill texts | `investment/grok-bot/skills/*.md` |

---

## C. On TradingView (after Agent Computer is signed in)

In the **Agent Computer** browser (not necessarily Chrome on your laptop):

| I said | Where |
|--------|--------|
| Stock Screener | tradingview.com → **Products** → **Screeners** → **Stocks**, or [tradingview.com/screener](https://www.tradingview.com/screener/) |
| **Save** the screen | Blue **Save** on the screener → name `JLaw Stage 2` |
| Chart layout | A daily chart → layout name at the top → **Save** as `JLaw Daily` |
| Watchlist | Right sidebar watchlist → new list `JLaw Watch` |

---

## Fast path (only these clicks)

1. Open **Grok Bot** desktop app (not Cursor).
2. Sidebar **New** → **Create new agent**.
3. **Bot actions** → **Edit Profile** → paste `PROFILE.md`.
4. In that chat, open **Agent Computer** → take over → sign in to TradingView.
5. Still in that chat, paste `FIRST-MESSAGE.md`.
6. Later: **View conversation details** → **Routines** for the 07:30 job.
