---
name: deidentify-brief
description: >-
  Turns high-sensitivity work material into a de-identified summary safe for
  Gemini Enterprise or sharing. Use when the user asks to de-identify, redact,
  sanitize, 脫敏, prepare an upload-safe brief, or move content from work-briefs
  to an external LLM.
---

# De-identify Brief

## When to use

User has high-sensitivity raw notes (clinical, contracts, financials, HR, unpublished strategy) and needs an upload-safe or shareable summary.

## Instructions

1. Follow `consultant-agents/privacy-policy.md`.
2. Prefer reading/writing under `consultant-agents/work-briefs/` for raw high-sensitivity content.
3. Produce a **脫敏摘要** that keeps decision utility but removes or replaces:
   - Person names → role labels (e.g. 「港區 KOL A」「臨床負責人」)
   - Patient/subject IDs, MRNs, phones, emails, precise addresses
   - Exact money amounts → ranges or index vs baseline
   - Contract clause text → commercial gist only
   - Internal unpublished codes → generic project aliases
4. Output structure:

```markdown
## 敏感級聲明
- 原料：高（僅本機）
- 本摘要：中或低（說明為何）
- 允許工具：Gemini Enterprise / 僅內部分享 / 仍建議本機

## 決策問題
## 已知（脫敏）
## 選項（若有）
## 約束與風險（無原始證據附件）
## 資料缺口與假設
## 建議下一步
## 仍不得外傳的項目清單
```

5. Never paste raw high-sensitivity source into suggestions for Perplexity.
6. If the user asks to upload the raw file externally, refuse and offer this de-identified brief instead.
7. Optionally save the summary as `work-briefs/YYYY-MM-DD-<topic>-deidentified.md` and remind that even de-identified mid-tier content should prefer Gemini Enterprise over consumer tools.
