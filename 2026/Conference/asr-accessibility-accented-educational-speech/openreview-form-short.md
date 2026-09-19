# OpenReview form, short version (highest-impact items only)

## Title
Promising knowledge-level evaluation of ASR for accented lecture speech, but the headline claims outrun the reported evidence and the central L1/L2 analysis is missing

## Summary
The paper argues that word error rate (WER) does not tell us whether a lecture transcript still conveys the lesson, since one mis-recognized technical term can remove the taught concept while the transcript stays fluent, and that this cost falls hardest on non-native (L2) instructors. It proposes a two-stage evaluation: (1) from a gold transcript, an LLM selects knowledge-intensive keywords and writes one multiple-choice question per keyword from a ±100-word window, filtered by a leak check and two LLM answerability judges; (2) three QA LLMs answer each item from the gold window and from the ASR window, and the accuracy drop is treated as lost accessible knowledge. It is applied to seven ASR systems (four Whisper, three wav2vec2) on 1,232 edX lecture videos (27 instructors) and 123 M3AV talks with per-speaker L1/L2 labels. Reported findings: L2 speakers have higher WER on every system; the largest Whisper checkpoints do worst (attributed to long-form hallucination); QA accuracy drops about 3.7 points pooled with Whisper-M (160 vs 37 discordant pairs, p ≈ 1e-19, h = 0.14), mostly from keyword substitutions; an open-ended variant on 300 items shows 10-14 point drops; a 235-clip human study finds L2 speakers rated more accented and ratings correlated with ASR keyword error.

## Review
The question is important and the core design is right: identical items answered from a gold window and from an ASR window, McNemar's exact test on discordant pairs, effect sizes beside p-values, questions generated from the reference rather than the ASR output. I recomputed every p-value and effect size in Tables 3-4 and the counts in Tables 1, 5 and 7; all reproduce, and the direction of the main effects is credible. My recommendation is driven by the gap between what is claimed and what is shown.

1. **Headline claims have no supporting result.** The abstract and conclusion claim QA gaps "across recording topics", "largest ... in knowledge-intensive material", and "substantial differences among QA LLMs". No table or figure reports QA accuracy by topic or by the knowledge-intensity label (defined on p.2, never used again); Figure 3 is ASR error, not QA. The three LLMs' reference accuracies are within 1.9 points and the text itself calls them "very similar".

2. **The central thesis is never tested.** QA accuracy, the reference-vs-ASR drop, and h are never split by L1/L2. The paper shows L2 speech has higher WER and, separately, that ASR errors lower QA accuracy; the interaction the title asserts is not evaluated. The only speaker-linked QA evidence, Table 7 (84% vs 91% L2 among 194 clips), has no test; on the implied counts a Fisher exact test gives p ≈ 0.20.

3. **The text contradicts the figures on the key number.** The text reports reference accuracies of 99.3/98.3/97.9% "as Figure 4 shows"; Figure 4's bars read 0.954/0.940/0.935, whose mean is Figure 1's 94.3%. The text's numbers reproduce the verified-subset h = 0.190; the figure's reproduce the full-set h = 0.140. The prose is describing a different item set from the figure it cites.

4. **Table 3's tests are pooled over three LLMs but labelled N = 1,107.** Only 3 × 1,107 = 3,321 model-item pairs reproduce the stated 3.7-point gap and h = 0.140 (per item, 160 − 37 = 123 would be an 11-point drop). Three answers to the same corrupted window are not independent trials, so the p-values overstate the evidence, and the per-model tests promised in the Methods never appear. The open-ended test (140/33 over 900 pairs) has the same issue.

5. **The item set is conditioned on ASR errors.** Items are built only from keywords the ASR corrupted, so the measured drop is P(QA fails | keyword corrupted), not the abstract's "how much of the recording's knowledge remains accessible". The system whose errors defined the items is never named, which biases the seven-system comparison in Figure 4, and there is no closed-book control although the Limitations concede the LLMs may answer from parametric knowledge.

6. **Three interpretive sentences are contradicted by the paper's own tables.** BWER is below WER for every Whisper row in Table 2 and every domain in Figure 3, so "topic-specific vocabulary presents a greater challenge than function words" holds only for wav2vec2. The L2/L1 WER ratio is about 1.4 for all seven systems and largest for Whisper-L (1.61), so "recent models reduce the L1/L2 gap" holds only in absolute terms. Whisper-L (WER 0.197) beats Wav2Vec2-L-s (0.164) on QA for every LLM, so the QA ordering does not "mirror Table 2".

7. **An acknowledged artifact is reused as a result.** The authors attribute the Whisper-L/L-t deficits to hallucination and repetition on long audio "rather than a genuine capability deficit", yet these numbers fill Table 2, produce the largest L1/L2 gap in Figure 2, enter Table 6, and decide which system is used downstream. No decoding settings are given and five of seven checkpoints are unidentified.

8. **Not self-contained, not reproducible, ethics unaddressed.** "Table 11" and an empty "see Section" reference dangle; the appendix, including the entire human-study protocol (raters, reliability, consent, scale anchors), is missing; no code, prompts, items, or data are released; there is no IRB or consent statement; and the biographical profiling of 27 identifiable instructors is not discussed in the section titled "Ethical Concerns".

**Pros:** important problem with a vivid failure mode (Figure 1); sound paired design with reproducible statistics; honest limitations; useful observations (multiple choice masks part of the effect; large Whisper checkpoints fail on long lecture audio off the shelf; substitutions of technical terms dominate).

**Cons:** items 1-8 above. The core idea is publishable once the text matches the data, the L1/L2 and per-topic QA analyses are reported, the pooling and item-selection issues are handled, and the appendix, ethics statement, and materials are provided.

## Strengths And Weaknesses
**Significance of the problem (3).** Caption accessibility and ASR bias against L2 speakers are established social-impact problems; the knowledge-level framing is a useful new take, but the prior work is not engaged.

**Engagement with literature (2).** Misses the closest lines: task-based and QA-based evaluation of ASR output (Munteanu et al. 2006; Spoken SQuAD; MQAG), DHH caption-usability metrics (Kafle & Huenerfauth), semantic WER alternatives (SemDist), Whisper long-form hallucination (Koenecke et al. 2024), and the Munro & Derwing paradigm the human study reproduces without citation.

**Significance to the AI community (2).** The observation that multiple-choice probes can mask ASR-induced knowledge loss is useful; the framework recombines known components with 2020-2022 checkpoints.

**Soundness (2).** Paired design and reproducible arithmetic, but important claims are unsupported: no QA-by-topic or QA-by-L1/L2 result; text/figure mismatch on reference accuracy; pooled tests labelled per item; item set conditioned on an unnamed system's errors with no closed-book baseline; two of three answerers are also the verifiers, inflating the verified subset; the open-ended judge is the unvalidated question generator; L1/L2 confounded with instructor (27 edX speakers) and venue (168 of 235 clips NIH) with no clustering or tests; Whisper-L artifact reused.

**Facilitation of follow-up work (1).** No code, prompts, item set, labels, or ratings released; five of seven checkpoints and both commercial LLM versions unidentified; decoding, window alignment, normalization, and filtering heuristics undefined; appendix absent.

**Scope and promise for social impact (2).** Practically useful findings are present but no implications for institutions or vendors are drawn, the LLM proxy is not validated against any human reader, and the "99% accuracy" policy claim is unsourced and never connected to the results.

**Presentation.** Text and figures disagree on the headline number; dangling references; Figure 4 has a truncated axis and unlabelled bars; Table 6 says "accuracy" for error-rate correlations; inconsistent model names.

## Questions For The Authors
1. Which item set do the 99.3/98.3/97.9% reference accuracies describe? Please give per-model, per-ASR accuracies for both the full and verified sets.
2. Are the Table 3 and open-ended tests pooled across the three QA models? Please report per-model toward/away counts, p, and h.
3. What is QA accuracy and the reference-vs-ASR drop separately for L1 and L2 instructors? This is the analysis the title implies and would most change my assessment.
4. What is QA accuracy by topic and by the knowledge-intensity label? If unavailable, will the abstract and conclusion claims be removed?
5. Which ASR system's errors defined the item set, how many items contain a keyword error under each of the seven systems, and how is the ASR window located when the keyword is substituted or deleted?
6. Exactly which checkpoints and decoding settings produced the Whisper results, and were Whisper-L/L-t re-run with standard long-form safeguards?
7. Human study: how many raters, how many per clip, what backgrounds, what reliability, and what ethics approval, consent, and compensation? Which ASR system and how many questions per clip underlie Table 7?

## Ratings
Significance Of The Problem 3 · Engagement With Literature 2 · Significance To The AI Community 2 · Soundness 2 · Facilitation Of Follow Up Work 1 · Scope And Promise For Social Impact 2 · Resources: No · Overall 2 (Reject) · Confidence 4 · Expertise: your call · Acknowledgement: Yes

## Ethical Considerations
Not adequately addressed; I recommend specialized ethics review. The study compiles national origin, native language, and US residence history for 27 named edX instructors and infers initial L1/L2 status for M3AV speakers from name and affiliation (verified for an unreported subset), with no ethics-board statement, consent, or retention discussion, and advertises release of datasets "enriched with speakers' demographics" that would be linkable to identifiable instructors. The human-listener study reports no IRB approval, consent, or compensation. Per-instructor error and accentedness scores carry a dual-use risk (evaluating or deprioritizing accented instructors) that is not discussed. The "Limitations and Ethical Concerns" section contains only methodological limitations.

## Overall Evaluation
2 (Reject). Important claims are not supported by the reported evidence, replication is not possible from the paper, and human-subjects and speaker-profiling ethics are unaddressed. The problem is significant and the paired design is sound; a revised version that reports the missing L1/L2 and per-topic QA analyses, reconciles text with figures, fixes the pooling and item-selection issues, and includes the appendix, an ethics statement, and released materials could be a good paper.

## Comments (confidential)
Arithmetic is internally consistent, so the concerns are about claims, not fabrication. Three checkable-in-minutes issues drive my score: text vs Figure 4 on reference accuracy (99.3/98.3/97.9 vs 0.954/0.940/0.935); Table 3's "N=1,107" is really 3,321 pooled pairs; no QA result is split by L1/L2 or topic despite the title and abstract. Please flag for ethics review (profiling of identifiable instructors, implied release of inferred demographics, no IRB/consent statement). If the rebuttal supplies the L1/L2 QA split and reconciles the numbers, I would move to Weak Reject.

## Post Rebuttal Comment
To be completed after the author response.
