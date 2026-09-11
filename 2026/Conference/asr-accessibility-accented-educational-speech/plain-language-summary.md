# Plain-Language Summary

**Paper:** "The Words Are There, but the Lesson Is Missing: Evaluating ASR Accessibility in Accented Educational Speech" (anonymous submission, 9 pages).

## The one-sentence version

The authors argue that automatic captions for lectures should be judged by whether a reader can still learn the lesson from them, not by how many words are wrong, and they find that captions of non-native-accented instructors lose more of the important words, but the paper's own numbers do not support several of the bigger claims it makes.

## The problem they care about

Imagine a biology lecture where the professor says "base excision repair". The automatic caption reads "basic session repair". Nearly every other word in the sentence is right, so the usual quality score (word error rate, which is just the fraction of words that are wrong) looks fine. But the one term that carried the lesson is gone. A student who relies on the captions, for example a Deaf student, never finds out what process was being taught.

The paper's point is that word error rate treats every mistake as equally bad, while in teaching some words matter far more than others. It also notes that speech recognizers make more mistakes on accented speech, so this hidden damage probably falls hardest on lectures by non-native-English instructors.

## What they built

Think of it as giving a quiz to a robot student.

1. **Pick the important words.** Starting from a correct, human-checked transcript, an AI model (Gemini) picks out the key technical terms of each lecture segment.
2. **Write quiz questions.** For each key term, the same AI writes one four-option multiple-choice question, using only the 200 or so words around that term. Two other AI models check that the marked answer really follows from the passage.
3. **Have AI "students" take the quiz twice.** Three different AI models (GPT-4o, Llama 3.1, Qwen 2.5) answer each question once while reading the correct transcript and once while reading the automatic caption of the same passage.
4. **Compare.** If the AI gets a question right from the correct transcript but wrong from the caption, the caption lost that piece of the lesson.

They ran this on about 1,350 real recordings (edX course videos and academic talks), with seven speech recognizers (four sizes of OpenAI's Whisper and three of Meta's wav2vec2), and they labelled each speaker as a native (L1) or non-native (L2) English speaker.

They used AI models rather than real students because it lets them grade over a thousand questions many times over. The trade-off is that an AI model already knows a lot of biology and can guess the answer even when the caption is garbled, so it is a proxy for a reader, not a real learner. The paper admits this in its limitations section.

They also ran a **human listening study**: people listened to 235 short clips (25 words or fewer), rated how accented and how hard to understand each speaker was, and typed out what they heard.

## What they found

- **Accented speakers get worse captions on every system.** For the best recognizer, about 5.6 of every 100 words were wrong for native speakers and about 8.0 for non-native speakers. Across all seven systems the non-native error rate was roughly 1.4 times the native rate.
- **Bigger is not better off the shelf.** The two largest Whisper models did much worse than the small and medium ones on long lecture audio because they sometimes get stuck repeating themselves or inventing text. The authors say this is a decoding problem, not a capability problem.
- **The quiz drop is real but small on multiple choice.** Averaged over the three AI students, accuracy fell from about 94 out of 100 with the correct transcript to about 91 with the best captions. When the AI changed its answer, it changed from right to wrong about four times as often as the reverse, which is very unlikely to be chance.
- **Fill-in-the-blank shows a bigger gap.** When 300 of the questions were rewritten so the AI had to type the answer instead of picking from four options, the drop grew to 10 to 14 points out of 100. The authors conclude that multiple choice was hiding part of the effect because the AI could eliminate wrong options.
- **Most of the damage comes from substitutions.** Cases where the caption replaced a technical term with a plausible ordinary word ("session" for "excision") caused far more quiz failures than cases where the term was simply dropped.
- **Technical fields suffer most.** Engineering, computer science, and biomedical talks had the highest error rates on technical vocabulary; humanities lectures the lowest.
- **Humans agree the speech is accented, and the machines track that.** Listeners rated the non-native speakers as more accented, and the more accented the listeners found a clip, the more errors the recognizers made on it.

## How much to trust it

A twelve-lens review of the paper, with every statistic recomputed and the numeric findings adversarially re-checked, found that the arithmetic checks out but the storytelling gets ahead of the evidence. Ranked by how much they matter:

1. **Some headline claims have no data behind them.** The abstract says the quiz gap is largest for "knowledge-intensive" material and differs "substantially" across topics and across the three AI models. There is no table or figure of quiz results by topic at all, and the three AI models are within two points of each other.
2. **The title's central claim was never directly tested.** The paper never reports quiz results separately for native and non-native instructors. It shows that non-native speech has more caption errors, and separately that caption errors hurt the quiz, but not that the quiz damage is bigger for non-native instructors. The one place it tries (a small side table) shows a difference that is not statistically distinguishable from chance.
3. **The text and the figures disagree on the main number.** The text says the AI students score 99, 98, and 98 out of 100 with correct transcripts. The paper's own bar chart shows 95, 94, and 94. The text appears to be quoting a filtered subset while pointing at a figure of the full set.
4. **A statistics label is misleading.** The main significance table says it tests 1,107 questions, but the counts only add up if the three AI models' answers are pooled into 3,321 tests. Pooling three answers to the same question as if they were independent makes the results look more certain than they are.
5. **The quiz only covers words the caption got wrong.** The questions were built around terms the recognizer had already mangled. So the "3 to 4 points lost" is the damage *given* that a key term was corrupted, not the overall loss a student would experience. Even then the AI still got about 91% right, which suggests it was often answering from its own knowledge rather than from the caption. There was no control run with no transcript at all.
6. **Two sentences contradict the paper's own tables.** The text says technical words are harder for the recognizer than everyday words, but for every Whisper model the technical-word error rate is *lower* than the overall error rate. The text also says newer models narrow the native/non-native gap. That is true in absolute points only because the better systems make fewer errors overall; in relative terms the gap is the same 1.4x for the best and the worst systems.
7. **The big-model results are admitted artifacts but still used.** The authors say the large Whisper models failed because of a decoding glitch, yet those numbers are kept in every table, feed the accent-gap analysis, and decide which system got used for everything else.
8. **The human study is mostly missing.** How many listeners there were, who they were, whether they consented, and how reliable their ratings were are all deferred to an appendix that was not included. The "intelligibility" score is the fraction of technical terms listeners could transcribe, which mostly measures whether the listener knows biology jargon, not how clear the speaker is.
9. **The setup is not reproducible.** Five of the seven recognizers are not precisely identified, no prompts are given, the exact AI model versions are not stated, and no code or data release is promised.
10. **Ethics are thin.** The team looked up the national origin and native language of 27 named instructors, and for other speakers started from guesses based on names and affiliations (how many were then verified is not reported), without any mention of ethics review or consent, and it plans to release these "demographics".

**What still holds despite all this:** every p-value and effect size recomputes correctly; non-native speakers really do get more caption errors on all seven systems; captions really do cause the AI students to miss questions they would otherwise get right, mostly through substituted technical terms; and the fill-in-the-blank format really does show a bigger gap than multiple choice. These are useful, believable results. They are just smaller and narrower than the title and abstract suggest.

## Why it matters

For a university or a captioning vendor the practical takeaways, once the paper is fixed, would be:

- Do not judge caption quality by word error rate alone; check the technical terms.
- Do not assume the biggest speech model is best for hour-long lectures without tuning how it processes long audio.
- Expect more damage in technical courses and for non-native instructors, and target human caption review there.
- No system tested came close to the "99% accuracy" that the paper says institutional policies demand, for either speaker group.

## Glossary

- **ASR (automatic speech recognition):** software that turns speech into text, the engine behind automatic captions.
- **WER (word error rate):** the fraction of words the ASR got wrong (substituted, dropped, or invented). 0.074 means 7.4 wrong words per 100.
- **CER (character error rate):** the same idea counted by letters instead of words.
- **BWER (biasing word error rate):** the error rate counted only on a list of important or technical words. In this paper the list comes from slide text for the academic talks and from all non-function words for the edX lectures.
- **L1 / L2 speaker:** a native (L1) or non-native (L2) speaker of English.
- **Whisper / wav2vec2:** two families of open speech recognizers, from OpenAI and Meta respectively, in several sizes.
- **LLM (large language model):** an AI text model such as GPT-4o; here used to write questions, check them, answer them, and grade answers.
- **Multiple-choice vs open-ended:** picking one of four options versus typing a short free answer. Open-ended is harder to guess.
- **McNemar's test:** a statistical test for paired yes/no outcomes. Here it asks whether "right with transcript, wrong with caption" happens significantly more often than the reverse.
- **Cohen's h:** a standard way to express the size of a difference between two percentages. Roughly, 0.2 is small, 0.5 medium, 0.8 large; the paper's values are 0.14 to 0.34.
- **Spearman correlation:** a number from -1 to 1 saying how consistently two rankings move together; the paper's values of 0.15 to 0.52 are weak to moderate.
