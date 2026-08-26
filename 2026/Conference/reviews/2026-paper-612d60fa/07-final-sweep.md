# 07 — Final completeness sweep (Stage 4/5, third pass)

Run 2026-08-25 via a 9-agent workflow: four sweepers with lenses **orthogonal** to
the prior dimension review (Sec-4 mechanics as mathematics; unaudited
figures/tables; line-by-line prose; a meta-critic reading our own findings
against the paper), each given the full known-findings digest with a
no-padding/empty-is-valid rule; a three-front verifier per lens (correct? new?
survives rebuttal? — DUPLICATE is a verdict); a synthesizer ranking the delta.

**Outcome: not dry.** 24 raw survivors, merged by the synthesizer to ~13 distinct
items (one candidate was itself caught as a duplicate of REVIEW W8 — the dedup
gate worked in both directions). **Score unchanged: 3/6 Weak Reject, confidence
4.** The sweep's obligations were instead: one new weakness class (W9, the
formalism-incoherence cluster — the pass's best catch), material hardening of
W1/W2/W3, and **five corrections to our own review text** (C1–C5), all applied
to REVIEW.md and 06-official-review-form.md.

## Corrections applied to our own review (C1–C5)

1. **C1 (mandatory):** our Summary misdescribed the mechanism — the cultural
   fusion has a *third* input (the retriever's own relevance score), not two
   views. Fixed in both files.
2. **C2:** "fusion rules specified at formula level" was overstated — the Action
   aggregation, the "basic dimension" class, and C_cul's Retrieval scalar are
   unspecified. Qualified in Clarity and Facilitation text.
3. **C3:** "mechanistically coherent pattern" praise for the budget sweep dropped;
   M-SQE's own curve is non-monotone and peaks at the reporting operating point.
4. **C4:** Soundness gained (f)-extension (synthesis-upgrade halves the margin;
   59.6-vs-59.5 invariance violation) and new (g) (formalism incoherence).
5. **C5:** W1 gained the non-parallel-subsets / supply-inversion / language-roster
   paragraphs.

## Synthesizer's full ranked assessment (verbatim)

All load-bearing numbers and quotes verified against the paper (cap rule ll.248-257; guard ll.324-339; Ccul ll.340-342; Table 3/4 cells; Fig 4 ll.623-656; Fig 6 ll.679-702; Table 2 rosters; Fig 3 bars; abstract ll.11-30; Table 1 sum 84,680). I also checked both review files — one "new" finding is already in the internal REVIEW.md, and one finding forces a correction to the review's own Summary. Synthesis follows.

# SYNTHESIS — Final sweep vs. submitted review (Overall 3/6 Weak Reject, conf 4)

## 1. Bottom line on the score

**No item — individually or jointly — moves the Overall 3/6, any dimension rating, or the confidence.** The core that earned the 3 (real +6.3pp aggregate, sign-robust across backbones, airtight integer bookkeeping) survives every new finding; nothing here flips a verified number. What the sweep changes is the *character* of the case: the review currently praises the paper's specification and robustness in three places that are now factually wrong or overstated (corrections C1-C4 below), and the rebuttal burden grows by a genuinely new defect class — **internal incoherence of the scoring formalism** — that no existing weakness cluster covers. Soundness stays 2/4 (floor for 1 not met: aggregate empirics intact). Facilitation stays 3/4 only because it was already conditioned on the release; its rationale sentence must be corrected. The working file's "genuinely movable to 6-7" framing should be tempered: the discussion now requires a mechanism-spec repair and an operating-point defense, not just new metrics.

**Deduplication rulings (synthesizer):** (a) `fig6-retrieve-only-scorer-dependent-cells` and `fig6-retrieve-only-scorer-invariance-violated` are the same 59.6-vs-59.5 observation at two severities — merged, major framing kept. (b) `theory-cap-classes` merges into `tool-use-guard` per its own verifier note. (c) `supply-success-inversion` + `fig3-absolute-levels` + `rely-on-rhetoric` share one evidence base — merged into one W1/social-impact addition. (d) `cultural-domain-query-language` + `table2-english-roster-asymmetry` merged into one roster item. (e) **`topn-equals-k-degenerate-general-fig4` is NOT new to the review**: REVIEW.md W8 already states "makes Fig 4's General Top-10 point vacuous (K = N = 10, so selection there is a no-op)" — the sweep's only new content is the +5.1pp live-domain quantification (3.4×3/2) and the ZN ⊂ CK notation nit; folded into item R2. The known-findings list simply failed to index W8's clause; do not present this as a discovery.

## 2. Ranked items (material → cosmetic), with slots

### MATERIAL — must reach the authors in the discussion phase

**R1. Scoring-formalism incoherence cluster** = `tool-use-guard-inconsistent-with-cap-arithmetic` (CONFIRMED) + `theory-cap-classes-undefined-and-contradictory` (merged) + `action-score-aggregation-undefined-risk-orientation` (CONFIRMED) + `ccul-z-scoring-underdefined` (minor tail).
The single most important product of the sweep, and the only new *genus* of defect: (i) the paper's own two illustrative "structurally unusable" defects (missing required slot, critical localization failure) score min(500/6, 80) = 80 ≥ 65 under the paper's own cap arithmetic and **pass the Cfunc guard the Fig. 1 flagship narrative says screens them out** — only a Correctness violation (cap 40) is guaranteed out, and Sec 4.4's "language red-line" has no referent in Sec 4.2's taxonomy ("basic dimension" appears once, undefined); (ii) the Action scalar consumed by all three fusion rules and the Table 4 ablation **has no stated aggregation**, and the inversely-oriented Misleading-risk dimension blocks any default reading — which also leaves Cfunc's "M larger than the Action range" unfixed; (iii) Ccul z-scores a per-candidate Retrieval quantity the formulation never defines (retriever returns a bare set), with no instantiation stated for the reimplemented SkillFlow pipeline. Verified: all quotes and arithmetic check.
**Slot:** new Con bullet (position 2, after the equality con) + new lettered item (g) in Soundness 2/4 text + new Question (see 4). Tool-Use carries the +12.9/+5.6 headline, so this is not a pedantic aside. **Material.** Fairness clause from new strength 1: the red-line path does cohere (40 < 65).

**R2. `fig4-msqe-nonmonotonic-and-top3-at-peak` (CONFIRMED).** M-SQE's own curve declines 68.2 → 67.6 → 66.4 beyond N=3 while Retrieve-only rises (52.8 → 59.6 → 63.0); the decline is never narrated (prose attributes large-budget cost solely to context length); **every headline table sits at Top-3, M-SQE's empirical argmax, a choice justified nowhere**; and the Top-10 endpoint of the praised "margin widening" trend is partly mechanical (General N=K=10 no-op — already W8; live-domain margin ≈ +5.1pp). **Slot:** W3 (statistical thinness → add "operating-point selection" paragraph) + correction C3 to the Pros bullet + new Question. **Material** — it bears on every headline number.

**R3. `fig6-retrieve-only-scorer-invariance-violated` (CONFIRMED, merged pair).** Two cells identical by construction (Retrieve-only uses no scorer) print 59.6 vs 59.5; on integer grids these cannot be one run twice, so it is a transcription error or ~1-task run-to-run nondeterminism — **the paper's only measured noise datum, the same size as 5 of the 9 per-cell wins**. **Slot:** W3, as direct empirical support for its thesis; add to Q3 (ask which it is). **Material** for W3's force, cosmetic in isolation.

**R4. `fig6-synthesis-upgrade-contradicts-premise` (WEAKENED, correctly narrowed).** The stronger pool synthesizer lowers *every* cell (incl. the scorer-free baseline) and roughly halves M-SQE's margin (+8.6/+9.0 → +3.5/+4.9); undiscussed; the sentence "ruling out pool-synthesis artifacts ... as explanations for the gains" overstates — sign survives, magnitude does not, and the main results sit at the gain-maximizing weak-synthesizer setting. **Slot:** W3 (joins the existing Fig 6 comparator point in Soundness (f)) + correction C4 + Question. **Material.**

**R5. `theory-view-below-selection-anchors` (WEAKENED, correctly narrowed).** Theory-only (67.0/28.7/59.6) trails Retrieve-only on General (-4.3pp) and Cultural (-19.2pp), exactly ties on Tool-Use, and on Cultural is statistically indistinguishable from Random (59.6 vs 60.0) — inside the band of the query-agnostic baselines the paper calls structurally inadequate; the ablation prose never discloses the at-or-below-anchor placement. **Slot:** W2 (attribution), one paragraph; sharpens the existing 7-of-411 point rather than replacing it; extend Q2. **Material** for W2's argument, not for the score.

**R6. Language-roster incoherence** = `cultural-domain-query-language-unspecified` + `table2-english-roster-asymmetry-unexplained` (both WEAKENED, merged). The Cultural domain — carrier of the cultural-equality headline — **never states what language its 52 queries are in** (Table 2 lists regions where the other rows list languages; the MT layer's "language roster" for its 1,283 MT skills is undefined; "Language fit" is uninterpretable there); and the three domains use three different rosters (en in Tool-Use, absent from General) with no acknowledgment. If cultural queries are English (their stated MT source material is), one of two equality-carrying domains never exercises the multilingual machinery on the query side. **Slot:** W1, new paragraph + new Question (potentially decisive for the cultural half of the framing). **Material.**

**R7. Cross-language comparability cluster** = `supply-success-inversion-nonparallel-language-sets` + `fig3-absolute-levels-contradict-supply-narrative` + `rely-on-rhetoric-vs-absolute-success` (all WEAKENED, merged). Per-language subsets are provably non-parallel (265/7, 94/6, 52/6 non-integer; no common per-language count < 72 reconciles en 45.8 with hi 54.6), so every cross-language level or delta comparison — including "lifts the lowest-resource languages most" — is task-mix-confounded; symptomatically, levels anti-track the audited supply (zero-supply Hindi best in Tool-Use at 54.6; best-supplied-non-English Chinese worst in both panels), unremarked; and Sec 2's "can actually rely on" rests on 41.1% (sw) / 54.6% (hi) absolute success. **Slot:** W1 (extends "baseline per-language values never reported" with "and even with them, subsets are non-parallel") + Social-Impact 2/4 text (the 41.1% point) + extend Q1 to ask for per-language task counts and difficulty-matching evidence. **Material** for W1; the inversion prong alone would be minor.

**R8. `cross-lingual-harm-premise-transferred-not-tested` (WEAKENED, correctly narrowed).** The central harm premise is an untested analogy (Lu et al. QA-evidence → skills, via bare "Skills play exactly this evidentiary role"; hedged "possibly due to" becomes "therefore inherits"), no in-language-vs-cross-language provision experiment exists though the pools make one cheap, and the **abstract asserts the borrowed effects in the paper's own voice** ("degrading accuracy and recall" — recall is not a metric anywhere in the paper). **Slot:** split — the untested premise joins W5 (closed universe / motivating regime never evaluated); the abstract sentence joins the W6-family abstract-accuracy list + Presentation fixes; add one clause to Q2 or a new question (run the in/cross-language provision contrast). **Material** at the framing level.

### MINOR — one-line additions to existing clusters

**R9. `general-domain-source-benchmark-unnamed` (WEAKENED).** "Source tasks are drawn from real, published benchmarks (detailed below)" is fulfilled for Tool-Use and Cultural but not General (a "paradigm" is a method, not a source; 23% of tasks). Slot: W5(i)/(ii), one sentence — it pre-empts the natural rebuttal to the closed-universe con. Minor but pointed.

**R10. `skillflow-reimplementation-unvalidated` (CONFIRMED).** Fidelity asserted by adverb only; the same author-built reimplementation is both strongest retriever and the +3.5 headline comparator; no reproduction check reported or referenced. Slot: W3 one-liner + add to Q5 or Q3 (report a calibration against Li et al.'s published numbers). Minor.

**R11. `source-task-selection-unauditable` (WEAKENED).** 52→7 language restriction with no stated criterion; no entered-vs-survived attrition counts for the three-stage filter. Slot: W5, one sentence + one ask in Q3/Q4. Minor (partially overlaps known circularity findings — say so if posted).

**R12. `scorer-side-blinding-unspecified` (WEAKENED).** "Judged on its own content alone" is asserted; anonymization is operationalized only at solver hand-off; scorer-side blinding unverifiable (Appendix F). Slot: W5, one sentence + half-line in Q4/Q5. Minor.

**R13. `leakage-rule-incompatible-with-tooluse-answer-keys` (WEAKENED to minor, correctly).** "Share no content-bearing terms with the answer key" cannot be literal for Tool-Use gold calls with language-invariant slot values; "content-bearing" undefined. Slot: fold into Q4's leakage/checker ask; W7 half-line. Minor.

### COSMETIC — include only if the discussion note has room

**R14. `fig1-caption-body-failure-mode-mismatch` (CONFIRMED).** Caption shows a language-independent slot-omission failure; body cites it as the cross-lingual mismatch illustration. Slot: Presentation list one-liner. Cosmetic — but note it rhetorically supports W5(iii): the intro's only illustration shows M-SQE fixing the one problem a post-retrieval scorer *can* fix. (Also now partially undercut by R1: the stated cap arithmetic does not actually screen out the caption's defect.)

**R15. `table1-rows-exhaust-total-implicit-zero-other-languages` (WEAKENED).** Seven listed languages absorb ~84,680 of ~84,700; either an undefended <~1%-for-all-other-languages claim or an unexplained near-exact match. Slot: W7 audit-caveat bullet, one clause in the audit question. Cosmetic.

**R16. `topn-equals-k-degenerate-general-fig4`.** Already in REVIEW.md W8 (dropped from the submitted form). New content folded into R2. Do not report as new.

## 3. Corrections to the existing review (precise text changes)

These are the sweep's sharpest obligations — the review currently asserts things the new findings falsify.

**C1 — Summary, BOTH files (from `two-view-framing-omits-cultural-retrieval-term`, CONFIRMED).** The review's own summary replicates the paper's misdescription. 06-official-review-form.md Summary: "a prompted domain router combines the two scores via one of three domain-specific fusion rules (... equal z-scored fusion for cultural tasks)" → change the cultural clause to "**equal z-scored fusion of Theory, Action, and the retriever's own relevance score for cultural tasks**" and "combines the two scores" → "combines these scores". Same edit in REVIEW.md's Summary ("combines them through ... equal z-scored fusion for cultural tasks"). The paper-side finding (every framing statement says two views; Ccul has an equal-weight third input, in the domain where Retrieve-only already reaches 78.8-90.4) goes to the W6/W8 claim-accuracy list. A reviewer misdescribing the mechanism in discussion is not survivable — this correction is mandatory regardless of what else is posted.

**C2 — Review field, Clarity sentence + Facilitation 3/4 rationale (from R1).** "the fusion rules are specified at formula level with the actual constants" (Review field) and "the main text specifies the full decision rule at formula level with actual constants" (Facilitation) are both now false as stated. Append to each: "— though three of their inputs are not: the Action-score aggregation (six 0-100 dimensions, one inversely oriented, with no stated combination rule), the cap rule's 'basic dimension' class (undefined; Sec 4.4's 'language red-line' has no referent), and the cultural rule's per-candidate Retrieval score." Internal strengths ledger: retract/qualify "Scoring math fully specified at formula level."

**C3 — Pros bullet 3 (from R2 + R16).** "budget sweep with a mechanistically coherent pattern (margin widens as budget tightens, +3.4pp at Top-10 → +9.7pp at Top-1)" must lose "mechanistically coherent" and gain: "though M-SQE's own curve is non-monotone (peaks at the Top-3 used for every headline table, declining thereafter — undiscussed), and the Top-10 endpoint averages in a General cell where N = K makes selection a no-op." Internal ledger: qualify the corresponding known strength.

**C4 — Soundness (f) / robustness praise (from R4).** After the existing Fig 6 comparator sentence, add: "(g) the same figure's pool-synthesis control moves in an unexplained direction — the stronger synthesizer lowers every cell including the scorer-free baseline and halves M-SQE's margin — so 'ruling out pool-synthesis artifacts' overstates what was shown: the sign is robust, the headline magnitude is not."

**C5 — W1 sentence (from R7).** "whether the spread shrank versus Retrieve-only cannot be determined because baseline per-language values are never reported as numbers" → append "— and even with them, the per-language subsets are provably non-parallel in size and content, so cross-language levels and deltas are task-mix-confounded (symptomatically, levels anti-track the audited supply: zero-supply Hindi is the best Tool-Use language, best-supplied-non-English Chinese the worst in both panels)."

## 4. New strengths — disposition

- **SF-identity invariant** (Retrieve-only(SF) = SkillFlow-selector(SF) in 3/3 cells, verified 74.5/37.4/90.4 both rows): add one clause to the Quality paragraph's verification list. Genuine, cosmetic-positive; further evidence the tables are real data.
- **Red-line/guard interlock** (40 < 65 coheres): do not report standalone; use as the fairness clause inside R1 ("the one path that must cohere does").

## 5. Recommended discussion-phase note (content, in posting order)

1. C1's mechanism correction (reviewer-side, quietly folded into the note's method recap).
2. R1 as a new numbered concern with the 80-vs-65 recomputation and a direct ask: define "basic dimension", reconcile "language red-line" with Sec 4.2, state the Action aggregation (incl. Misleading-risk orientation) and Ccul's Retrieval scalar per retriever.
3. R2+R4+R3 as one "operating point and stability" concern: justify Top-3; report strongest-baseline margins at N=5/10; explain 59.6 vs 59.5 (typo or rerun — and if rerun, report variance); explain the synthesis-upgrade absolute drops and reword "ruling out pool-synthesis artifacts."
4. R6 as a direct factual question: what language are the 52 Cultural queries and the Cultural MT layer in, and why do the three rosters differ?
5. R7 folded into existing Q1 (add: per-language task counts, difficulty-matching evidence, and the supply-inversion explanation); R5 folded into existing Q2 (add: report Theory-only against the anchors); R8's abstract sentence added to the presentation-fix list ("recall" is not measured); R9-R13 as single-sentence asks where space permits.

**Blunt summary:** R1 is the sweep's one finding that would have restructured a section of the review had it surfaced earlier; R2-R8 materially harden existing clusters and add five concrete author burdens; R9-R13 are one-liners; R14-R16 are cosmetic or already known. Score, dimensions, and confidence all stand. C1-C5 are mandatory edits to the review's own text before any discussion post, because three of them currently praise exactly what the new findings break.
