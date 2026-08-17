# Conference

Conference material for 2026.

## Contents

- [`workflow/`](workflow/) — the paper-review pipeline: stage definitions,
  rubrics, per-stage checklists, templates, and the scripts that automate
  extraction, integrity scanning, and numeric auditing. Start at
  [`workflow/README.md`](workflow/README.md); the stage-by-stage spec is in
  [`workflow/PIPELINE.md`](workflow/PIPELINE.md).
- [`reviews/`](reviews/) — one directory per submission, containing the completed
  checklists, extracted artifacts, verified findings, and the final review.

## Reviews

| Submission | Venue | Status |
| --- | --- | --- |
| [EditSleuth: A Dataset of Grounded Reasoning Chains for Image-Edit Forensics](reviews/2026-neurips-ed-editsleuth/) | NeurIPS 2026 D&B (ED) | Complete — integrity flag raised |
| [M-SQE: Multilingual Skill Quality Estimation for Enhancing Language Equality in Agentic Skill Use](reviews/2026-paper-612d60fa/) | AAAI-style main track | Complete — 5/10 borderline reject, integrity clean |

## Quick start

```bash
./workflow/scripts/run_review.sh path/to/submission.pdf <slug>
```
