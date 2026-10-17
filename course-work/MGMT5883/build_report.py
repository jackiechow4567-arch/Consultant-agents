#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the MGMT5883 consulting report and estimate double-spaced pages."""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from PIL import ImageFont

OUT = Path("/workspace/course-work/MGMT5883")
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

PAGE_W_IN = 6.5
PAGE_H_IN = 9.0
PT = 12
LINE_PT = 24


def wrap_first_indent(text, font, width_px, indent_px):
    words = text.split()
    lines, cur, limit = [], "", width_px - indent_px
    for w in words:
        trial = w if not cur else cur + " " + w
        if font.getlength(trial) <= limit:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
            limit = width_px
    if cur:
        lines.append(cur)
    return lines or [""]


def wrap_lines(text, font, width_px):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = w if not cur else cur + " " + w
        if font.getlength(trial) <= width_px:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def estimate(blocks):
    width_px = PAGE_W_IN * 72
    font_r = ImageFont.truetype(FONT_REG, PT)
    font_b = ImageFont.truetype(FONT_BOLD, PT)
    font_title = ImageFont.truetype(FONT_BOLD, 14)
    used_pt = 0.0
    section_start = 0.0
    print("--- pagination estimate (Liberation Serif ~= Times, double, 1-inch) ---")
    for kind, text in blocks:
        if kind == "title":
            lines = wrap_lines(text, font_title, width_px)
            h = len(lines) * 18 + 6
        elif kind == "subtitle":
            lines = wrap_lines(text, font_r, width_px)
            h = len(lines) * 16 + 10
        elif kind == "h":
            if section_start:
                print(f"   section length {((used_pt - section_start) / (PAGE_H_IN * 72)):.2f} p")
            section_start = used_pt
            lines = wrap_lines(text, font_b, width_px)
            h = 10 + len(lines) * LINE_PT
        else:
            lines = wrap_first_indent(text, font_r, width_px, 36)
            h = len(lines) * LINE_PT
        used_pt += h
        pages_here = used_pt / (PAGE_H_IN * 72)
        print(f"{kind:8} {len(lines):3} lines  cum {pages_here:.2f}p  {text[:64]}")
    if section_start:
        print(f"   section length {((used_pt - section_start) / (PAGE_H_IN * 72)):.2f} p")
    pages = used_pt / (PAGE_H_IN * 72)
    words = sum(len(t.split()) for k, t in blocks if k == "p")
    print(f"TOTAL {pages:.2f} pages | BODY WORDS {words}")
    # Conservative Word double-spacing (single ~14pt, double ~28pt)
    cons_lines = sum(
        len(wrap_first_indent(t, font_r, width_px, 36)) for k, t in blocks if k == "p"
    )
    cons_pages = (cons_lines * 28 + 8 * 28) / (PAGE_H_IN * 72)
    print(f"CONSERVATIVE Word double ~ {cons_pages:.2f} pages ({cons_lines} body lines)")


def set_run_font(run, name, size, bold=False, italic=False, color=None):
    run.bold = bold
    run.italic = italic
    run.font.name = name
    run.font.size = Pt(size)
    if color:
        run.font.color.rgb = color
    r = run._element
    rPr = r.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = r.makeelement(qn("w:rFonts"), {})
        rPr.append(rFonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(a), name)


def add_p(doc, text, *, size=12, bold=False, italic=False, center=False,
          indent=True, space_before=0, space_after=0, double=True):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing_rule = WD_LINE_SPACING.DOUBLE if double else WD_LINE_SPACING.SINGLE
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if indent and not center:
        pf.first_line_indent = Inches(0.5)
    run = p.add_run(text)
    set_run_font(run, "Times New Roman", size, bold=bold, italic=italic)
    return p


def main():
    title = "Creativity under Trial Overload at IQVIA RDS Limited"
    subtitle = "A consulting report  |  October 2026"

    intro = (
        "This report is about IQVIA RDS Limited. It is part of IQVIA Holdings Inc., an international contract research "
        "organisation listed in the United States (ticker: IQV). In mid-October 2026, the listed parent had a market "
        "capitalisation of about $44 billion. I worked in this company for 6.5 years. I started as a Clinical Research "
        "Associate, and my last title was Associate Clinical Project Manager. My projects were clinical trials, and we "
        "delivered the results to both internal parties and external clients. In this course, creativity means a new "
        "and useful idea, and innovation means the idea is carried out. Below I explain two obstacles that hindered "
        "creativity in this organisation, and I give one recommendation for each, including how I would implement it."
    )

    obs_open = (
        "The workload is well known in the industry, so a resignation is hard to replace. Usually only fresh graduates, or "
        "people who want a faster promotion, will join. Hence turnover is high, and both obstacles below get worse."
    )

    obs1 = (
        "The first obstacle is overload. I handled 8 to 10 studies at the same time. Ex-colleagues told me that about 5 "
        "studies is the usual load in other companies in this industry. The quieter studies still had routine work. When "
        "several were active, client requests and deadlines filled the day. It was hard to manage the rest, and I had no "
        "time to look at the whole picture. For example, a human "
        "trial needs many documents. We collect them from the hospitals and upload them to the company database. These "
        "tasks are less urgent, so they are easily omitted. Leave was also hard. Client and hospital emails piled up. A "
        "backup CRA could take some urgent tasks, but study access is limited to the responsible CRA, so the backup could "
        "only do easy tasks. Amabile (1998) says that if time is not sufficient, people only cope with deadlines. Session 4 "
        "taught that very high time pressure made people 45% less likely to think creatively, and the effect continued "
        "into the next days (Amabile et al., 2002). The document work, which shows the whole study, was the first thing dropped."
    )

    obs2 = (
        "The second obstacle is that people cannot help each other. The hierarchy is clear, and each person only manages "
        "his or her own tasks. When a colleague is in trouble, others are already too busy, and they may not have access "
        "to that study. Hence exposure stays inside one's own position. For internal audits, we asked clinical research "
        "assistants to update the database. An internal request is less urgent than a client request, and assistants have "
        "no buffer time. Besides, this work is usually not billable, so the priority is lower. If the system is not "
        "updated, higher management cannot see the latest status. Amabile (1998) says creativity needs help through a "
        "difficulty, and it needs information to move. The IDEO article adds that help fails when people are already full, "
        "so spare time has to be planned (Amabile, Fisher, and Pillemer, 2014). Thompson's chapter says the same thing "
        "about facts: if one person keeps the update, the others work with an incomplete picture."
    )

    rec1 = (
        "For the overload, I recommend capping active trials at about five per associate. To do this, headcount should "
        "be requested. More manpower is required to handle the study work. I would count the active trials, divide by "
        "five, and subtract the current number of associates. That gap is the headcount to request. Salary should also "
        "be increased, so the company can attract talents who have already run a study, not only fresh graduates. "
        "Amabile (1998) treats expertise as one part of creativity, and she treats time as a resource that has to be "
        "sufficient. If the load stays at 8 to 10, a higher salary alone still leaves no time to look at the whole "
        "picture. The salary is to bring in capable people. The headcount is to bring the load down to about five."
    )

    rec1b = (
        "Besides, each study should have at least two associates with access. The second associate should be limited "
        "to a written list of items that cannot wait. Then, when the responsible associate takes leave, the backup is "
        "not stuck with easy tasks only, and the study does not stop. This follows the IDEO point that a person who "
        "cannot reach the work cannot help (Amabile, Fisher, and Pillemer, 2014). I would do it in three steps. In the "
        "first month, I would count the active trials and prepare the headcount and salary request. In the second month, "
        "I would hire and put two associates on each study. In the third month, after the active load is near five, I "
        "would set a weekly time block for the quieter studies, so the hospital documents that are now omitted can be "
        "followed up. I would check two results: each person has about five active trials, and the document list is "
        "reviewed every week. If one deadline is truly urgent, Session 4 suggests protecting that person from other "
        "interruptions and stating why the job is important (Amabile et al., 2002)."
    )

    rec2 = (
        "For the second problem, I recommend hiring university interns for the internal work. This work faces the "
        "company, not the client, so it does not directly affect the client. Interns can support the associate on "
        "documentation, for example collecting hospital files, checking them against the list, and uploading them. "
        "They can also update the internal database for audits. Payment will not be handled by them. Through this "
        "process, interns can learn more about the industry, and regular staff can have more time. AI can support the "
        "regular work as well, for example report writing, document categorisation, and preparing the payment process "
        "to hospitals. The associate still checks whether the report is correct and whether the payment is right. "
        "Session 4 taught that AI can increase output, but the drafts can also become more similar, so the judgment "
        "should stay with the person who knows the study (Doshi and Hauser, 2024). The time saved is the spare time "
        "that the IDEO article says a helping culture needs (Amabile, Fisher, and Pillemer, 2014)."
    )

    rec2b = (
        "I would write the intern's job list clearly: documentation support and internal updates, and no payment. This "
        "matches Amabile's point that the task should fit the person (Amabile, 1998). An intern can learn from the "
        "files without taking client risk, and the associate is no longer the only person who can complete the document "
        "set. AI would start with three types of work: report drafts, document categories, and payment preparation for "
        "an associate to approve. I would still check the date of the last database update, so a gap is seen before the "
        "audit. Thompson's chapter explains why this check matters: the updated status has to leave one person's queue "
        "and reach the manager. Interns and the AI tools can start in the same quarter as the headcount request. They "
        "can ease the current team while the new associates are being hired."
    )

    close = (
        "In this organisation, a creative idea is a useful improvement in how a trial is run. Examples are a complete "
        "document set, a status that management can trust, and a second associate who can cover the items that cannot "
        "wait. I recommend two actions. First, request headcount and a higher salary so that each associate handles "
        "about five active trials, and assign two associates with access to each study. Second, let university interns "
        "support documentation and internal updates, and use AI for routine reports, document categorisation, and "
        "payment preparation. Payment decisions stay with the associates. The two actions need each other. Headcount "
        "alone still leaves the internal work undone."
    )

    blocks = [
        ("title", title),
        ("subtitle", subtitle),
        ("h", "Introduction"),
        ("p", intro),
        ("h", "Obstacles to creativity and innovation"),
        ("p", obs_open),
        ("p", obs1),
        ("p", obs2),
        ("h", "Recommendations and how I would implement them"),
        ("p", rec1),
        ("p", rec1b),
        ("p", rec2),
        ("p", rec2b),
        ("h", "Conclusion"),
        ("p", close),
    ]
    estimate(blocks)
    for name, text in (
        ("intro", intro),
        ("obstacles", " ".join([obs_open, obs1, obs2])),
        ("recs", " ".join([rec1, rec1b, rec2, rec2b])),
        ("close", close),
    ):
        print(f"WORDS {name:10} {len(text.split())}")

    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Inches(8.5)
    sec.page_height = Inches(11)
    sec.left_margin = Inches(1)
    sec.right_margin = Inches(1)
    sec.top_margin = Inches(1)
    sec.bottom_margin = Inches(1)

    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)
    normal._element.rPr.rFonts.set(qn("w:ascii"), "Times New Roman")
    normal._element.rPr.rFonts.set(qn("w:hAnsi"), "Times New Roman")
    pf = normal.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    pf.space_after = Pt(0)
    pf.space_before = Pt(0)

    header = sec.header.paragraphs[0]
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = header.add_run("IQVIA RDS Limited  |  Consulting report")
    set_run_font(r, "Times New Roman", 9, italic=True, color=RGBColor(0x55, 0x55, 0x55))
    header.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE

    footer = sec.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = footer.add_run("Course draft  |  Page ")
    set_run_font(r, "Times New Roman", 9, color=RGBColor(0x55, 0x55, 0x55))
    fld = footer.add_run()
    fldChar1 = fld._r.makeelement(qn("w:fldChar"), {qn("w:fldCharType"): "begin"})
    instr = fld._r.makeelement(qn("w:instrText"), {})
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fldChar2 = fld._r.makeelement(qn("w:fldChar"), {qn("w:fldCharType"): "end"})
    fld._r.append(fldChar1)
    fld._r.append(instr)
    fld._r.append(fldChar2)
    set_run_font(fld, "Times New Roman", 9, color=RGBColor(0x55, 0x55, 0x55))

    add_p(doc, title, size=14, bold=True, center=True, indent=False, double=False, space_after=2)
    add_p(doc, subtitle, size=11, italic=True, center=True, indent=False, double=False, space_after=6)

    sections = [
        ("Introduction", [intro]),
        ("Obstacles to creativity and innovation", [obs_open, obs1, obs2]),
        ("Recommendations and how I would implement them", [rec1, rec1b, rec2, rec2b]),
        ("Conclusion", [close]),
    ]
    for h, paras in sections:
        add_p(doc, h, size=12, bold=True, indent=False, space_before=8, double=True)
        for para in paras:
            add_p(doc, para, size=12, indent=True, double=True)

    docx_path = OUT / "consulting-report.docx"
    doc.save(docx_path)
    print("WROTE", docx_path)

    md_parts = [f"# {title}", "", f"*{subtitle}*", ""]
    for h, paras in sections:
        md_parts.append(f"## {h}")
        md_parts.append("")
        for para in paras:
            md_parts.append(para)
            md_parts.append("")
    md_path = OUT / "consulting-report.md"
    md_path.write_text("\n".join(md_parts), encoding="utf-8")
    print("WROTE", md_path)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
  @page {{ size: letter; margin: 1in; }}
  body {{
    font-family: "Times New Roman", Times, serif;
    font-size: 12pt;
    line-height: 2;
    max-width: 6.5in;
    margin: 1in auto;
    color: #111;
  }}
  h1 {{ font-size: 14pt; text-align: center; line-height: 1.3; margin: 0 0 0.2em; }}
  .sub {{ text-align: center; font-style: italic; font-size: 11pt; line-height: 1.3; margin-bottom: 0.6em; }}
  h2 {{ font-size: 12pt; line-height: 2; margin: 0.4em 0 0; }}
  p {{ margin: 0; text-indent: 0.5in; }}
</style>
</head>
<body>
<h1>{title}</h1>
<p class="sub">{subtitle}</p>
"""
    for h, paras in sections:
        html += f"<h2>{h}</h2>\n"
        for para in paras:
            html += f"<p>{para}</p>\n"
    html += "</body></html>\n"
    html_path = OUT / "consulting-report.html"
    html_path.write_text(html, encoding="utf-8")
    print("WROTE", html_path)


if __name__ == "__main__":
    main()
