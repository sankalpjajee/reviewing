# Stage 4 — Methodology and evaluation validity

Run as part of the multi-agent dimension review (5 reviewers → adversarial
verification). The completed output for this stage lives in:

- [`findings.json`](findings.json) — dimension `method` (10 surviving findings) and
  `stats` (10), each with verifier notes
- [`REVIEW.md`](REVIEW.md) — weakness clusters **W2** (attribution / missing
  rubric-free LLM baseline), **W3** (per-cell significance), **W4** (trajectory
  overreach), **W5** (closed evaluation universe: author-built pools, rubric/task
  team overlap, source-included Top-N protocol, router taxonomy)

Checklist items were exercised by the agents; notable passes recorded as strengths:
scorer≠solver confound directly probed (Fig 6 off-diagonals), router corruption
sweep properly uncertainty-quantified, solver blinding stated, skill-necessity
anchor verified against Table 3.
