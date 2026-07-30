# Severity scale

Severity answers one question: **what does this cost the reader who believes the
paper?** Not how irritating it was to find.

| Severity | Test | Effect on rating |
| --- | --- | --- |
| **Critical** | A headline claim is unsupported or contradicted by the paper's own evidence; or the artifact cannot be obtained; or the result cannot be reproduced even in principle from what is written. A reader acting on the paper would be misled. | Caps the rating below the acceptance threshold until fixed. |
| **Major** | A substantive claim is overstated, an important validation is missing, or a design choice that the conclusions rest on is unjustified. The contribution survives but is smaller than advertised. | Moves the rating down a step; several majors compound. |
| **Minor** | Presentation, missing detail, an unverifiable-but-plausible number, a citation that should be discussed rather than listed. Fixable in a camera-ready. | No rating effect. Listed so the authors can fix it. |

## Distinctions that matter more than severity

Tag every finding with one of these. They read differently to an author and carry
different weight in a decision:

- **Wrong** — the paper states something its own evidence contradicts. Not
  fixable by rewriting; either the number or the sentence has to change.
- **Under-specified** — the paper may well be right, but a reader cannot check.
  Usually fixable in a rebuttal, and often *is* fixed there.
- **Debatable** — a defensible choice a reviewer would have made differently.
  Say so, argue it, and do not price it as a defect.

The common reviewing error is filing *debatable* as *wrong*. The second most
common is filing *wrong* as *under-specified* out of politeness, which reads to
an AC as a minor complaint and quietly disappears from the decision.

## Escalation

A finding escalates one level when:

- It recurs — the same error in the abstract, the body, and the conclusion is
  worse than in one place, because each repetition is another chance to have
  caught it.
- The paper explicitly claims to have checked the thing that is wrong. "We find
  no faithfulness violations" alongside a visible violation is worse than silence,
  because it converts an omission into an assertion.
- It concerns the artifact being contributed rather than an incidental
  experiment. On a dataset track, a defect in the dataset outranks a defect in a
  pilot model by construction.

## De-escalation

A finding drops one level when the paper names the problem itself in a
limitations section. Honest self-report is worth something, and penalising it
teaches authors to hide things. It does not drop to zero: acknowledging that a
core validation is missing does not supply it.
