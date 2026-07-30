# Stage 3 — Numeric and statistical audit

```bash
python3 workflow/scripts/audit_numbers.py \
    reviews/2026-neurips-ed-editsleuth/artifacts/checks.json \
    --json reviews/2026-neurips-ed-editsleuth/artifacts/numeric_audit.json
# 19 passed, 5 failed, 0 errored — exit 1
```

24 relations transcribed from the paper. Tolerances set generously enough to absorb
the paper's own rounding, so every FAIL below is a real disagreement.

## Arithmetic

- [x] Table totals equal the sum of their parts
- [x] Percentages recompute from the counts
- [x] Every number the prose derives from a table is checked
- [x] Every counting claim checked with `count_true`, not read
- [x] Appendix worked examples checked against body thresholds
- [x] Tolerances calibrated to the paper's rounding

### Passed (19)

Table 1 sums exactly to 257,725 (Pico-Banana) and 528 (MagicBrush). All percentage
cells round correctly. §4.3's tertile counts sum to the total. Both σ-widening
figures reproduce (+55.7% and +94.1%). All four §5.2 threshold/cdm.mean offsets match
Table 2 to the digit. **All six conditional accuracies in §5.4 reproduce exactly**
from Table 3's accuracy ÷ extraction-recall columns — the paper's arithmetic is
right.

### Failed (5)

| Check | Result |
| --- | --- |
| `sec54-two-of-three-claim` | Paper says chain-target "matches or exceeds label-only on **two of three** fields." Recomputed: **1 of 3** holds (category 33.4 ≱ 39.7; spatial 37.2 ≱ 42.2; bin 40.8 ≥ 33.1), even with a full percentage point of slack granted to "matches". → **W1** |
| `abstract-matches-baseline` | Abstract's unqualified "matches a label-only baseline" reads as all three fields; 1 of 3 holds. → **W1** |
| `appD-difficulty-vs-tertile-{object-removal, other, scene}` | Three Appendix D examples binned *medium* with scores 0.21 / 0.16 / 0.19, below §4.3's stated 0.406 easy/medium cutoff. |

The control case `appD-difficulty-photometric-consistent` (score 0.48, a
Pico-Banana-labelled example) **passes**, which is what made the three failures
diagnostic rather than noise: the anomaly tracks classification *source*, not the
scorer.

### Note on the three Appendix D failures — refuted as filed, escalated as rewritten

Stage 5 **refuted** the naive reading. §3.2 bins by dataset-internal percentiles, so
the rule-classified (MagicBrush) examples are binned against MagicBrush's own cutoffs,
which the paper never reports. Resolving provenance, the three Pico-Banana examples
land exactly where the stated cutoffs put them (0.48 → medium, 0.51 → hard, 0.56 →
hard) and the nine MagicBrush examples are strictly monotone in bin (easy
0.10/0.11/0.13, medium 0.16/0.19/0.21, hard 0.23/0.24/0.28). The paper is not wrong
here; it is unverifiable.

The correct finding is stronger and is **W2**: every MagicBrush example, *including
all three labelled `hard`*, sits below Pico-Banana's easy/medium cutoff. Training and
evaluation difficulty labels are therefore not the same function, which is what makes
Table 3's difficulty-bin column uninterpretable — and that column is the sole field
on which the paper claims chain-target beats label-only.

*The machine check earned its keep by surfacing an anomaly whose obvious explanation
was wrong and whose real explanation was worse.*

## Statistical treatment

- [x] **Runs / seeds:** one run. No seed reported anywhere in 26 pages.
- [x] **Error bars:** none on Table 2 or Table 3. The paper's only interval is
      §3.1's mask bootstrap (`p < 10⁻⁴`, 95% CI [0.0085, 0.0164]) — correctly
      specified, but supporting no abstract-level claim. Checklist item 7 answers
      [Yes] citing "confidence intervals". → **W11**
- [x] **Significance tests:** none where comparisons are asserted. Running the tests
      the paper omits on Table 3: category *z* = −1.86 (*p* = 0.063), spatial
      *z* = −1.57 (*p* = 0.118), bin *z* = +2.36 (*p* = 0.018).
- [x] **Chance performance:** computed independently. Difficulty bin = **33.3%** by
      construction (tertiles); label-only scores 33.1%, i.e. exactly chance.
      Category: a constant `other` predictor scores **44.5%**, beating both trained
      arms. Ceiling on category = 55.5%. None reported. → **W2**, **W3**
- [x] **Scale-invariance:** σ is not scale-free; multiplying V1 by 1.557 reproduces
      the +55% headline with zero change to any tertile assignment. V1's mean is
      never reported, so no CV can be computed. → **W10**
- [x] **Quantisation:** MagicBrush σ given to 2 s.f., so "+94%" spans +90% to +98%.
      τ values sit on a 0.02 grid, five times coarser than the 0.004/0.005
      agreements claimed in §5.2.
- [x] **Denominators:** stated for the accuracy columns; **not** for the joint row
      (1.9% / 3.4%), which has no extraction column, so the parseability control
      cannot be applied to it.
- [x] **Metric definitions:** extraction recall is defined ambiguously enough that
      label-only's 93.6 / 100 / 100 pattern is unexplained, and all six conditional
      accuracies divide by it.

## Uncheckable from the text

Recorded as findings rather than left silent: MagicBrush's tertile cutoffs; V1's
mean and its four component weights; absolute Stage B IoU; the identity of the "best
two-signal subset"; per-stack τ in the §3.1 comparison; the `s_instr` formula; the
LPIPS backbone; the morphological kernel; all training hyperparameters and decoding
settings; counts for the `ambiguous` and `alignment_failed` scope values.
