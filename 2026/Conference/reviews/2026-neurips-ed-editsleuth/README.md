# EditSleuth — NeurIPS 2026 D&B (ED)

**[→ REVIEW.md](REVIEW.md)** — the deliverable.

**Recommendation: 2/6 Reject** (confidence 4/5), with a separate research-integrity
finding referred to the AC and excluded from the score.

## Contents

| File | What it holds |
| --- | --- |
| [`REVIEW.md`](REVIEW.md) | The review: summary, 6 strengths, 13 weaknesses, 5 questions, rating, integrity note, working notes |
| [`findings.json`](findings.json) | 64 verified findings + 29 strengths, machine-readable ([schema](../../workflow/templates/findings.schema.json)) |
| [`00-intake.md`](00-intake.md) | Stage 0 — intake record |
| [`01-integrity.md`](01-integrity.md) | Stage 1 — hidden-text finding, technique analysis, judgement |
| [`03-stats.md`](03-stats.md) | Stage 3 — numeric audit results and statistical assessment |
| [`artifacts/`](artifacts/) | Extracted text, `integrity.json`, `checks.json`, `numeric_audit.json` |

## How this was produced

Via [`../../workflow/`](../../workflow/). Reproduce stages 0–1 with:

```bash
cd 2026/Conference
./workflow/scripts/run_review.sh <submission>.pdf 2026-neurips-ed-editsleuth
python3 workflow/scripts/audit_numbers.py \
    reviews/2026-neurips-ed-editsleuth/artifacts/checks.json
```

Stage 1 raised an integrity flag (exit 2) before any content was read. Stage 3
machine-checked 24 numeric relations: **19 passed, 5 failed**. Stages 4–5 ran five
independent dimension reviewers followed by an adversarial refutation pass over every
finding: **63 of ~100 survived** — 22 confirmed outright, 41 weakened and rewritten to
the version that withstands rebuttal, the remainder dropped.

## The three things that decided it

1. **§5.4's headline is arithmetically false.** The paper's own conditional numbers
   put chain-target behind label-only on two of three fields and ahead on one, and
   the sentence directly after them says "two of three." The abstract escalates it
   to an unqualified "matches." Caught by `audit_numbers.py`, confirmed under
   adversarial verification against three attempted rebuttals.
2. **The one field it wins on is uninterpretable, and no baseline exists.** Difficulty
   bins are dataset-internal percentiles, so train and eval labels denote different
   quantities; the baseline there scores 33.1% against a construction-guaranteed
   chance of 33.3%. On category, a constant `other` predictor scores 44.5% —
   beating both trained arms. No baseline of any kind is reported.
3. **The artifact cannot be reached.** Four present-tense release claims; zero
   artifact pointers in 26 pages; no licence named for either upstream corpus or for
   the release itself. On a dataset track, the artifact is the contribution.

## Integrity finding (separate from the score)

The PDF carries a hidden instruction to an automated reviewer on pages 2 and 26,
built by drawing each character in its own single-use embedded font that renders
blank while still yielding the letter to a text extractor. Assessed as targeted.
It was not acted on. Detail in [`01-integrity.md`](01-integrity.md); it is reported
in `REVIEW.md` in its own section and deliberately kept out of the rating, so the
paper's merits stand on their own.
