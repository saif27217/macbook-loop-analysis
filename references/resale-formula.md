# Resale Value Formula

Approximate resale as percentage of purchase price at N years.

## Base formula

```
Year 1 depreciation:  20%
Year 2 depreciation:  12%
Year 3 depreciation:  12%
Annual years 4–5:      10% each

resale_at_yearN = 1.0 - sum(depreciations through N)
```

## Config modifiers

| Modifier | Condition | Adjustment |
|---------|-----------|-----------|
| `ram_bonus` | RAM ≥ 64GB | +5% (scarcity premium) |
| `ram_bonus` | RAM ≥ 32GB | +2% |
| `ram_bonus` | RAM < 16GB | 0% |
| `cooling_bonus` | Active cooling (Pro/Max) | +3% |
| `cooling_bonus` | Fanless (Air) | 0% |
| `support_penalty` | macOS support < 3 years remaining | −5% |
| `support_penalty` | macOS support ≥ 5 years | +0% |

## Example

M1 Max, 64GB, 1TB, bought at ₹1.3L:

```
Year 1: 1.0 - 0.20 = 0.80
Year 2: 0.80 - 0.12 = 0.68
Year 3: 0.68 - 0.12 = 0.56
+5% (64GB) +3% (active cooling) = +8% → 0.64

Resale floor year 3 = 0.64 × 1,30,000 = ₹83,200
```

With macOS support ~2028 for feature updates (from 2026 purchase = ~3 years), apply `-5%` support penalty in year 3:
```
0.56 + 0.08 - 0.05 = 0.59 → ₹76,700
```

## Gate threshold

`resale_floor` gate PASS if 3-year resale estimate ≥ 30% of purchase price.
