# Stage 2 — Claim extraction

Filled in from the abstract, contribution bullets, social-impact section, and conclusion before the
dimension review ran. Verdict column completed after Stages 3–5.

- [x] Every empirical sentence in the abstract is a row below
- [x] Every contribution bullet is a row below
- [x] Social-impact and conclusion claims rowed
- [x] Each row names its supposed support
- [x] Quantifiers recorded exactly
- [x] Comparators recorded

| # | Claim (quantifier verbatim) | Where claimed | Where supported | Verdict |
| --- | --- | --- | --- | --- |
| 1 | Audit of ~84,700 community skill entries finds Swahili and Hindi have **zero** in-language skill bodies | Abstract, Sec 1, Table 1 | Table 1; protocol in App A (unprovided) | **partial** — Table 1 sums check (84,680≈84,700); method unverifiable from provided material |
| 2 | Cross-language query/skill mismatch "degrad[es] accuracy and recall" | Abstract, Sec 1 | Cited to Lu et al. 2026 | supported-by-citation (transferred premise, not measured here) |
| 3 | Task success "exceeds existing baseline's average by **at least +3.5** points across three different retrievers" | Abstract | Table 3 | **partial** — holds as average-of-9 (+3.51); fails per-retriever (Neural +3.07, SF-retr +2.97). Machine check `abstract-at-least-3p5-*` |
| 4 | "+12.9pp on Hindi and +5.6pp on Swahili", "lifts the lowest-resource languages most" | Abstract, Sec 2, Sec 5.5 | Fig 3 (bars only) | **partial** — figure-only; comparator (vs Retrieve-only?) and per-language n unstated in main text |
| 5 | "strong performance across all six culture regions", "matches or exceeds both baselines in every breakdown" | Abstract, Fig 3 caption | Fig 3 | **partial** — figure-only; per-region n≈4–15 tasks makes region deltas fractions of one task; see stats findings |
| 6 | "first post-retrieval quality estimation framework purpose-built for multilingual agent skills" (hedged "to our knowledge") | Contribution 1 | Sec 3 positioning | **debatable** — narrow-but-plausible; LLM-as-reranker line uncited; see related-work findings |
| 7 | "average +6.3pp task-success gain across all nine evaluation settings" | Contribution 1 | Table 3 | **supported** — 69.1 vs Retrieve-only 62.8; wording ("average ... across") accurate |
| 8 | "first or tied-first against the single strongest baseline in all 9 domain-by-retriever settings" | Sec 5.5 | Table 3 | **supported** — machine check passes 9/9 (two ties: Tool-Ne, Cul-Ne) |
| 9 | "M-SQE is also strictly ahead of both selection anchors in all 9 settings" | Sec 5.5 | Table 3 | **supported** — 9/9 vs Retrieve-only |
| 10 | Open-source release of evaluation set, skill pools, implementation | Contribution 3 | Footnote 1 → Supplementary | unverifiable from provided material (concrete pointer exists) |
| 11 | Router reaches "98.5% accuracy"; M-SQE survives up to 90% router corruption | Sec 4.4, Fig 5 | Fig 5 | **partial** — corruption sweep coherent; router eval set/labels unstated in main text |
| 12 | Fusion constants "stay stable under parameter perturbation" | Sec 4.4 | App C (unprovided) | unverifiable from provided material |
| 13 | Backbone robustness: "+3.5–9.0pp above Retrieve-only" across six configs, "ruling out pool-synthesis artifacts and scorer or solver bias" | Sec 5.5, Fig 6 | Fig 6 | **partial** — range verified against Fig 6 labels; "ruling out" is stronger than a 6-cell grid can carry; see method findings |
| 14 | Trajectory fine-tuning: "M-SQE yields the best fine-tuned model averagely in three domains" | Sec 5.5, Table 5 | Table 5 | **partial** — true on average by +0.84pp = 3 tasks/411 vs Retrieve-only, with a tie on cultural and +1 task on tool; "best" is literal but the margin is 1–2 tasks per domain |
| 15 | "This region-by-region consistency ... is the evidence that M-SQE's quality signal captures cultural correctness rather than surface fluency" | Sec 2 | Fig 3 | **debatable** — consistency across regions does not by itself distinguish cultural correctness from generic quality signal; see claims findings |
| 16 | Pools "mirror today's ecosystem" / are built "the way a multilingual pool is assembled in practice" | Sec 1, 5.2 | Sec 5.2 construction | **debatable** — all three layers are author-constructed; ecological layer is itself rendered by authors |
| 17 | Budget sweep: margin widens from +3.4pp (Top10) to +9.7pp (Top1) | Sec 5.5, Fig 4 | Fig 4 | **partial** — Top3 point machine-verified against Table 3; other points figure-only |

## Note

Rows 3–5 are the abstract's three quantitative selling points, and all three are *partial* for the same
reason: the strongest phrasing appears in the abstract while the body's own numbers support a more
qualified version. None is fabricated — the gap is between "at least, across three retrievers" and
"on average"; between headline deltas and unstated denominators. This is a wording-discipline issue,
not an integrity one.
