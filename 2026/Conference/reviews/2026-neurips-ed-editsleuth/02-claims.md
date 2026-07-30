# Stage 2 — Claim extraction

Filled in from the abstract, Contributions list, and conclusion before reading §5.
Verdicts added during Stage 4/5.

- [x] Every empirical sentence in the abstract is a row below
- [x] Every item in the contributions list is a row below
- [x] Every claim in the conclusion is a row below
- [x] Each row names the section that is supposed to support it
- [x] Quantifier recorded exactly
- [x] Comparative claims record the comparison class

| # | Claim (paraphrased; quantifier verbatim) | Where claimed | Where supported | Verdict |
| --- | --- | --- | --- | --- |
| 1 | 257,725 image-edit triplets, each with edited image, source, binary mask, 12-class label, difficulty score, six-step chain | Abstract, §4.1 | Table 1 | **supported** — counts sum exactly |
| 2 | Chains generated "deterministically", each statement "tied to a specific computable source of evidence" | Abstract, §3.4 | §3.4, App. D | **supported** — back-solving *s*<sub>compact</sub> across all 12 exemplars gives values monotone in the Step-3 descriptor |
| 3 | Naive four-component difficulty "suffers from a rank-2 correlation collapse" | Abstract, §1, Contrib. (iii), §3.2, §5.1, §7 | §5.1 | **partial** — pairwise \|*r*\| given; no eigenvalue/singular-value evidence anywhere → W10 |
| 4 | Three-component formulation "substantially increases score dispersion" on both corpora | Abstract, §5.1 | §5.1 | **partial** — arithmetic exact, but σ is not scale-invariant and percentile binning makes it downstream-irrelevant → W10 |
| 5 | Difficulty "varies meaningfully within most edit categories", so "not a proxy for edit type" | Abstract, §4.3 | Table 1 | **supported** as stated — but never validated against any external referent of difficulty → W9 |
| 6 | Chain-as-target "matches a label-only baseline on classification accuracy among parseable answers" | Abstract | §5.4, Table 3 | **unsupported** — 1 of 3 fields, not 3 → **W1** |
| 7 | Chain-target "matches or exceeds label-only on **two of three** fields once parseability is controlled for" | §5.4 Results | Table 3 | **unsupported** — 1 of 3 → **W1** |
| 8 | Chain-target matches label-only "on category, spatial, and difficulty classification, indicating no loss in underlying prediction quality" | §5.4 Interpretation | Table 3 | **unsupported** — strengthens an already-wrong claim to all three → **W1** |
| 9 | "additionally yielding grounded explanatory prose that label-only supervision cannot produce" | Abstract, §5.4 | §5.4 | **unsupported** — §6 says the model does not compute the fields; "all generations include evidence" falsified by 67.4%/68.6% recall → **W12** |
| 10 | "We release the dataset, the deterministic construction pipeline, and pilot training scripts" | Abstract, §6, §7, Checklist 4/5/13 | — | **unsupported** — no artifact pointer in 26 pages → **W4** |
| 11 | Contrib. (i): pipeline re-purposing editing triplets as forensic training data | §1 | §3 | **supported** — and the best idea in the paper |
| 12 | Contrib. (ii): 12-category taxonomy "adapted from the Pico-Banana grouping" with three changes | §1, §3.3 | §3.3 | **partial** — two of the three "changes" already exist upstream; the two real deltas go unstated → W13 |
| 13 | Contrib. (iv): pilot "validates chain-as-target supervision at the classification level" | §1 | §5.4 | **unsupported** — rests entirely on claims 6–8 → **W1** |
| 14 | Threshold offsets track combined-diff means, so calibration "mainly corrects max-pool inflation" | Abstract, §5.2, §7 | Table 2 | **partial** — arithmetic exact, but on 2 data points at 0.02 quantisation; verb hardens from "suggesting" (§5.2) to "showing" (§7) |
| 15 | "no faithfulness violations" found in the qualitative audit | §5.3 | §5.3 | **unsupported** — non-falsifiable as framed; ≥3 of 12 showcase chains misassigned → **W6** |
| 16 | "first dataset to combine edited-image triplets with auditable reasoning-chain supervision for forensic VLM training" | §2 Positioning | §2 | **unsupported** — refuted by FakeShield/LEGION/SIDA/FakeXplain in the paper's own bibliography → **W7** |
| 17 | Multi-signal stack improves MagicBrush IoU by 1.3 points over best two-signal subset | §3.1 | §3.1 | **partial** — the one properly-specified test in the paper, but relative-only and on 0.2% of the release → **W5** |
| 18 | 30.4% global routing target matches the share of whole-image edit labels | §5.2 | Table 1 | **unsupported** — the four named categories sum to 61.4% → **W8** |
| 19 | Pico-Banana "covers all 11 non-`other` categories" | §4.1 | Table 1 | **unsupported** — covers 10; Table 1's own caption says so → W13 |

## Note

Writing this table before reading §5 is what made **W1** unmissable. Rows 6–8 are the
same underlying claim at three escalating strengths — abstract, Results,
Interpretation — and seeing them side by side before opening Table 3 is what framed
the arithmetic check that `audit_numbers.py` then failed. Read in the other order,
the experiments quietly redefine the promise and the escalation is invisible.
