#!/usr/bin/env python3
"""Build Word files documenting the MPNicare Hong Kong overlay."""
from pathlib import Path
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

OUT = Path("/workspace/samples/mpnicare-hk-locale/word")
ART = Path("/cursor/stores/self/artifacts/mpnicare-hk-review")
OUT.mkdir(parents=True, exist_ok=True)
ART.mkdir(parents=True, exist_ok=True)

NAVY = RGBColor(0x12, 0x35, 0x3A)
TEAL = RGBColor(0x0B, 0x6E, 0x6E)


def set_run_font(run, name="Calibri", size=11, bold=False, color=None, east="Microsoft JhengHei"):
    run.bold = bold
    run.font.size = Pt(size)
    run.font.name = name
    if color:
        run.font.color.rgb = color
    r = run._element.get_or_add_rPr()
    rFonts = r.find(qn("w:rFonts"))
    if rFonts is None:
        from lxml import etree
        rFonts = etree.SubElement(r, qn("w:rFonts"))
    rFonts.set(qn("w:ascii"), name)
    rFonts.set(qn("w:hAnsi"), name)
    rFonts.set(qn("w:eastAsia"), east)


def heading(doc, text, level=1):
    p = doc.add_heading(text, level=level)
    for run in p.runs:
        set_run_font(run, size=16 if level == 1 else 13, bold=True, color=NAVY, east="Microsoft JhengHei")
    return p


def para(doc, text, *, size=11, bold=False, space_after=8):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold)
    return p


def shade_header(cell, hex_color="12353A"):
    tc = cell._tePr if hasattr(cell, "_tePr") else cell._tc
    tcPr = tc.get_or_add_tcPr()
    from docx.oxml import parse_xml
    tcPr.append(parse_xml(
        f'<w:shd xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:fill="{hex_color}"/>'
    ))


def add_table(doc, headers, rows, col_widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        p = hdr[i].paragraphs[0]
        run = p.add_run(h)
        set_run_font(run, size=10, bold=True, color=RGBColor(255, 255, 255))
        shade_header(hdr[i])
    for r_i, row in enumerate(rows, start=1):
        for c_i, val in enumerate(row):
            cell = table.rows[r_i].cells[c_i]
            cell.text = ""
            p = cell.paragraphs[0]
            run = p.add_run(str(val))
            set_run_font(run, size=10)
    if col_widths:
        for row in table.rows:
            for i, w in enumerate(col_widths):
                row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return table


def setup_doc(title, subtitle):
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Cm(1.8)
    section.bottom_margin = Cm(1.8)
    section.left_margin = Cm(2.0)
    section.right_margin = Cm(2.0)
    p = doc.add_paragraph()
    r = p.add_run("MPNicare ｜ PharmaEssentia Hong Kong")
    set_run_font(r, size=10, color=TEAL, bold=True)
    h = doc.add_paragraph()
    r = h.add_run(title)
    set_run_font(r, size=20, bold=True, color=NAVY)
    para(doc, subtitle, size=11)
    para(doc, "Date: 21 August 2026  ·  Sensitivity: Low (public patient-education site)  ·  Status: implementation spec / legal-review draft", size=10)
    return doc


def build_change_log():
    doc = setup_doc(
        "Hong Kong Chinese wording overlay — change log",
        "Layout, page structure and column placement stay the same. Only Hong Kong chrome (menu, titles, footer, terms) and regional-content labels change. Article bodies in the three regional columns are not rewritten.",
    )

    heading(doc, "1. What this file is", 1)
    para(doc, "This is the working change log for the 中文（香港） locale on mpnicare.org. Use it with web (Wix strings), Medical (disclaimer lines only) and Legal (terms page). It records what was implemented in the overlay sample after the 21 August 2026 review: regional notices must not appear on 病人教育專區; they belong only on the three source columns.")

    heading(doc, "2. Labelling rules (do not rewrite articles)", 1)
    para(doc, "Applies only to these three columns (menu names change; bodies stay original): 血腫專欄 → 血液腫瘤專欄; 健康照護 → 健康資訊; 品味生活 (title unified from 生活品味).")
    add_table(
        doc,
        ["Placement", "Add this", "Do not add on"],
        [
            ["Column page — under existing title, above article list", "其他地區內容提示\n本欄文章由香港以外地區的團隊或醫護專業人員提供，內容未必適用於香港，僅供一般參考。", "病人教育專區, 關於MPN, 首頁整頁, 友善連結, 使用條款"],
            ["Article card — beside existing category name", "其他地區內容", "病人教育專區 tiles"],
            ["Article page — under title or byline, one line", "其他地區內容｜原文保留，內容未必適用於香港。", "Hong Kong chrome pages"],
        ],
        [5.2, 7.5, 4.5],
    )
    para(doc, "Homepage: no full-page warning box. The three latest-article cards only get the small tag beside the category name.")

    heading(doc, "3. Wording changes implemented", 1)
    add_table(
        doc,
        ["Page", "Original", "In this sentence / place", "Hong Kong wording", "Note"],
        [
            ["Site menu", "血腫專欄", "Menu item", "血液腫瘤專欄", "hematoma ≠ haematology-oncology. Menu only."],
            ["Site menu", "健康照護", "Menu item", "健康資訊", "Menu only; article bodies unchanged."],
            ["Menu + page title", "品味生活 / 生活品味", "Menu vs title word order", "品味生活 (both)", "Unify; do not rewrite articles."],
            ["Footer (site-wide)", "信息", "非本網站所有之信息", "資料", "Shared HK footer."],
            ["Footer (site-wide)", "帳號", "加入MPN官方line帳號", "賬號", "HK 賬. Site-wide footer, so change."],
            ["Footer (site-wide)", "智慧財產權", "為了尊重授權使用之智慧財產權", "知識產權", "Site-wide HK footer."],
            ["Home", "並發症", "易引發嚴重並發症甚至危及生命", "併發症", "Correct medical character. Live /zh-hk introduced 並."],
            ["About MPN", "紅細胞", "真性紅細胞增多症 / 主要是紅細胞增生", "紅血球", "Stop machine-translation regression."],
            ["About MPN", "白細胞", "血小板與白細胞增多", "白血球", "Align with 紅血球."],
            ["About MPN", "血細胞", "If present on the same page", "血球", "Avoid ⋯細胞 for blood cells."],
            ["About MPN", "按我了解更多", "按我了解更多MPN", "按此了解更多", "HK web copy rarely uses 按我."],
            ["Education page", "衛教專區", "Page / category name", "病人教育專區", "Name only. No regional banner on this page."],
            ["Education page", "紅細胞增多症", "認識紅細胞增多症", "認識紅血球增多症", "Align titles."],
            ["Education page", "有愛相髓病友故事集", "Category title", "病友故事集", "Name only; story bodies unchanged."],
            ["Terms", "無限製", "您無限製或無條件地接受這些條款", "無限制", "Simplified-to-traditional error."],
            ["Terms", "個資", "刪除您的個資等權利", "個人資料", "Not used in HK legal copy."],
            ["Terms", "個人資料保護法 第3、10、11條", "Taiwan PDPA clause numbers", "Rewrite under 《個人資料（私隱）條例》(Cap. 486)", "Do not keep Arts. 3/10/11. See File 2."],
            ["Terms", "互聯網事業", "如同非互聯網事業的使用方式", "網上業務", "HK commercial wording."],
            ["Terms", "藥華藥 / 藥華醫藥", "Two short names mixed", "藥華醫藥 (first mention: PharmaEssentia 藥華醫藥)", "Unify."],
            ["Terms", "百份百 / 資訊", "無法保證資訊百份百正確無誤", "百分百 / 資料", "Correct character + footer alignment."],
        ],
        [3.0, 3.2, 4.0, 4.2, 3.8],
    )

    heading(doc, "4. What must not change", 1)
    para(doc, "• All article bodies in 血腫專欄 / 健康照護 / 品味生活 (including after menu rename).")
    para(doc, "• Treatment methods, drug lists, studies, doses and percentages in those articles.")
    para(doc, "• Local terms, hospital names, product names and system names in those articles.")
    para(doc, "• Current layout, pagination and column structure.")
    para(doc, "• Friendly links page: no wording change required. Keep existing non-HK organisation links; add HK organisations later as extra rows.")

    heading(doc, "5. Do not use the live Wix /zh-hk pack as-is", 1)
    para(doc, "The current public https://www.mpnicare.org/zh-hk empties the three article columns, introduces 紅細胞 / 白細胞 / 並發症 / 無限製, and still cites Taiwan PDPA Arts. 3, 10 and 11. Replace it with this overlay: original articles + labels + HK chrome.")

    heading(doc, "6. Review owners", 1)
    add_table(
        doc,
        ["Item", "Owner", "Decision needed"],
        [
            ["String table + three label placements on Wix", "PM + web", "Implement overlay, do not rebuild templates"],
            ["Three disclaimer lines only", "Medical", "Confirm wording; do not rewrite articles"],
            ["Cap. 486 terms (File 2)", "Legal / Compliance", "Sign off before production"],
            ["UMAO check of chrome + labels", "PM + Legal", "Await user-supplied Cap. 231 files"],
        ],
        [5.5, 4.0, 7.5],
    )
    para(doc, "This is a patient-education site, not a BESREMi promotional piece. No new product claims. ET/MF material in source articles stays labelled as non-Hong Kong content.")

    path = OUT / "MPNicare-HK-wording-change-log.docx"
    doc.save(path)
    return path


def build_terms():
    doc = setup_doc(
        "使用條款與私隱政策 — Hong Kong rewrite (legal review draft)",
        "Not a find-and-replace of Taiwan《個人資料保護法》Arts. 3, 10 and 11. Rewrite under Hong Kong Cap. 486. Do not publish until Legal signs off.",
    )

    heading(doc, "1. Mapping from the current page", 1)
    add_table(
        doc,
        ["Current (do not keep)", "Hong Kong"],
        [
            ["無限製", "無限制"],
            ["個資", "個人資料"],
            ["個人資料保護法第三條 / 第10條 / 第11條", "《個人資料（私隱）條例》(第486章) — data access s.18; correction s.22; refusal s.20 / s.24; fee s.28"],
            ["互聯網事業", "網上業務"],
            ["藥華藥 and 藥華醫藥 mixed", "PharmaEssentia 藥華醫藥 on first mention; 藥華醫藥 thereafter"],
            ["資訊百份百", "資料百分百"],
            ["使用條款與隱私權政策", "使用條款與私隱政策"],
        ],
        [8.0, 9.0],
    )

    heading(doc, "2. Draft copy for the Hong Kong page", 1)
    para(doc, "使用條款與私隱政策", size=14, bold=True)

    blocks = [
        "本網站由 PharmaEssentia 藥華醫藥股份有限公司（以下簡稱「藥華醫藥」）所建立經營。我們重視每一位使用者所享有的服務，特此說明本網站的使用政策，以保障您的權益，請您細讀本使用條款的內容。",
        "一般性資料",
        "對於本站所載資料的取覽或使用，您受下列條款和條件以及所有適用法律所規範。經由取覽或瀏覽本網站，您無限制或無條件地接受這些條款和條件，並確認其將取代您和藥華醫藥之間其他任何的協議。",
        "醫療資料",
        "本網站之醫療相關資料僅供科學資料或病人教育目的使用。由於醫療科技的發展日新月異，本公司無法保證資料百分百正確無誤。任何疾病治療、醫學問題及專業知識，應諮詢您的專業醫生及護士，本站不提供任何診斷、用藥或治療建議。",
        "私隱政策（香港）",
        "藥華醫藥尊重訪客私隱，並按香港法例第486章《個人資料（私隱）條例》（下稱「《條例》」）的保障資料原則處理個人資料。",
        "您可向本公司提出：（一）查閱資料要求（Data Access Request，《條例》第18條）；以及（二）改正資料要求（Data Correction Request，《條例》第22條）。",
        "本公司會在《條例》規定的時限內回覆。在第20條所列明的情況下，本公司可拒絕依從查閱資料要求；在第24條所列明的情況下，可拒絕依從改正資料要求。本公司亦可按第28條收取不超逾直接成本的合理費用。",
        "《條例》並無賦予與台灣《個人資料保護法》第3條相同的概括「刪除／停止處理」法定權利。本公司仍會按保障資料第2原則（保留期間）及第3原則（使用限制），在不再需要時刪除或停止使用個人資料。您亦可要求退出通訊服務。是否接納個別申請，須視乎執行業務所必須、法定保存期間及《條例》准許的豁免而定。",
        "個人資料的使用",
        "個人資料包括您的姓名、地址、電話號碼、電郵地址，或其他可合理用於識別您的資料。藥華醫藥只在您自願提供時收集該等資料。",
        "當藥華醫藥收到個人資料時，我們可能將資料用於合理商業用途，如同非網上業務的使用方式。例如，我們可能透過通訊軟件或定期訊息聯絡您。為提供準確服務，收集的資料亦可能用於編製統計及分析，但不會公開可識別個別人士的資料。",
        "您的資料可能傳送至位於其他國家的藥華醫藥附屬機構處理。藥華醫藥不會出售或出租個人資料，除非事先通知並取得您的明確同意。",
        "請聯絡我們：sales@museshc.com",
    ]
    for b in blocks:
        is_h = b in {"一般性資料", "醫療資料", "私隱政策（香港）", "個人資料的使用"}
        para(doc, b, size=12 if is_h else 11, bold=is_h)

    heading(doc, "3. Legal review flags", 1)
    para(doc, "• Confirm data-access / correction / refusal / fee sections against current Cap. 486 and PCPD guidance.")
    para(doc, "• Confirm whether a voluntary deletion / opt-out line should stay as company policy (not as a statutory PDPA Art. 3 right).")
    para(doc, "• Confirm cross-border transfer wording for PharmaEssentia affiliates.")
    para(doc, "• UMAO (Cap. 231) is out of this file; chrome and labels to be checked separately when the user uploads the ordinance pack.")
    para(doc, "• Do not publish this draft as the live privacy notice until Legal signs off.")

    path = OUT / "MPNicare-HK-terms-privacy-rewrite.docx"
    doc.save(path)
    return path


def main():
    a = build_change_log()
    b = build_terms()
    for p in (a, b):
        dest = ART / p.name
        dest.write_bytes(p.read_bytes())
        print("wrote", p, p.stat().st_size)
        print("artifact", dest)


if __name__ == "__main__":
    main()
