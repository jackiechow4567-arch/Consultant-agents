# Gem 06 — Medical Affairs Knowledge Pack

> Generated 2026-11-10 06:53 for Gemini Gem Knowledge upload.
> Rebuilt: 2026-11-10 06:53 · Run `python build.py` after vault or gm-reference updates.
> Paste the matching system instruction from `gem-system-prompts.md`.

BESREMi scientific response. Cite only these cards and the distilled HK PI summary. If a fact is absent, say it is not in the current paper library. Do not prescribe for a named patient.

---

## Source: MA index

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


---

## Source: Response rules

# How to answer a BESREMi medical question

## Hong Kong label boundary

From `industry/pm-reference/besremi-hk-pi-summary.md` (distilled HK PI; full PI PDF not in the vault):

- **Indication:** monotherapy in adults for polycythaemia vera **without symptomatic splenomegaly**.
- **Not a proactive topic in HK:** essential thrombocythemia, myelofibrosis, and any other non-PV use. Those stay reactive scientific exchange, logged through MedInfo, citing the local PI.
- **Potency:** the PI says the potency of this product should not be compared with another pegylated or non-pegylated protein of the same therapeutic class. No interferon-versus-interferon superiority claim.
- **Dosing in the distilled PI (not a patient order):** titration starts at 100 µg (50 µg if the person is already on other cytoreductive therapy), increases by 50 µg every 2 weeks, maximum 500 µg every 2 weeks. Hematologic targets used in the PI: hematocrit <45%, platelets <400×10⁹/L, leukocytes <10×10⁹/L. After at least 1.5 years at a stable dose every 2 weeks, the interval may be extended to every 4 weeks.
- **Contraindications named in the distilled summary:** decompensated cirrhosis (Child-Pugh B or C); end-stage renal disease (GFR <15); severe psychiatric history; severe uncontrolled cardiovascular disease; autoimmune disease; transplant immunosuppression; combination with telbivudine; hypersensitivity.
- **Excipients named:** benzyl alcohol 10 mg/mL; polysorbate 80 0.05 mg/mL.
- The summary notes a mean titration of about 3.7 months for ropeginterferon versus about 2.6 months for hydroxycarbamide, and that hydroxycarbamide may be preferred when an early count reduction is needed to prevent thrombosis or bleeding. Report that as PI nuance, not as a reason to avoid the product.

If the user needs the exact PI sentence, say the full HK PI PDF is not in the library.

## What may be said proactively in HK

Only when the sentence names the comparator and the endpoint as studied:

| Comparator | Source in this library | May be used in proactive scientific materials if lexicon and PI allow |
|------------|------------------------|------------------------------------------------------------------------|
| Hydroxyurea / best available therapy in the PROUD-PV program | Kiladjian 2022 (5 years); Gisslinger 2023 (6 years, same program) | Yes, with the endpoint and the time point |
| Phlebotomy alone in low-risk PV | Barbui, NEJM Evidence 2023, and the 5-year drug-survival paper | Yes, and state that the study dose was fixed 100 µg every 2 weeks on top of phlebotomy and aspirin |
| Pegasys, other interferon, China-sourced ropeginterferon, anagrelide | No head-to-head results in this library | No superiority claim |
| Ruxolitinib | Not a BESREMi comparison in this library | No |

## Evidence rank

Use the highest rank that actually answers the question. Say the rank in the evidence table.

1. Randomized trial result in a paper that is in the vault
2. Single-arm trial
3. Prospective cohort that is not BESREMi (label the drug)
4. Consensus statement
5. Case series
6. Single case
7. Trial protocol or conference review — design or context only, no efficacy number unless that review quotes a primary paper you also have

## Patient-specific questions

If the user describes a real person (age, counts, pregnancy, prior drugs) and asks what to prescribe:

- Answer the **class of evidence** that matches the situation (for example low-risk PV, or pregnancy).
- State the labeled dosing framework from the distilled PI.
- Do **not** choose a starting dose, a target dose, or a hold/restart rule for that person.
- Close with: the treating physician decides, using the current local label and the patient’s own monitoring.
- If the message contains a name, record number, or other identifier, treat it as High sensitivity. Do not repeat the identifier.

## Pregnancy

The library does not contain an HK PI pregnancy section. Do not invent a pregnancy category, a contraindication, or a “safe in pregnancy” claim.

What is present:

- One case report (Bang 2023): a woman with JAK2-positive PV, pregnant at 40, treated with ropeginterferon alfa-2b for more than 6 months and delivered without neonatal or maternal complications described in the abstract. The case used a 250 µg start because counts were rising quickly, then 350 µg and 500 µg, with a temporary hold for raised AST/ALT, then dosing every 3 weeks and later every 4 weeks. Eight cycles during the pregnancy. This is one case, and the start dose was not the 100 µg labeled start.
- A 2025 conference review (Bose) says limited real-world cases were reported as safe, similar to pegylated interferon alfa-2a, and points to pharmacokinetics “in preparation.” Those pharmacokinetic results are **not** in this vault.
- Okikiolu 2023 mentions pregnancy among five real-world cases after prior Pegasys. It is a case series, not a pregnancy safety study.

Posture: reactive only, needs Medical review, not proactive material.

## Essential thrombocythemia and myelofibrosis

- SURPASS-ET (`2022 Verstovsek.pdf`) is a phase III **protocol** (NCT04285086) of ropeginterferon alfa-2b versus anagrelide as second-line therapy in high-risk ET after hydroxyurea resistance or intolerance. This PDF has no results.
- Chen ASH 2021 and Okikiolu 2023 and Pei include some ET or MF patients. Small, uncontrolled. Not an ET or MF indication claim.
- Asia consensus (Gill et al.) says that in PV, ET, and early/prefibrotic disease, recombinant interferon-α (pegylated interferon alfa-2a **or** ropeginterferon alfa-2b) should be considered when cytoreduction is needed and hydroxyurea is not suitable. That is a consensus recommendation, not a head-to-head trial, and it is not the HK label.

## Dosing science versus a prescription

You may explain regimens **as used in a named study**:

| Regimen | Where it appears | How to describe it |
|---------|------------------|--------------------|
| Start 50–100 µg, add 50 µg every 2 weeks, max 500 µg every 2 weeks; 50 µg if already on cytoreduction | PROUD-PV description inside Gisslinger 2023; Edahiro 2022; distilled HK PI | Labeled-style titration. Still not an order for a named patient |
| Fixed 100 µg every 2 weeks, with phlebotomy and aspirin | Low-PV | Study regimen in low-risk PV. Do not silently substitute it for the HK titration schedule |
| 250 µg, then 350 µg at week 2, then 500 µg at week 4 | Chinese phase II **protocol** (Jin 2023); described as HIDAT in Pei and in the Bose review | Investigational or real-world accelerated titration. No efficacy result from the Chinese protocol is in the vault. Pei is seven cases |
| Start 250 µg, then +100 µg every 2 weeks to 500 µg | Chen ASH 2021 compassionate-use abstract | Uncontrolled series, n=20, mixed MPN |

## Safety language

- Report adverse events with the denominator and grade rule the paper used.
- “No new safety concerns” in a 29-patient single-arm study means that study did not find a new signal. It does not mean the drug has no serious risks.
- Class effects that the phase 3 papers list (cytopenias, liver-enzyme elevation, fatigue, arthralgia, headache, flu-like symptoms, and, in the Japan study, alopecia) belong in the answer when the question is about tolerability.
- Psychiatric disease, autoimmune disease, and decompensated liver disease are contraindication themes in the distilled PI. Do not soften them.

## Numbers you must not invent

The older PM summary (`pv-clinical-evidence.md`) is a claim-boundary note for commercial work. If a figure there is not also in `evidence-ropeg.md` or the distilled PI summary, do not use it in a medical answer. Medical Affairs uses this folder as the source of truth.


---

## Source: Ropeginterferon evidence

# Ropeginterferon evidence cards

Numbers below were taken from the PDFs in the repo root. CHR = complete hematologic response. ELN = European LeukemiaNet. BAT = best available therapy. HU = hydroxyurea.

Same-trial rule: Kiladjian 2022 and Gisslinger 2023 report different time cuts of PROUD-PV / CONTINUATION-PV. Barbui NEJM Evidence 2023 and Barbui Annals of Hematology (5-year) report Low-PV and its follow-up.

---

## 1. PROUD-PV / CONTINUATION-PV — 6-year event-free survival

**Source:** Gisslinger et al., Leukemia. 2023;37:2129–2132. File: `2023 Gisslinger.pdf`. DOI: 10.1038/s41375-023-02008-6.

**Design, as described in this letter:** PROUD-PV (NCT01949805) was a phase 3, randomized, open-label trial at 48 European centers. Adults with PV (WHO 2008) who needed cytoreduction, hydroxyurea-naive or pretreated for under 3 years, were randomized 1:1 to ropeginterferon alfa-2b or hydroxyurea. Stratification: age, thrombotic history, hydroxyurea pretreatment. Ropeg dose escalated from 50–100 µg to a maximum of 500 µg every 2 weeks until counts normalized. Hydroxyurea from 500 mg to 3000 mg daily. After 1 year, patients could enter CONTINUATION-PV (NCT02218047) for 5 further years. Control-arm patients could switch to any standard cytoreductive therapy (BAT). Ropeg patients could extend the interval to every 3 or 4 weeks.

**Who is in the 6-year efficacy set:** 127 patients treated in each PROUD-PV arm; 95 (ropeg) and 74 (control) rolled into the extension. Efficacy over 6 years uses the CONTINUATION-PV full analysis set. Safety uses all treated patients. Maximum exposure 7.3 years. Cumulative exposure 568 patient-years (ropeg) and 451 patient-years (control). Study end for this report: 29 April 2021, when all patients had been treated for at least 6 years. In year 6, median cumulative 4-weekly ropeg dose was 499 µg (IQR 268–782 µg), given every 3 or 4 weeks in 61.9%. In the control arm, 87.8% were still on hydroxyurea at the 72-month assessment.

**Event-free survival:** time to first thromboembolic event, disease progression, or death. Median not reached. Probability of event-free survival **0.94 versus 0.82** (log-rank p = 0.04). Cox hazard ratio **0.34** (95% CI 0.12–0.97; p = 0.04). First risk events: **5/95 (5.3%)** ropeg (thromboembolic 2, myelofibrosis 1, death 2) versus **12/74 (16.2%)** hydroxyurea/BAT (thrombotic 5, myelofibrosis 2, acute leukemia 2, death 3).

**Molecular response at 6 years (ELN, last observation carried forward):** **62/94 (66.0%)** versus **14/72 (19.4%)**. Risk ratio 3.23 (2.01 to 5.19); p < 0.0001. Median JAK2V617F allele burden at month 72: **8.5% versus 50.4%** (p < 0.0001). Allele burden >50% in year 6: **11.6% versus 50.0%** (p < 0.0001).

**CHR at month 72** (modified ELN; discontinuations counted as non-responders): **48/88 (54.5%) versus 22/63 (34.9%)**. Risk ratio 1.55 (95% CI 1.07 to 2.26); p = 0.02. Last-observation-carried-forward sensitivity: **69/95 (72.6%) versus 35/74 (47.3%)**. Risk ratio 1.54 (1.18 to 2.00); p = 0.001. Mean proportion of time in CHR: **60.9% versus 41.2%** (p = 0.04). CHR definition used for the time-in-response figure: hematocrit <45% without phlebotomy for at least 3 months, platelets <400×10⁹/L, leukocytes <10×10⁹/L.

**Leukocytes at month 72:** mean absolute change from baseline −6.67×10⁹/L versus −3.59×10⁹/L (p < 0.0001). Mean proportion of time with a normal leukocyte count: 93.7% versus 80.9% (p = 0.02).

**Safety up to 7.3 years:** discontinuation for drug-related toxicity **14/127 (11.0%)** versus **3/127 (2.4%)**. The letter says the higher ropeg rate may reflect protocol-mandated withdrawal for interferon class effects under intensive monitoring. Grade ≥3 treatment-related adverse events over the whole period: **15.7% versus 16.5%**. PV-associated adverse events in year 6: 7.1% versus 12.1%. Events were mostly mild or moderate. Kiladjian 2022, the 5-year cut of the same program, reported drug-related discontinuation in 13/127 (10.2%) versus 4/127 (3.1%), and grade ≥3 treatment-related events in 21/127 (16.5%) in each arm. Quote the cut you are using. Do not average them.

**Limits the answer must keep:** open-label; extension is not the original randomized cohort in full (95 and 74 of 127); control arm could change therapy; overall survival was not evaluated; the 12-month primary PROUD-PV paper is not in this vault; rare events mean the event-free survival result rests on 5 versus 12 events.

---

## 2. Same program — 5-year hematologic and molecular outcomes

**Source:** Kiladjian et al., Leukemia. 2022. File: `2022 Kiladjian.pdf`. DOI: 10.1038/s41375-022-01528-x.

**Cut:** efficacy to month 60 in patients who entered CONTINUATION-PV. At 5 years, 53/95 (55.8%) ropeg and 33/75 (44.0%) control had CHR by modified ELN (risk ratio 1.30, 95% CI 0.95 to 1.77; **p = 0.0974**), with discontinuation counted as non-response. Last-observation-carried-forward CHR: **69/95 (72.6%) versus 40/76 (52.6%)** (risk ratio 1.43, 95% CI 1.12–1.81; p = 0.004).

**Molecular response at 5 years (ELN):** **65/94 (69.1%) versus 16/74 (21.6%)** (risk ratio 3.04, 95% CI 1.96–4.71; p < 0.0001). Median JAK2V617F allele burden on ropeg fell from **37.3% at baseline to 8.5% at 60 months**. Control fell from 38.1% to 18.2% at 12 months and rebounded to **44.4%** at 60 months (p < 0.0001 between arms). Allele burden <10% at month 60: **50/92 (54.3%)** on ropeg. Allele burden <1%: **18/92 (19.6%)** versus **1 patient (1.4%)** on control (p = 0.0002).

**Clinical events over 499 and 401 patient-years:** disease progression **0.2 per 100 patient-years** on ropeg (1 myelofibrosis) versus **1.0 per 100 patient-years** on control (2 myelofibrosis, 2 acute leukemia). Major thromboembolic events: 5 events in 4 patients versus 5 events in 5 patients (**1.0 versus 1.2 per 100 patient-years**). All affected patients were aged 60 or older. The letter says thromboembolic events did not appear to correlate with higher hematocrit or greater phlebotomy need.

**Safety over the whole treatment period:** most common adverse events in >10% on ropeg, regardless of cause: thrombocytopenia, anemia, leukopenia, elevated hepatic enzymes, arthralgia, fatigue, headache, dizziness, splenomegaly, pyrexia, back pain. Control: thrombocytopenia, anemia, leukopenia, fatigue, headache, nausea, diarrhea, influenza, nasopharyngitis. Mostly grade 1–2. Grade ≥3 treatment-related events: **21/127 (16.5%) in each arm**, including one grade 4 (increased GGT on ropeg) and one grade 5 (fatal acute leukemia on control). Discontinuation for drug-related adverse events: **13/127 (10.2%) versus 4/127 (3.1%)**, about half of those in the first year.

**Author hypothesis, not a stopping rule:** applying allele burden <10%, CHR sustained for at least 2 years, and no progression, thrombosis, or worsening, **30.4% versus 4.2%** (p < 0.0001) “might be considered” for treatment discontinuation. The letter says prerequisites for stopping remain a subject of research. Do not recommend stopping therapy from this sentence.

**How this sits next to the 6-year letter:** the month-60 CHR difference was not statistically significant in the primary (dropout = non-response) analysis. The month-72 analysis in Gisslinger 2023 was significant on that same rule. Say which time point you are quoting.

---

## 3. Low-risk PV versus phlebotomy — Low-PV, 12 and 24 months

**Source:** Barbui et al., NEJM Evidence. 2023;2(6). File: `2023 Barbui.pdf`. DOI: 10.1056/EVIDoa2200335. Published 15 May 2023.

**Design:** phase 2, open-label, randomized. Low-risk PV (the paper’s introduction: age 60 or under, no prior thrombosis; guidelines would usually recommend phlebotomy and low-dose aspirin only). Ropeg **100 µg every 2 weeks on top of phlebotomy and low-dose aspirin**, versus phlebotomy and low-dose aspirin. The PDF text layer prints the dose unit poorly in the abstract (“100 mg”); the 5-year paper and the methods context confirm **100 µg**. Primary endpoint: maintain median hematocrit ≤45% over 12 months without progressive disease. Crossover allowed if the primary endpoint was not met. Funded by AOP Health.

**Enrollment:** 127 patients (ropeg 64, standard 63). About 70% had disease duration under 3 years. Leukocytosis in 53%, thrombocytosis in 83%, palpable splenomegaly under 5 cm in 31%.

**Primary endpoint at 12 months:** **52/64 (81%) versus 32/63 (51%)**, p < 0.001. Odds ratio **4.20** (95% CI 1.77 to 10.23). The PDF text layer prints the p-value as “P,0.001”; that is read as P < 0.001. Hematocrit ≤45% component: **52/64 (81%) versus 37/63 (59%)**, odds ratio 3.05 (95% CI 1.28 to 7.50). Protocol-defined disease progression occurred only in the phlebotomy group: **8/63 (13%)** — six with progressive thrombocytosis and microvascular symptoms, plus one cerebral TIA and one splenic-vein thrombosis. Mean phlebotomies per patient per year: **2.91 versus 4.17** (mean difference 1.27; 95% CI 0.27 to 2.26).

**To month 24:** responders who stayed on assigned treatment maintained response in **83% versus 59%** (p = 0.02). The PDF text layer prints this as “P 50.02”; that is read as P = 0.02. Among ropeg responders, moderate or severe symptoms **33% versus 67%**, palpable splenomegaly **14% versus 37%**, with normalization of ferritin and blood counts described in the abstract. Non-responders crossed over (9 from ropeg to standard; 23 from standard to ropeg). Of those switched to ropeg, **7 of 23** met response criteria in 12 months, and phlebotomy need was **4.7 per patient per year**. Discontinuation for adverse events: **seven patients** treated with ropeg. Abstract: no dose-limiting toxicities noted; **9.2% developed neutropenia**.

**Limits:** open-label phase 2; fixed 100 µg, not the labeled titration to 500 µg; low-risk population; “superior to phlebotomy alone” applies to hematocrit maintenance on this endpoint, not to a survival claim.

---

## 4. Low-PV — drug survival up to 5 years

**Source:** Barbui et al., Annals of Hematology. File: `2023 Barbui 5y survival.pdf`. DOI: 10.1007/s00277-023-05577-9. Received 13 November 2023.

**What it adds:** drug survival as a stand-in for efficacy, safety, adherence, and tolerability after the Low-PV core study. During the first 2 years, ropeg and phlebotomy-only were discontinued in **33% and 70%**. Reasons included lack of response (12 versus 34), adverse events (6 versus 0), and withdrawal of consent (3 versus 10). Thirty-six ropeg responders continued, and the probability of drug survival after a median of 3.15 years was **59%**. Among patients still on drug, the primary composite endpoint was maintained in **97%, 94%, and 94%** at 3, 4, and 5 years. **60%** of those cases were phlebotomy-free. **23 of 63 (37%)** phlebotomy-only patients failed the primary endpoint and crossed to ropeg; needing more than three phlebotomies in the first 6 months was the strongest factor named.

**Author suggestion, not a label change:** the paper suggests increasing the dose and using ropeg earlier when phlebotomy need is high in the first 6 months. Report that as the authors’ conclusion. The studied dose in the core trial remained 100 µg every 2 weeks.

The paper also states that ropeginterferon alfa-2b is approved for adults with PV in the United States, and in Europe for PV without splenomegaly. That is a regulatory statement in the article, not the Hong Kong label. Hong Kong remains the distilled PI: monotherapy in adults for PV without symptomatic splenomegaly.

---

## 5. Japanese phase 2 — single arm

**Source:** Edahiro et al., International Journal of Hematology. 2022;116:215–227. File: `2022 Edahiro.pdf`. DOI: 10.1007/s12185-022-03341-9. NCT04182100.

**Design:** phase 2, open-label, multicenter, single-arm, 29 Japanese patients with PV, including younger patients and patients at low thrombotic risk. Subcutaneous ropeg every 2 weeks, start **100 µg** ( **50 µg** if switching from prior therapy), increase to a maximum of **500 µg**. **14/29 (48.3%)** reached 500 µg.

**Primary outcome:** durable complete hematologic response without phlebotomy at **both** month 9 and month 12: **8/29 (27.6%)**. Fastest CHR observed at week 12. Mean change in JAK2V617F allele burden from baseline to 52 weeks: **−19.2% ± 22.6% (SD)**.

**Safety:** no new safety concerns versus prior European ropeg studies, in the authors’ words. Most common treatment-related adverse events: **alopecia 55.2%, fatigue 27.6%, influenza-like illness 27.6%**. Most treatment-related events were mild or moderate; **none were grade ≥3**. All 29 patients had at least one treatment-related adverse event.

**Limits:** single arm, n=29, no control group. The 27.6% figure is a strict durable endpoint (months 9 and 12), not a 12-month single-time-point CHR. Do not set it next to the European 54.5% at 6 years as if they measured the same thing.

---

## 6. Taiwan compassionate use — abstract only

**Source:** Chen et al., Blood. 2021;138(Supplement 1):4631–4632. File: `2021 Chen ASH abstract v2.pdf`. DOI: 10.1182/blood-2021-147746.

**Design:** compassionate-use series before Taiwan approval, for MPN resistant or intolerant to hydroxyurea and/or anagrelide. Excluded autoimmune disease, psychiatric illness, and acute or chronic infection. Accelerated dosing: start **250 µg**, increase by **100 µg every 2 weeks** to **500 µg** if tolerated. Hematologic remission: for ET, platelets ≤400×10⁹/L and leukocytes <9.5×10⁹/L; for PV, platelets ≤400×10⁹/L, leukocytes <10×10⁹/L, and hematocrit <45% with no phlebotomy in the past 3 months. Molecular response: JAK2V617F reduced by at least 50% if baseline was under 50%, or by at least 25% if baseline was at least 50%.

**Results:** **n=20** (14 PV, 4 ET, 1 post-ET myelofibrosis, 1 prefibrotic primary myelofibrosis). 12 women, 8 men, median age 56.1 years. JAK2V617F in 18; prior thrombosis in 5. Hematologic remission in **13 of 18** ET and PV patients. The abstract says ET remission looked faster than PV (19.3 versus 33.2 weeks). Of 18 JAK2-positive patients, molecular response in **7 PV and 1 post-ET MF**, median 46 weeks. Allele-burden reduction in 12 patients. One MF patient stopped for progression. One PV patient stopped for AML transformation, later returned to a PV state and resumed ropeg. Most treatment-related events mild to moderate; no discontinuation for unbearable side effects. The abstract’s own off-label disclosure: the series includes MPN beyond the PV indication.

**Limits:** abstract, no control arm, mixed diagnoses, n=20. Not proactive HK material.

---

## 7. Younger patients, high-initial-dose titration — seven cases

**Source:** Pei et al. File: `2025 Pei.pdf`. Header: Hemato 2026, 7, x (article PDF; page numbers not finalized in the file).

**Design:** retrospective consecutive case series, seven hospitals. Seven patients, all under 60. Median age at diagnosis 43 years; median age at ropeg start 45 years. Four women, three men. Regimen described as high-initial-dose accelerated titration: start **250 µg**, maintenance **500 µg**. Reasons for choosing ropeg differed (declined hydroxyurea, young age, or hydroxyurea resistance in one case).

**What the results section supports:** the authors describe hematologic responses and a reduction in JAK2V617F variant allele frequency. All but one patient with PV stopped phlebotomy after ropeg; the remaining patient had one phlebotomy at week 18. No autoimmune disorder was observed in the series. Mild transaminase elevation in two cases. Ferritin improved in the three cases where it was followed. Case 1 is described in detail: JAK2V617F variant allele frequency fell from 99.4% to 11.7% over 3 years (the case heading calls this an 88% reduction), with the dose later extended to every 8 weeks. That interval extension is this patient’s course, not a labeled schedule.

**Limits:** n=7, no control group, mixed reasons for treatment, not a response-rate trial. Do not quote a cohort CHR percentage; the PDF abstract does not give one. Do not present HIDAT as the Hong Kong labeled titration.

---

## 8. Protocols with no results

**Chinese phase II protocol.** Jin et al., Future Oncology. 2023;19(11):753–761. DOI: 10.2217/fon-2022-1141. File name begins `A phase II trial to assess the efficacy and safety of ropeginterferon`. Single-arm multicenter plan in Chinese patients with PV: start **250 µg**, **350 µg at week 2**, **500 µg at week 4**, adjusted for tolerability. Planned about 49 patients at 12–15 hospitals, to support a China license application. This PDF is the trial design. **No efficacy or safety results.**

**SURPASS-ET protocol.** Verstovsek et al. File: `2022 Verstovsek.pdf`. Phase III, open-label, randomized, **NCT04285086**. Ropeginterferon alfa-2b versus anagrelide as second-line therapy in high-risk essential thrombocythemia after hydroxyurea resistance or intolerance. Outcomes planned: safety, efficacy, tolerability, pharmacokinetics. **No results in this PDF.** ET is outside the HK PV indication.

---

## 9. Real-world switch from Pegasys — five cases

**Source:** Okikiolu et al., Leukemia Research Reports. 2023;19:100360. File: `2022 Okikiolu.pdf`. DOI: 10.1016/j.lrr.2022.100360.

**What it is:** five patients at one UK center treated with ropeginterferon alfa-2b after prior peginterferon alfa-2a, doses variable, diagnoses ET or PV, including a pregnancy mention. The abstract says the series shows safety and tolerability and “corroborates reports of efficacy” in PV and use in pregnancy.

**How to use it:** anecdotal switch experience. Case 1 (JAK2 ET with prior Budd-Chiari) did not control platelets on ropeg 250 µg every 2 weeks and moved to anagrelide. Do not claim that BESREMi is better than, worse than, or equivalent to Pegasys. Do not use the series as pregnancy proof.

---

## 10. One pregnancy case

**Source:** Bang and Lee, Hematology Reports. 2023;15:172–179. File: `2023 Bang (PV Pregnancy Case).pdf`. DOI: 10.3390/hematolrep15010018.

**Case:** JAK2V617F-positive low-risk PV (allele frequency 63.96% at diagnosis), diagnosed 2017, pregnant at age 40 (5 weeks on 9 December 2021). Hydroxyurea and anagrelide were stopped; low-dose aspirin continued. Ropeg was delayed about 6 weeks because it was not readily available in South Korea. Start **250 µg** on 8 February 2022 (chosen because counts were rising; the authors note the usual recommended start is 100 µg with 50 µg steps). Then 350 µg, then 500 µg. AST 59 U/L and ALT 80 U/L led to a temporary hold; treatment resumed, then every 3 weeks and later every 4 weeks at 500 µg. **Eight cycles during pregnancy.** Abstract: treated for more than 6 months and **delivered without neonatal or maternal complications** as described by the authors.

**Limits:** one case. Not a pregnancy indication. Not proactive material. See `response-rules.md`.


---

## Source: Disease and regional context

# Context papers — not BESREMi efficacy

Use these when the question is about disease background, Hong Kong or Chinese MPN, why allele burden matters, or what a consensus says. Do not move their response rates onto BESREMi.

---

## Allele burden and clinical correlates (not a drug trial)

**Source:** Chen et al., Annals of Hematology. File: `2024 Chen.pdf`. DOI: 10.1007/s00277-024-05754-4.

Systematic review and meta-analysis of JAK2V617F allele burden in PV. 1,851 records screened; 39 studies informed the association; 21 entered meta-analyses; about 5,462 patients. Higher allele burden was associated with higher leukocyte count and hematocrit, and with lower platelet count. Higher allele burden carried higher odds of pruritus, splenomegaly, thrombosis, myelofibrosis, and acute myeloid leukemia.

**Use:** explains why molecular response is discussed as a disease-relevant endpoint in the ropeg trials. **Do not** treat this paper as evidence that ropeginterferon prevents those events. Event reduction has to come from the trial cards in `evidence-ropeg.md`.

---

## MPN Asia 2025 conference review

**Source:** Bose et al., Current Hematologic Malignancy Reports. 2025;20:9. File: `2025 Bose.pdf`. DOI: 10.1007/s11899-025-00752-3.

A review of meeting presentations. It describes ropeginterferon alfa-2b as a long-acting monopegylated interferon with durable PV efficacy across European, Chinese, Korean, Japanese, US, and Taiwan presentations, and it describes the 250–350–500 µg every-2-weeks HIDAT approach as associated with faster CHR, faster JAK2V617F decline, and a higher complete molecular remission rate than conventional titration, **citing other papers**. Those primary HIDAT trials are not all in this vault. The Chinese phase II PDF in this vault is a protocol without results. Pei is seven cases.

Pregnancy paragraph: limited real-world cases reported as safe, similar to pegylated interferon alfa-2a; pharmacokinetics described as minimal placental transfer and undetectable in breast milk, from a manuscript “in preparation.” **That pharmacokinetic paper is not in this vault.** Do not quote the pharmacokinetic claim as data you hold.

Also a meeting summary of myelofibrosis risk scores (MIPSS70+ v2.0, MYSEC-PM, GIPSS) and of ruxolitinib combinations. Those are not BESREMi results.

---

## Asian Myeloid Working Group consensus

**Source:** Gill et al., Clinical and Experimental Medicine. File: `AMWG MPN consensus.pdf`. DOI: 10.1007/s10238-023-01189-9. Literature search to 31 January 2023.

Consensus on classical Philadelphia-negative MPN in Asia (PV, ET, PMF). Driver mutations as stated: JAK2V617F in >95% of PV; CALR and MPL in a minority of ET and MF.

Treatment statement relevant to interferon: management should be patient-specific. In PV, ET, and early/prefibrotic myelofibrosis, when cytoreduction is indicated and the patient has resistance or intolerance to hydroxyurea, **recombinant interferon-α (pegylated interferon alfa-2a or ropeginterferon alfa-2b) should be considered**. This names both products. It is not a comparative trial.

Epidemiology notes in the paper: in Asian series, ET is often more common than PV, unlike many Western series; ET shows a female predominance. Five-year overall survival figures quoted from regional series (for example 97.7% PV, 92.2% ET, 53.1% MF in one cited cohort; Thailand 5-year OS 91.7% for PV) are **citations inside the consensus**, not a Hong Kong BESREMi cohort. Use them only as background, and name them as consensus citations.

---

## Hong Kong and Chinese disease background

These papers do not study BESREMi.

**Chim et al., American Journal of Hematology. 1997;56:59–62.** File name includes “1998”. Queen Mary Hospital. 41 patients meeting PVSG criteria, 1960–1996. 23 men, 18 women. Median follow-up 66.5 months. Median age 62 (37–85). Median hemoglobin 18.8 g/dL. Treatment era: venesection, hydroxyurea, radioactive phosphorus. Thrombotic events in **14/41 (34%)**, 19 events (16 arterial, 3 venous). Thrombosis-free survival 83% at 10 years and 73% at 20 years. Overall survival **83% at 10 years, 62% at 20 years**. One post-polycythemic myeloid metaplasia. One secondary AML among 17 patients exposed to radioactive phosphorus; no secondary malignancy in 20 hydroxyurea-treated patients (median 63.5 months on hydroxyurea). Authors’ conclusion at the time: PV in Chinese patients looked relatively benign versus Caucasian series they cited. Historical diagnostic criteria (PVSG), pre-JAK2 era. Do not use the thrombosis rate as the current Hong Kong BESREMi population.

**Leung et al., Blood. 2017;130(Supplement 1):5273.** File: `1-s2.0-S0006497119857890-main.pdf`. Single Hong Kong tertiary center, diagnoses 2012–2016, retrospective. **285** patients (142 men, 143 women): PV 22%, ET 60%, PMF 10%, MPN-unclassifiable 8%. Among 230 with molecular annotation, JAK2V617F in **70% (162/230)**; among 28 JAK2-negative, CALR in 14 and JAK2 exon 12 in 1; 13 triple-negative. Treatment exposure in the cohort: aspirin 92% (263), hydroxyurea 92% (261), pegylated interferon 10.5% (30), ruxolitinib 6.3% (18). Cardiovascular events in **45/285 (16%)**. Age >50 years (p=0.002) and hypertension (p=0.038) associated with cardiovascular events. Progression to myelofibrosis in 17% of PV (median follow-up 14.7 years) and 12% of ET. Leukemic transformation in 9 patients (3%). Age >60 and splenomegaly associated with inferior progression-free survival in PV/ET; on multivariate analysis splenomegaly remained the significant factor they highlight. Abstract only in this file. The pegylated interferon here is not identified as ropeginterferon.

**Gill et al., Hematology. 2016;21(1):10–18.** File begins `Clinicopathologic features…myelofibrosis`. Chinese myelofibrosis cohort from seven hospitals: primary MF plus post-PV MF (n=27) and post-ET MF (n=36). Median overall survival **66 months** for primary MF and **44 months** for 63 patients with secondary MF. Age >65, platelets <100×10⁹/L, and leukemic transformation associated with worse survival in the multivariate analysis described. 10-year cumulative leukemic transformation about 28% (primary) and 31% (secondary). Eighteen allografts; median overall survival after transplant 19 months. Authors: clinicopathologic features and outcomes similar to Western patients. Not a ropeg study. Useful only if the question is the outlook of myelofibrosis after PV in Chinese series.

**Gill et al., Hematology (real-world treatment).** File begins `Myeloproliferative neoplasms treated with hydroxyurea…`. Prospective real-world study of hydroxyurea ± anagrelide, **pegylated interferon alfa-2a**, or ruxolitinib. 125 patients (70 men, 55 women): PV 23, ET 56, MF 46. Median follow-up 36 months (19–42). In **PV, responses were comparable across modalities**. In ET, pegylated interferon alfa-2a had superior clinicohematologic complete response (p=0.045). In MF, higher overall response with ruxolitinib (p=0.018). Ruxolitinib reduced spleen size within 6 months and improved MPN-SAF total symptom score (p<0.001). Grade 1–2 adverse events in 44%, 62%, and 20% for conventional therapy, pegylated interferon alfa-2a, and ruxolitinib; grade 3–4 in 7% (pegylated interferon) and 9% (ruxolitinib). **This interferon is alfa-2a, not ropeginterferon alfa-2b.** Do not transfer the ET p-value or the adverse-event rates to BESREMi. It is fair to say a Hong Kong group has published real-world pegylated interferon alfa-2a experience, and that this paper did not find a PV response difference between the modalities it studied.

---

## Early myelofibrosis slideshow — do not use for BESREMi

**File:** `20230508162013_1_slideshow.pdf`. Key Opinions in Medicine, volume 7, issue 4, July 2022. Commissioned and sponsored by Novartis Singapore. Topic: management of early myelofibrosis, with ruxolitinib as the main treatment discussed and a short interferon section. Not a BESREMi trial and not an independent source for ropeginterferon claims.


---

## Source: Paper catalog

# Paper catalog — what each PDF may support

| File | Citation (short) | Kind | May support | Do not support |
|------|------------------|------|-------------|----------------|
| `2023 Gisslinger.pdf` | Gisslinger 2023, Leukemia 37:2129 | 6-year letter, same phase 3 program | Event-free survival, month-72 CHR and molecular response, long-term safety counts | A separate trial from Kiladjian 2022; an overall-survival claim |
| `2022 Kiladjian.pdf` | Kiladjian 2022, Leukemia | 5-year letter, same program | Month-60 CHR (including the non-significant primary p-value), molecular response, allele-burden drop, event rates per 100 patient-years | A rule to stop treatment; independence from the 6-year letter |
| `2023 Barbui.pdf` | Barbui 2023, NEJM Evidence | Phase 2 randomized, low-risk PV | Hematocrit control vs phlebotomy, phlebotomy counts, 24-month maintenance, symptom and spleen figures in responders | Survival benefit; the HK titration schedule (this study used fixed 100 µg) |
| `2023 Barbui 5y survival.pdf` | Barbui, Ann Hematol, DOI 10.1007/s00277-023-05577-9 | Follow-up of Low-PV | Drug survival, discontinuation reasons, response while still on drug, phlebotomy-need signal | A labeled dose increase |
| `2022 Edahiro.pdf` | Edahiro 2022, Int J Hematol 116:215 | Japan phase 2, single arm, n=29 | Durable CHR 8/29, allele-burden change, alopecia/fatigue/flu-like rates, no grade ≥3 treatment-related events in that study | Comparison with hydroxyurea |
| `2021 Chen ASH abstract v2.pdf` | Chen, Blood 2021 abstract | Compassionate use, n=20, mixed MPN | Remission and molecular response counts in HU/anagrelide-resistant or intolerant patients; accelerated 250 µg start | Proactive HK promotion; a controlled ET or MF claim |
| `2025 Pei.pdf` | Pei et al., Hemato article PDF | 7-case series, age under 60 | Feasibility notes for 250 µg start / 500 µg maintenance in this series; one detailed allele-burden course | A response rate; labeled dosing |
| `2023 Bang (PV Pregnancy Case).pdf` | Bang 2023, Hematol Rep 15:172 | One pregnancy | What happened in this case, including 250 µg start and a liver-enzyme hold | “Safe in pregnancy” |
| `2022 Okikiolu.pdf` | Okikiolu 2023, Leuk Res Rep 19:100360 | 5 cases after Pegasys | Switch experience is variable, including one platelet failure | Any superiority or equivalence versus Pegasys |
| `A phase II trial…Chinese patients….pdf` | Jin 2023, Future Oncol 19:753 | Phase II **protocol** | The planned 250 / 350 / 500 µg schema and the China development intent | Efficacy or safety results |
| `2022 Verstovsek.pdf` | Verstovsek et al. | SURPASS-ET **protocol**, NCT04285086 | That a phase 3 vs anagrelide in second-line high-risk ET was designed | ET efficacy; any result |
| `2024 Chen.pdf` | Chen, Ann Hematol, DOI 10.1007/s00277-024-05754-4 | Meta-analysis of JAK2 allele burden | Association of higher allele burden with counts, symptoms, thrombosis, progression | Drug effect of ropeg |
| `2025 Bose.pdf` | Bose 2025, Curr Hematol Malig Rep 20:9 | Conference review | Themes from MPN Asia 2025, clearly labeled as review | Primary endpoints not also in a paper in this vault; unpublished pharmacokinetics |
| `AMWG MPN consensus.pdf` | Gill et al., Clin Exp Med | Asia consensus | When interferon (pegylated alfa-2a **or** ropeg) is considered after hydroxyurea is unsuitable | Head-to-head superiority; HK label text |
| `American J Hematol - 1998 - Chim….pdf` | Chim 1997, Am J Hematol 56:59 | Historical QMH PV cohort, n=41 | Pre-JAK2 natural history under older therapy | Current treatment effect |
| `1-s2.0-S0006497119857890-main.pdf` | Leung, Blood 2017 abstract | HK MPN cohort, n=285 | Local mix (ET more common than PV), JAK2 rate, cardiovascular and progression associations | BESREMi efficacy. Pegylated interferon exposure is not identified as ropeg |
| `Clinicopathologic features…myelofibrosis.pdf` | Gill 2016, Hematology 21:10 | Chinese MF cohort | Survival and leukemia risk of MF, including post-PV MF | A ropeg disease-modification claim |
| `Myeloproliferative neoplasms treated with hydroxyurea….pdf` | Gill et al., Hematology | Real-world HU, **peginterferon alfa-2a**, ruxolitinib | That alfa-2a, not ropeg, was studied; PV responses comparable across those modalities | Transfer of ET or safety numbers to BESREMi |
| `20230508162013_1_slideshow.pdf` | Key Opinions in Medicine 2022;7(4), Novartis-sponsored | Early MF education piece | Not used for BESREMi answers | Any BESREMi claim |

## Distilled label file (not a paper)

| File | Use |
|------|-----|
| `industry/pm-reference/besremi-hk-pi-summary.md` | HK indication, titration, contraindications, potency sentence, the single 12-month 43.1% figure attributed to the PI |

The 12-month PROUD-PV publication itself is not in the PDF set. Repeat 43.1% only as “stated in the distilled HK PI summary,” and do not add endpoints around it that the summary does not state.


---

## Source: Worked questions

# Worked medical questions

Use these to check that an answer stays inside the library. They are not extra data.

## 1. Event-free survival versus hydroxyurea

**Must cite:** Gisslinger 2023, same PROUD-PV / CONTINUATION-PV program. Probability 0.94 versus 0.82 at the 6-year analysis, log-rank p = 0.04, hazard ratio 0.34 (95% CI 0.12–0.97), events 5/95 versus 12/74.

**Must also say:** open-label extension; not all randomized patients entered; overall survival was not evaluated; events were few.

**Must not say:** that BESREMi has been shown to extend overall survival.

## 2. “Is BESREMi better than Pegasys?”

**Must say:** this library has no head-to-head trial. The distilled HK PI says potency should not be compared with another pegylated or non-pegylated protein of the same class. Okikiolu is five switch cases, not a comparison. Gill’s real-world paper studied pegylated interferon alfa-2a, not ropeginterferon.

**Must not say:** greater efficacy, better tolerability, or equivalent outcomes versus Pegasys.

## 3. Pregnancy

**Must say:** one case report (Bang 2023) of a delivery without neonatal or maternal complications described by the authors, after an off-protocol 250 µg start and a hold for raised transaminases. Bose 2025 is a review and its pharmacokinetic source is not in the vault. The distilled HK PI summary in this vault has no pregnancy section.

**Must not say:** BESREMi is safe in pregnancy, or choose a dose for the person asking.

## 4. Low-risk patient, hematocrit control

**Must cite:** Barbui, NEJM Evidence 2023. 52/64 (81%) versus 32/63 (51%), p < 0.001, fixed 100 µg every 2 weeks plus phlebotomy and aspirin, versus phlebotomy and aspirin. Mean phlebotomies 2.91 versus 4.17 per patient-year.

**Must also say:** this fixed dose is the study regimen. The distilled HK PI describes titration from 100 µg (or 50 µg) by 50 µg steps to a maximum of 500 µg. Do not prescribe which schedule a named patient should start.

## 5. Chinese phase II “what was the response rate?”

**Must say:** Jin 2023 in this vault is a protocol (250 / 350 / 500 µg). No response rate is reported in that PDF.

## 6. ET versus anagrelide

**Must say:** SURPASS-ET is a designed phase 3 study (NCT04285086) in the Verstovsek protocol PDF. Results are not in the library. ET is outside the Hong Kong PV indication and is reactive only.


---

## Source: HK PI summary (distilled)

# BESREMi — Hong Kong Prescribing Information (distilled)

> Source: `HK-PI_Besremi-final.pdf` (HK local PI). On-label boundary for all proactive HK promotion.

## Product

- **Name:** Besremi® ropeginterferon alfa-2b — solution for injection, prefilled syringe **500 mcg/mL** (1 mL)
- **Form:** SC injection; prefilled syringe 50–500 mcg adjustable increments
- **Excipients (known effect):** benzyl alcohol 10 mg/mL; polysorbate 80 0.05 mg/mL

## Indication (HK)

**Monotherapy in adults** for **polycythaemia vera without symptomatic splenomegaly**.

## Critical PI language for PM/compliance

- **Potency warning (Section 2 / 5.1):** *"The potency of this medicinal product should not be compared to that of another pegylated or non-pegylated protein of the same therapeutic class."* — supports **no IFN-to-IFN superiority** claims in HK materials.
- **Titration vs HU:** PI notes mean titration phase ~**3.7 months** for ropeginterferon vs ~**2.6 months** for hydroxycarbamide; HU may be preferred when **early** count reduction needed to prevent thrombosis/bleeding — use carefully in value messaging (clinical nuance, not anti-product).

## Dosing (summary)

| Phase | Rule |
|-------|------|
| Titration | Start 100 mcg (50 mcg if on other cytoreductive therapy); +50 mcg q2w; parallel taper of other cytoreductive therapy |
| Target | Hct <45%, platelets <400×10⁹/L, WBC <10×10⁹/L |
| Max | 500 mcg q2w |
| Maintenance | q2w ≥1.5y at stable dose; may extend to q4w |

## Key contraindications

Decompensated cirrhosis (Child-Pugh B/C); ESRD (GFR <15); severe psychiatric history; severe uncontrolled CV disease; autoimmune disease; transplant immunosuppression; telbivudine combination; hypersensitivity.

## Efficacy in PI (PROUD-PV / CONTINUATION-PV)

- Phase III vs hydroxycarbamide, n=254 (1:1), 12-month disease response **43.1%** (ropeg arm)
- At **72 months** (extension): **complete hematologic response 54.5%** (ropeg); JAK2V617F burden reduction documented in PI tables
- PI is the **primary** local claim source for on-label efficacy language

## ADR reporting (PI Section 4.8)

HCPs report suspected ADRs via **Drug Office ADR Online Reporting System:** http://www.drugoffice.gov.hk/adr.html

## Reactive / off-label

ET, MF, and other non-PV indications are **not** in HK PI — reactive scientific exchange only per `role-pm.md`.


---
