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

1. **Development versus test.** What were the two development families used for (skill, metamodel, review prompt, judge rubric, benchmark construction)? Please report Tables 2 and 3 on the six test families only (36 Closed / 36 Open tasks).
2. **Variance.** What decoding settings were used? Can you report at least 3 seeds for K2D, LATS, Vanilla, ReAct and the three ablations, with CIs and paired tests (exact McNemar for Closed; paired permutation or Wilcoxon for Open)? Which orderings in Tables 2 and 3 survive?
3. **Decisive-evidence acquisition.** How is it defined and measured, including for Claude Code and Codex? How does 100% acquisition for IRCoT and HippoRAG fit with their 43.75% C-Support? Since acquisition is at ceiling for every system, what evidence supports the claim that K2D addresses *pre*-acquisition failures? Are there tasks where decisive evidence is hard to find?
4. **Graph versus any persistent notes.** Can you add (a) the same skill and review loop with a free-text notes file returned after every edit, and (b) an untyped graph without the metamodel? How exactly is "No post-edit" implemented, given that the agent observes $\Phi(G_t)$ at every turn?
5. Why does every single-component ablation score *below* the graph-free Vanilla agent on Closed (70.83 / 68.75 / 66.67 vs 72.92)?
6. **Industrial systems and invalid outputs.** Which backbone, version and configuration did Claude Code and Codex use, and were their native tools disabled? What happened to the Claude Code Open task that the 47-task denominator implies? Please give invalid-output counts per system and backbone.
7. **Compute.** What are the mean tokens, tool calls, turns, wall-clock time and cost per task for each system? How does K2D compare with LATS at a matched budget?
8. **Judging.** Which three LLMs form the panel, and do any overlap with the agent backbones? How are Open validity and HCV decided (rules, judges or experts)? Please report D, F, R and A per system, and describe any control for length or format bias.
9. **RQ3.** Please give a per-backbone table (Closed k/48, Open mean ± SE, HCV k/48) and a stratified pooled test. Why is ReAct on Flash so much weaker than Vanilla (−12.5) when it beats Vanilla on the other backbones? What happened in the Qwen3.6 and DiffusionGemma runs?
10. **Closed failures.** How do they break down (wrong option / missing required fields / constraint violation / invalid submission)? What is option-only accuracy? What are the candidate-set sizes and the chance baseline, and how does a no-tool (closed-book) agent perform?
11. **Benchmark authorship.** Who or what wrote the worlds, candidate sets, rules, rubrics and reference plans, and which LLMs, if any, were used? How many worlds were admitted or rejected? How many experts took part, with what qualifications and what agreement? Were any of them practitioners in these domains?
12. **DSG dynamics.** In Figure 5 both DeepSeek traces add all edges in the final revision. At population level, when are relational edges written relative to the last acquisition? What fraction of inquiry nodes lead to tool calls? Does perturbing a decisive Knowledge node change the decision (faithfulness)?
13. **Intended use and release.** Who would use K2D, and is it meant to recommend or to decide? Has any practitioner assessed whether the DSG helps them audit or contest a decision? Will K2D-Bench, the replay harness, the skill, prompts and rubrics be released, and under what licences given the source terms?

---

## Ethical Considerations

The paper does not adequately address the relevant ethical considerations, although I do not think it needs a separate specialised ethics review provided the following are added:

- **Intended use and risk.** The Introduction motivates agents that "determine eligibility, prioritize an intervention", and the families include housing services, food and product safety, clinical-trial reporting and 311 requests. Yet there is no ethics or broader-impact statement, and nothing about the following:
  - whether the system recommends or decides;
  - human oversight;
  - accountability;
  - contestability for affected people;
  - automation bias. A persuasive, source-linked decision graph may *increase* over-reliance even when, as the Limitations admit, the graph "may omit requirements, misread evidence, or remain inconsistent".
- **Fairness and equity.** Objectives and constraints are fixed by the benchmark authors (sometimes as "benchmark-defined decision roles"). The Open rubric (D/F/K/R/A) has no dimension for distributional effects or affected parties. The paper should discuss whose values the objectives encode. Labelling 100 − HCV as "Safety" should be reconsidered, since it concerns constraint compliance, not safety for people.
- **Data.** The paper records source "terms" but does not report them, the licensing, or any redistribution plan. Some sources can contain identifying information: NYC HPD registration contacts, business names and licence numbers in inspection data, locations of 311 requests. A data statement on identifying fields and how they were handled is needed.
- **Human participants.** The admission reviewers, "two domain experts" and "three blinded experts" are undocumented. The paper should report their recruitment, qualifications, compensation and IRB or exemption status.
- **Limitations.** The two-sentence Limitations section should be expanded. It should cover single-run evaluation, jurisdictions limited to English-speaking UK/EU/North American sources, the gap between frozen single-answer worlds and real discretionary decisions, and harmful failure modes such as confident wrong determinations.

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
