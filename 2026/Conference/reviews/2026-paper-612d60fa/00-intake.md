# Stage 0 — Intake

- [x] Title, venue, track recorded
- [x] Page count vs. track limit
- [x] `artifacts/paper.txt` and `artifacts/paper_clean.txt` produced
- [x] Extracted character count plausible (45,431 chars / 9 pages — dense two-column, normal)
- [x] Figures/tables carrying results identified by page
- [x] Anonymity checked
- [x] Reviewer conflicts of interest: none
- [x] Claimed artifact pointers recorded verbatim

## Record

| Field | Value |
| --- | --- |
| Title | M-SQE: Multilingual Skill Quality Estimation for Enhancing Language Equality in Agentic Skill Use |
| Venue | Anonymous AAAI-style main-track submission (7pp content + 2pp references, two-column, mandatory social-impact section) |
| Pages | 9 total: content p1–7, references p8–9. **Appendices A–I are in Supplementary Material (footnote 1) and were NOT provided with this file.** |
| Artifact pointer | Footnote 1: "Code, data and appendices are in Supplementary Material" — a concrete pointer to the submission's supplementary, which this review does not have. Distinct from claiming a release with no pointer. |
| Extraction quality | Good; text-native. Figure bar labels survive only as bare number lists (Fig 3 especially) — series attribution from extraction is unreliable and flagged to all reviewers. |
| Upload metadata | Claimed 34 pages; actual PDF is 9 (verified with pypdf). Metadata error, noted and disregarded. |
| Integrity scan | **Clean** — exit 0, no hidden spans of any confidence, no injection-phrase hits. |

## Where the results live

| Content | Page |
| --- | --- |
| Abstract, intro, **Table 1** (ecosystem audit: ~84,700 entries, per-language counts) | 1 |
| Social impact (Sec 2); related work (Sec 3) | 2 |
| Framework (Sec 4): Theory/Action views, unified scoring, domain router, three fusion rules | 3–4 |
| **Table 2** (eval setup: 94/265/52 tasks, three-layer pools 1,750/2,299/5,285, depths 10/20/50) | 5 |
| **Fig 3** (per-region/per-language bars), **Table 3** (main results, 10 methods × 9 settings), **Table 4** (view ablation) | 6 |
| **Fig 4** (budget sweep), **Fig 5** (router corruption), **Fig 6** (backbone grid), **Table 5** (trajectory fine-tuning) | 7 |
| References | 8–9 |

## Notes

- The only learning-free headline: Table 3 — M-SQE 69.1% avg vs strongest baseline SkillFlow 65.6%.
- Significance analyses, audit protocol, rubrics, perturbations, checker criteria, limitations: all deferred
  to appendices A–I that are not in this file. Load-bearing but unverifiable-from-provided-material — to be
  treated as such, not as absent.
- Evaluation sets are small (94 / 265 / 52 tasks); per-region and per-language breakdowns slice these
  further. Flagged to the stats reviewer.
