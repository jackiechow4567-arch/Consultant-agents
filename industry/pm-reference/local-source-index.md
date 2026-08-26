# Local source file index (PM Space materials)

> **Location:** User's `Downloads/` folder on this machine. Files are **not** copied into git. Agents use **distilled** notes in `pm-reference/`; open originals locally when full text is needed.

## Already distilled into vault

| Local file | Vault reference |
|------------|-----------------|
| `HK-PI_Besremi-final.pdf` | `besremi-hk-pi-summary.md` |
| `2023-Gisslinger.pdf`, `2023-Barbui.pdf`, + paper list | `pv-clinical-evidence.md` |
| `21st-edition_HKAPI-Code-of-Practice.pdf`, ADR docs, Cap 486 | `regulatory-compliance.md` |
| `HADF-Drug-Formulary-Operation-Guidline-v21.4_250426.pdf`, `Executive-Digest-Issue-1-_-2026_28.pdf` | `ha-formulary-access.md` |
| `Hospital-Address-OfficialMapLocationLink.csv` | `hk-hospitals-landscape.md` |
| `Role-Whattheycareabout-HowIusuallyengage.csv` | `../role-pm.md` § Stakeholders |
| `20250613-Primary-Healthcare-Sharing-Session-2025_For-HKAPI-Members.pdf`, `20260429-COP-TTT-Workshop_slides-for-members.pdf` | `hkapi-policy-updates.md` |

## High sensitivity — local only (`work-briefs/pm/`)

| Local file | Why local-only |
|------------|----------------|
| `2025-HK-Ad-Board-Transcript-and-AI-Summary.docx` | KOL input, confidential discussion |
| `Hong-Kong-Advisory-Board-Polycythemia-Vera.docx` | Advisory board content |
| Draft formulary dossier (when created) | Unpublished HA submission |
| Internal pricing / PSP uptake reports | Commercial sensitivity |

## Clinical PDF library (reference locally; summaries in `pv-clinical-evidence.md`)

`2020-Gisslinger-Age-Group.pdf`, `2025-Pei.pdf`, `2025-Bose.pdf`, `2024-Chen.pdf`, `2023-Barbui-5y-survival.pdf`, `2023-Bang-PV-Pregnancy-Case.pdf`, `2022-Verstovsek.pdf`, `2022-Okikiolu.pdf`, `2018-Gisslinger-Peginvera-Extension.pdf`, `2022-Kiladjian.pdf`, `2022-Edahiro.pdf`, `2021-Chen-ASH-abstract-v2.pdf`, `2021-Barbui-appendix-Full-access.pdf`, `2021-Barbui-Full-access.pdf`, `2020-Huang.pdf`, `2020-Gisslinger-Full-access.pdf`, `2020-De-Oliveira.pdf`, `2015-Gisslinger-Blood.pdf`

## Regulatory / HA (full PDF locally)

`guidance_notes_registration-of-nda.pdf`, `ADR_Report_Form_en.pdf`, `PPB_Guidance_ADR_Industry_en.pdf`, `Cap-113-HA-Ordinance.pdf`, `Code-of-Professional-Conduct.pdf`, `Cap-486-Consolidated-version-for-the-Whole-Chapter-01-10-2022-English.pdf`

## Physician training source pieces (2026-08-25)

Attached approved-style artworks used to revise `physician-product-training.md` (not copied into git):

| Piece | Identifier | Content folded into training |
|-------|------------|------------------------------|
| Disease education board | PharmaEssentia MPN/PV infographic | MPN classification (PV/ET/PMF), JAK2 signaling, WHO 2016 PV criteria, age/thrombosis risk table, treatment goals |
| *Rediscovering Polycythemia Vera* | `PEC-BES-HK020126` · PharmaEssentia Asia (Hong Kong) Limited | NCCN low- and high-risk pathways, HU 1/5/10-year transformation and mortality, CHR definition and 5-year visual, EFS p=0.04 (5/95 vs 12/74) |

Numbers on those pieces were reconciled to HK PI + Gisslinger *Leukemia* 2023 in the training module (primary CHR 54.5% vs 34.9%; LOCF 72.6% vs 47.3% as graph explanation).

**Full physician brochure (EFFICACY / SAFETY / OTHER INFO tabs)** shared 2026-08-26: 5-year CHR graph, 84.3% ever-CHR, JAK2 8% vs 44%, EFS KM, 36-month all-causality AE table, PI page. Map vs training: [`physician-product-training-brochure-map.md`](physician-product-training-brochure-map.md).

## Publication library on `origin/main` (uploaded 2026-08-25)

Commit `09bf80c` added 19 PDFs to the repo root. Gap analysis vs current physician training: [`physician-product-training-gaps.md`](physician-product-training-gaps.md).

## Maintenance

When adding a new Space file:

1. Add row here  
2. Distill 5–15 bullets into the matching `pm-reference/*.md`  
3. If High sensitivity → `work-briefs/pm/README.md` only
