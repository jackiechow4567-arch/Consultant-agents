# ISOM5120 — Frameworks reference

> Companion to [cheat-sheet.md](cheat-sheet.md). Used by [data-story-brief playbook](../../playbooks/data-story-brief.md).

---

## 1. Course arc (4 lectures)

```
LEC 1                    LEC 2                      LEC 3                    LEC 4 (labs)
────────                 ─────                      ─────                    ────────────
What/why/when            Effectiveness criteria     Dashboard types          Visual analytics
Input/output/tools       Marks & channels           Design principles        Table calc, forecast
Tableau intro            Color                      Chart choice             Clusters, parameters
Vision & purposes        Truthfulness/perception    Strategic vs operational Power BI compare
```

---

## 2. Design workflow

```
Business question (not "show data")
        │
        ▼
Purpose + Audience + Sensitivity tier
        │
        ▼
Exploratory or Explanatory?
        │
        ├── Exploratory → interactive dashboard, filters
        └── Explanatory → fixed story, one message/view
        │
        ▼
Pick insight type → chart type
        │
        ▼
Encode (marks + channels) + design principles
        │
        ▼
Caveats + what NOT to show
```

---

## 3. Effectiveness audit checklist

```
[ ] Usefulness — answers decision question
[ ] Truthfulness — axes, baselines, labels honest
[ ] Perceptibility — accurate channels for magnitude
[ ] 5-second — primary insight immediate
[ ] Less is more — junk removed
[ ] Color — semantic, accessible, limited palette
[ ] Completeness — scope without clutter
[ ] Sensitivity — no raw PHI/PII required to get point
```

---

## 4. Channel accuracy hierarchy (quantitative)

```
Position on common scale  →  best for magnitude compare
Length (bar)              →  good; zero baseline
Angle, area, color sat    →  use carefully
Volume, curvature         →  avoid for precise compare
```

---

## 5. Dashboard layout pattern

```
┌─────────────────────────────────────┐
│ KPI headline + period               │
├──────────────┬──────────────────────┤
│ Trend (time) │ Breakdown (category) │
├──────────────┴──────────────────────┤
│ Exception table or drill filter   │
└─────────────────────────────────────┘
Filters: time, region, product — tied across views
```

---

## 6. Playbook output crosswalk

| Playbook section | ISOM5120 source |
|------------------|-----------------|
| Decision visual must support | Purpose + viewers |
| Recommended visuals table | Insight → chart guide |
| Story flow | Lec 3 message design |
| Data caveats | Symbolic vs pattern + sensitivity |
| Design rules | Effectiveness + 5-second rule |

---

## 7. When NOT to use dashboards

| Situation | Prefer |
|-----------|--------|
| Single number lookup | Table or KPI tile only |
| No clear decision owner | Clarify question first |
| Data quality unknown | Exploration offline; don't publish |
| High sensitivity raw rows | Aggregate brief only |
