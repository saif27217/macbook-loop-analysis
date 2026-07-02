# MacBook Loop Analysis

Loop Engineering methodology applied to MacBook purchase decisions.

Gate-based L1 triage with token-budgeted research, kill switches, and stateful audit trail.
Produces a defensible BUY / HOLD / REJECT verdict from cross-referenced market data,
model capacity benchmarks, resale math, and physical inspection.

## Quick start

```bash
git clone https://github.com/saif27217/macbook-loop-analysis.git
cd macbook-loop-analysis
```

1. Copy templates from `templates/` → project root: `LOOP.md`, `STATE.md`, `loop-budget.md`, `loop-run-log.md`
2. Fill `LOOP.md` with your gate criteria and price ceiling
3. Run research slots while tracking tokens in `loop-budget.md`
4. Update `STATE.md` as gates go PASS/FAIL/PENDING
5. Derive verdict from gate counts (see `LOOP.md`)
6. Physical inspection → confirm gates before marking PASS

## Files

| File | Purpose |
|------|---------|
| `LOOP.md` | Control file — cadence, gates, kill switches, human gates |
| `STATE.md` | Live triage state — gate results, watch list, verdict |
| `loop-budget.md` | Token/time budget per research slot |
| `loop-run-log.md` | Append-only audit trail per investigation pass |
| `references/inspection-checklist.md` | 10-point physical machine checklist |
| `references/resale-formula.md` | 3-year resale estimator with modifiers |
| `scripts/loop_triage_helper.py` | CLI helper to mark gates and derive verdict |
| `templates/` | Blank templates for all of the above |

## Verdict thresholds (L1)

| Result | Meaning |
|--------|---------|
| 8/8 PASS | STRONG BUY |
| 6–7/8 PASS | BUY (note pending/marginal gates) |
| 4–5/8 PASS | HOLD |
| ≤3/8 PASS | REJECT |

Hard fail on `ram_verified` or `warranty_verified` auto-flips to HOLD regardless of other gates.

## License

MIT — see [LICENSE](LICENSE)
