# OpenReview form draft (AAAI-27 AISI track)

## Title
Promising knowledge-level evaluation of ASR for accented lecture speech, but the headline claims outrun the reported evidence and the central L1/L2 analysis is missing

## Summary
The paper argues that word error rate (WER) does not tell us whether a lecture transcript still conveys the lesson: a single mis-recognized technical term can remove the taught concept while leaving the transcript fluent, and this cost is expected to fall disproportionately on non-native (L2) instructors. It proposes a two-stage evaluation. Stage 1: from a gold reference transcript, an LLM (Gemini) selects "knowledge-intensive" keywords and writes one four-option multiple-choice question per keyword from a ±100-word window; items pass a programmatic leak filter and an answerability check by two LLM judges (GPT-4o, Llama-3.1-8B). Stage 2: three QA LLMs (GPT-4o, Llama-3.1-8B, Qwen2.5-7B) answer each item once from the gold window and once from the corresponding ASR window; the accuracy drop is treated as the loss of accessible knowledge. The framework is applied to seven off-the-shelf ASR systems (four Whisper and three wav2vec2 checkpoints) on 1,232 edX lecture videos from 27 instructors and 123 M3AV academic talks, with each speaker labelled L1 or L2 through biographical research.

Reported findings: (i) L2 speakers have higher WER under every ASR system (e.g. Whisper-M 0.080 vs 0.056); (ii) the two largest Whisper checkpoints perform far worse than the small and medium ones, attributed to hallucination and repetition on long audio; (iii) QA accuracy drops by about 3.7 points (pooled over the three LLMs) with Whisper-M transcripts and more with wav2vec2, with discordant pairs running strongly toward "reference right, ASR wrong" (160 vs 37; McNemar p ≈ 1e-19; Cohen's h = 0.14), driven mainly by keyword substitutions; (iv) on 300 items reformatted as open-ended questions the drop grows to 10-14 points; (v) a human study of 235 clips of at most 25 words finds L2 speakers rated more accented, human ratings correlate with ASR keyword error rates (Spearman 0.15-0.52), and clips with imperfect QA have a higher L2 share and accentedness. The stated contributions are the framework, the two enriched datasets, and the human study.

## Review
**Overall assessment.** The question is important and the basic design is right: the same items are answered from a gold window and from an ASR window, discordant pairs are tested with McNemar's exact test, effect sizes are reported next to p-values, questions are generated from the reference rather than the ASR output, and the format ablation (open-ended vs multiple choice) changes only the answer format. I recomputed every p-value in Table 3 and the open-ended test, the Cohen's h values in Table 4, and the count bookkeeping in Tables 1, 5 and 7; all reproduce. The directions of the main effects are credible.

The problem is that the manuscript's claims run well ahead of what it reports, in several places contradict its own tables and figures, and omit the analysis the title promises.

1. **Headline claims without supporting results.** The abstract states "substantial differences among QA LLMs and across recording topics, with the largest performance gaps occurring in knowledge-intensive material", and the conclusion repeats "downstream QA models differ substantially across topics". No table or figure reports QA accuracy by topic, venue, or the lower/higher knowledge-intensity label defined in the Methodology, which is never used again. Figure 3 is Whisper-M ASR error by domain, not QA. The three LLMs' reference accuracies span 1.9 points and the text itself calls them "very similar"; the between-LLM tests promised in Evaluation Metrics are absent.

2. **The central thesis is never tested.** The title and conclusion frame the result as accented instructors' lessons becoming less accessible, but QA accuracy, the reference-vs-ASR drop, and h are never split by L1/L2 (nor is ASR BWER). The paper shows that L2 speech has higher WER and, separately, that ASR errors reduce QA accuracy; the interaction is not evaluated. The only speaker-linked QA evidence is Table 7 (194 clips; 84% vs 91% L2; no test). On the implied counts (47/56 vs 126/138) a two-sided Fisher exact test gives p ≈ 0.20.

3. **The text contradicts the figures on the key number.** The text says GPT-4o, Llama3 and Qwen2.5 reach 99.3/98.3/97.9% in the reference condition, attributing this to Figure 4. Figure 4's reference bars read 0.954/0.940/0.935, whose mean equals Figure 1's "94.3%". Reconstruction indicates the text quotes the ground-truth-verified subset while pointing at the full-set figure: h(0.985, 0.985 − 77/2439) = 0.189 (reported 0.190) and h(0.943, 0.943 − 123/3321) = 0.141 (reported 0.140).

4. **Mislabelled, pooled tests.** Table 3 is labelled N = 1,107 / 813 and the Methods promise per-model McNemar tests, but the counts only reproduce the stated 3.7-point gap and h = 0.140 if pooled over 3 × 1,107 = 3,321 model-item pairs (123/1,107 would be an 11-point drop). The open-ended test (140/33 over 900 pairs) has the same issue. Three answers to the same corrupted window are not independent trials, so the p-values overstate the evidence, and no per-model result is given.

5. **The item set is conditioned on ASR errors.** Items are built from "knowledge-error keywords", i.e. reference/ASR pairs that denote different concepts, so the measured drop is P(QA fails | the keyword was corrupted), not the abstract's "how much of the recording's knowledge remains accessible". The paper never says which ASR system's errors defined the set, which also biases the seven-system comparison in Figure 4. There is no closed-book control, although the Limitations concede that the LLMs may answer from parametric knowledge, and the Figure 1 example is answerable from general biology.

6. **Interpretive sentences contradicted by the paper's own data.** "Topic-specific vocabulary presents a greater challenge than surrounding function words" and "BWER exposes disparities that WER understates": in Table 2 BWER is below WER for all four Whisper checkpoints on both corpora, and in Figure 3 BWER ≤ WER in all eight domains; the claim holds only for wav2vec2. "This suggests recent models reduce the L1/L2 accessibility gap": the L2/L1 WER ratio is 1.40, 1.43, 1.38, 1.61, 1.40, 1.39, 1.31 across the seven systems, i.e. flat, and largest for a Whisper model; only the absolute gap shrinks, mechanically. "This ordering closely mirrors the ASR error-rate ordering from Table 2": Whisper-L (WER 0.197) beats Wav2Vec2-L-s (0.164) on QA for every LLM, and if Figure 4's unlabelled bars follow Table 2 order, the worst-WER Whisper checkpoint yields the highest QA accuracy.

7. **An acknowledged artifact is reused as a result.** The authors say the Whisper-L/L-t deficits are "driven by hallucination and repetition failures on long lecture audio rather than a genuine capability deficit", yet these numbers populate Table 2, produce the largest L1/L2 gap in Figure 2, enter Table 6, and determine which system is used downstream. No decoding configuration is reported and five of the seven checkpoints are unidentified ("L-t" is never expanded).

8. **The paper is not self-contained.** "Table 11" and "(see Section for details)" are dangling references; four results are deferred to an appendix that is not in the submission, including the entire human-study protocol (rater count, background, reliability, consent, scale anchors) and the multiple-choice drops that anchor the open-ended comparison. Table 6's caption says "ASR accuracy" for what are correlations with an error rate.

**Originality.** The specific combination (an LLM-QA probe over real ASR output, accented educational speech, keyword-level error typing, human accent ratings) is new. Each component has substantial prior work the paper does not engage: task-based evaluation of lecture transcripts (Munteanu et al. 2006), spoken QA under ASR noise (Spoken SQuAD, ODSQA, SLUE), QA-based consistency metrics using the same generate-MCQ-then-answer design (MQAG), DHH caption-usability metrics that already argue WER is insufficient (Kafle & Huenerfauth 2017, 2019), semantic alternatives to WER (SemDist), Whisper long-form hallucination (Koenecke et al. 2024), and the Munro & Derwing accentedness/comprehensibility/intelligibility paradigm that the human study reproduces without citation. The "underexplored" gap claim is overstated.

**Clarity.** Readable overall, but with the contradictions above, a bullet list rendered as a run-on paragraph, inconsistent model naming, a truncated y-axis and illegible labels in Figure 4, "two-stage" meaning different pairs of stages in the abstract and in the Methods, and a section titled "Ethical Concerns" that contains no ethics content.

**Pros**
- Important, well-motivated problem with a concrete failure mode (Figure 1's "base excision repair" → "basic session repair").
- Correct paired design; all reported statistics reproduce; effect sizes reported and honestly called modest.
- Generation from the reference, generator excluded from answering, disclosed partial verifier/answerer overlap, deterministic decoding.
- Real educational speech at scale with per-speaker L1/L2 labels.
- Useful observations: the multiple-choice format masks part of the effect; large Whisper checkpoints fail on long audio off the shelf; substitutions of technical terms dominate.

**Cons**
- Abstract and conclusion claims (topics, knowledge intensity, LLM differences) have no supporting result.
- The title's L1/L2 → QA claim is never tested; Table 7 is untested and non-significant.
- Text contradicts figures on reference accuracy; Table 3's N is mislabelled and the tests are pooled.
- The item set is conditioned on ASR errors; no closed-book control; verifier/answerer overlap inflates the verified subset.
- Several interpretive claims are contradicted by Table 2, Figure 2 and Figure 3.
- The Whisper-L artifact is reused; checkpoints and decoding are unspecified.
- The human-study protocol, ethics approval, consent, and appendix are missing; the ethics of biographical profiling are not discussed.
- No code, data, prompt, or question release.

## Strengths And Weaknesses
**Significance of the problem (3).** Caption accessibility for Deaf and hard-of-hearing and multilingual learners, and ASR bias against L2 speakers, are established social-impact problems (Koenecke et al. 2020; Kuhn et al. 2023; Kafle & Huenerfauth 2017). The knowledge-level framing (does the lesson survive transcription?) is a genuinely useful new take. Not a 4, because the problem has been addressed before and the paper does not engage that work.

**Engagement with literature (2).** Strength: the core sociolinguistic ASR-bias literature and recent L2 ASR-vs-human studies are cited. Weaknesses: the Related Work is one column placed after the Results and misses the closest lines of work (task-based and QA-based evaluation of ASR output, DHH caption metrics, semantic WER alternatives, Whisper hallucination, accent-bias benchmarks of the same model families), including work outside computer science: the human study adopts Munro & Derwing's constructs and 9-point scales without citing them. BWER is attributed to the M3AV paper rather than the contextual-biasing literature. Some Introduction citations do not support the sentences they are attached to (Zheng et al. 2023 and Sidiropoulos et al. 2022 are cited for "LLMs ... producing transcripts").

**Significance to the AI community (2).** The observations that multiple-choice probes can mask ASR-induced knowledge loss, and that window-local QA is blind to transcript-level failures such as hallucination loops, are useful to anyone using LLM-QA to evaluate noisy inputs. The framework itself recombines known components, the ASR models are 2020-2022 checkpoints, and no new technique is introduced.

**Soundness (2).** Strengths: paired design, exact tests, reproducible arithmetic, deterministic decoding, a clean format ablation, candid limitations. Weaknesses that leave important claims unsupported: (a) no QA-by-topic or knowledge-intensity result behind the abstract; (b) no L1/L2 split of QA behind the title; (c) text/figure mismatch on reference accuracy; (d) pooled tests labelled as per-item N with independence violated; (e) item set conditioned on one (unnamed) ASR system's errors and no closed-book baseline; (f) two of the three answerers are also the answerability verifiers, so the verified subset's near-ceiling reference accuracy and its higher h (0.19 vs 0.14 despite a smaller net drop, 3.2 vs 3.7 points) are partly selection artifacts; (g) the open-ended judge is the question generator, is unvalidated, and gold-window accuracy falls to 77-84%, so the size of the "unmasked" effect is uncertain even though its direction is real; (h) L1/L2 is confounded with subject and instructor (27 edX instructors) and, in the human study, with venue (168 of 235 clips are NIH), with no speaker-level clustering, confidence intervals, or tests anywhere in the ASR or human-rating comparisons; (i) the Whisper-L/L-t artifact is reused; (j) BWER is defined differently per corpus (slide-OCR terms vs all non-function words) yet compared side by side; (k) edX platform captions are called "independently verified gold-standard" without audit.

**Facilitation of follow-up work (1).** No code, prompts, item set, keyword lists, demographic labels, or rating data are released or promised; five of seven ASR checkpoints and both commercial LLM versions are unidentified; decoding settings, the ASR-window alignment procedure, the function-word list, the "approved equivalent" list, and the "fragmentation/gluing heuristic" are undefined; option shuffling, seeds, and repeat runs are not reported; the appendix is absent. Replication would require considerable effort and guesswork.

**Scope and promise for social impact (2).** The framework could inform captioning procurement and post-editing priorities, and several practically useful findings are present (off-the-shelf large Whisper checkpoints are worse on long lectures; substitutions of technical terms dominate; no system tested meets the 99% threshold the paper invokes for either speaker group). But the paper draws no implications for institutions or vendors, validates the LLM proxy against no human reader, its human study samples hearing listeners rating audio rather than transcript users, and the unsourced "99% accuracy" policy claim is never connected to the results.

**Quality of presentation.** Generally readable, but: reference accuracies in text and figures disagree; "Table 11", an empty "Section" reference, and four appendix pointers with no appendix; Figure 4 uses a truncated 0.75-1.00 axis, roughly 3pt rotated labels, and a family-only legend so individual systems cannot be identified; Figure 1 places question construction inside Stage 2, labels a single Llama icon with three-LLM pooled numbers, and prints results absent from the body; Table 6's caption says "accuracy" for error-rate correlations, with undefined significance stars and no n; Table 5's comprehensibility scale runs opposite to its name without saying so; model names are inconsistent (Wav2Vec2/Wav2Vec, GPT4o/gpt4o, Llama3/Llama-3.1-8B); the keyword-priority criteria render as a run-on paragraph; several sentences are garbled; Related Work sits after the Results.

## Questions For The Authors
1. Which item set do the reference accuracies 99.3/98.3/97.9% describe? Please give per-model, per-ASR accuracies for both the full (1,107) and verified (813) sets.
2. Are the Table 3 and open-ended McNemar tests pooled across the three QA models? Please report per-model toward/away counts, p-values, and h.
3. Which ASR system's errors defined the 1,113 "knowledge-error keywords" and the "ASR-mishearing" used by the leak filter? For each of the seven systems, how many items actually contain a keyword error?
4. What is QA accuracy, the reference-vs-ASR drop, and h separately for L1 and L2 instructors (and by accentedness rating)? This is the analysis the title implies and would most change my assessment.
5. What is QA accuracy by topic family and by the lower/higher knowledge-intensity label? If unavailable, will the corresponding abstract and conclusion sentences be removed?
6. Which bar in Figure 4 corresponds to which ASR system? Does Whisper-L yield the highest QA accuracy despite the worst WER, and if so how does that square with "ordering closely mirrors Table 2"?
7. What decoding configuration (library, chunking/VAD, condition-on-previous-text, thresholds, beam size) produced the Whisper results, and exactly which checkpoints are Whisper-S, Whisper-L, Whisper-L-t, Wav2Vec2-B and Wav2Vec2-L? Were Whisper-L/L-t re-run with standard long-form safeguards?
8. Which Whisper run (auto-detect or language="en") populates Table 2 and Figures 2-3 for edX?
9. How is the ±100-word ASR window located when the keyword is substituted or deleted, and how are repetition loops handled? Were any items dropped per system?
10. What is closed-book accuracy (no transcript) on the items for each QA model?
11. How were open-ended answers judged, and what is the judge's agreement with human graders on a sample? Why does gold-window accuracy fall to 77-84% on verified items?
12. Why did 294 of 1,107 items fail answerability verification, which judge rejected them, and why are they retained in the headline analysis given the stated retention rule?
13. Human study: how many raters, how many per clip, what L1 backgrounds, what scale anchors, what inter-rater reliability, and what ethics approval, consent and compensation? How were the 235 clips sampled and how many unique speakers do they represent? Why did question generation fail for about 45% of L1 clips but only about 12% of L2 clips?
14. Table 7: which transcript condition and ASR system, how many questions per clip, and was reference-condition QA run on the same clips? Please add a test.
15. What is the operational definition of L1/L2? How many M3AV speakers were biographically verified rather than inferred from name and affiliation, and what rule selected 123 talks from 228+ candidate speakers to reach the 75/25 target?
16. Will code, prompts, the item set, keyword lists, and de-identified ratings be released, and under what terms were edX videos and captions used?

## Significance Of The Problem
3

## Engagement With Literature
2

## Significance To The AI Community
2

## Soundness
2

## Facilitation Of Follow Up Work
1

## Scope And Promise For Social Impact
2

## Resources
No. The paper describes two "cleaned and enriched" datasets (L1/L2 labels, 1,107 knowledge-centred questions) as a contribution, but no release, licence, or availability statement appears anywhere, so no resource is actually contributed to the community in the submission as it stands.

## Ethical Considerations
Not adequately addressed; I recommend specialized ethics review. (1) The study compiles country of origin, native language, years of US residence and "accent/background" for 27 named, publicly identifiable edX instructors, and forms initial L1/L2 hypotheses for M3AV academics from name origin and affiliation (verified for an unreported subset), with no ethics-board statement, consent, data-minimization or retention discussion. National origin and native language are sensitive attributes, and the paper's own sentence disavowing name-based inference is in tension with its M3AV procedure. (2) The contributions advertise datasets "enriched with speakers' demographics", implying release of inferred labels linked to identifiable instructors (each of 27 courses maps to one instructor). (3) The human-listener study reports no IRB/ethics approval, consent, or compensation, and its protocol is deferred to a missing appendix. (4) Per-instructor error rates, accentedness ratings and "accessibility" scores create a dual-use risk (deprioritizing or evaluating accented instructors) that is not discussed; remediation should target ASR systems and captioning provision, not speakers. (5) The section titled "Limitations and Ethical Concerns" contains only methodological limitations. (6) Licensing of edX content and transmission of transcripts to commercial APIs are described only as "availability under applicable terms". The framing of the results as a system-side equity problem is appropriate; the governance around the data is not yet.

## Overall Evaluation
2 (Reject). Reasons to reject outweigh reasons to accept under the AISI criteria: important claims are not supported by the reported evidence (soundness), replication is not possible from the paper (follow-up work), and the human-subjects and speaker-profiling ethics are unaddressed. The problem is significant and the paired design is sound, so a revised version that reports the missing L1/L2 and per-topic QA analyses, reconciles text with figures, handles the pooling and item-selection issues, includes the appendix and an ethics statement, and releases materials could be a good paper.

## Confidence
4

## Expertise
[Set this yourself based on your background: 5 if speech/NLP/accessibility evaluation is your current area, 4 if closely related, 3 if past work.]

## Comments (confidential to SPC/PCs)
The paper's arithmetic is internally consistent (all p-values and effect sizes reproduce), so the concerns are about what is claimed rather than about fabrication. Three issues drive my recommendation and are checkable in minutes: (a) the text's reference accuracies (99.3/98.3/97.9%) versus Figure 4's bars (0.954/0.940/0.935) and Figure 1's 94.3%, which appear to mix the verified subset with the full set; (b) Table 3's "N=1,107" tests are pooled over three LLMs (3,321 pairs), which is the only way to reproduce the 3.7-point gap and h=0.140; (c) no QA result is split by L1/L2 or by topic despite the title, abstract and conclusion. I would flag the paper for ethics review given the biographical profiling of identifiable instructors, the implied release of inferred demographics, and the absence of any IRB/consent statement for the listener study. If the authors can supply the L1/L2 QA split and reconcile the numbers in rebuttal, I would move to Weak Reject; acceptance would require the revisions listed in my review.

## Acknowledgement
Yes

## Post Rebuttal Comment
To be completed after the author response. (If the form requires an entry now: "Pre-rebuttal; no author response yet.")
