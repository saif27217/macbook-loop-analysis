# Bias Mitigation Protocol — m1-max-64gb-purchase
## Loop Engineering addendum v3 — 2026-07-02

> Structured counter-bias questioning. Each question maps to a known cognitive
> distortion that can override rational gate-based verdicts.
>
> Purpose: surface concealed uncertainty, not confirm the existing decision.
> If all answers resolve cleanly → STRONG BUY verdict holds.
> If any answer reveals a hidden blocker → HOLD, regardless of earlier gates.

---

## Bias → Targeted Question Mapping

### 1. Confirmation Bias
*"You seek information supporting your choice while ignoring contradictory evidence."*

**Q1.1:** What's the strongest argument against buying this machine that you haven't already factored into the gate analysis? Be specific — not "it's expensive" but a concrete, unique negative.

**Q1.2:** If a friend came to you with this exact same financial situation, specs, and use case, what would you advise them to do? Would your advice match what you're about to do?

---

### 2. Overconfidence
*"You trust your judgment more than it deserves, assuming your logic is flawless."*

**Q2.1:** What would have to be true for this purchase to be a mistake 12 months from now? Name three specific failure scenarios, not vague ones.

**Q2.2:** The 15-gate analysis assumed your use case stays stable. What if your AI interests shift in 6 months toward CUDA-specific research, on-device training at scale, or a toolchain that runs poorly on Metal? How likely is that shift, and what would you do if it happened?

---

### 3. Anxiety / Stress
*"Emotional pressure clouds judgment, making you second-guess sound decisions."*

**Q3.1:** What part of this decision feels most emotionally heavy right now? Is it the money, the family reaction, the fear of regret, or something else? Name it precisely.

**Q3.2:** If you removed all emotion from this decision and looked at it as a spreadsheet, where would the break-even point be? Days of usage, projects completed, API costs avoided — what's the minimum utilization to justify the cost?

---

### 4. Loss Aversion
*"Fear of failure distorts risk assessment, leading to hesitation."*

**Q4.1:** You're not actually afraid of losing ₹1.3L. What are you *really* afraid of losing? Reputation? Family trust? Your own sense of discipline? The opportunity cost of *not* having this capability?

**Q4.2:** What's the regret you'd feel more acutely in 3 years — buying the machine and underutilizing it, or NOT buying it and having a project fail because you lacked the hardware to attempt it?

---

### 5. Complexity Paralysis
*"Too many variables make it hard to pinpoint certainty, creating doubt."*

**Q5.1:** If you could only keep ONE piece of information from all our research to make the final call, what would it be? (Bandwidth, resale floor, API cost avoidance, MLX speedup, battery risk, buyer's remorse rate?)

**Q5.2:** If I told you the machine would definitely break in exactly 14 months, at what price would you still buy it? That number is your true value threshold. How does ₹1.3L compare?

---

### 6. Social Pressure
*"External expectations undermine confidence in your choice."*

**Q6.1:** Who in your life would think this purchase is reckless? Whose opinion is shaping your guilt more than your own analysis?

**Q6.2:** If no one else ever knew you bought this machine, would you still buy it? If the answer changes, the purchase is partly for signaling — and ₹1.3L is too expensive for signaling.

---

### 7. Biological Variation
*"Real-world decisions aren't static — natural fluctuations introduce irreducible uncertainty."*

**Q7.1:** The battery health at pickup could be anywhere from 95% to 70%. The actual used resale in 2028 could be ₹55K–90K. Mr. Mac's warranty response time to a claim could be 2 days or 2 months. Name the three biggest irreducible uncertainties. Can you live with each of them at their worst realistic case?

**Q7.2:** If the battery comes back at 78% health (just below the 80% threshold), the machine is still functional and the warranty covers most of the replacement cost. Is that your worst case, or is there a worse outcome you haven't named?

---

## Protocol

1. User answers all 14 questions in a single response.
2. Answers are classified as RESOLVED (clear, decisive, no hidden blocker) or UNRESOLVED (hedging, rationalization, deferred).
3. Any UNRESOLVED answer → loop reopens, additional probing questions follow.
4. All 14 RESOLVED cleanly → verdict confirmed STRONG BUY.
5. Any single answer reveals a hidden structural blocker (e.g., Q6.2 reveals signaling motive, Q4.2 reveals wrong regret direction) → verdict drops to HOLD.

**This is not an interrogation.** It's a structured QC check on a high-stakes decision. The goal is to surface what the gate analysis missed — which is always the human layer.
