# Playbook: HQ Field Progress Slides

Use when a **Product Manager** must show field progress to GM / HQ without sending a trip report.

**Pair with:** [exec-comms](exec-comms.md) (ask first) · [data-story-brief](data-story-brief.md) (one message per view) · role memory `industry/role-pm.md`

**Files (editable PowerPoint):**
- **Blank template (start here):** [`hq-field-progress-slides-blank.pptx`](hq-field-progress-slides-blank.pptx) — `[brackets]` to fill
- **Example copy:** [`hq-field-progress-slides.pptx`](hq-field-progress-slides.pptx) — sample text to show density
- Present in browser (optional): [`hq-field-progress-slides.html`](hq-field-progress-slides.html)
- Rebuild: `python3 scripts/generate_hq_field_progress_pptx.py`

**How to open:** download the `.pptx` to your computer first. GitHub’s web preview cannot open PowerPoint. Open in **Microsoft PowerPoint**, **Google Slides** (File → Import), or **Keynote**.

**Sensitivity:** Mid as a method. High the moment you paste named HCPs, patient stories, unpublished dossier data, or exact unreleased figures. Strip those before any forwardable send.

---

## Recommendation

**Do:** five slides — Ask → RAG scorecard → three field signals → conversion barriers → options + HQ ask.  
**Do not:** visit logs, CRM dumps, or a 12-slide “what I did this week.”

Fold this pack into the standing **biweekly HQ update**. Escalate mid-cycle only if there is a material access, competitor, or compliance signal.

---

## Slide contract

| # | Title job | HQ must see in 30 seconds | Fill with | Leave out |
|---|-----------|---------------------------|-----------|-----------|
| 1 | **The ask** | What to decide, by when | One-sentence ask, why now, do/don’t | Itinerary |
| 2 | **Scorecard** | On/off thesis | RAG: uptake vs plan · formulary · compliance, each with a definition | Call volume as a KPI |
| 3 | **Signals** | What repeated | Max 3 patterns: Observed → So what → Implication | Named HCPs, quotes that imply off-label claims |
| 4 | **Barriers** | Where conversion dies | Funnel + ranked barriers + what moved | Patient-level rows |
| 5 | **Decision** | Options and owners | Recommended option highlighted, 2 risks, 3 actions (role + date) | Open-ended “for discussion” |

**Always include (PM):**
- Sensitivity tier
- HA formulary impact line (strengthened / delayed / no change)
- PSP path in play (Base Case vs Private Sector; Private Sector expires end-2026)
- PV-only / lexicon boundary; ET/MF reactive-only
- Decision date and role owners (titles, not names)

---

## How to present the HTML

1. Open `playbooks/hq-field-progress-slides.html` in a browser.
2. **Example** = sample copy so you can see density. **Empty template** = `[brackets]` to fill.
3. Keys: `←` `→` change slides · `E` example · `T` template · `P` print to PDF (landscape).
4. Print to PDF if HQ wants a file and you do not want to edit PowerPoint.

URL flags: `?slide=3&mode=template`

---

## RAG rules (lock with GM once)

| Row | Green | Amber | Red |
|-----|-------|-------|-----|
| Uptake vs plan | On or ahead of the agreed HQ plan | Initiation/conversion lag; awareness alone is not green | Material miss vs plan, or forecast now untrustworthy |
| Formulary trajectory | This cycle strengthened the dossier or window | No change; still on the multi-quarter path | Delayed, evidence gap, or unauthorized pricing talk |
| Compliance | Materials cleared; no open UMAO/HKAPI issue | Question logged and contained (e.g. reactive ET/MF) | Uncleared claim, hospitality breach, or unreported promo risk |

Do not colour from optimism. If the definition is missing, the row is Amber until GM agrees the definition.

---

## What never goes on a forwardable slide

- HCP or patient names, institutions that identify a person in a small market
- Verbatim advisory-board or Veeva notes
- Exact unreleased revenue, PSP uptake, or pricing cells
- Draft claims not through global lexicon + local compliance
- ET/MF efficacy discussion (reactive-only; not a field “win”)

---

## Quality bar

- [ ] Ask is in the first screen
- [ ] One primary message per slide (insight title, not “Update”)
- [ ] Every RAG row has a definition
- [ ] Max three signals; max four barriers
- [ ] Recommended option is visually marked
- [ ] High-sensitivity detail removed
