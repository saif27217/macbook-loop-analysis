# Loop Configuration — MacBook Purchase Triage

## Active Loops

| Pattern | Cadence | Status | Command |
|---------|---------|--------|---------|
| purchase-triage | one-shot | L1 report-only | manual invocation |

## Decision Gates

All gates must PASS for STRONG BUY verdict. Single FAIL on `ram_verified` or `warranty_verified` auto-flips to HOLD.

| Gate | PASS threshold |
|------|---------------|
| ram_verified | 16GB min for AI; 64GB preferred for 70B-class models |
| ssd_verified | 512GB min; 1TB for model storage |
| battery_health | ≥80% capacity, <200 cycles |
| warranty_verified | Active AppleCare or seller warranty >6 months |
| price_ceiling | ≤ defined max (see loop-budget.md) |
| model_capacity | Target model runs at ≥3 tok/s Q4 |
| resale_floor | 3-yr resale ≥30% of purchase price |
| cooling_risk | Active cooling or no sustained-load throttle |

## Human Gates

- No auto-purchase. Human closes the buy after verdict.
- Physical inspection is mandatory before marking `ram_verified`/`ssd_verified` PASS.
- Never mark warranty PASS from seller word alone — require written terms.

## Kill Switch

| Trigger | Action |
|---------|--------|
| token_budget_exceeded | Write partial STATE, halt research, report what we have |
| gate FAIL on ram or warranty | Stop, verdict = HOLD, escalate |
| machine not physically accessible | Cannot mark inspect gates → verdict = HOLD |

## Links

- Pattern: purchase-triage
- Gates: references/gates.md
- Budget template: references/loop-budget.template.md
- Inspection checklist: references/inspection-checklist.md
- Resale formula: references/resale-formula.md
