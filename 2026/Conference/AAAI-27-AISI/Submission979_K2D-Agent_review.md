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

The paper names a *knowledge-to-decision (K2D) gap* in LLM agents, which it says occurs at two stages:

- **Before acquisition:** latent decision dependencies do not reveal what the agent needs to find out.
- **After acquisition:** retrieved evidence sits in the context window but never explicitly changes the decision state.

**K2D-Agent.** A single LLM agent maintains a task-instance **Decision State Graph (DSG)**:

- An advisory metamodel with four node classes (Problem, Knowledge, Decision Elements, Candidate Decisions) and typed edges (support, challenge, dependence, satisfaction, violation, harm), with scope, uncertainty and provenance kept as properties.
- The agent uses unresolved structure in the graph to decide what to look up with SEARCH/READ/QUERY tools.
- It writes findings back as atomic, agent-authored graph edits and receives the updated graph after each edit.
- It performs one graph-grounded review before committing.
- A "recommended operating skill" guides graph use without fixing a tool sequence.

**K2D-Bench.** 48 frozen worlds built from official public data in eight families (UK Parliament, Calgary traffic and flood, Chicago food inspections, EU Safety Gate, NYC HPD, ClinicalTrials.gov, Vancouver 3-1-1). Each world yields two matched tasks:

- a **Closed** task: a finite candidate set, scored deterministically;
- an **Open** task: a bounded action plan, scored by a blind three-LLM panel, with a hard-constraint violation (HCV) capping the score at 49.

**Results.**

- **RQ1 (DeepSeek V4 Flash, 10 baselines including Claude Code and Codex):** K2D ties LATS on Closed (75.00%), has the highest Open score (76.47) and has 0% HCV.
- **RQ2 (ablations):** removing the skill, post-edit graph feedback, or the final review lowers Closed accuracy. Removing post-edit feedback lowers it most (66.67%).
- **RQ3 (four complete backbones):** K2D averages +8.33 Closed points over ReAct and +10.94 over Vanilla. Open gains are small and depend on the model.
- **Judge audit:** a 12-case human audit reports moderate judge–expert rank agreement.

---

## Review

### Overall assessment

The paper asks a relevant question: does an explicit, revisable decision state help LLM agents turn evidence they have retrieved into better commitments? The benchmark engineering is careful: frozen and hashed public snapshots, a shared tool interface, deterministic Closed scoring, leakage-aware splits, and matched Closed/Open tasks. The authors are also candid in places. They say K2D only ties LATS on Closed, that it trails on C-Support, and that it loses to ReAct on Open for two backbones, and they label Figure 5 as illustrative.

However, the central empirical claims are not supported at the level of confidence the abstract and contributions imply:

- The Table 2 and Table 3 differences that carry the argument amount to 0–4 tasks out of 48, each from a single run.
- The development families appear to be included in every reported number.
- The diagnostic meant to separate acquisition failures from use failures is undefined and sits at 100% for every system. The "pre-acquisition" half of the K2D claim is therefore never tested.
- No condition isolates the graph itself from any persistent, re-read scratchpad.

For the AISI track, the social-impact case is also underdeveloped. There are no stakeholders, no intended users, no deployment pathway, no evaluation of the DSG's natural selling point (auditability), no ethics statement, and no engagement with literature outside CS. I think this could become a good paper with the analyses requested below, but in its current form I lean toward rejection.

### Pros

1. **Well-motivated representational idea.** The graph is task-instance and decision-centric, not corpus-centric. Knowledge enters the decision state only through agent-authored edits, and the agent sees the updated graph after each edit. This is a clear design hypothesis that can be tested.
2. **Thoughtful benchmark design.** Matched Closed/Open tasks share one world. Sources are official and frozen, with publisher, URL, terms and content hash recorded. Replay is deterministic, and the split is designed to prevent leakage across source, entity, time, rule and near-duplicate groups. This mix of documents and structured records needing row-level queries is closer to real administrative decisions than most QA-style agent benchmarks, and may be the paper's most lasting contribution.
3. **Broad comparison.** The baselines cover general agents, knowledge/graph agents and two industrial agents. There are component ablations and a four-backbone transfer study.
4. **Honest reporting of some negative results,** as noted above, and a human audit whose unfavourable numbers are reported rather than hidden (Pearson 0.396, a +14.83 offset).

### Major concerns

**M1. The headline differences are within single-run noise.** Each configuration "runs once on all 96 tasks" and the paper gives no seeds, temperature, SDs, CIs or significance tests. Converting Table 2 and Table 3 to counts out of 48 Closed tasks gives:

| Comparison | Closed (k/48) | Tasks behind K2D (36/48) | Best-case exact McNemar *p* (all discordant pairs favour K2D) |
|---|---|---|---|
| LATS | 36 | 0 | – |
| Vanilla Tool Agent | 35 | 1 | 1.00 |
| Reflexion / KnowAgent-AK / Claude Code / Codex | 34 | 2 | 0.50 |
| AriGraph | 32 | 4 | 0.125 |
| ReAct | 29 | 7 | 0.016 (fails a Holm correction across the 10 baselines) |
| No skill / No review / No post-edit | 34 / 33 / 32 | 2 / 3 / 4 | 0.50 / 0.25 / 0.125 |

The 95% Wilson interval for K2D's own 36/48 is [61.2%, 85.1%], which covers every system from AriGraph upward.

- **Open:** K2D leads by 1.57 over ReAct, 1.89 over LATS and 1.98 over KnowAgent-AK, on a 0–100 LLM-judged scale, with no variance reported. The paper's own audit section cautions "against interpreting small Open differences as evaluator-independent effects". Yet the claim of the "strongest combined Closed/Open performance" rests on exactly these margins, because Closed is a tie.
- **HCV:** "zero observed HCV" is 0/48 against 1/48 for LATS (Fisher *p* = 1.0) and 2/48 for most baselines (*p* ≈ 0.49). Because an HCV caps an Open score at 49, "best Open" and "zero HCV" partly count the same one or two tasks twice.

**M2. The development families are included in the reported results.** Figure 3 and the text describe a "2 Dev + 6 Test families" split, but Table 2 is "E1 on all 96 tasks", and the ablations and audit also cover all families. The paper never says what the development families were used for. If the operating skill, metamodel, review prompt or judge rubric were iterated on them, 25% of the reported tasks are in-sample for K2D and not for the baselines. With margins of 0–2 tasks, this could change the ranking. The results should be reported on the six test families only (36 Closed and 36 Open tasks).

**M3. The acquisition-versus-use diagnostic is undefined and saturated, so the pre-acquisition claim is untested.** The paper's causal argument rests on this sentence: "all methods acquire the declared decisive evidence on every Closed task … the gain is better explained by decision use". RQ2 adds that "All ablations retain 100% decisive-evidence acquisition … locating the loss after retrieval". Three problems follow:

- **The measure is not defined anywhere.** It is not in Table 1 and is never tabulated. It is not explained how it was measured for the black-box Claude Code and Codex. It also sits uneasily beside a C-Support of 43.75% for IRCoT and HippoRAG. The two can be reconciled (evidence can be acquired without being cited), but the paper must say how.
- **Pre-acquisition failure is never observed.** The measure is 100% for all 11 systems and all 3 ablations, so the benchmark never produces the failure that motivates half the method: Figure 1's "FAILURE 1" and the DSG-guided inquiry. As a result, the abstract's claim that K2D "addresses pre- and post-acquisition K2D failures" and contribution (2)'s diagnostics that "separate knowledge-acquisition from knowledge-use failures" are only half supported.
- **C-Support is not a clean acquisition measure either.** It combines two procedures in one column ("required-source coverage substitutes when logs are unavailable") and depends on citations in the final output.

**M4. The graph itself is never isolated, and the ablation narrative does not match Table 3.**

- **No graph-free control with the same loop.** RQ2 removes the skill, post-edit feedback or review, but no condition keeps the loop while replacing the typed DSG with an unstructured, persistent notes file that is also returned after each edit.
- **The key ablation is a weak contrast.** The "No post-edit" condition compares K2D with an agent that writes state it cannot see. Standard tool loops and memory-editing agents return the result of a write by default. The result therefore shows that writing without reading back hurts, not that a decision-typed graph helps.
- **Every ablation falls below no architecture at all.** On Closed, each single-component ablation scores below the graph-free Vanilla agent (72.92): No skill 70.83, No review 68.75, No post-edit 66.67. So removing any one part is worse than having no K2D architecture. Either the components are strongly interdependent, or noise of ±2–4 tasks dominates. The design cannot tell these apart.
- **"Only" is false.** The sentence "Only removal of post-edit feedback simultaneously degrades Closed, Open, and Judge agreement" is contradicted by Table 3: all three ablations lower Closed and Open and raise J-disagree.
- **The functional attribution does not follow either.** "The skill chiefly improves support coverage, while review improves commitment" is not what Table 3 shows: No review also cuts C-Support by 8.34 points (4 tasks), more than its Closed drop.
- **The post-edit condition is unspecified.** The agent observes $O_t=\Phi(G_t)$ at every turn, so it is unclear what "No post-edit" removes.

**M5. Fairness of the comparison is under-specified.**

- **Compute:** there is "no explicit tool or token budget", and no tokens, tool calls, turns, time or cost are reported for any system. K2D's edit/observe/review loop and LATS's tree search may simply use more compute.
- **Baseline ports:** the paper does not describe how IRCoT, HippoRAG and AriGraph (designed for static multi-hop QA or games) or LATS and Reflexion (value and feedback sources, rollouts) were adapted to an interactive SEARCH/READ/QUERY decision environment. The conclusion that "retrieval graphs or world-model memory are not sufficient substitutes" depends on how faithful these ports are.
- **Industrial systems:** Claude Code and Codex are "official releases evaluated as black boxes", but the paper does not say whether they ran on DeepSeek V4 Flash or on their native models, which versions were used, or whether their native tools were disabled. If they used native models, backbone and architecture are confounded.
- **A missing Claude Code task:** Claude Code's HCV (6.38) and J-disagree (21.28) only work out as 3/47 and 10/47. Every other rate in Table 2 is out of 48. This is probably one invalid Open output, which the protocol allows, but it should be disclosed, together with invalid-output counts for every system. Each invalid output moves an Open mean by about 1.5 points, which is comparable to K2D's Open margins.
- **Format versus correctness:** Closed success requires "exact option selection satisfying hard constraints *and required fields*". K2D explicitly turns "process or submission requirements" into graph elements and re-checks them in review, so part of its Closed advantage may be format compliance. A failure breakdown is needed: wrong option, missing fields, constraint violation, invalid submission.
- **Missing baseline type:** no decision-structured baseline is included (see Literature below).

**M6. The Open evaluation is weakly validated.**

- **Unnamed judges:** the three judge LLMs are never named, so self-preference toward the DeepSeek or GPT backbones cannot be checked. A preference for K2D's evidence-linked, structured output format is also plausible and untested.
- **Small audit:** it covers 12 cases, sampled by disagreement stratum rather than at random. With n = 12, Pearson 0.396 has a 95% CI of roughly [−0.23, 0.79] and Spearman 0.586 roughly [0.02, 0.87].
- **Mislabelled reliability:** ICC(2,k) = 0.587 is described as "within-expert consistency", but it is the inter-rater reliability of the three-expert mean. The implied single-rater ICC(2,1) is about 0.32.
- **No system-level check:** the audit correlates individual cases, not systems, so "ordering is broadly preserved" does not show that K2D really beats ReAct or LATS on Open.
- **Missing dimensions:** only K and R correlations are reported. D/35 and F/25 carry 60% of the rubric weight and are omitted, and in Tables 2–3 only K/20 of the five rubric dimensions appears at all. F/25 (feasibility and constraints) is the natural evidence for the paper's "constraint-sensitive commitment" claim.
- **J-disagree is not a quality measure:** it is marked "↓ better" and used as mechanism evidence, but it measures evaluator reliability. HippoRAG, the second-worst Open system, has the lowest (bolded) value.

**M7. RQ3 is reported only as a truncated radar plot, and the averages hide heterogeneity.** Figure 4's radial scale starts at 50, and the MiniMax M3 Vanilla Closed point falls below that floor and is clipped. Taking the Flash numbers out of the reported averages, the other three backbones average:

| Contrast | Closed | Open |
|---|---|---|
| K2D over ReAct | +6.25 (≈3 tasks per backbone) | +0.22 |
| K2D over Vanilla | +13.89 | +2.64 |

- **Flash's ReAct looks anomalous.** ReAct − Vanilla on Closed is −12.5 on Flash but about +7.6 on the other backbones. That anomalous run supplies RQ1's headline "14.58 Closed points over ReAct".
- **Zero HCV is not specific to K2D here.** In the GPT-5.5 panel, all three systems sit at Safety = 100.
- **The strongest evidence is untested.** The pooled evidence, 192 paired Closed tasks with net +16 tasks over ReAct and +21 over Vanilla, may be the paper's most defensible result, but it is never tested (e.g. with a CMH or mixed-effects logistic model with task and backbone effects).
- **Missing results:** the paper needs a per-backbone table. The partial Qwen3.6 and DiffusionGemma runs are mentioned twice but never reported.

**M8. The mechanism narrative leans on one trace, and that trace suggests the relations are written at the end.** "Figure 5 illustrates that relational integration matters more than graph size" is concluded from one task across three different LLMs, so graph structure is confounded with the backbone.

- **When edges appear:** in both DeepSeek traces, every edge appears in the final revision (Flash: revision 2 has 19 nodes / 0 edges, revision 3 has 19 / 18; Pro: revision 3 has 16 nodes / 0 edges, revision 4 has 16 / 27). The relations linking evidence to candidates are therefore written in one batch at commitment time, not incrementally while guiding inquiry. That is closer to the "post-hoc explanation" the paper says the DSG is not.
- **Missing statistics:** the paper gives no population-level DSG statistics, such as revisions per episode, edges added before versus after the last acquisition, the fraction of inquiry nodes that led to tool calls, or unresolved dependencies at commit time.
- **Faithfulness untested:** there is no test of whether the graph actually drives the decision, e.g. by perturbing a decisive Knowledge node.

**M9. The AISI social-impact case (see also Strengths and Weaknesses).**

- **No concrete problem:** the paper does not define a concrete social-impact problem, decision-maker, affected population or baseline harm. It is a general agent architecture evaluated on public-sector-flavoured tasks, and the only concrete tasks shown are flood-resilience planning.
- **Recommend or decide?** The Introduction motivates the work with agents that "determine eligibility, prioritize an intervention", but the paper never says whether K2D is meant to recommend or to decide.
- **Auditability untested:** the most plausible social-impact route is the DSG as an auditable, contestable decision record for human officials, but it is not evaluated with any human user.
- **No ethics statement, short Limitations:** there is no ethics or broader-impact statement, and the Limitations section is two sentences long.
- **Misleading "Safety" label:** relabelling 100 − HCV as "Safety" invites a reading about safety for affected people that the metric does not support.
- **No equity dimension:** the Open rubric has no equity or affected-party dimension, even though the families include housing services.

### Literature (details for the "Engagement" rating)

There is no related-work section; prior work is compressed into one Introduction paragraph. All 18 references are CS/NLP papers or product pages. The abstract claims that "existing decision-oriented LLM agents typically place retrieved material in context", yet no decision-oriented LLM agent is cited, and the AI4SS framing has no citation. The closest competitors are missing:

- **LLM methods that already make decision structure explicit:**
  - DeLLMa (Liu et al., ICLR 2025)
  - DecisionFlow (Chen et al., Findings of EMNLP 2025)
  - STRUX (Lu et al., NAACL 2025)
  - Argumentative LLMs (Freedman et al., AAAI 2025)
  - LLM-constructed influence diagrams (e.g. LAMDA, *Decision Analysis*, 2025)

  At least one of these should be a baseline.
- **Structured and agent-authored memory:** CoALA (Sumers et al., TMLR 2024), MemGPT (Packer et al., 2023), A-Mem (Xu et al., NeurIPS 2025), Graph of Thoughts (Besta et al., AAAI 2024), Think-on-Graph (Sun et al., ICLR 2024).
- **Self-verification, relevant to the review step:** Self-Refine, CRITIC, Chain-of-Verification.
- **Related gap framings:** the LLM "knowing-doing gap" (Schmied et al., ICLR 2026); the knowledge-conflict survey (Xu et al., EMNLP 2024).
- **Benchmark positioning:** τ-bench (Yao et al., ICLR 2025); requirements for public-sector agent benchmarks (Rystrøm et al., IASEAI 2026).
- **Outside CS, which the DSG closely echoes:**
  - decision analysis: PrOACT (Hammond, Keeney & Raiffa 1999), influence diagrams (Howard & Matheson 1984), value of information (Howard 1966). The inquiry-creation rule is essentially an informal value-of-information criterion.
  - argumentation and design rationale: Toulmin (1958), Dung (1995), bipolar argumentation (Cayrol & Lagasquie-Schiex 2005), IBIS (Kunz & Rittel 1970).
  - structured analytic techniques: Analysis of Competing Hypotheses (Heuer 1999), and evidence that ACH can increase inconsistency (Dhami et al. 2019).
  - automation bias and public-sector algorithmic advice: Skitka et al. (1999); Alon-Barkat & Busuioc (2023, JPART).
  - the implementation-science "knowledge-to-action gap" (Graham et al. 2006).

With these in view, the novelty is narrower than claimed, though it is real: incremental, tool-driven, agent-authored decision state interleaved with acquisition, plus read-back after each edit.

### Minor issues and presentation

- **Figure 2:** it contains the typo "Hidden Constrainies". The Reflective Deliberation row repeats the Decision Workflow sub-captions word for word, so Propose / Review DSG / Revise-or-Commit are never actually described. The "Constrain" edge label is not among the edge types listed in the text.
- **Figure 5:** node labels are truncated and overlapping, edge types have no legend, and an internal task ID ("TASK-5F32A2F71D269400") and "1 nodes" appear in the figure. For GPT-5.5, "Initial" and "Middle" are the same revision-1 snapshot.
- **Figure 4:** the radial axis starts at 50 and clips data, and the normalisation of D and K is not stated. A table would be clearer.
- **Naming:** E1/E2/E3 appear in captions and RQ1–RQ3 in the text. "Categories are separated by rules" (Table 2 caption) is unclear.
- **Unused metrics:** Table 1 defines D, F, R, A and a family macro that are never reported. With six worlds per family, the family macro equals the plain mean, so a per-family breakdown would be more informative.
- **Formalism:** $\mathcal{P}=(q,\mathcal{A},\mathcal{O},\mathcal{C},x_0,\mathcal{E})$, $\pi_\theta$, $\Phi$ and $\Psi$ are introduced but not used operationally. $\Phi$ is never defined and $R_t$ is never used again. Concrete specifications of the edit API, the projection returned after each edit, the skill text and the review prompt would be far more useful.
- **Undefined jargon:** "protected Open authority", "source–receipt binding", "created in an unpassed state", "hash-bound at one cutoff", "benchmark-field extraction", "final feedback edge".
- **"Holding information constant":** Closed tasks expose candidates and rules that Open tasks never see, so information is not held constant; only the world and sources are. The Closed/Open pairing is also never analysed as a pairing.
- **Industrial systems** are cited by product page without the version evaluated.

### What would change my assessment

In rough order of importance:

1. Test-family-only results.
2. At least three seeds per configuration, with CIs and paired tests.
3. A graph-free control that keeps the same loop (a persistent notes file returned after each edit), plus a definition of "No post-edit".
4. An operational definition and per-system reporting of decisive-evidence acquisition, plus some tasks where acquisition is actually hard.
5. A per-backbone RQ3 table with a pooled, stratified test.
6. Compute and cost reporting, and the backbone and configuration used for Claude Code and Codex.
7. Named judges, all five rubric dimensions, and a larger, system-level human audit.
8. A release commitment.
9. A related-work section, an ethics statement, and a clearer account of intended human use.

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
- *Weakness:* single runs with no uncertainty; margins of 0–4 of 48 tasks. Development families are included in the reported results. The acquisition diagnostic is undefined and at 100% for everyone, so the pre-acquisition claim is untested. One RQ2 sentence is contradicted by Table 3. Compute is unbudgeted and unreported, and baseline adaptation and the industrial systems' backbones are unspecified. The judge panel is unnamed, with a small, mislabelled human audit. RQ3 appears only as a clipped radar plot. See M1–M8.

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
