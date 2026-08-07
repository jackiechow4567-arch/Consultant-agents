#!/usr/bin/env python3
"""Validate consultant agent wiring and knowledge packs."""
from pathlib import Path

VAULT = Path(__file__).resolve().parents[1]
errors: list[str] = []
warnings: list[str] = []

courses = [
    "MGMT5410", "MARK5120", "ECON5110", "FINA5120", "ACCT5100", "ISOM5700",
    "MGMT6501T", "MGMT6501W", "MGMT5590", "ISOM5020", "SBMT6012G", "MGMT6501Q", "ISOM5120",
]

for c in courses:
    p = VAULT / "mba-notes" / c / "cheat-sheet.md"
    if not p.exists():
        errors.append(f"Missing cheat-sheet: {c}")

for rel in [
    "industry/role-pm.md",
    "industry/role-gm.md",
    "industry/role-clinical-pm.md",
    "industry/pm-reference/_index.md",
    "industry/cpm-reference/_index.md",
    "industry/gm-reference/_index.md",
]:
    if not (VAULT / rel).exists():
        errors.append(f"Missing: {rel}")

agents = list((VAULT / "agents").glob("*.md"))
if len(agents) != 6:
    errors.append(f"Expected 6 agents, found {len(agents)}")

cursor_agents = Path.home() / ".cursor" / "agents"
for name in [
    "consultant-router",
    "strategy-marketing",
    "finance-accounting",
    "ops-clinical-pm",
    "product-gm",
    "tech-geopolitics",
]:
    if not (cursor_agents / f"{name}.md").exists():
        warnings.append(f"Missing ~/.cursor/agents/{name}.md")

gem = VAULT / "gem-knowledge-pack"
for f in [
    "00-router-knowledge.md",
    "01-strategy-marketing-knowledge.md",
    "02-finance-accounting-knowledge.md",
    "03-ops-clinical-pm-knowledge.md",
    "04-product-gm-knowledge.md",
    "05-tech-geopolitics-knowledge.md",
    "gem-system-prompts.md",
]:
    if not (gem / f).exists():
        errors.append(f"Missing gem pack: {f}")

g4_path = gem / "04-product-gm-knowledge.md"
if g4_path.exists():
    g4 = g4_path.read_text(encoding="utf-8")
    for needle in [
        "GM ref: HK Employment Ordinance",
        "MGMT6501T",
        "role-gm",
        "Continuous contract",
    ]:
        if needle not in g4:
            errors.append(f"Gem 04 missing: {needle}")

a4_path = VAULT / "agents" / "04-product-gm.md"
if a4_path.exists():
    a4 = a4_path.read_text(encoding="utf-8")
    if "gm-reference" not in a4:
        errors.append("Agent 04 missing gm-reference wiring")

for pb in ["exec-comms.md", "data-story-brief.md", "decision-one-pager.md"]:
    if not (VAULT / "playbooks" / pb).exists():
        warnings.append(f"Missing playbook: {pb}")

print("=== CONSULTANT VAULT VALIDATION ===")
print(f"Agents: {len(agents)}")
print(f"MBA courses checked: {len(courses)}")
if g4_path.exists():
    print(f"Gem 04 size: {g4_path.stat().st_size // 1024} KB")
print()
if errors:
    print(f"ERRORS ({len(errors)}):")
    for e in errors:
        print(f"  - {e}")
else:
    print("ERRORS: none")
print()
if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings:
        print(f"  - {w}")
else:
    print("WARNINGS: none")
print()
print("RESULT:", "PASS" if not errors else "FAIL")
