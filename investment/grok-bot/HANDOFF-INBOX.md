# Give JLaw Inbox in-app access (Circle, Kajabi, Patreon)

No Gmail. No Connect button. Sign in **once** on Agent Computer; a Routine polls those tabs.

Clicks: [`WHERE-TO-CLICK.md`](WHERE-TO-CLICK.md).  
URLs: copy [`../inbox/sources.example.md`](../inbox/sources.example.md) → `investment/inbox/sources.md`.

---

## Message 1 — create the Bot

Grok Bot app → **New** → **Create new agent** → **Edit Profile**: paste [`PROFILE-inbox.md`](PROFILE-inbox.md). Pin it.

---

## Message 2 — sign in (you type the passwords)

Open **Agent Computer** in the **JLaw Inbox** chat. Paste (fill the three URLs):

```text
Open Agent Computer. Go to my paid member URLs in this order:
1) Circle: <paste>
2) Kajabi: <paste>
3) Patreon: <paste>

If login, 2FA, or CAPTCHA appears, stop and ask me to take over.
Do not type or ask for passwords. After I sign in, confirm you can
see JLaw official posts/courses on each site. Read only.
Never post, like, or reply. Save these URLs as canonical.
```

**Take over** → sign in on each site → then:

```text
Continue. Sessions are live. Do not store passwords.
```

Logins are shared with every Bot on this account.

---

## Message 3 — first poll (before automating)

```text
Follow investment/playbooks/community-digest.md.

Poll Circle, then Kajabi, then Patreon. Official JLaw posts only.
Compare to investment/inbox/seen.json. For each NEW item write one
digest row (no full body) into investment/inbox/digests/YYYY-MM-DD.md
and update seen.json. If a site is a login wall, mark SESSION DEAD
and skip it.

Then @JLaw Daily with only new rows (tickers + catalyst + URL).
If git is available, commit those two files on this branch.
Save this as skill "Community digest".
```

Watch the preview the first time. Optional: **Teach a task** while you click Circle feed → Kajabi library → Patreon posts (≤10 min), then paste the skill rules.

---

## Message 4 — automatic poll (required)

Until this Routine exists, nothing runs by itself. Also in [`routines/community-poll.md`](routines/community-poll.md).

```text
Create two weekday routines. Do not wait for me. Do not use Gmail.

Every weekday at 08:15 Asia/Hong_Kong AND every weekday at 21:00
Asia/Hong_Kong, run skill "Community digest":
open signed-in Circle, Kajabi, Patreon; official JLaw posts only;
append digest + seen.json; @JLaw Daily with new rows only.

If login/2FA: SESSION DEAD for that site, continue the others.
Never type passwords. Never post on those sites. Never paste
full lesson text into git. No trades.
```

**View conversation details** → **Routines** → **Test run** → **Enable**.  
Notifications on for **JLaw Inbox**. Timezone **Asia/Hong_Kong**.

---

## If a site dies

In the Inbox chat: *Open Agent Computer, that site needs login. Pause for take-over.* Sign in again, then `Continue`.
