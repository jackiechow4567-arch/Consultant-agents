#!/usr/bin/env python3
"""Generate the HQ field-progress 16:9 PowerPoint template."""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

NAVY = RGBColor(0x0E, 0x27, 0x44)
INK = RGBColor(0x1C, 0x2A, 0x3A)
MUTED = RGBColor(0x5B, 0x6B, 0x7C)
TEAL = RGBColor(0x1B, 0x7A, 0x6E)
WHITE = RGBColor(0xFF, 0xFC, 0xF7)
PAPER = RGBColor(0xF4, 0xF1, 0xEA)
GOLD = RGBColor(0xB8, 0x86, 0x0B)
GREEN = RGBColor(0x1F, 0x7A, 0x4D)
AMBER = RGBColor(0xB8, 0x6E, 0x13)
LINE = RGBColor(0xD8, 0xD2, 0xC6)
TEAL_SOFT = RGBColor(0xE4, 0xF3, 0xEF)
GREEN_SOFT = RGBColor(0xE3, 0xF3, 0xEA)
AMBER_SOFT = RGBColor(0xF8, 0xED, 0xD6)
WHITE_CARD = RGBColor(0xFF, 0xFF, 0xFF)

W = Inches(13.333)
H = Inches(7.5)
MARGIN = Inches(0.45)


def set_run(run, size=14, bold=False, color=INK, font="Calibri", italic=False):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name = font
    rPr = run._r.get_or_add_rPr()
    ea = rPr.find(qn("a:ea"))
    if ea is None:
        ea = rPr.makeelement(qn("a:ea"), {})
        rPr.append(ea)
    ea.set("typeface", font)


def add_text(shape, lines, default_size=14, default_color=INK, default_bold=False):
    tf = shape.text_frame
    tf.word_wrap = True
    tf.clear()
    for idx, item in enumerate(lines):
        if isinstance(item, str):
            text, size, bold, color = item, default_size, default_bold, default_color
        else:
            text = item[0]
            size = item[1] if len(item) > 1 else default_size
            bold = item[2] if len(item) > 2 else default_bold
            color = item[3] if len(item) > 3 else default_color
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.space_after = Pt(4)
        run = p.add_run()
        run.text = text
        set_run(run, size=size, bold=bold, color=color)


def fill(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def card(slide, l, t, w, h, fill_color=WHITE_CARD):
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l, t, w, h)
    fill(sh, fill_color)
    sh.line.color.rgb = LINE
    sh.adjustments[0] = 0.08
    return sh


def footer(slide, n):
    bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, MARGIN, Inches(7.18), Inches(12.43), Inches(0.22)
    )
    fill(bar, PAPER)
    add_text(
        bar,
        [
            (
                f"Patterns only · no named HCPs, patient stories, unpublished dossier data  ·  {n} / 5",
                10,
                False,
                MUTED,
            )
        ],
    )


def header(slide, left, right):
    a = slide.shapes.add_textbox(MARGIN, Inches(0.16), Inches(7.2), Inches(0.32))
    add_text(a, [(left, 11, True, NAVY)])
    b = slide.shapes.add_textbox(Inches(7.4), Inches(0.16), Inches(5.5), Inches(0.32))
    tf = b.text_frame
    tf.clear()
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    run = p.add_run()
    run.text = right
    set_run(run, size=11, bold=True, color=MUTED)


def kicker(slide, text, top=Inches(0.48)):
    box = slide.shapes.add_textbox(MARGIN, top, Inches(12.4), Inches(0.28))
    add_text(box, [(text.upper(), 11, True, TEAL)])


def title(slide, text, top=Inches(0.72), height=Inches(0.7)):
    box = slide.shapes.add_textbox(MARGIN, top, Inches(12.4), height)
    add_text(box, [(text, 26, True, NAVY)])


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def build():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    blank = prs.slide_layouts[6]

    # --- Slide 1 ---
    s = prs.slides.add_slide(blank)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    fill(bg, PAPER)
    header(s, "BESREMi · HK PV · PM field pack", "Biweekly · [dates] · Mid · Internal · De-identified")
    flag = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, MARGIN, Inches(0.48), Inches(6.6), Inches(0.32))
    fill(flag, RGBColor(0xF8, 0xEE, 0xD3))
    add_text(flag, [("SAMPLE — replace before sending to HQ", 11, True, RGBColor(0x6B, 0x4E, 0x00))])
    kicker(s, "The ask · first 30 seconds", Inches(0.88))
    ask = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, MARGIN, Inches(1.18), Inches(12.43), Inches(1.7))
    fill(ask, NAVY)
    add_text(
        ask,
        [
            ("HQ SHOULD DO THIS", 11, True, GOLD),
            (
                "Concentrate the next two weeks on initiation barriers in priority private accounts. Do not treat call volume as the progress metric.",
                22,
                True,
                WHITE,
            ),
        ],
    )
    c1 = card(s, MARGIN, Inches(3.08), Inches(6.05), Inches(2.2))
    add_text(
        c1,
        [
            ("WHY NOW", 11, True, MUTED),
            (
                "Private-sector PSP expiry (end-2026) is already changing close conversations. Formulary packaging needs field themes, not visit counts, while the evidence window is still open.",
                16,
                False,
                INK,
            ),
        ],
    )
    c2 = card(s, Inches(6.83), Inches(3.08), Inches(6.05), Inches(2.2))
    add_text(
        c2,
        [
            ("RECOMMENDATION", 11, True, MUTED),
            (
                "Do: report 3 conversion signals mapped to uptake / formulary / compliance. Do not: send trip logs, named HCPs, or CRM dumps.",
                16,
                False,
                INK,
            ),
        ],
    )
    snaps = [
        ("FORMULARY THIS CYCLE", "No change to dossier — themes usable, no new unlock", MARGIN),
        ("PSP IN PLAY", "Base Case + Private Sector (expires end-2026)", Inches(4.75)),
        ("COMPLIANCE", "Green · PV-only lexicon · ET/MF reactive-only", Inches(9.05)),
    ]
    for label, value, left in snaps:
        card(s, left, Inches(5.4), Inches(3.85), Inches(1.15))
        add_text(
            s.shapes.add_textbox(left + Inches(0.16), Inches(5.46), Inches(3.55), Inches(1.0)),
            [(label, 10, True, MUTED), (value, 13, True, NAVY)],
        )
    for label, value, left in [
        ("DECISION NEEDED BY", "[YYYY-MM-DD]", MARGIN),
        ("OWNER", "PM, with GM for HQ send", Inches(4.75)),
        ("GOES INTO", "Standing biweekly HQ update", Inches(9.05)),
    ]:
        box = s.shapes.add_textbox(left, Inches(6.68), Inches(3.9), Inches(0.42))
        add_text(box, [(f"{label}:  {value}", 11, True, MUTED)])
    footer(s, 1)
    notes(
        s,
        "Remember: one ask. Feel: HK is in control and compliant. Do: approve concentration on initiation, not more calls. Strip names before send.",
    )

    # --- Slide 2 ---
    s = prs.slides.add_slide(blank)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    fill(bg, PAPER)
    header(s, "BESREMi · HK PV · PM field pack", "Biweekly · [dates] · Mid · Internal · De-identified")
    kicker(s, "Five-second scorecard")
    title(s, "Initiation, not awareness, is the stall.")
    rags = [
        (
            "UPTAKE VS PLAN",
            "AMBER",
            AMBER_SOFT,
            AMBER,
            "Awareness holds; initiation is slow.",
            "Definition: private uptake vs agreed HQ plan — not vs last week’s call count.",
            "Vs last cycle: unchanged conversion quality.",
            MARGIN,
        ),
        (
            "FORMULARY TRAJECTORY",
            "AMBER",
            AMBER_SOFT,
            AMBER,
            "Field themes are usable; dossier not advanced this cycle.",
            "Definition: whether this cycle strengthened, delayed, or did not change HADF packaging.",
            "Vs last cycle: no new evidence gap; no new unlock.",
            Inches(4.75),
        ),
        (
            "COMPLIANCE",
            "GREEN",
            GREEN_SOFT,
            GREEN,
            "No uncleared claims. ET/MF stayed reactive-only.",
            "Definition: materials cleared; no open UMAO/HKAPI issues; lexicon intact.",
            "Vs last cycle: clean. Keep raw notes in the vault.",
            Inches(9.05),
        ),
    ]
    for name, label, pill_bg, pill_fg, status, defin, delta, left in rags:
        card(s, left, Inches(1.55), Inches(3.85), Inches(5.3))
        head = s.shapes.add_textbox(left + Inches(0.2), Inches(1.7), Inches(2.4), Inches(0.4))
        add_text(head, [(name, 11, True, MUTED)])
        pill = s.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(2.45), Inches(1.72), Inches(1.15), Inches(0.32)
        )
        fill(pill, pill_bg)
        add_text(pill, [(label, 10, True, pill_fg)])
        body = s.shapes.add_textbox(left + Inches(0.2), Inches(2.2), Inches(3.45), Inches(4.3))
        add_text(
            body,
            [
                (status, 18, True, NAVY),
                (defin, 13, False, MUTED),
                (delta, 14, True, INK),
            ],
        )
    footer(s, 2)
    notes(s, "Lock RAG definitions with GM once. Green is not optimism. Missing definition = Amber.")

    # --- Slide 3 ---
    s = prs.slides.add_slide(blank)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    fill(bg, PAPER)
    header(s, "BESREMi · HK PV · PM field pack", "Biweekly · [dates] · Mid · Internal · De-identified")
    kicker(s, "Field signals · max three")
    title(s, "What repeated in the field — not who we visited")
    signals = [
        (
            "Affordability is understood; initiation is not.",
            "Observed: Priority private accounts can repeat PSP logic, then still do not start.",
            "So what: Uptake risk sits after the affordability pitch, not before it.",
            "Implication: Next cycle = onboarding friction, not more awareness meetings.",
            MARGIN,
        ),
        (
            "Price vs traditional IFN is the #1 close-blocker.",
            "Observed: Same objection across accounts: why pay a premium vs off-label IFN.",
            "So what: Stay inside approved PV evidence and dosing convenience.",
            "Implication: No IFN-to-IFN superiority claim. Standing lexicon response only.",
            Inches(4.75),
        ),
        (
            "Two PSP paths are creating two close motions.",
            "Observed: Base Case vs Private Sector (expires end-2026) used as different close paths.",
            "So what: Expiry is a sequencing issue for HQ, not a slogan.",
            "Implication: Do not informal-tweak terms. Confirm eligibility before quoting.",
            Inches(9.05),
        ),
    ]
    for title_t, obs, so, impl, left in signals:
        card(s, left, Inches(1.55), Inches(3.85), Inches(5.3))
        box = s.shapes.add_textbox(left + Inches(0.18), Inches(1.7), Inches(3.5), Inches(4.9))
        add_text(
            box,
            [
                (title_t, 16, True, NAVY),
                (obs, 13, False, INK),
                (so, 13, False, INK),
                (impl, 13, True, TEAL),
            ],
        )
    footer(s, 3)
    notes(s, "Three patterns maximum. ET/MF questions stay off this slide except as 'reactive-only, logged.'")

    # --- Slide 4 ---
    s = prs.slides.add_slide(blank)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    fill(bg, PAPER)
    header(s, "BESREMi · HK PV · PM field pack", "Biweekly · [dates] · Mid · Internal · De-identified")
    kicker(s, "Conversion, not coverage")
    title(s, "Where field time dies")
    card(s, MARGIN, Inches(1.55), Inches(5.9), Inches(5.3))
    add_text(
        s.shapes.add_textbox(MARGIN + Inches(0.2), Inches(1.68), Inches(5.5), Inches(0.3)),
        [("ACCOUNT MOTION (QUALITATIVE)", 11, True, MUTED)],
    )
    steps = [
        ("Awareness · holding", Inches(0.7), Inches(2.15)),
        ("Intent · holding", Inches(1.1), Inches(3.05)),
        ("Initiation · STALL — mark this bar", Inches(1.6), Inches(3.95)),
        ("Persistency · too early to claim", Inches(2.1), Inches(4.85)),
    ]
    widths = [Inches(5.1), Inches(4.3), Inches(3.5), Inches(2.8)]
    for (label, left, top), width in zip(steps, widths):
        sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, Inches(0.72))
        fill(sh, NAVY)
        add_text(sh, [(label, 13, True, WHITE)])
    card(s, Inches(6.7), Inches(1.55), Inches(6.18), Inches(5.3))
    tbl_box = s.shapes.add_textbox(Inches(6.9), Inches(1.7), Inches(5.8), Inches(4.9))
    add_text(
        tbl_box,
        [
            ("RANKED BARRIERS (MAX 4)", 11, True, MUTED),
            ("1  Initiation / onboarding after PSP explanation  → Uptake  · New as the pattern", 14, False, INK),
            ("2  Price vs traditional IFN — lexicon-bound answer only  → Uptake + compliance  · Unchanged", 14, False, INK),
            ("3  Private Sector PSP clock changing urgency unevenly  → Access / PSP  · Rising", 14, False, INK),
            ("4  [Fourth barrier or delete row]", 14, False, MUTED),
            (
                "Moved this cycle: Stopped spreading coverage. Next two weeks: initiation checklist on the priority-account list (titles only; no HCP names on this slide).",
                14,
                True,
                NAVY,
            ),
        ],
    )
    footer(s, 4)
    notes(s, "Funnel widths are illustrative. Do not invent patient or account counts. HA formulary line belongs in RAG, not as a fourth vanity chart.")

    # --- Slide 5 ---
    s = prs.slides.add_slide(blank)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    fill(bg, PAPER)
    header(s, "BESREMi · HK PV · PM field pack", "Biweekly · [dates] · Mid · Internal · De-identified")
    kicker(s, "Decision page")
    title(s, "Options, risks, and the HQ ask")
    opts = [
        ("NOT RECOMMENDED", "A. Keep activity reports", "Visit counts and trip notes. Easy to write; HQ cannot see the thesis.", MARGIN, WHITE_CARD),
        ("RECOMMENDED", "B. Signal → implication → ask", "This pack. Three patterns, RAG vs plan, one decision date.", Inches(4.75), TEAL_SOFT),
        ("NOT RECOMMENDED", "C. CRM dump", "Looks rigorous, usually unreadable, often too sensitive to forward.", Inches(9.05), WHITE_CARD),
    ]
    for tag, ttl, body, left, col in opts:
        card(s, left, Inches(1.48), Inches(3.85), Inches(2.15), col)
        box = s.shapes.add_textbox(left + Inches(0.16), Inches(1.55), Inches(3.55), Inches(2.0))
        add_text(box, [(tag, 10, True, TEAL), (ttl, 15, True, NAVY), (body, 12, False, INK)])
    card(s, MARGIN, Inches(3.78), Inches(6.05), Inches(1.35))
    add_text(
        s.shapes.add_textbox(MARGIN + Inches(0.16), Inches(3.86), Inches(5.75), Inches(1.2)),
        [
            ("PRE-MORTEM", 11, True, MUTED),
            ("If this fails: someone still scores the team on call volume, so activity theatre returns.", 13, False, INK),
        ],
    )
    card(s, Inches(6.83), Inches(3.78), Inches(6.05), Inches(1.35))
    add_text(
        s.shapes.add_textbox(Inches(7.0), Inches(3.86), Inches(5.75), Inches(1.2)),
        [
            ("SHAREABLE-PACK RISK", 11, True, MUTED),
            ("A named KOL or patient-adjacent story leaks into a forwardable deck.", 13, False, INK),
        ],
    )
    card(s, MARGIN, Inches(5.25), Inches(12.43), Inches(1.75))
    add_text(
        s.shapes.add_textbox(MARGIN + Inches(0.16), Inches(5.32), Inches(12.1), Inches(1.6)),
        [
            ("NEXT ACTIONS  ·  role + date, not names", 11, True, MUTED),
            ("1  Rewrite last trip report into this 5-slide pack; strip names  ·  PM  ·  This week", 14, False, INK),
            ("2  Lock RAG definitions with GM (uptake / formulary / compliance)  ·  PM + GM  ·  Next HQ cycle", 14, False, INK),
            ("3  Compliance pass: no ET/MF promotion, no uncleared claims  ·  PM + Legal/Compliance  ·  Before send", 14, False, INK),
        ],
    )
    footer(s, 5)
    notes(
        s,
        "Always: PSP Base Case vs Private Sector (end-2026), HA formulary impact line, PV-only lexicon, sensitivity Mid unless raw notes are attached (then High — do not attach).",
    )

    out = Path(__file__).resolve().parents[1] / "playbooks" / "hq-field-progress-slides.pptx"
    prs.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    build()
