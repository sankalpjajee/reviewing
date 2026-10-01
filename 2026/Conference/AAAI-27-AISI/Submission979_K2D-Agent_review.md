# AAAI-27 AISI Track — Submission 979 (OpenReview `v3K1wpuT8y`)

**Paper:** K2D-Agent: Bridging the Knowledge-to-Decision Gap in LLM Agents via Graph-Structured Deliberation

## Ratings at a glance

| Field | Rating |
|---|---|
| Significance of the Problem | **2: Fair** |
| Engagement with Literature | **2: Fair** |
| Significance to the AI Community | **2: Fair** |
| Soundness | **2: Fair** |
| Facilitation of Follow-up Work | **1: Poor** (raise to 2–3 if the supplementary material contains code, benchmark, skill and prompts) |
| Scope and Promise for Social Impact | **2: Fair** |
| Resources | **Yes** (K2D-Bench: 48 worlds / 96 tasks; not yet released) |
| Overall Evaluation | **3: Weak Reject** |
| Confidence | **4: Quite confident** |
| Expertise | *(reviewer's own self-assessment)* |
| Acknowledgement | *(reviewer to tick)* |

Each section below matches one OpenReview field and can be pasted as it is.

---

## Title

Promising explicit decision-state agent and a well-built matched benchmark, but the headline gains are 0–2 tasks from single runs, the pre-acquisition claim is untested, and the social-impact case is thin

---

## Summary

The paper identifies a *knowledge-to-decision (K2D) gap* in LLM agents. An agent may fail to recognise what it needs to know (before acquisition), or retrieve evidence that never changes its decision (after acquisition). The proposed **K2D-Agent** has a single LLM build and revise a task-specific **Decision State Graph (DSG)** that links the problem, source-grounded knowledge, decision elements and candidate decisions. The agent uses the graph to direct its tool queries, sees the updated graph after every edit, and reviews its proposal against the graph before committing.

The paper also introduces **K2D-Bench**: 48 frozen worlds built from official public data in eight public-administration domains. Each world has a deterministically scored Closed task and an LLM-judged Open planning task.

With DeepSeek V4 Flash, against ten baselines, K2D ties LATS on Closed (75%), has the best Open score (76.47) and has no hard-constraint violations. Ablations point to post-edit graph feedback as the most important component. Averaged over four backbones, K2D's Closed gains over ReAct and Vanilla hold.

---

## Review

**Quality.** The benchmark engineering is careful: frozen and hashed public sources, one shared tool interface, deterministic Closed scoring and a leakage-aware split. The main claims, however, are weakly supported.

The results come from single runs with no seeds, CIs or tests, and the headline margins are tiny. Out of 48 Closed tasks, K2D ties LATS (36 vs 36), beats Vanilla by 1 task and beats Claude Code and Codex by 2. Even if every differing task favoured K2D, exact McNemar would give only p = 1.0 against Vanilla and 0.5 against Claude Code/Codex. The Open leads are 1.6–2.0 judge points, and "zero HCV" is 0/48 against 1–2/48.

All 96 tasks are reported, even though two families are designated for development. The "decisive-evidence acquisition" measure is undefined and sits at 100% for every system, so the pre-acquisition failure the method targets is never observed. No control separates the graph from a plain notes file. Every ablation scores below the graph-free Vanilla agent on Closed, and Table 3 contradicts the claim that "only" removing post-edit feedback degrades all metrics.

Compute, baseline adaptation and the backbones used for Claude Code and Codex are unreported. The three LLM judges are unnamed, and the human audit covers only 12 cases (Pearson 0.396). RQ3 appears only as a radar plot clipped at 50. The mechanism claim rests on a single Figure 5 trace, and in it all edges appear only in the final revision.

**Clarity.** The prose is fluent and Figure 1 conveys the idea well, but the paper is hard to verify or reimplement. The core components are described only in prose: the projection $\Phi$, the edit API, the skill text, the review $\Psi$ and the "No post-edit" condition. The formalism is never used. There is no appendix with decoding settings, judge prompts, baseline adaptations, or an account of how the benchmark tasks were authored. The benchmark section relies on undefined jargon ("protected Open authority", "source–receipt binding", "hash-bound at one cutoff").

There are also presentation problems:
- Figure 2 has a typo ("Hidden Constrainies") and duplicated sub-captions.
- Figure 5 is unreadable.
- Experiments are labelled E1–E3 in some places and RQ1–RQ3 in others.
- Table 1 defines metrics (D, F, R, A and a family macro) that are never reported.
- Results are given as percentages, without counts or uncertainty.

**Originality.** The paper's new contribution is a decision-typed state that the agent writes and revises as it gathers evidence, seeing the updated graph after each edit. It also contributes a matched Closed/Open benchmark built on frozen public data.

The novelty is narrower than claimed. The K2D gap overlaps three known problems: context utilisation, knowledge conflict and the LLM "knowing-doing gap". The DSG closely echoes established methods from decision analysis (PrOACT, influence diagrams, value of information), argumentation and IBIS, and Analysis of Competing Hypotheses.

The closest LLM competitors are neither cited nor used as baselines: DeLLMa (ICLR 2025), DecisionFlow (Findings of EMNLP 2025), STRUX (NAACL 2025) and Argumentative LLMs (AAAI 2025). The same goes for structured-memory methods (CoALA, MemGPT, A-Mem) and self-verification methods (Self-Refine, CRITIC). There is no related-work section, and all 18 references are from CS.

**Significance.** If the results hold up, "explicit decision state with read-back" would be a reusable design principle, and the benchmark template could transfer to other domains. As it stands, the paper does not show that the decision-typed graph itself matters.

For the AISI track, the social-impact case is thin:
- There is no concrete problem, decision-maker, affected population, deployment path or user study. A user study is needed for the DSG's most natural benefit: auditability for human officials.
- There is no ethics statement, although the paper motivates agents that "determine eligibility".
- The Limitations section is two sentences long.
- The "Safety" metric actually measures constraint compliance.

### Strengths (pros)

1. **A clear, testable design hypothesis:** knowledge enters the decision state only through explicit, agent-authored edits that the agent then reads back.
2. **Careful, reusable benchmark design:** official frozen sources with provenance and hashes, deterministic replay, a leakage-aware split, matched Closed/Open tasks, and a mix of document and structured-record queries.
3. **Broad evaluation:** general, knowledge/graph and industrial baselines, component ablations, and four backbones.
4. **Candid reporting of some negative results:** the tie with LATS, lower C-Support, losses to ReAct on Open for two backbones, and the unfavourable audit numbers.
5. **Socially relevant domains** built from real public data.

### Weaknesses (cons)

1. Headline gains are 0–4 of 48 tasks from single runs, with no statistical testing.
2. The development families are included in the reported results.
3. The pre-acquisition claim is untested: the acquisition metric is undefined and at 100% for every system.
4. The graph's own contribution is not isolated, and the ablation narrative contradicts Table 3.
5. Compute, baseline adaptation and the industrial systems' backbones are unreported.
6. The Open evaluation is weakly validated: the judges are unnamed and the human audit covers only 12 cases.
7. RQ3 is shown only as a clipped radar plot, and the mechanism claim rests on a single trace.
8. Engagement with the literature is weak: nothing from outside CS, and the closest competitors are missing.
9. The social-impact case is thin, and there is no ethics statement.
10. The work cannot be reproduced: there is no code, data, prompts or appendix.

**What would change my assessment:**
- results on the test families only;
- at least three seeds, with CIs and paired tests;
- a notes-file control that keeps the same loop;
- a defined, per-system acquisition metric;
- a per-backbone RQ3 table;
- cost reporting, and the backbones used for Claude Code and Codex;
- named judges, a larger audit and all five rubric dimensions;
- a release commitment;
- a related-work section and an ethics statement.

---

## Strengths And Weaknesses

**1) Significance of the problem — 2 (Fair).**
- *Strength:* evidence-grounded decision support in public administration is important. Making explicit *how* a piece of evidence changes a decision is relevant to accountability and contestability.
- *Weakness:* the paper does not define a concrete social-impact problem. It names no decision-maker, affected population, current error or harm, or deployment context. The domains serve as test beds (six worlds each) rather than as problems the paper sets out to solve. The "AI4SS" framing has no citation and does not fit the tasks well: AI4SS usually means AI as a tool for social-science research, whereas these are operational public-administration decisions.

**2) Engagement with literature — 2 (Fair).**
- *Strength:* covers the core RAG, planning and graph-memory agent literature, and cites work on context utilisation and knowledge competition to motivate the gap.
- *Weakness:* there is no related-work section and all 18 references are CS. The closest competitors, LLM methods that already structure decisions explicitly (DeLLMa, DecisionFlow, STRUX, ArgLLMs, LLM-built influence diagrams), are missing and are not used as baselines. There is no engagement with decision analysis, argumentation, structured analytic techniques, public-sector algorithmic decision-making or automation bias, all of which bear directly on the DSG's design and its intended use (details in the Review).

**3) Significance to the AI community — 2 (Fair).**
- *Strength:* agent-authored, revisable decision state with read-back after each edit is a clean, general hypothesis. The matched Closed/Open, frozen public-data benchmark design could be reused in other domains.
- *Weakness:* the evidence does not yet show that the *decision-typed graph* matters. There is no control with a generic persistent scratchpad. Gains over the strongest baselines are 0–2 tasks, and the headline mechanism result is a contrast with an agent that writes state it cannot see.

**4) Soundness — 2 (Fair).**
- *Strength:* deterministic Closed scoring, frozen and hashed sources with replay, and matched ablations, backbones and baselines, all under one shared tool interface.
- *Weakness:* single runs with no uncertainty; margins of 0–4 of 48 tasks. Development families are included in the reported results. The acquisition diagnostic is undefined and at 100% for everyone, so the pre-acquisition claim is untested. One RQ2 sentence is contradicted by Table 3. Compute is unbudgeted and unreported, and baseline adaptation and the industrial systems' backbones are unspecified. The judge panel is unnamed, with a small, mislabelled human audit. RQ3 appears only as a clipped radar plot. Details are in the Quality section of the Review.

**5) Facilitation of follow-up work — 1 (Poor), as submitted.**
- *Strength:* the benchmark is engineered for reproducibility (hashes, terms, deterministic tool replay, leakage checks).
- *Weakness:* there is no code, data or benchmark release statement, no anonymised link and no appendix. The skill text, graph-edit API, projection function, review prompt, baseline adaptations, judge models and prompts, rubrics, and the pipeline for writing worlds, candidates and reference plans ("scenario generation") are all unspecified. Neither K2D nor K2D-Bench could be rebuilt from the paper.

**6) Scope and promise for social impact — 2 (Fair).**
- *Strength:* the domains are socially relevant and drawn from real public sources. An explicit, source-linked decision graph is a plausible basis for auditable, contestable decision support.
- *Weakness:* worlds use frozen, sometimes "benchmark-defined decision roles rather than real institutional policy". There are no stakeholders or practitioners in problem formulation, no user study, and no test of whether the DSG is faithful to the decision or useful to a human reviewer. Cost and latency are not reported. "Zero HCV" (0/48 vs 1–2/48) is not statistically distinguishable from the baselines, and the rubric has no equity dimension. Substantial additional work is needed before practical impact.

**Presentation quality.** The prose is fluent and Figure 1 conveys the idea well. However:
- the text is dense with undefined jargon;
- Figure 2 has a typo and copy-pasted panels;
- Figure 5 is unreadable;
- Figure 4 clips data;
- several defined metrics are never reported;
- naming is inconsistent (E# vs RQ#);
- percentages are given without counts or uncertainty;
- the abstract and contributions state more than the paper's own caveats support.

---

## Questions For The Authors

1. **Development vs test.** What were the two development families used for (skill, metamodel, review prompt, judge rubric)? Please report Tables 2–3 on the six test families only.
2. **Variance.** What decoding settings were used? Can you report at least 3 seeds with CIs and paired tests (McNemar for Closed, paired permutation or Wilcoxon for Open)? Which orderings in Tables 2–3 survive?
3. **Acquisition.**
   - How is "decisive-evidence acquisition" defined and measured, including for Claude Code and Codex?
   - How does 100% acquisition fit with the 43.75% C-Support of IRCoT and HippoRAG?
   - Since acquisition is 100% for every system, what evidence supports the claim that K2D fixes *pre*-acquisition failures?
4. **Graph vs notes.** Can you add a control with the same skill and review loop, but a free-text notes file returned after every edit instead of the graph? An untyped graph would also help. How exactly is "No post-edit" implemented, given that the agent observes $\Phi(G_t)$ at every turn?
5. **Ablations below Vanilla.** Why does every single-component ablation score below the graph-free Vanilla agent on Closed (70.83 / 68.75 / 66.67 vs 72.92)?
6. **Baselines and compute.**
   - Which backbone and version did Claude Code and Codex use?
   - How were IRCoT, HippoRAG, AriGraph and LATS adapted?
   - Please report tokens, tool calls and cost per task.
   - Why does one Claude Code Open task seem to be missing (its rates only work out over 47 tasks)?
   - Please give invalid-output counts per system.
7. **Judging.** Which three LLMs form the panel, and do any of them overlap with the agent backbones? Who decides HCV and Open validity? Please report all five rubric dimensions (D, F, K, R, A).
8. **RQ3.** Please give a per-backbone table (Closed k/48, Open mean ± SE, HCV) and a pooled stratified test. Why is ReAct much weaker than Vanilla only on Flash? What happened with the Qwen3.6 and DiffusionGemma runs?
9. **Closed failures and benchmark authorship.** How do Closed failures break down (wrong option, missing fields, constraint violation, invalid output)? Who or what wrote the worlds, candidates, rules, rubrics and reference plans? How many experts reviewed them, and with what qualifications?
10. **DSG dynamics.** In Figure 5, all edges appear only in the final revision. Across all episodes, when are relational edges written relative to the last acquisition? Does perturbing a decisive Knowledge node change the decision?
11. **Intended use and release.** Is K2D meant to recommend or to decide? Has any practitioner assessed whether the DSG helps them audit or contest a decision? Will the benchmark, harness, skill, prompts and rubrics be released, and under what licences?

---

## Ethical Considerations

No. The paper has no ethics or broader-impact statement, even though it motivates agents that "determine eligibility, prioritize an intervention", and its benchmark covers housing services, food and product safety, clinical trials and 311 requests. It does not say whether K2D recommends or decides. It also does not discuss human oversight, accountability, contestability or automation bias. This matters because a persuasive, source-linked graph could increase over-reliance even when, as the Limitations admit, it "may omit requirements, misread evidence, or remain inconsistent". The Open rubric has no equity or affected-party dimension, and "Safety" (100 − HCV) measures constraint compliance, not safety for people. On data, the paper does not report source terms, licensing or redistribution plans, and some sources may contain identifying information (NYC HPD registration contacts, business names in inspection records, 311 request locations). It does not describe how the human experts were recruited, their qualifications, their compensation, or IRB status, and the two-sentence Limitations section should be expanded. I do not think a specialised ethics review is needed, provided the authors add an ethics statement, a data statement and expanded limitations.

---

## Comments (confidential to SPC and Program Chairs)

My recommendation is Weak Reject. The idea and the benchmark engineering have merit, but the evidence does not yet support the claims. After converting percentages to task counts, K2D ties LATS on Closed (36/48 each), beats the graph-free Vanilla agent by 1 task, and beats Claude Code and Codex by 2, all from single runs. The "clearest mechanism-level" ablation is 36 vs 32 of 48, with a best-case *p* ≈ 0.125. Results pool the development and test families. The acquisition diagnostic that is supposed to separate failure types is undefined and at 100% for every system, so the pre-acquisition half of the story is untested.

For the rebuttal, the most decision-relevant answers would be:
- test-only numbers;
- multi-seed results;
- a graph-free control with the same loop;
- a per-backbone RQ3 table.

The four-backbone pooled Closed advantage (about +16 to +21 net tasks over 192 paired tasks) may turn out to be the paper's strongest evidence if it is tested properly.

On AISI fit, this is primarily a general LLM-agent architecture paper evaluated on public-sector-flavoured tasks. It has no stakeholder engagement, no user evaluation and no ethics statement.

I reviewed only the 8-page PDF. If supplementary material with code or data exists, my Facilitation score (1) should be read as provisional.

---

## Post Rebuttal Comment

*(To be completed after the author response.)*
