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
        "This report concerns IQVIA RDS Limited, part of IQVIA Holdings Inc., an international contract research "
        "organization listed in the United States under the ticker IQV. The listed parent had a market capitalization "
        "of about $44 billion in mid-October 2026. I worked there for six and a half years, first as a Clinical "
        "Research Associate and later as an Associate Clinical Project Manager. The company runs clinical trials and "
        "delivers results to internal functions and to external clients. Creativity here means a novel and useful "
        "improvement in how a trial is run. Innovation means that improvement is carried out. I identify the obstacles "
        "that kept staff from that kind of creativity, then recommend one feasible action for each of the two most "
        "serious obstacles, and the steps I would use to put those actions in place."
    )

    obs_open = (
        "Turnover makes both worse. Vacancies are hard to fill, and joiners are mostly new graduates or people seeking "
        "faster promotion. Two obstacles do the direct damage."
    )

    obs1 = (
        "The first is concurrent overload. Associates in peer companies handle about five trials, a figure I take from "
        "former colleagues in those firms. Here the same role carried eight to ten at once. Quieter trials still need "
        "routine work. When several are active, client requests and dated tasks fill the day. A view of the whole study "
        "appears only in a quiet stretch. Hospital documents for a human trial are the clear case: they must be collected "
        "and uploaded to the company database, they are less urgent than a client deadline, and they are omitted when the "
        "week is full. Leave does not create real cover. Client and hospital mail accumulates. A backup associate can take "
        "some urgent items, but study access sits with the responsible associate, so the backup can do only the easy tasks. "
        "Amabile (1998) treats time as a resource that must reach a threshold of sufficiency; below it, effort goes into "
        "coping. Extreme pressure also cuts creative thinking on that day and the days after (Amabile et al., 2002, as "
        "taught in Session 4). The omitted hospital file is the whole-study picture that pressure never allows."
    )

    obs2 = (
        "The second obstacle is that help has no place in the priority order. The hierarchy gives each person a small piece "
        "of the trial. Colleagues rarely step in, because their own list is full and the task often sits outside their "
        "access. During internal database audits, associates ask assistants to update the records. Those requests lose to "
        "external client work: they are less urgent, and they are not billable. Assistants have no buffer. Management then "
        "cannot see the current status of the study. Amabile (1998) includes help through difficulty, and information that "
        "actually moves, among the conditions for creativity. IDEO's helping study adds that help fails when the right "
        "person is overloaded, so slack has to be designed (Amabile, Fisher, and Pillemer, 2014). If that status fact stays "
        "in one queue, managers work from a partial picture (Thompson, chapter 9). Staff also rarely see past their own "
        "fragment, and new graduates inherit it."
    )

    rec1 = (
        "For the overload, I recommend a staffed cap of about five active trials per associate. The cap needs people. "
        "I would ask the team for the missing headcount: count the active trials, divide by five, and subtract the "
        "associates already in the role. Pay has to rise with those seats. The present load is known in the industry, "
        "and the people who accept it are mostly new graduates or candidates seeking a fast promotion. A higher salary "
        "is how associates who have already run a whole trial will take the job. That is Amabile's expertise component. "
        "It is the resource that lets the load reach a threshold of sufficiency. Pay above a fair load does not buy "
        "creativity. Pay that brings the load to about five, and brings people who can see a whole study, is the money "
        "the 1998 article says is missing (Amabile, 1998)."
    )

    rec1b = (
        "Every study would have at least two associates with access. The second person's authority is limited to a "
        "written list of items that cannot wait, so cover is standing and a week of leave does not freeze the study. "
        "IDEO's helping article is direct: a person who cannot reach the work cannot help (Amabile, Fisher, and "
        "Pillemer, 2014). I would make one request. In the first month I would count active trials and write the "
        "headcount and pay case. In the second month I would hire against that number and pair every study. In the "
        "third month, once the active load is near five, the quieter trials would get a weekly block for the hospital "
        "documents that are now omitted. The test is the load itself. Active trials sit near five per person, and the "
        "document queue is reviewed every week. Where one deadline is genuinely urgent, Session 4 still applies: protect "
        "that person from every other interruption and state why the job is vital (Amabile et al., 2002)."
    )

    rec2 = (
        "For the failure of help, I recommend moving internal work, and the documentation that supports it, to university "
        "interns. That work faces the company, not the client. Interns would support the associate on documentation: "
        "collecting hospital files, checking that a set is complete against a list, and uploading it. They would also "
        "keep the internal database current for audits. They would not handle payments. Through the documents and the "
        "status updates they would learn how a trial actually runs, which is the industry knowledge a narrow job never "
        "shows them. An AI system would still draft routine reports, categorize documents, and prepare hospital payment "
        "steps. Associates keep the judgment, including whether a payment is right. Session 4 teaches that a model can "
        "raise output and can also make drafts more alike, while usefulness stays with the person who knows the study "
        "(Doshi and Hauser, 2024, as taught). The hour freed is the slack IDEO says helping requires (Amabile, Fisher, "
        "and Pillemer, 2014)."
    )

    rec2b = (
        "The intern's list would be written: documentation support and internal updates, and no payments. Amabile's "
        "challenge rule is to match the task to the person. An intern can learn the trial from the files without "
        "carrying client risk, and the associate is no longer the only one who can complete a document set (Amabile, "
        "1998). The AI tools would start on three streams: report drafts, document categories, and payment preparation "
        "for an associate to approve. The associate clinical project manager would still read the date of the last "
        "database update. Thompson's chapter is why that line exists: the fact has to leave one person's queue. Interns "
        "and the tools can start in the same quarter as the headcount request. They ease the present team while the "
        "new associates are being found."
    )

    close = (
        "Creativity in this organization is a useful improvement in how a trial is run: a complete document set, a "
        "status a manager can trust, and a second associate who can cover the items that cannot wait. The two actions "
        "are a staffed cap near five, with pay that can attract experienced people and two-person access on every "
        "study, and a shift of internal documentation to interns and of routine drafting to AI, so that regular staff "
        "have time to see the whole trial. Payments stay with the associates. Headcount, pay, access, interns, and "
        "tools are one design. Each piece fails if the others are left out."
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
