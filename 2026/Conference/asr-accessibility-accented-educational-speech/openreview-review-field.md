# Review field (quality / clarity / originality / significance + pros and cons)

## Quality

The core design is sound: identical items are answered from a gold ±100-word window and from the corresponding ASR window, discordant pairs are tested with McNemar's exact test, Cohen's $h$ is reported beside $p$-values, and questions are generated from the reference transcript rather than the ASR output. I recomputed every $p$-value in Table 3 and the open-ended test, every $h$ in Table 4, and the counts in Tables 1, 5 and 7; all reproduce (e.g. 160 vs 37 discordant pairs gives $p = 9.9\times10^{-20}$). The directions of the main effects are credible.

However, several important claims are not supported by what is reported:

1. **No result behind the topic and knowledge-intensity claims.** The abstract and conclusion state that QA gaps differ "substantially ... across recording topics" and are "largest ... in knowledge-intensive material". No table or figure reports QA accuracy by topic or by the knowledge-intensity label (defined on p.2 and never used again). Figure 3 is ASR error, not QA. The "substantial differences among QA LLMs" are a 1.9-point spread the text itself calls "very similar", with no between-model test.

2. **The central thesis is never tested.** QA accuracy, the reference-vs-ASR drop, and $h$ are never split by L1/L2. The paper shows L2 speech has higher WER and, separately, that ASR errors lower QA accuracy; the interaction the title asserts is not evaluated. The only speaker-linked QA evidence, Table 7 (84% vs 91% L2 among 194 clips), has no test; on the implied counts (47/56 vs 126/138) a two-sided Fisher exact test gives $p \approx 0.20$.

3. **Pooled tests labelled as per-item.** Table 3 is labelled $N = 1{,}107$ and the Methods promise per-model tests, but the counts only reproduce the stated gap if pooled over three LLMs: $\frac{160-37}{3 \times 1107} = 3.7$ pt and $h(0.943, 0.906) = 0.141$ (reported 0.140), whereas $\frac{123}{1107} = 11.1$ pt per item. Three answers to the same corrupted window are not independent trials, so the $p$-values overstate the evidence, and no per-model result is given. The open-ended test (140 vs 33 over $3 \times 300 = 900$ pairs) has the same issue.

4. **The item set is conditioned on ASR errors.** Items are built only from "knowledge-error keywords", so the measured drop is $P(\text{QA fails} \mid \text{keyword corrupted})$, not the abstract's "how much of the recording's knowledge remains accessible". The ASR system whose errors defined the items is never named, which biases the seven-system comparison in Figure 4, and there is no closed-book control although the Limitations concede the LLMs may answer from parametric knowledge.

5. **Interpretive sentences contradicted by the paper's own tables.** BWER is below WER for every Whisper row in Table 2 and every domain in Figure 3, so "topic-specific vocabulary presents a greater challenge than surrounding function words" holds only for wav2vec2. The L2/L1 WER ratio is $\approx 1.4$ for all seven systems (1.40, 1.43, 1.38, 1.61, 1.40, 1.39, 1.31) and largest for Whisper-L, so "recent models reduce the L1/L2 accessibility gap" holds only in absolute terms. Whisper-L (WER 0.197) yields higher QA accuracy than Wav2Vec2-L-s (WER 0.164) for every LLM, so the QA ordering does not "closely mirror" Table 2.

6. **An acknowledged artifact is reused as a result.** The authors attribute the Whisper-L/L-t deficits to hallucination and repetition on long audio "rather than a genuine capability deficit", yet these numbers fill Table 2, produce the largest L1/L2 gap in Figure 2, enter Table 6, and decide which system is used downstream. No decoding settings are reported and five of the seven checkpoints are unidentified.

7. **Verifier and judge roles contaminate the measurements.** Two of the three answerers are also the answerability verifiers, so the verified subset's near-ceiling reference accuracy and its larger $h$ (0.19 vs 0.14 despite a smaller net drop, 3.2 vs 3.7 pt) are partly selection artifacts. The open-ended answers are graded by the question generator with no validation, and gold-window accuracy falls to 77-84%, so the size of the "unmasked" effect is uncertain even though its direction is real.

## Clarity

The paper is readable, but the presentation undermines its own results. The text reports reference accuracies of 99.3/98.3/97.9% "as Figure 4 shows"; Figure 4's bars read 0.954/0.940/0.935, whose mean is Figure 1's 94.3%. The text's numbers reproduce the verified-subset $h = 0.190$ and the figure's reproduce the full-set $h = 0.140$, so the prose describes a different item set from the figure it cites. Figure 4 identifies systems only by colour family, so the "mirrors Table 2" claim cannot be checked by a reader. "Table 11" and an empty "(see Section for details)" reference dangle, and four results are deferred to an appendix that is not in the submission, including the entire human-study protocol (rater count, background, reliability, consent, scale anchors) and the multiple-choice drops that anchor the open-ended comparison. Table 6's caption says "ASR accuracy" for what are correlations with an error rate; Table 5's comprehensibility scale runs opposite to its name without saying so; "two-stage" means different pairs of stages in the abstract and in the Methods.

## Originality

The specific combination is new: an LLM-QA probe over real ASR output, applied to accented educational speech, with keyword-level error typing and human accent ratings. Each component, however, has substantial prior work the paper does not engage: task-based evaluation of lecture transcripts (Munteanu et al. 2006), spoken QA under ASR noise (Spoken SQuAD, ODSQA, SLUE), QA-based consistency metrics using the same generate-MCQ-then-answer design (MQAG), DHH caption-usability metrics that already argue WER is insufficient (Kafle & Huenerfauth 2017, 2019), semantic alternatives to WER (SemDist), Whisper long-form hallucination (Koenecke et al. 2024), and the Munro & Derwing accentedness/comprehensibility/intelligibility paradigm that the human study reproduces without citation. The claim that transcript quality as LLM input is "underexplored" is overstated.

## Significance

The problem matters: captions are treated as accessibility infrastructure for Deaf, hard-of-hearing and multilingual learners, and a knowledge-level metric is a useful complement to WER. But the paper's significance is limited by what it does not do. Accessibility is operationalized as LLM multiple-choice accuracy on a pre-selected window, with no validation against any human reader; the human study samples hearing listeners rating audio, the inverse of the target population. The effect the paper can defend is small (2.7-4.7 pt on multiple choice, $h = 0.14$-$0.19$, below Cohen's "small" anchor), and the analysis that would establish the equity claim (QA by L1/L2) is absent. No implications are drawn for institutions or vendors although useful ones are present (off-the-shelf large Whisper checkpoints are worse on long lectures; substitutions of technical terms dominate; no system tested meets the "99%" policy threshold the paper invokes without a source). Nothing is released, so the framework and datasets claimed as contributions cannot be used by others.

## Pros

- Important, well-motivated problem with a vivid failure mode (Figure 1: "base excision repair" → "basic session repair").
- Correct paired design; all reported statistics reproduce; effect sizes reported and honestly called modest.
- Questions generated from the reference, generator excluded from answering, partial verifier/answerer overlap disclosed, deterministic decoding.
- Real educational speech at scale (1,355 recordings, two corpora) with per-speaker L1/L2 labels.
- Useful observations: the multiple-choice format masks part of the effect; large Whisper checkpoints fail on long lecture audio off the shelf; keyword substitutions dominate deletions.
- Candid Limitations section.

## Cons

- Abstract and conclusion claims about topics, knowledge intensity, and LLM differences have no supporting result.
- The title's L1/L2 → knowledge-loss claim is never tested; the one speaker-linked QA table is untested and non-significant ($p \approx 0.20$).
- Text contradicts Figures 1 and 4 on the headline reference accuracy.
- Table 3's tests are pooled over three LLMs but labelled $N = 1{,}107$; independence violated; no per-model results.
- Item set conditioned on an unnamed ASR system's errors; no closed-book control; verifier/answerer overlap and an unvalidated generator-as-judge inflate or blur the reported gaps.
- Three interpretive claims are contradicted by Table 2, Figure 2 and Figure 3.
- Whisper-L/L-t artifact reused throughout; checkpoints and decoding unspecified.
- Appendix, human-study protocol, IRB/consent statement, and ethics discussion of instructor profiling are all missing.
- No code, prompts, item set, or data release.
