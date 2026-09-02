# Decision one-pager: MPNicare Hong Kong Chinese overlay

**Recommend: ship a chrome-only Hong Kong locale overlay (menu, titles, footer, terms, regional labels). Do not machine-translate article bodies, and do not keep the live `/zh-hk` Wix translation as the Hong Kong experience.**

Sensitivity: **Low** (public patient-education site; no patient, PSP, or unpublished commercial data).  
Role lens: Product Manager.  
Audience: local web / medical / legal; HQ brand if asked to confirm lexicon boundaries.

## Why

1. Hong Kong readers need accurate chrome (血液腫瘤, 紅血球, 知識產權, Cap. 486), not a second site redesign.
2. Column articles are written by non-Hong Kong teams. Relabelling them is safer and faster than rewriting clinical copy.
3. The live `/zh-hk` locale already fails: empty article rails, 紅細胞/並發症 regressions, and Taiwan PDPA clause numbers left in the privacy page.

## Options

| Criterion | A. Overlay + labels (recommended) | B. Keep live Wix `/zh-hk` machine translation | C. Fully rewrite every article into Hong Kong Chinese |
|---|---|---|---|
| Strategic fit | High — HK chrome, source science unchanged | Low — looks localised, is not | Medium — local voice, high claim risk |
| Resources | Low — string table + 3 label placements | Already built, but wrong | High — medical rewrite + lexicon review |
| Compliance / risk | Best — labels + PDPO rewrite for legal | High — wrong law, emptied content, new errors | High — UMAO/HKAPI if clinical claims are rewritten |
| Speed | Can implement on current Wix structure | Immediate but defective | Slow |

## Explicit non-goals

- Do not restyle the mint header, hero, three-column latest articles, or LINE footer.
- Do not translate 血腫專欄 / 健康照護 / 品味生活 article bodies, drug lists, or percentages.
- Do not put BESREMi / ET / MF promotional claims on this patient site.
- Do not treat the PDPO terms draft as final without Legal.

## Upward (5 sentences)

We should localise MPNicare for Hong Kong by overlaying chrome copy, not by rebuilding the site or translating every article. The live Wix Hong Kong language pack currently hides the three columns and introduces medical-character errors, so it should not remain the public HK experience. Regional articles stay in the original wording and carry a clear “其他地區內容” label on the category page, card, and article. Menu names move to 血液腫瘤專欄, 健康資訊, and 品味生活; education becomes 病人教育專區; footer and terms use Hong Kong legal Chinese, with privacy rewritten to the Personal Data (Privacy) Ordinance (Cap. 486). Legal must sign off the terms page before production; Medical should confirm the disclaimer line only.

## Downward (5 sentences)

Keep the current page grid. When language = 中文（香港）, swap the string table and turn on three labels. Do not edit article CMS fields. Do not replace Taiwan PDPA Arts. 3/10/11 with the same numbers under a Hong Kong statute name. Friendly links stay as they are; add Hong Kong organisations later as extra rows.

## Compliance caveat

This is a patient-education site, not a BESREMi promotional piece. No new product claims. Off-label ET/MF content in source articles remains reactive/educational source material and is labelled as non-Hong Kong. HA formulary impact: none direct; clearer HK chrome reduces mixed-market confusion. PSP: not in scope.

## Risks

1. Legal rejects a privacy page that still reads like Taiwan PDPA — mitigated by a Cap. 486 rewrite marked for review.
2. Readers assume labelled articles are Hong Kong treatment advice — mitigated by banner + card tag + article line, without changing clinical text.

## Next actions

| Action | Owner |
|---|---|
| Confirm overlay vs rebuild with web vendor (Wix multilingual strings, not new templates) | PM + web |
| Legal review of Cap. 486 terms draft | Legal / Compliance |
| Medical review of the three-line regional disclaimer only | Medical |
| Replace live `/zh-hk` machine translation with this string table | Web |
| Add Hong Kong organisation links later, no redesign | PM |

## Assumptions

- Source articles remain Taiwan/other-region authored.
- English leaflet form on the homepage stays as today.
- ~public site only; no PSP or formulary messaging on these pages.
