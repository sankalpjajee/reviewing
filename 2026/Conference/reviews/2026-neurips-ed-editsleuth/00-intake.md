# Stage 0 — Intake

- [x] Title, venue, track, submission ID recorded
- [x] Page count vs. track limit
- [x] `artifacts/paper.txt` and `artifacts/paper_clean.txt` produced
- [x] Extracted character count plausible for page count (94,389 chars / 26 pages — normal)
- [x] Figures/tables carrying results identified by page
- [x] Anonymity checked
- [x] Reviewer conflicts of interest: none declared
- [x] Claimed artifact URLs recorded verbatim

## Record

| Field | Value |
| --- | --- |
| Title | EditSleuth: A Dataset of Grounded Reasoning Chains for Image-Edit Forensics |
| Venue | NeurIPS 2026, Datasets & Benchmarks (Evaluations and Datasets) Track |
| Pages | 9 body + references (p10–11) + Appendix A–E (p12–19) + checklist (p20–26) = 26 |
| Artifact URL in paper | **None.** The only two URLs in the full text are `neurips.cc` policy links. No repository, no dataset host, no anonymised link, no supplementary pointer — despite the abstract's "We release the dataset, the deterministic construction pipeline, and pilot training scripts." |
| Extraction quality | Good. Text-native PDF. |
| Anonymity | Author block anonymised. No de-anonymising URLs (a consequence of there being no URLs at all). |

## Where the results live

| Content | Page |
| --- | --- |
| Abstract, introduction, contributions | 1–2 |
| Related work | 2–3 |
| Pipeline, Stages B–E | 3–5 |
| Dataset characterization; **Table 1** (per-category counts × difficulty) | 5–6 |
| Experiments; **Figure 2** (V1/V2 distributions), **Table 2** (threshold calibration) | 7 |
| **Table 3** (pilot fine-tuning results) — the paper's only model-facing result | 8 |
| Limitations, broader impact, conclusion | 9 |
| Appendix A (adapters), B (prior templates), C (sweep tool) | 12–13 |
| Appendix D (per-category chain examples) | 14–17 |
| Appendix E (qualitative mask comparison, Figures 3–4) | 17–19 |
| NeurIPS checklist | 20–26 |

## Notes

- Figures 3 and 4 (Appendix E) carry the *only* comparison of Stage B masks
  against real ground-truth masks, and it is qualitative — nine hand-picked
  examples, no IoU distribution. Flagged for Stage 4.
- Table 3 is the sole result involving a trained model. Everything else
  characterises the construction pipeline's own outputs.
