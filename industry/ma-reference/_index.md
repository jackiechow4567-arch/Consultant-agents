# BESREMi Medical Affairs library

> **For the Medical Affairs agent.** Answer from these cards. The PDFs sit in the repo root. Open a PDF only when a card does not contain the number the user asked for.
> **Built:** 2026-11-10 from the PDFs present in the vault at that date. Published papers are Low sensitivity.
> **Hong Kong label:** distilled in `industry/pm-reference/besremi-hk-pi-summary.md`. The full HK PI PDF is not in this vault.

## Load order

1. This index (pick the file)
2. [`response-rules.md`](response-rules.md) — always
3. One evidence file below
4. The distilled HK PI summary when the question touches indication, dose, or contraindications

## Which file

| Question is about | Read |
|--------------------|------|
| Efficacy vs hydroxyurea, event-free survival, CHR, JAK2 response in the phase 3 program, Low-PV vs phlebotomy, Japan phase 2, Taiwan compassionate use | [`evidence-ropeg.md`](evidence-ropeg.md) |
| How to phrase an answer, promo vs reactive, pregnancy, ET, MF, dosing science, case reports, protocols with no results | [`response-rules.md`](response-rules.md) plus the matching evidence section |
| Disease background, Hong Kong / Chinese MPN, allele-burden biology, Asia consensus, Pegasys (not BESREMi), early myelofibrosis slideshow | [`evidence-context.md`](evidence-context.md) |
| Paper-by-paper: what each PDF is allowed to support | [`library-catalog.md`](library-catalog.md) |

## Papers in this vault (19 PDFs)

Ropeginterferon primary or case evidence: `2023 Gisslinger.pdf`, `2022 Kiladjian.pdf`, `2023 Barbui.pdf`, `2023 Barbui 5y survival.pdf`, `2022 Edahiro.pdf`, `2021 Chen ASH abstract v2.pdf`, `2025 Pei.pdf`, `2023 Bang (PV Pregnancy Case).pdf`, `2022 Okikiolu.pdf`.

Ropeginterferon with **no efficacy results** in the file: `A phase II trial to assess the efficacy and safety of ropeginterferon α-2b in Chinese patients with polycythemia vera.pdf` (protocol), `2022 Verstovsek.pdf` (SURPASS-ET protocol).

Secondary or context only: `2025 Bose.pdf`, `2024 Chen.pdf`, `AMWG MPN consensus.pdf`, `American J Hematol - 1998 - Chim - Polycythemia vera in Chinese patients.pdf`, `1-s2.0-S0006497119857890-main.pdf`, `Clinicopathologic features and prognostic indicators in Chinese patients with myelofibrosis.pdf`, `Myeloproliferative neoplasms treated with hydroxyurea, pegylated interferon alpha-2A or ruxolitinib….pdf`, `20230508162013_1_slideshow.pdf`.

The 2020 Lancet Haematology PROUD-PV primary paper is **not** in this vault. Do not reconstruct its 12-month primary analysis from memory. The distilled PI summary records one 12-month figure; label it as PI summary, not as a paper you have read here.

## Maintenance

When a new PDF is added to the repo root:

1. Add a row to `library-catalog.md`
2. Add a card only for results you verified in that PDF
3. Leave the older cards unchanged unless the new paper is a later cut of the same trial — then say so
