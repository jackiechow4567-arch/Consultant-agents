# Skill — News & 催化劑

Save in Grok Bot as **News & 催化劑**.

```text
When to use: after a shortlist exists, or when the user names tickers. Also run on the live watchlist every weekday.

Required inputs:
- Tickers (from daily_brief.py, watchlist.md, or the user)
- investment/knowledge/jlaw-operating-system.md (catalyst vs tip rules)
- investment/playbooks/news-catalyst.md
- Public web, company IR, SEC-style filings, X. Cite URL + date.

Sequence:
1. For each ticker, find: next earnings date, last earnings reaction, dilution/offering, sector news, and any dated event in the next 10 trading days.
2. Separate the table into:
   - 催化劑 that confirms leadership or changes RISK (earnings, offering, FDA, sector move, volume tell)
   - Noise / 消息 (tips, TV, “it’s cheap”) — mark IGNORE
3. If earnings are inside 10 trading days, label HOLD-SIZE-RISK. Never suggest an oversized position through the print.
4. Do not upgrade a failed chart because the headline is bullish.
5. Prefer primary sources (IR, filing, exchange notice) over aggregators.

Validate:
- Every catalyst row has a date and a source.
- Tips without a source are dropped, not paraphrased as research.
- Stale articles (>7 days) are marked stale unless they are the last earnings print.

Return: catalyst calendar + per-name risk notes, using the playbook template.

Approval: do not email, tweet, or message anyone. Draft only in this thread.
```
