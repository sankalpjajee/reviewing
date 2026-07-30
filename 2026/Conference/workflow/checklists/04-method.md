# Stage 4 — Methodology and evaluation validity

## Artifact construction

- [ ] Provenance of every shipped annotation: human, inherited, or heuristic
- [ ] Validation of each derived annotation against something external
- [ ] Sample size and agreement rate for any human validation
- [ ] Failure modes the authors concede — quote them; concessions in an appendix
      often contradict claims in the body
- [ ] Parameters chosen by calibration: what target, and is the target justified
      independently or chosen to produce a desired output?

## Evaluation validity

- [ ] **Circularity**: is anything evaluated using the procedure that produced it?
- [ ] Ground-truth provenance for the evaluation set, stated explicitly
- [ ] Fallback/`other`/`unknown` rate, and its effect on every downstream number
- [ ] Held-out set genuinely held out — by source, generator, and style
- [ ] Baseline from prior work, run on this artifact
- [ ] Chance performance, computed
- [ ] Ablations isolate the claimed cause

## Task framing

- [ ] The label distribution contains what the motivating task requires
- [ ] Negative/control examples exist if the task is detection
- [ ] Derived scores (difficulty, quality, confidence) validated against something
      external, or acknowledged as unvalidated constructs

## Internal consistency

- [ ] Worked examples agree with the taxonomy and thresholds defined in the body
- [ ] Steps within a single generated example do not contradict one another
- [ ] Appendix figures support the claims the body makes about them
