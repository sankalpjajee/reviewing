# Review — M-SQE: Multilingual Skill Quality Estimation for Enhancing Language Equality in Agentic Skill Use

**Venue:** Anonymous AAAI-style main-track submission · **Date:** 2026-08-17

> **Process notes.** (1) The PDF's integrity scan is **clean** — no hidden text, no
> instruction-like content, at any confidence level. (2) The paper's appendices A–I
> and code/data are in Supplementary Material (footnote 1) that was **not provided**
> with the reviewed file. Claims deferred there are treated as *unverifiable from
> the provided material*, not as absent — several findings below may dissolve when
> the supplementary is consulted, and the rating accounts for that.

---

## Summary

M-SQE is a post-retrieval selection layer for agent skills in multilingual settings.
Given a retriever's candidate set, an LLM scores each candidate under two rubrics —
a query-independent **Theory view** (correctness, completeness, executability,
cross-lingual faithfulness, localization, context efficiency) and a query-grounded
**Action view** (applicability, procedure/constraint/output match, language fit,
misleading risk) — and a domain router combines them through one of three
domain-specific fusion rules (convex mix for general tasks, a Theory≥65 gate for
tool use, equal z-scored fusion for cultural tasks). The paper also contributes an
audit of ~84,700 community skill entries (finding zero in-language skill bodies for
Swahili and Hindi), a three-domain multilingual evaluation (94 general / 265
tool-use / 52 cultural tasks) over three-layer skill pools mixing ecological-style,
machine-translated, and self-generated skills, and a pledged release of all of it.
Headline result: 69.1% average task success over nine domain×retriever settings,
+3.5pp over the strongest baseline (SkillFlow) and +6.3pp over Retrieve-only, with
the largest gains reported on Hindi and Swahili.

The execution at the data level is unusually strong, and the aggregate result is
real. The paper's problem is its claim layer: the equality framing in the title,
abstract, and social-impact section is never measured, and the attribution of the
gain to the novel machinery is never isolated.

---

## Strengths

These were verified adversarially, not taken on trust.

1. **The tabulation is airtight — a property we verified exhaustively.** All ten
   Table 3 row averages recompute exactly; **all 102 deterministic cells across
   Tables 3, 4, and 5 (81 + 9 + 12; Table 3's seed-averaged Random row excluded)
   are consistent with integer success counts over the stated task totals**
   (e.g. 39.6 = 105/265, 94.2 = 49/52, 38.30 = 36/94). One apparent
   rounding anomaly (M-DaQ's 53.5 vs a naive 53.556) turns out to be evidence of
   care: averaging the exact count fractions gives 53.546, so the Avg column was
   computed from unrounded values. Cross-artifact checks all pass: Fig 4's Top-3
   point, Fig 6's main cell, Fig 5's floor and star, the Prompt-only anchors, pool
   sums, and the candidate-depth rule all reconcile with Table 3 and Table 2.

2. **Fig 3 plots real data.** Its bar labels are arithmetically impossible as
   single-retriever rates but reconcile *exactly* with Table 3's implied integer
   counts as the M-SQE series pooled over the three retrievers (cultural: 143/156).
   The figure survives forensic recomputation; what is missing is the stated
   aggregation (see W1).

3. **Real confound controls, honestly reported.** The scorer=solver worry is
   directly probed: Fig 6's off-diagonal cells (scorer≠solver) stay positive
   (+9.0, +6.4pp) and are not smaller than matched cells. The router-corruption
   sweep is the one place uncertainty is properly quantified (1,000 seeds per rate,
   empirical 95% bands) and it *limits the authors' own component* — the text
   concedes "routing sharpens the margin, and the two views hold the floor." The
   solver is blinded ("anonymized skill bodies ... without any gold answer or
   checker metadata") and the Prompt-only anchor verifies the tasks need skills.

4. **The motivating citations check out externally.** The load-bearing 70.1%
   adoption-without-gain statistic attributed to SkillFlow, and the
   curated-helps/self-generated-hurts premise attributed to SkillsBench, were both
   verified against the cited arXiv sources and are accurately reported.

5. **Two genuinely novel artifacts.** The multilingual skill-supply audit (the
   citable fact that Swahili and Hindi have zero in-language skill bodies among
   ~84,700 entries, pending Appendix A's protocol) and the three-layer
   mixed-provenance pool design have no precedent in the cited or adjacent
   literature that our search found.

6. **Honest lineage and adversarial baseline reuse.** The rubric's basis (MIDB's
   taxonomy) is named, with the new dimensions identified; SkillFlow is called
   state-of-the-art, reimplemented as both retriever and selector, and beaten on
   top of its own pipeline. The ablation volunteers that the Action view carries
   most of the gain rather than overselling the two-view story.

7. **Wording is mostly calibrated.** "First or tied-first" is accurate (the two
   ties exist and the phrase covers them); "+6.3pp over Retrieve-only ... on
   average" is exactly right; Fig 6's "+3.5–9.0pp" range matches its six deltas.
   The exceptions are cataloged below.

---

## Weaknesses

Ordered by decision impact. Tagged **wrong** / **under-specified** / **debatable**.

### W1. The equality claim — the paper's title, abstract, and social thesis — is never measured. **[under-specified · major]**

"Narrows the language inequality" (contribution 2) and "moving agentic skill use
toward linguistic and cultural equality" (abstract, title) are claims about the
**cross-language gap**. No dispersion, variance, min-language, or gap-to-baseline
metric appears anywhere in the paper. The only evidence is absolute gains on two
languages in one domain.

The paper's own numbers leave the gap large: Fig 3's M-SQE series (verified as
three-retriever pooling) spans **27.2 (zh) to 54.6 (hi)** in Tool-Use and **56.9
(zh) to 100.0 (ko)** in General — a 27–43pp residual spread, with the two
*highest*-resource non-English languages now at the bottom. That pattern is
consistent with inequality being *relocated* rather than narrowed; whether the
spread shrank versus Retrieve-only cannot be determined because baseline
per-language values are never reported as numbers.

Compounding this: the headline **+12.9pp/+5.6pp deltas never state their
comparator** (vs Retrieve-only? vs Random?); "lifts the lowest-resource languages
*most*" is unverifiable because no other language's delta is reported; and the
abstract states the deltas unscoped while Sec 2/5.5 scope them to Tool-Use — in
General, Fig 3 shows Hindi *second-lowest* of six languages. This is likely
computable from the authors' existing logs, which is why it is under-specified
rather than wrong — but as submitted, the paper's distinctive selling point is its
least supported claim.

### W2. The gain is never attributed to the novel machinery. **[under-specified · major]**

M-SQE *is* Gemini-3-Flash prompted with a rubric — yet no baseline is the same LLM
prompted with a generic relevance/usefulness reranking prompt over the same
candidates. So "the two-view rubric helps" is never separated from "any strong LLM
judging candidates helps." The closest proxy the paper itself provides, Table 4's
**Action-only**, already gains +9.8pp (Tool) and +9.7pp (Cultural) over
Retrieve-only; everything distinctively novel beyond it — the Theory view, the
router, the three fusion rules — adds **3+3+1 = 7 tasks out of 411** (+2.1pp mean),
and the ablation runs in only one of nine settings. Meanwhile three of the six
"strong external baselines" (DEITA, M-DaQ, JQL) are query-agnostic by design and
lose structurally (three cultural cells below Random; one at the no-skill floor),
so the effective comparison set is narrower than Table 3 suggests.

### W3. Per-setting superiority is statistically thin, and its defense lives in unprovided Appendix B. **[under-specified · major]**

Of the nine "first or tied-first" settings, five margins over the strongest
baseline are 1–5 tasks and two are exact ties (never individually acknowledged in
prose). Arithmetic alone guarantees most cells cannot individually reach p<0.05
under any paired test — +5/94 caps at p=0.0625 even with fully one-sided
discordance; +1 or +2 of 52 can never get there. The nine settings also reuse the
same 411 tasks across retrievers: correlated repetitions, not nine confirmations.
All deterministic rows are single runs; the Random row's draw count is unstated
(its cells are provably not single-draw integer counts). **In fairness:** the
aggregate anchor comparison is robust — the Tool-Use margins over Retrieve-only
are +29 and +28 tasks of 265 and would clearly survive testing. The defensible
claim is aggregate superiority plus one strong domain, not nine wins.

Two aggravating details. Task-weighted (micro) rather than domain-averaged, the
per-retriever margins over SkillFlow are +5.4 / **+1.7** / +2.9pp — the Neural
margin is 7 tasks of 411. And Fig 6's claim of "ruling out ... scorer or solver
bias as explanations for the gains" measures every backbone-swap margin against
**Retrieve-only**, not the strongest baseline; SkillFlow averages ~2.8pp above
Retrieve-only, so the +3.5 and +5.0 Fig 6 cells leave the strongest-baseline
margin potentially under ~1–2pp in swapped configurations — re-established
nowhere. The cultural cells (86.5–94.2%) also sit near ceiling, compressing all
margins in that domain.

### W4. The trajectory-generalization contribution rests on 3 net tasks of 411. **[wrong (overreach) · major]**

Table 5's margins over Retrieve-only are exactly **+2 tasks (General), +1 task
(Tool), and a tie (Cultural, 26/52 both — unmentioned in prose)**, from a single
fine-tuning run with no variance. Margins of 2/1/0 can never reach significance
under any paired test; no appendix can mathematically rescue this. The conclusion
drawn — "the signal that picks better skills to read also picks better skills to
learn from, extending M-SQE ... to a beneficial training-data constructor" — is a
named contribution supported at noise level. The data supports "no worse than
Retrieve-only." Notably, Cultural, where the *inference-time* gain is largest
(+11.6pp), shows zero training-time benefit.

### W5. The evaluation universe is closed and self-referential. **[debatable · major, as a validated risk cluster]**

Four items, each individually defensible, jointly capping generalization: (i) all
three pool layers pass through author construction — the "ecological-style" layer
is itself rendered/distilled by the authors, with the degree of transformation
deferred to Appendix E; no condition uses unmodified community entries. (ii) The
same expert team authored the rubric's extensions *and* all 411 task rewrites,
with no independently-authored task subset to control construct alignment (the
leakage control governs string overlap, not taxonomy overlap). (iii) The
source-included, mandatory Top-N protocol means the motivating regime of Sec 1 — a
query facing a pool with **no** usable option — is never measured; abstention does
not exist in the protocol. (iv) The router's three domains are exactly the three
evaluation domains, and its 98.5% is suite-membership classification on the
benchmark's own partition; the promised five-example extensibility to a fourth
domain is never demonstrated. Each was weakened under refutation (external task
sources, published taxonomy anchor, declared construction, honest corruption
sweep) — but together they scope the results to the authors' synthesize-then-select
regime.

### W6. The abstract's headline sentence fails its natural reading. **[wrong · minor, but abstract-level]**

"Exceeds existing baseline's average by **at least +3.5 points across three
different retrievers**": read distributively (per retriever), the margins over the
strongest baseline are +4.5 / **+3.1** / **+3.0** — below the stated bound for two
of three retrievers. The sentence is true only as the pooled nine-cell average
(+3.51 vs SkillFlow, zero slack for "at least"). Sec 5.5's own phrasing ("+3.5pp
over the strongest baseline ... 69.1% average") is the accurate version; the
abstract's is not. Machine-checked (`abstract-at-least-3p5-*` in the audit).

### W7. Main-text reporting and ethics gaps, mostly deferral-calibrated. **[under-specified · minor cluster]**

- The mandated social-impact section argues **benefits only**; no sentence in the
  provided nine pages engages any risk, harm, or misuse of the work ("risk"
  appears only as the Misleading-risk scoring dimension). Limitations are wholly
  in unprovided Appendix H.
- Cultural norms are checked against **single gold answers** across six regions,
  one of which is "Africa and the Middle East"; how regionally variant norms were
  handled is unverifiable from the provided material (Appendix D/G). The paper's
  own example treats "the customary amount" for red envelopes as one recoverable
  fact.
- No annotator reporting in the main text (team size, recruitment, compensation);
  no licensing statement for a release derived from community skill files,
  official product skills, and API documentation; no cost/latency reporting for a
  method adding up to ~100 LLM calls per query (K up to 50, two views); API
  backbone (Gemini-3-Flash) unpinned; audit "Est." counts carry no stated
  detection recall; paraphrase-set authorship for checkers unstated at one-task
  margins.

### W8. Presentation minors. **[minor]**

Two Fig 6 delta labels contradict their own printed endpoints by 0.1pp (computed
from unrounded values, rounded independently). The K = 10·⌊|S|/1000⌋ rule is
degenerate for pools under 1,000 and makes Fig 4's General Top-10 point vacuous
(K = N = 10, so selection there is a no-op). Router accuracy lacks n and label
provenance. Related work omits the LLM-as-reranker line (RankGPT and successors),
LLM-as-judge rubric scoring (G-Eval, Prometheus), Self-RAG/CRAG, and score-fusion
precedents for its three (standard-form) fusion rules — though the closest lineage
is engaged empirically via SkillFlow and the quality-scorer baselines. DEITA is
mischaracterized as judging only "language quality." The "first" claim is true
only through all four of its qualifiers; the verified-synthesis line (SkillGen,
CoEvoSkills) is cited but absent from the two-gap positioning.

---

## Questions for the authors

Ordered by how much the answer would move the rating.

**Q1 (equality — decisive for the framing).** Report the full per-language and
per-region success numbers for M-SQE, Retrieve-only, and Random (the Fig 3
baseline series, as numbers), with per-cell task counts, the exact comparator and
aggregation behind +12.9/+5.6/+6.6/+8.4pp, and a before/after cross-language
dispersion or gap-to-best metric. Does M-SQE *reduce* the spread relative to
Retrieve-only, or relocate it (zh/ko now lowest)? This should be computable from
existing logs; a favorable answer moves the paper up a step on its own.

**Q2 (attribution — decisive for the methods contribution).** Run the same
Gemini-3-Flash scorer with a generic, rubric-free relevance/usefulness reranking
prompt over identical candidate sets (at minimum BM25 × three domains), and extend
the Theory/Action ablation beyond the single BM25/Top-3 setting. How much of the
margin survives against "same LLM, generic prompt," and is the 7-task increment
beyond Action-only stable across retrievers?

**Q3 (statistics — decisive for how results may be stated).** What does Appendix B
contain — paired per-cell tests (e.g. McNemar) for the nine settings and a
task-level aggregate test? How many draws produce the Random row? For Table 5,
provide multi-seed results or downgrade the training-data-constructor claim to an
observation. State the router-accuracy protocol (n, label provenance, flip
semantics).

**Q4 (cultural checkers).** For norm-type tasks, how were regionally variant norms
handled — does the verifiability filter exclude contested norms, and who authored
the accepted-paraphrase sets? One example of a discarded contested task would be
convincing.

---

## Limitations and societal impact

The main text contains no limitations discussion (deferred to Appendix H) and the
social-impact section engages only benefits, partly restating results. For a paper
whose title claims an equality contribution, the missing risk discussion is
conspicuous: single-gold-answer cultural checking under a six-region taxonomy is
itself an essentialism risk the paper never names, and the release of pools derived
from community and product documentation raises licensing questions the main text
does not address. All of this may be handled in the supplementary; at minimum a
summary belongs in the reviewed pages.

---

## Rating

**Score: 5 / 10 — borderline reject** (weak reject, leaning to the fence)
**Confidence: 4 / 5**

The verified core is close to the bar: a real +6.3pp aggregate gain over
Retrieve-only that is robust to backbone swaps and would survive significance
testing in the Tool-Use domain; airtight tabulation (45/45 cells
integer-consistent); genuine confound controls including one that bounds the
authors' own component; and two first-of-kind artifacts (the audit and the
mixed-provenance pools) with a concrete release pointer. This is a competent
"standard mechanism, new setting, novel evaluation infrastructure" paper.

What holds it under the bar as submitted is that the claim layer outruns the
evidence in ways a rebuttal must actively repair, not reword: the title-level
equality claim needs a computed gap metric that currently does not exist in the
paper and may be adverse (W1); the attribution of the gain to the novel two-view
machinery needs a rubric-free LLM baseline that was never run (W2); and the
trajectory-constructor contribution is beyond statistical rescue at its current
margins and should be withdrawn or re-run (W4). W6 and most of W7–W8 are
camera-ready edits; parts of W3/W7 may dissolve when the unprovided appendices are
consulted.

**What moves it to 6–7:** Q1 answered with a favorable dispersion metric plus Q2
showing the rubric still ahead of a generic LLM reranker. **What confirms 5 or
lower:** a gap metric showing relocated inequality, or the generic prompt matching
the rubric — the honest residue would be good benchmark infrastructure plus a
modest selection result under an oversized title.

---

## Integrity note

Stage-1 scan: **clean**. No hidden text at any confidence level, no
instruction-like content, no anomalous font structure (median 5 font resources per
page, no outliers). Double-anonymity: no violation found; overlapping-author-
cluster citations are in third person, which policy permits. Nothing to report.

---

### Reviewer working notes (not for authors)

**Method.** Produced with [`../../workflow/`](../../workflow/): clean integrity
gate → claims-before-results table (`02-claims.md`) → machine numeric audit
(27 checks: 25 pass; failures are the abstract's per-retriever reading and a
trivial rounding slip) → 5 dimension reviewers → adversarial verification → AC
synthesis. **42 of ~60 findings survived** (23 confirmed, 19 weakened, rest
refuted); 32 strengths recorded. 11 agents, ~874K tokens.

**Refuted in verification (kept out of the review).** "Fig 3 is impossible" as an
error claim — the verifier's exhaustive integer-feasibility search *resolved* it
instead: the bars are M-SQE pooled over three retrievers, matching Table 3 exactly
(143/156 cultural). The anomaly became W1's "aggregation unstated" rather than a
correctness finding. Similarly, "social-impact section restates results" was
weakened to the venue-expectation form, and the LLM-reranker citation gap was
weakened from "mechanism unsituated" to "citation completeness" because the paper
does engage its closest lineage empirically.

**Rebuttal-fixable?** W1 partially (compute the metric — risk: it may be adverse);
W2 no (new experiment); W3 mostly (Appendix B may already contain it); W4 no
(needs seeds or a downgrade); W5 no (design-level, scope claims instead); W6–W8
yes. The 5 is genuinely movable — this is the rare borderline where the rebuttal
questions are answerable from existing logs plus one cheap experiment.

**Fresh-judgment check.** No priors imported: rating started neutral; the numeric
audit here *passed* almost everywhere (25/27), the integrity scan was clean and
reported as clean, and the strengths section is longer than in any prior review
this workflow has produced because this paper earned it.

**Deadline-day re-evaluation (2026-08-24).** Before submission, two independent
passes were run. (1) A fresh-eyes reviewer with no access to this review read the
paper cold and converged on the same verdict — 5/10 borderline reject — with the
same top findings ranked in the same order, adding the micro-averaged
per-retriever margins, the Fig 6 comparator observation, and the cultural ceiling
note, all now folded into W3. (2) A red-team pass re-verified the review's quoted
numbers against the paper; the one defect it surfaced was in our own strengths
census — "45 deterministic cells" was an *undercount*: an exhaustive recount
gives **102/102** integer-consistent cells (81 + 9 + 12), corrected above. The
score stands at 5/10.
