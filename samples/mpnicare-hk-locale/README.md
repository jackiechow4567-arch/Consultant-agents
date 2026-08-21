# MPNicare Hong Kong Chinese locale sample

Interactive overlay of [mpnicare.org](https://www.mpnicare.org/). Layout, page structure, and column placement stay the same. Switching to **中文（香港）** changes chrome copy, adds regional-content labels, and rewrites the terms page for Hong Kong law.

## Open the sample

If you only need to review the look: open **`REVIEW.html`** (static screenshots, no clicking required).

To try the language toggle: open `index.html` in a browser.

1. Default view = current Traditional Chinese chrome (Taiwan source site).
2. Click **中文（香港）** in the top-right language control.
3. Walk Home, About MPN, Patient education, the three columns, Friendly links, Terms, and one article.

## What changes in Hong Kong Chinese

| Surface | Change |
|---|---|
| Menu | 血腫專欄 → 血液腫瘤專欄; 健康照護 → 健康資訊; 品味生活 unified |
| Education | 衛教專區 → 病人教育專區; 認識紅血球增多症; 病友故事集 |
| About MPN | 紅血球／白血球; 按此了解更多 |
| Home | 併發症 (correct medical character) |
| Footer | 知識產權; 資料; line賬號 |
| Column pages | Banner under the existing title: 其他地區內容提示 |
| Article cards | Tag beside category: 其他地區內容 |
| Article pages | One line under title/byline; **body copy not rewritten** |
| Terms | 《個人資料（私隱）條例》(Cap. 486) rewrite, not Taiwan PDPA Arts. 3/10/11 |

## What does not change

- Article bodies in 血液腫瘤專欄 / 健康資訊 / 品味生活
- Treatment methods, drug names, studies, doses, percentages
- Local hospital, product, and system names in those articles
- Page grid, column order, and visual system (mint header, pale-blue hero, three cards, green LINE footer)

## Why not the live `/zh-hk` machine translation

The live Wix Hong Kong locale currently:

- Empties the three article columns instead of showing source articles with a label
- Introduces 紅細胞 / 白細胞 / 並發症 / 無限製 — worse than the Taiwan original
- Still cites Taiwan’s Personal Data Protection Act articles 3, 10 and 11

This sample is the recommended overlay: keep the original articles, label them, and localise only chrome + legal.

## Screenshots

| File | What it shows |
|---|---|
| `screenshots/sample-tw-home.png` | Default Traditional Chinese chrome (source layout) |
| `screenshots/sample-hk-home.png` | After clicking **中文（香港）**: menu, labels, footer |
| `screenshots/sample-hk-article.png` | Article page with one-line regional disclaimer; body unchanged |
| `screenshots/sample-hk-edu.png` | 病人教育專區 / 紅血球增多症 / 病友故事集 |
| `screenshots/sample-hk-about.png` | 紅血球／白血球; 按此了解更多 |
| `screenshots/sample-hk-terms.png` | Cap. 486 privacy rewrite (legal review draft) |
| `original-homepage.png` | Live mpnicare.org homepage captured for layout matching |

Direct HK homepage link when served locally: `index.html?lang=zh-HK&page=home`

## Word files (change log)

兩份繁體中文 `.docx` 檔位於 `word/`，供未能打開網頁樣本的持份者審閱：

| File | Contents |
|---|---|
| `word/MPNicare-HK-wording-change-log.docx` | 台灣原文 → 香港用語對照表（選單、首頁、關於MPN、教育專區、頁尾、地區標示）。文章正文標明不改。 |
| `word/MPNicare-HK-terms-privacy-rewrite.docx` | 現有台灣條款 vs 香港第486章私隱重寫稿（法律審閱草稿，非正式定稿）。 |
