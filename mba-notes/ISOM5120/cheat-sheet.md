# ISOM5120 — Visualizing Data for Business Decisions cheat sheet

> HKUST Spring 2026 · Jean Wang · Distilled for **data-story-brief playbook** · **Done 2026-07-27**  
> Attach when user needs chart choice, dashboard brief, or executive data story

---

## Core premise

**Data visualization** turns granular data into **understandable, decision-oriented** views — static or interactive.  
Goal is not "show all data" but **support a business decision** with the right encoding, story flow, and audience takeaway.

**Tools in course:** Tableau (primary), Power BI (comparison lab) — principles are tool-agnostic.

---

## When to use what (agent quick map)

| Question | Start with |
|----------|------------|
| What am I trying to do? | **Purpose:** Exploration · Communication · Cognition · Decision |
| Who is looking? | **Define before design** — purpose, viewers, data, message |
| Which chart? | **Insight type → chart type** (ranking, change, part-to-whole, etc.) |
| Is this dashboard or slide? | **Strategic vs operational** dashboard |
| Is the viz honest? | **Effectiveness criteria** — especially truthfulness & perceptibility |
| Symbolic vs pattern question? | Table may beat chart for **precise lookup** |

---

## Four purposes of visualization

| Purpose | Use when |
|---------|----------|
| **Exploration** | Unknown patterns; analyst drills |
| **Communication** | Fixed narrative for audience |
| **Cognition** | Understand complexity (e.g., market shift) |
| **Decision making** | Choice requires comparison to target/baseline |

**Explanatory vs exploratory:** Executives usually need **explanatory** — one primary message per view.

---

## Define before you design

| Step | Questions |
|------|-----------|
| **Purpose** | Why this viz? Goals? Polish level? Format? Interactivity? |
| **Viewers** | Who? Prior knowledge? Expectations? Detail need? |
| **Data** | Relevant fields? Raw vs aggregated? Groupings? Outliers? |
| **Message** | Takeaway? Emotion? Leftover questions? |
| **Design** | How many views? Marks/channels? Reading order? |

---

## Effectiveness criteria (check all)

| Criterion | Test |
|-----------|------|
| **Usefulness** | Shows decision-relevant information |
| **Engagement** | Connects; yields insight |
| **Aesthetics** | Clean; no decoration |
| **Perceptibility** | Eye/brain decode with minimal effort |
| **Truthfulness** | No skewed axes or misleading ratios |
| **Intuitiveness** | Easy to read |
| **Completeness** | Covers question scope — not clutter |

**5-second rule:** Key insight visible in ~5 seconds.

---

## Visual encoding — marks & channels

**Mark:** Point, line, area, bar (geometric item)  
**Channel:** Position, size, color, shape, orientation  

**Encoding = Marks + Channels** mapped to data attributes (qualitative vs quantitative).

**Channel choice rules:**
- **Quantitative magnitude** → position on common scale (best accuracy)  
- **Identity / categories** → color hue, shape (limited classes)  
- Prefer **accurate channels** for critical comparisons  

**Anscombe's quartet lesson:** Same summary stats, different stories — **always plot**.

---

## When NOT to visualize

**Symbolic questions** — precise single values ("total cases Tuesday?") → **table** often better.  
**Pattern questions** — trends, outliers, distributions → **chart**.

---

## Dashboard types

| Type | Audience | Update | Focus |
|------|----------|--------|-------|
| **Strategic / KPI** | Executives, board | Daily–quarterly | Goals vs strategy |
| **Operational** | Operators, supervisors | Real-time/near-real | Act on exceptions |

**Components:** Data source · metrics · charts · filters · navigation · interactivity tying views.

---

## Design principles (course checklist)

1. **5-second rule** — insight fast  
2. **Right chart type** for the analytical question  
3. **Less is more** — remove non-informative ink  
4. **Color wisely** — 5–8 distinct colors; meaning not decoration  
5. **Alignment** — related elements aligned; diverging bars when appropriate  
6. **Clear captions** — title states insight; annotate key points  
7. **White space** — guides eye; reduces cognitive load  

---

## Insight → chart type guide

| Analytical need | Common chart forms |
|-----------------|-------------------|
| **Ranking** | Ordered bar, slope graph |
| **Change over time** | Line, area, slope |
| **Part-to-whole** | Stacked bar (careful), treemap, waffle |
| **Distribution** | Histogram, box plot, violin |
| **Correlation** | Scatter, bubble |
| **Deviation from target** | Bar + reference line, bullet chart |
| **Magnitude comparison** | Bar (start at zero) |
| **Flow / process** | Sankey (when justified) |
| **Spatial** | Map (only if geography is the insight) |

**Re-chart same data** when question changes (e.g., yearly trend vs cumulative return vs range).

---

## Visual analytics (exploration layer)

Techniques in course labs:
- **Calculated fields** · **table calculations** (% of total, period change)  
- **Reference lines / parameters** — adjustable goals (e.g., profit margin threshold)  
- **Trend lines & forecast** — describe model; show confidence when useful  
- **Cluster analysis** — segment profiling after clustering  

Use when audience must **drill** — pair with guardrails so they don't drown.

---

## Story flow (executive brief)

1. **Context** — what decision, what data  
2. **So what** — primary insight (one sentence)  
3. **Options / variance** — vs target, baseline, or scenario B  
4. **Ask / next step** — owner, date  

---

## Data caveats block (always include)

- Metric definitions · aggregation level · time window  
- Missing data / sample bias  
- **What NOT to show** — clutter, raw rows, sensitive identifiers  

**Sensitivity:** Aggregate, index, or delay if High tier — per playbook.

---

## Exclusions

Personal final project submission, `.twbx` workbooks, lab CSV/XLS datasets. Lecture 4 slides not separately filed — Week 3–4 lab PDFs cover dashboard + visual analytics techniques.

---

## Source

OneDrive: `Spring 2026\ISOM5120 Visualizaing Data for Business Decisions` — syllabus, lec1–3 PDFs, lab1–5 PDFs, project brief.

## References

Munzner *Visualization Analysis & Design* · Wilke *Fundamentals of Data Visualization* · Wexler et al. *Big Book of Dashboards*
