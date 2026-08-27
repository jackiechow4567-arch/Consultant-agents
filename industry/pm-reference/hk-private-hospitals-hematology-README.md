# HK Private Hospitals — Haematology Directory

**Last verified:** 2026-08-27  
**Scope:** All 14 private hospitals licensed under the Private Healthcare Facilities Ordinance (Cap. 633), plus Adventist Medical Centre satellite sites where clinical haematology is offered.

## Definitions used

| `service_type` | Meaning |
|---|---|
| **Clinical Haematology & Haematological Oncology** | Specialist consultation and treatment for blood disorders / blood cancers |
| **Paediatric Haematology & Oncology** | Paediatric blood disease and oncology services |
| **Clinical Haematology (visiting specialist)** | Hospital lists haematology; care via visiting/honorary consultants |
| **Laboratory Haematology only** | Pathology/lab testing (CBC, coagulation, etc.) — not a haematology clinic |

## Summary (clinical vs lab)

### Clinical haematology / hemonc (8 licensed hospitals + 2 Adventist satellites)

- Gleneagles Hospital Hong Kong
- Hong Kong Sanatorium & Hospital (Happy Valley)
- HKSH Eastern Medical Centre (Island East)
- Union Hospital (+ Union Oncology Centre, TST)
- Hong Kong Adventist Hospital – Stubbs Road
- Hong Kong Adventist Hospital – Tsuen Wan
- CUHK Medical Centre
- Matilda International Hospital (visiting specialists)
- Adventist Medical Center – Causeway Bay *(network clinic)*
- Adventist Medical Center – Taikoo Place *(network clinic)*

### Laboratory haematology only (6 licensed hospitals)

- Hong Kong Baptist Hospital (+ EKMC satellite lab)
- St. Paul's Hospital
- Canossa Hospital
- Evangel Hospital
- St. Teresa's Hospital
- Precious Blood Hospital

## Opening hours (`department_opening_hours`)

Both CSVs include a **`department_opening_hours`** column with published reception/clinic or lab counter hours for each haematology-related department or centre. **`opening_hours_notes`** (locations tab only) clarifies caveats such as “by appointment only”, extended lab coverage, or unpublished hours.

| Site type | What the hours represent |
|---|---|
| Clinical haematology centres | Clinic/centre reception hours; specialist consultations are typically by appointment within these times |
| Laboratory haematology | Lab service or specimen collection hours (may differ from clinical clinic hours) |
| Unpublished | Row notes say to contact the department directly (e.g. Canossa lab) |

**21 location rows** cover all 14 licensed private hospitals plus Adventist Medical Centre satellites and HKSH pathology lab.

## Inpatient pharmacies tab (14 hospitals)

`hk-private-hospitals-inpatient-pharmacy.csv` lists the **inpatient pharmacy department** for each of the 14 licensed private hospitals, including:

- `inpatient_pharmacy_address_en` — full published address (hospital campus + floor/building where listed)
- `inpatient_pharmacy_floor_location` — floor or wing within the hospital
- `pharmacy_hours` — published counter or service hours where available
- `notes` — e.g. internal-only pharmacy (HKSH Eastern), separate inpatient vs outpatient counters (CUHKMC, Baptist Block E 24hr)

Satellite outpatient sites (Union polyclinics, Adventist Medical Centre, HKBH EKMC) are excluded — inpatient pharmacy is at the main licensed hospital campus.

## Haematologists tab (20 doctors)

Clinical / paediatric consultants are listed in `hk-private-hospitals-hematologists.csv`, including:

- **Gleneagles HK** — 6 haematology/hemonc specialists
- **HKSH** — 2 adult + 2 paediatric clinical; 2 pathology haematologists
- **Union** — 2 consultants (3 practice sites between them)
- **Adventist network** — Dr Ma (Stubbs + AMC); Dr Chan (Tsuen Wan)
- **CUHKMC** — Dr Li Wa (in-house)
- **Matilda** — Dr Herman Liu (honorary/visiting)

Each haematologist row includes **`department_opening_hours`** aligned to their listed practice location(s).

## Data files

| File | Contents |
|---|---|
| `hk-private-hospitals-hematology.csv` | Locations, contacts, and department opening hours (Tab 1 source) |
| `hk-private-hospitals-hematologists.csv` | Haematologists by hospital with department hours (Tab 2 source) |
| `hk-private-hospitals-inpatient-pharmacy.csv` | Inpatient pharmacy address and contact per licensed hospital (Tab 3 source) |
| `hk-private-hospitals-hematology.xlsx` | Excel workbook with all three tabs |

Regenerate Excel after CSV edits:

```bash
python3 scripts/build_hk_hematology_workbook.py
```

## Data sources

- [HK Private Hospitals Association](https://www.privatehospitals.org.hk/en/hospitals.htm) — master list of 14 licensed hospitals
- [data.gov.hk — DH licensed private hospitals](https://data.gov.hk/en-data/dataset/hk-dh-dh_hq-dh-orphf-phl) — official registry (contact refresh)
- Individual hospital websites (cited per row in CSV)

## Refresh checklist

1. Re-download DH licensed hospital CSV from data.gov.hk  
2. Re-check each hospital's clinical services / hospital directory page  
3. Spot-call 2–3 high-priority sites before using for partnerships
