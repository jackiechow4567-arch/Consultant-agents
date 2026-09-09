# Playbook — News and 催化劑

News exists to **time risk** and to **confirm** a leader. It is not an entry system. Tips are a hard fail (operating system rule on low-quality buys).

---

## Split every headline

| Bucket | Keep? | Examples |
|--------|-------|----------|
| **催化劑 / USE** | Yes, as risk or confirmation | Earnings date, offering, FDA/product, sector-wide breakout, volume dry-up then expansion, RS new high |
| **IGNORE / 消息** | No | Tips, TV, Discord, “cheap so bounce”, rumour without filing |

If the chart already fails the buy checklist, a bullish headline does **not** rescue it.

---

## Per ticker (10-session window)

1. Next **earnings** (BMO/AMC) — if <10 trading days, tag `HOLD-SIZE-RISK`
2. Dilution / convert / ATM
3. Sector news that explains why **leaders** are moving together
4. Unusual volume vs 10-day (scanner `relative_volume_10d_calc` is a hint, not a pivot)
5. Primary source: IR, filing, exchange notice. Aggregators are a pointer, not the citation.

Mark articles older than 7 days as **stale** unless they are the last print.

---

## Template

```markdown
## Catalysts — <date>
| Date | Ticker | Event | USE / IGNORE | Size implication | Source |
|------|--------|-------|--------------|------------------|--------|
| | | | | e.g. HOLD-SIZE-RISK / none | URL |

## Ignored noise
- 
```

## Bot language

- “This headline is why **risk** changed” — good
- “Buy because I heard” — kill
- “Laggard will catch up on the same news” — kill
