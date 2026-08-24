# Stage 3 — Numeric and statistical audit

```bash
python3 workflow/scripts/audit_numbers.py \
    reviews/2026-paper-612d60fa/artifacts/checks.json \
    --json reviews/2026-paper-612d60fa/artifacts/numeric_audit.json
# 25 passed, 2 failed, 0 errored — exit 1
```

27 relations transcribed from the paper. This submission is the most numerically
consistent this workflow has audited: every structural check passes.

## Passed (25)

- **Row averages:** all Table 3 Avg cells recompute from their nine cells (M-SQE
  69.1, SkillFlow 65.6, Retrieve-only 62.8, Random 55.1, Prompt-only 39.9).
- **Prose deltas:** +3.5 / +6.3 / +14.0 all exact.
- **Counting claims:** "first or tied-first in all 9" → 9/9 (ties at Tool-Ne and
  Cul-Ne); "strictly ahead of both anchors in all 9" → 9/9.
- **Integer consistency:** all nine M-SQE cells sit within 0.032pp of an exact
  k/n over the stated task counts (70/94 … 49/52). Extended by the stats agent:
  **all 102 deterministic cells** across Tables 3/4/5 are integer-consistent (81 non-Random Table 3 cells + 9 + 12; exhaustively recounted at re-evaluation — the workflow agent's original count of 45 was an undercount).
- **Cross-artifact:** Fig 4 Top-3 = Table 3 BM25 mean (68.17→68.2); Fig 6 main
  cell (59.6/68.2/+8.6) = Table 3-derived; Fig 6 "+3.5–9.0pp" range matches its
  six deltas; Table 4's M-SQE row = Table 3's BM25 cells; K-rule reproduces all
  three candidate depths; Table 1 audit sums (84,680 ≈ ~84,700).
- **Table 5:** all checked cells integer-consistent; margins vs Retrieve-only are
  +2 tasks / +1 task / tie — passed as *arithmetic*, escalated as *inference*
  (→ REVIEW W4).
- **Diagnostic:** Random-row cells are provably NOT single-draw integer counts
  (60.0, 79.2, 66.2 all off-grid) → seed-averaging that the main text never
  states. Encoded as an expected-negative check; passes as such.

## Failed (2)

| Check | Result |
| --- | --- |
| `abstract-at-least-3p5-per-retriever-reading` | "at least +3.5 points across three different retrievers": per-retriever margins vs strongest baseline are +4.50 / **+3.07** / **+2.97** — 1 of 3 relations hold. The companion average-of-9 check passes at +3.51 with zero slack. → REVIEW **W6** |
| `tbl3-avg-mdaq-rounding` | M-DaQ avg printed 53.5 vs naive 53.556. Resolved by the stats agent as *evidence of care*: averaging exact count fractions gives 53.546 → 53.5. The Avg column was computed from unrounded values. Not a finding. |

## Statistical treatment (from the dimension review, verified)

- **Runs/seeds:** all deterministic rows single-run; Random row seed count
  unstated (cells off the k/n grid prove averaging happened).
- **Significance:** deferred entirely to unprovided Appendix B. Arithmetic bounds
  what it can contain: five of nine per-cell margins vs the strongest baseline are
  1–5 tasks; +5/94 caps at p=0.0625 fully one-sided; ties at two cells. The
  aggregate anchor margins (+29/+28 tasks of 265 on Tool-Use) would survive any
  reasonable test. The nine settings share task sets → correlated.
- **Subgroup resolution:** 52 cultural tasks / 6 regions ≈ 8.7 per region; the
  quoted +6.6pp and +8.4pp region deltas each equal **one task** (14/15−13/15;
  11/12−10/12). Hindi's +12.9pp ≈ 5 tasks of ~38; Swahili's +5.6pp ≈ 2.
- **Fig 3 denominators:** bar rates are impossible as single-retriever rates
  (min denominators sum to 56>52 cultural, 98>94 general) and reconcile exactly
  as three-retriever pooling (cultural 143/156 = Table 3's 47+47+49). Real data,
  unstated aggregation, unstated per-cell n.
- **Router:** 98.5% ≈ 6 errors on 411 queries (n and label provenance unstated);
  corruption sweep properly uncertainty-quantified (1,000 seeds/rate, 95% bands).
- **Uncheckable from provided material:** Appendix B tests; Random draw count;
  per-language/region task counts; Fig 3 baseline series values; prompts and
  decoding parameters; audit detection recall.
