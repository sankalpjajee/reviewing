# Review field (quality / clarity / originality / significance + pros and cons)

## Quality

The design is sound: identical items answered from a gold ±100-word window and from the ASR window, McNemar's exact test on discordant pairs, Cohen's $h$ beside $p$-values, questions generated from the reference rather than the ASR output. Every reported $p$-value, $h$, and count reproduces, and the main effects point the right way. But the evidence does not support several central claims:

1. The abstract's and conclusion's claims of QA gaps "across recording topics" and "largest ... in knowledge-intensive material" have no supporting table or figure; the knowledge-intensity label is defined and never used, and the "substantial differences among QA LLMs" are a 1.9-point spread the text calls "very similar".
2. The title's thesis is never tested: QA accuracy is never split by L1/L2. The only speaker-linked QA evidence (Table 7, 84% vs 91% L2) has no test; the implied counts give Fisher $p \approx 0.20$.
3. Table 3's tests are pooled over three LLMs but labelled $N = 1{,}107$: only $\frac{160-37}{3\times1107} = 3.7$ pt reproduces the stated gap and $h = 0.14$. The three answers per item are not independent, and the promised per-model tests are absent.
4. Items are built only from keywords the ASR corrupted, so the drop is $P(\text{fail}\mid\text{keyword corrupted})$, not "how much knowledge remains accessible"; the selecting system is unnamed and there is no closed-book control.
5. Three interpretive sentences are contradicted by the paper's own tables: BWER is below WER for every Whisper cell (Table 2, Figure 3); the L2/L1 WER ratio is $\approx 1.4$ for all seven systems and largest for Whisper-L; Whisper-L (WER 0.197) beats Wav2Vec2-L-s (0.164) on QA.
6. The Whisper-L/L-t results are an acknowledged long-form decoding artifact yet fill Table 2, drive the largest gap in Figure 2, and pick the downstream system; decoding settings and five of seven checkpoints are unspecified.
7. Two of three answerers are also the answerability verifiers (inflating the verified subset), and the open-ended judge is the unvalidated question generator with gold-window accuracy at 77-84%.

## Clarity

Readable, but the text contradicts its figures on the headline number: 99.3/98.3/97.9% reference accuracy in the text versus 0.954/0.940/0.935 in Figure 4 and 94.3% in Figure 1 (the text's values reproduce the verified-subset $h = 0.19$, the figures' the full-set $h = 0.14$). Figure 4's bars are identified only by colour family; "Table 11" and an empty "see Section" reference dangle; the appendix, including the whole human-study protocol, is missing; Table 6's caption says "accuracy" for error-rate correlations.

## Originality

The combination (LLM-QA probe over real ASR output, accented educational speech, keyword-level error typing, human accent ratings) is new, but each component has unengaged prior work: task-based lecture-transcript evaluation (Munteanu et al. 2006), spoken QA under ASR noise (Spoken SQuAD, SLUE), generate-then-answer consistency metrics (MQAG), DHH caption-usability metrics (Kafle & Huenerfauth), semantic WER alternatives (SemDist), Whisper hallucination (Koenecke et al. 2024), and the Munro & Derwing paradigm the human study reproduces without citation. The "underexplored" claim is overstated.

## Significance

The problem is real and a knowledge-level complement to WER would be useful. But "accessibility" is measured as LLM multiple-choice accuracy on a pre-selected window with no validation against any human reader, the human study samples hearing listeners rating audio rather than transcript users, the defensible effect is small ($h = 0.14$-$0.19$), the L1/L2 QA analysis that would carry the equity claim is absent, no implications are drawn for institutions or vendors, and nothing is released.

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
