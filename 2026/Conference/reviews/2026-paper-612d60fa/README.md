# M-SQE — AAAI-style main track

**[→ REVIEW.md](REVIEW.md)** — the deliverable.

**Recommendation: 5/10 borderline reject** (confidence 4/5). Integrity scan
**clean**. Genuinely movable in rebuttal — the decisive questions are answerable
from the authors' existing logs plus one cheap experiment.

## Contents

| File | What it holds |
| --- | --- |
| [`REVIEW.md`](REVIEW.md) | The review: summary, 7 strengths, 8 weakness clusters, 4 questions, rating, working notes |
| [`findings.json`](findings.json) | 42 verified findings + 32 strengths, machine-readable ([schema](../../workflow/templates/findings.schema.json)) |
| [`00-intake.md`](00-intake.md) | Stage 0 — intake record (incl. the appendices-in-supplementary caveat) |
| [`02-claims.md`](02-claims.md) | Stage 2 — 17 claims tabled before reading results, with verdicts |
| [`03-stats.md`](03-stats.md) | Stage 3 — numeric audit (27 checks: 25 pass) and statistical assessment |
| [`artifacts/`](artifacts/) | `integrity.json`, `checks.json`, `numeric_audit.json` (extracted text not committed — confidential) |

## How this was produced

Via [`../../workflow/`](../../workflow/): clean integrity gate → claims table
before results → machine numeric audit → 5 dimension reviewers → adversarial
verification of every finding → AC synthesis. 11 agents, ~874K tokens. **42
findings survived** (23 confirmed, 19 weakened); 32 strengths recorded.

## The shape of the verdict

The execution is unusually strong — all 45 deterministic table cells are
integer-consistent with the stated task counts, every cross-figure value
reconciles, the confound controls are real, and the two motivating citations were
verified against their sources. What holds it under the bar is the claim layer:

1. **The equality claim (title/abstract) is never measured.** No gap or dispersion
   metric exists in the paper; M-SQE's own per-language numbers retain a 27–43pp
   spread with Chinese and Korean now lowest — consistent with inequality
   relocated, not narrowed.
2. **The gain is never attributed to the novel machinery.** No rubric-free
   LLM-rerank baseline; the paper's own Action-only ablation captures all but
   7 tasks of 411 of the full framework's gain.
3. **The trajectory-generalization contribution rests on +2/+1/0 tasks** across
   the three domains — beyond statistical rescue at those margins.

Caveat threaded through the review: appendices A–I live in supplementary material
that was not provided; findings were phrased as "unverifiable from provided
material" rather than "missing," and the rating accounts for it.
