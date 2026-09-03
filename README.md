# Consultant Agents Vault (v2)

MBA × industry consultant agents for Hong Kong subsidiary work (Clinical PM / Product Manager / GM).

## Tool split

| Tool | Use for | Do not use for |
|------|---------|----------------|
| **Cursor** (local skills + this vault) | High-sensitivity drafts, agent prompts, workflows, de-ID then export | Pasting raw clinical/contract files into external chats |
| **Gemini Enterprise** | Mid-sensitivity long docs, Drive/Workspace, multi-file synthesis | Primary live web research |
| **Perplexity Pro** | Low-sensitivity public research with citations | Internal finance, patient data, unpublished roadmaps |

**Rule:** high-sensitivity raw → process locally → export only de-identified conclusions.  
See [privacy-policy.md](privacy-policy.md).

## Agents (6)

| File | Cursor skill | Role |
|------|--------------|------|
| [agents/00-router.md](agents/00-router.md) | `consultant-router` | Sensitivity, tool, consultant routing |
| [agents/01-strategy-marketing.md](agents/01-strategy-marketing.md) | `strategy-marketing-consultant` | Strategy + marketing + microeconomics |
| [agents/02-finance-accounting.md](agents/02-finance-accounting.md) | `finance-accounting-consultant` | Corporate finance + reporting |
| [agents/03-operations-clinical-pm.md](agents/03-operations-clinical-pm.md) | `ops-clinical-pm-consultant` | Operations + clinical PM delivery |
| [agents/04-product-gm.md](agents/04-product-gm.md) | `product-gm-consultant` | Product / GM / healthcare decisions |
| [agents/05-tech-geopolitics.md](agents/05-tech-geopolitics.md) | `tech-geopolitics-consultant` | Tech strategy + emerging-tech geopolitics |

Job titles (CPM / PM / GM) are **role lenses**, not separate personas.

## Install in Cursor

This repo ships the full setup: vault content at the repo root plus Cursor integration under `.cursor/`.

**Option A — clone into a project (recommended for vault + skills together)**

```powershell
git clone https://github.com/jackiechow4567-arch/Consultant-agents.git
```

Open the cloned folder in Cursor. Skills in `.cursor/skills/` and subagents in `.cursor/agents/` load automatically for that workspace.

**Option B — global skills only (use vault elsewhere)**

Copy or symlink `.cursor/skills/*` into your user skills folder:

```powershell
$src = "C:\path\to\Consultant-agents\.cursor\skills"
$dst = "$env:USERPROFILE\.cursor\skills"
Get-ChildItem $src -Directory | ForEach-Object {
  Copy-Item $_.FullName (Join-Path $dst $_.Name) -Recurse -Force
}
```

## Quick start in Cursor

1. Start with: `Use consultant-router. …` (state sensitivity + role lens).
2. Continue with the skill it names, e.g. `Use product-gm-consultant.`
3. For HQ-facing output, ask it to attach `exec-comms` or `decision-one-pager`.

### Gemini Enterprise

Create one Gem per agent file (`00`–`05`) and paste the system prompt from each markdown file.

## Role memory

| File | Role |
|------|------|
| [industry/role-pm.md](industry/role-pm.md) | Product Manager |
| [industry/pm-training/](industry/pm-training/README.md) | BESREMi PM competency training + self-test |
| [industry/role-gm.md](industry/role-gm.md) | General Manager |
| [industry/role-clinical-pm.md](industry/role-clinical-pm.md) | Clinical PM / quality lens |

Fill these over time (forward distillation is fine; full Perplexity history export is optional).

## Playbooks

- [Decision one-pager](playbooks/decision-one-pager.md)
- [Project risk & resources](playbooks/project-risk-resource.md)
- [Finance Q&A brief](playbooks/finance-qa-brief.md)
- [Executive communication](playbooks/exec-comms.md)
- [Data story brief](playbooks/data-story-brief.md)
- [Perplexity Space distill](playbooks/perplexity-space-distill.md) (optional)
- [Notion agent databases + prompts](playbooks/notion-agent-db.md)

## MBA notes

Course → agent map: [mba-notes/_index.md](mba-notes/_index.md)  
Add `cheat-sheet.md` per course when ready (PDFs stay in OneDrive).

## Development plan

[DEVELOPMENT-PLAN-v2.md](DEVELOPMENT-PLAN-v2.md)

## Other personal skills

- `deidentify-brief` — high → de-identified summary  
- `decision-one-pager` — exec decision memo  
