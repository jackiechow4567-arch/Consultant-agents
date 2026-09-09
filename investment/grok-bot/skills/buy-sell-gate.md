# Skill — Buy / sell gate

Save in Grok Bot as **Buy / sell gate**.

```text
When to use: user is about to act on ONE ticker (or asks “can I buy / should I sell”).

Required inputs:
- Ticker and intended action
- investment/knowledge/buy-checklist.md or sell-checklist.md
- A current chart (TradingView) and the latest catalyst note

Sequence (buy):
1. Walk the buy checklist. Hard fail = NO BUY TODAY. List defects; do not “mostly fine” a broken pivot.
2. State stop, stop %, 2:1 target, and distance from breakout.
3. If >5% above breakout: WAIT. If earnings <10 sessions and size would be large: CUT THE PROPOSED SIZE.
4. Confirm sector leadership vs laggard.

Sequence (sell):
1. Walk lock-profit vs risk-control lists.
2. If stop hit or behaviour is wrong: SELL. Do not negotiate.

Return: PASS / FAIL / WAIT with the filled checklist and one recommended action for the USER to take.

Approval: never send the order.
```
