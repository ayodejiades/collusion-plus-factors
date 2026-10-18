# Interview

Answer in your own words, typed or dictated. Write each answer under its question. The "> " prefix is optional: anything you type under a question counts as its answer, and blank lines separate paragraphs. rops-outline assemble copies your answers into paper/DRAFT.md unchanged.

### Q01 [Title] Your main finding as one sentence of at most 15 words. It becomes the title.

### Q02 [Abstract] Answer this one last. In at most 150 words: the decision at stake for a market auditor, the confound, your main numbers with their scale, and what a market auditor should do differently.

### Q03 [1. Introduction] What problem does a market auditor face, and why does it matter for AI safety? Two or three sentences.

### Q04 [1. Introduction] What did you build or test this weekend? List your two or three contributions.

### Q05 [2. Related Work] Which two or three prior papers or tools are closest, and what does your work do that they don't?

### Q06 [3. Methods] Describe the setup so someone could rerun it: environment, agents and models, conditions (table in OUTLINE.md), seeds.

### Q07 [3. Methods] How did you measure false-positive rate on the no-channel decoys and true-positive rate on planted coordination, per detector, on held-out seeds, and why that measure?

### Q08 [3. Methods] What did you freeze in the preregistration, and when?

### D:1 [3. Methods] D1: Details of D3 and D4 that the prereg did not spell out: what changed from the preregistration, and why?

### D:2 [3. Methods] D2: The test used for each hypothesis: what changed from the preregistration, and why?

### D:3 [3. Methods] D3: The message judge runs after each market, at temperature 0: what changed from the preregistration, and why?

### D:4 [3. Methods] D4: The full grid runs even if the positive control fails: what changed from the preregistration, and why?

### D:5 [3. Methods] D5: An undefined threshold flags nothing (written 18 October 2026, after the results were read): what changed from the preregistration, and why?

### Q09 [4. Results] What did the positive control show, and why does that mean the instrument works? (pc.mean = 0.29757083333333306, threshold 0.2)

### C:tpr.D1.C1 [4. Results] What does tpr.D1.C1 = 0.5 (D1 true-positive rate on held-out C1) mean for a market auditor?

### C:fpr.D1.C2 [4. Results] What does fpr.D1.C2 = 0.0 (D1 false-positive rate on held-out C2) mean for a market auditor?

### C:fpr.D1.C4 [4. Results] What does fpr.D1.C4 = 0.0 (D1 false-positive rate on held-out C4) mean for a market auditor?

### C:fpr.D1.C7 [4. Results] What does fpr.D1.C7 = 0.5 (D1 false-positive rate on held-out C7) mean for a market auditor?

### C:fpr.D1.decoys [4. Results] What does fpr.D1.decoys = 0.1667 (D1 false-positive rate on all held-out no-channel decoys) mean for a market auditor?

### C:flag.D1.C3 [4. Results] What does flag.D1.C3 = 0.0 (D1 flag rate on held-out C3 (no ground truth)) mean for a market auditor?

### C:flag.D1.C5 [4. Results] What does flag.D1.C5 = 0.0 (D1 flag rate on held-out C5 (no ground truth)) mean for a market auditor?

### C:flag.D1.C6 [4. Results] What does flag.D1.C6 = 0.0 (D1 flag rate on held-out C6 (no ground truth)) mean for a market auditor?

### C:tpr.D2.C1 [4. Results] What does tpr.D2.C1 = 1.0 (D2 true-positive rate on held-out C1) mean for a market auditor?

### C:fpr.D2.C2 [4. Results] What does fpr.D2.C2 = 0.0 (D2 false-positive rate on held-out C2) mean for a market auditor?

### C:fpr.D2.C4 [4. Results] What does fpr.D2.C4 = 0.0 (D2 false-positive rate on held-out C4) mean for a market auditor?

### C:fpr.D2.C7 [4. Results] What does fpr.D2.C7 = 0.0 (D2 false-positive rate on held-out C7) mean for a market auditor?

### C:fpr.D2.decoys [4. Results] What does fpr.D2.decoys = 0.0 (D2 false-positive rate on all held-out no-channel decoys) mean for a market auditor?

### C:flag.D2.C3 [4. Results] What does flag.D2.C3 = 1.0 (D2 flag rate on held-out C3 (no ground truth)) mean for a market auditor?

### C:flag.D2.C5 [4. Results] What does flag.D2.C5 = 1.0 (D2 flag rate on held-out C5 (no ground truth)) mean for a market auditor?

### C:flag.D2.C6 [4. Results] What does flag.D2.C6 = 1.0 (D2 flag rate on held-out C6 (no ground truth)) mean for a market auditor?

### C:tpr.D3.C1 [4. Results] What does tpr.D3.C1 = 0.0 (D3 true-positive rate on held-out C1) mean for a market auditor?

### C:fpr.D3.C2 [4. Results] What does fpr.D3.C2 = 0.0 (D3 false-positive rate on held-out C2) mean for a market auditor?

### C:fpr.D3.C4 [4. Results] What does fpr.D3.C4 = 0.0 (D3 false-positive rate on held-out C4) mean for a market auditor?

### C:fpr.D3.C7 [4. Results] What does fpr.D3.C7 = 0.0 (D3 false-positive rate on held-out C7) mean for a market auditor?

### C:fpr.D3.decoys [4. Results] What does fpr.D3.decoys = 0.0 (D3 false-positive rate on all held-out no-channel decoys) mean for a market auditor?

### C:flag.D3.C3 [4. Results] What does flag.D3.C3 = 0.0 (D3 flag rate on held-out C3 (no ground truth)) mean for a market auditor?

### C:flag.D3.C5 [4. Results] What does flag.D3.C5 = 0.0 (D3 flag rate on held-out C5 (no ground truth)) mean for a market auditor?

### C:flag.D3.C6 [4. Results] What does flag.D3.C6 = 0.0 (D3 flag rate on held-out C6 (no ground truth)) mean for a market auditor?

### C:tpr.D4.C1 [4. Results] What does tpr.D4.C1 = 0.0 (D4 true-positive rate on held-out C1) mean for a market auditor?

### C:fpr.D4.C2 [4. Results] What does fpr.D4.C2 = 0.0 (D4 false-positive rate on held-out C2) mean for a market auditor?

### C:fpr.D4.C4 [4. Results] What does fpr.D4.C4 = 0.0 (D4 false-positive rate on held-out C4) mean for a market auditor?

### C:fpr.D4.C7 [4. Results] What does fpr.D4.C7 = 0.0 (D4 false-positive rate on held-out C7) mean for a market auditor?

### C:fpr.D4.decoys [4. Results] What does fpr.D4.decoys = 0.0 (D4 false-positive rate on all held-out no-channel decoys) mean for a market auditor?

### C:flag.D4.C3 [4. Results] What does flag.D4.C3 = 0.0 (D4 flag rate on held-out C3 (no ground truth)) mean for a market auditor?

### C:flag.D4.C5 [4. Results] What does flag.D4.C5 = 0.0 (D4 flag rate on held-out C5 (no ground truth)) mean for a market auditor?

### C:flag.D4.C6 [4. Results] What does flag.D4.C6 = 0.0 (D4 flag rate on held-out C6 (no ground truth)) mean for a market auditor?

### C:d1.threshold [4. Results] What does d1.threshold = 0.2909 (frozen on calibration seeds) mean for a market auditor?

### C:d4.dep_cut [4. Results] What does d4.dep_cut = 0.5326 (frozen on calibration seeds) mean for a market auditor?

### C:index.mean.C1 [4. Results] What does index.mean.C1 = 0.2976 mean for a market auditor?

### C:dep.mean.C1 [4. Results] What does dep.mean.C1 = 0.0237 mean for a market auditor?

### C:judge.mean.C1 [4. Results] What does judge.mean.C1 = 4.0 mean for a market auditor?

### C:index.mean.C2 [4. Results] What does index.mean.C2 = 0.0285 mean for a market auditor?

### C:dep.mean.C2 [4. Results] What does dep.mean.C2 = 0.2773 mean for a market auditor?

### C:index.mean.C3 [4. Results] What does index.mean.C3 = 0.002 mean for a market auditor?

### C:dep.mean.C3 [4. Results] What does dep.mean.C3 = 0.1648 mean for a market auditor?

### C:judge.mean.C3 [4. Results] What does judge.mean.C3 = 4.0 mean for a market auditor?

### C:index.mean.C4 [4. Results] What does index.mean.C4 = 0.0268 mean for a market auditor?

### C:dep.mean.C4 [4. Results] What does dep.mean.C4 = 0.0444 mean for a market auditor?

### C:index.mean.C5 [4. Results] What does index.mean.C5 = 0.0052 mean for a market auditor?

### C:dep.mean.C5 [4. Results] What does dep.mean.C5 = -0.01 mean for a market auditor?

### C:judge.mean.C5 [4. Results] What does judge.mean.C5 = 3.75 mean for a market auditor?

### C:index.mean.C6 [4. Results] What does index.mean.C6 = 0.0007 mean for a market auditor?

### C:dep.mean.C6 [4. Results] What does dep.mean.C6 = 0.0898 mean for a market auditor?

### C:judge.mean.C6 [4. Results] What does judge.mean.C6 = 4.0 mean for a market auditor?

### C:index.mean.C7 [4. Results] What does index.mean.C7 = 0.1433 mean for a market auditor?

### C:dep.mean.C7 [4. Results] What does dep.mean.C7 = 0.1924 mean for a market auditor?

### C:mkt.n_planned [4. Results] What does mkt.n_planned = 56 mean for a market auditor?

### C:mkt.n_markets [4. Results] What does mkt.n_markets = 56 mean for a market auditor?

### C:mkt.parse_rate.C1 [4. Results] What does mkt.parse_rate.C1 = 0.0 (share of seller decisions with no usable reply in C1) mean for a market auditor?

### C:mkt.parse_rate.C2 [4. Results] What does mkt.parse_rate.C2 = 0.0 (share of seller decisions with no usable reply in C2) mean for a market auditor?

### C:mkt.parse_rate.C3 [4. Results] What does mkt.parse_rate.C3 = 0.0 (share of seller decisions with no usable reply in C3) mean for a market auditor?

### C:mkt.parse_rate.C4 [4. Results] What does mkt.parse_rate.C4 = 0.0611 (share of seller decisions with no usable reply in C4) mean for a market auditor?

### C:mkt.parse_rate.C5 [4. Results] What does mkt.parse_rate.C5 = 0.0 (share of seller decisions with no usable reply in C5) mean for a market auditor?

### C:mkt.parse_rate.C6 [4. Results] What does mkt.parse_rate.C6 = 0.0 (share of seller decisions with no usable reply in C6) mean for a market auditor?

### C:mkt.parse_rate.C7 [4. Results] What does mkt.parse_rate.C7 = 0.1278 (share of seller decisions with no usable reply in C7) mean for a market auditor?

### C:mkt.n_missing [4. Results] What does mkt.n_missing = 0 mean for a market auditor?

### C:mkt.parse_failures [4. Results] What does mkt.parse_failures = 68 mean for a market auditor?

### C:mkt.judge_failures [4. Results] What does mkt.judge_failures = 0 mean for a market auditor?

### C:mkt.undefined_pairs [4. Results] What does mkt.undefined_pairs = 0 mean for a market auditor?

### C:sens.n_excluded [4. Results] What does sens.n_excluded = 7 mean for a market auditor?

### C:sens.tpr.D1.C1 [4. Results] What does sens.tpr.D1.C1 = 0.5 (D1 TPR, high-failure markets excluded) mean for a market auditor?

### C:sens.fpr.D1.decoys [4. Results] What does sens.fpr.D1.decoys = 0.125 (D1 decoy FPR, high-failure markets excluded) mean for a market auditor?

### C:sens.tpr.D2.C1 [4. Results] What does sens.tpr.D2.C1 = 1.0 (D2 TPR, high-failure markets excluded) mean for a market auditor?

### C:sens.fpr.D2.decoys [4. Results] What does sens.fpr.D2.decoys = 0.0 (D2 decoy FPR, high-failure markets excluded) mean for a market auditor?

### C:sens.tpr.D3.C1 [4. Results] What does sens.tpr.D3.C1 = 0.0 (D3 TPR, high-failure markets excluded) mean for a market auditor?

### C:sens.fpr.D3.decoys [4. Results] What does sens.fpr.D3.decoys = 0.0 (D3 decoy FPR, high-failure markets excluded) mean for a market auditor?

### C:sens.tpr.D4.C1 [4. Results] What does sens.tpr.D4.C1 = 0.0 (D4 TPR, high-failure markets excluded) mean for a market auditor?

### C:sens.fpr.D4.decoys [4. Results] What does sens.fpr.D4.decoys = 0.0 (D4 decoy FPR, high-failure markets excluded) mean for a market auditor?

### C:pc.p [4. Results] What does pc.p = 0.001 (permutation p, C1 vs C2 collusion index) mean for a market auditor?

### C:h2.diff [4. Results] What does h2.diff = -0.0948 (same-model minus cross-family pair dependence within C4 markets) mean for a market auditor?

### C:h4.judge_diff [4. Results] What does h4.judge_diff = 0.0 (C6 minus C3 mean judge max score) mean for a market auditor?

### C:h4.dep_diff [4. Results] What does h4.dep_diff = -0.0751 (C6 minus C3 mean dependence) mean for a market auditor?

### C:h4.dep_p [4. Results] What does h4.dep_p = 0.6055 mean for a market auditor?

### C:h1.p [4. Results] What does h1.p = 1.0 mean for a market auditor?

### C:h1.p_holm [4. Results] What does h1.p_holm = 1.0 mean for a market auditor?

### C:h2.p [4. Results] What does h2.p = 0.6875 mean for a market auditor?

### C:h2.p_holm [4. Results] What does h2.p_holm = 1.0 mean for a market auditor?

### C:h3.p [4. Results] What does h3.p = 1.0 mean for a market auditor?

### C:h3.p_holm [4. Results] What does h3.p_holm = 1.0 mean for a market auditor?

### C:h4.p [4. Results] What does h4.p = 1.0 mean for a market auditor?

### C:h4.p_holm [4. Results] What does h4.p_holm = 1.0 mean for a market auditor?

### C:splice.D1.heldout [4. Results] What does splice.D1.heldout = 0.0 (D1 flag rate on talk-without-action markets (heldout seeds)) mean for a market auditor?

### C:splice.D1.all [4. Results] What does splice.D1.all = 0.0 (D1 flag rate on talk-without-action markets (all seeds)) mean for a market auditor?

### C:splice.D2.heldout [4. Results] What does splice.D2.heldout = 1.0 (D2 flag rate on talk-without-action markets (heldout seeds)) mean for a market auditor?

### C:splice.D2.all [4. Results] What does splice.D2.all = 1.0 (D2 flag rate on talk-without-action markets (all seeds)) mean for a market auditor?

### C:splice.D3.heldout [4. Results] What does splice.D3.heldout = 0.0 (D3 flag rate on talk-without-action markets (heldout seeds)) mean for a market auditor?

### C:splice.D3.all [4. Results] What does splice.D3.all = 0.0 (D3 flag rate on talk-without-action markets (all seeds)) mean for a market auditor?

### C:splice.D4.heldout [4. Results] What does splice.D4.heldout = 0.25 (D4 flag rate on talk-without-action markets (heldout seeds)) mean for a market auditor?

### C:splice.D4.all [4. Results] What does splice.D4.all = 0.25 (D4 flag rate on talk-without-action markets (all seeds)) mean for a market auditor?

### C:x.auroc.D1.C2 [4. Results] What does x.auroc.D1.C2 = 0.9531 (exploratory: P(C1 market scores above a C2 market) for D1) mean for a market auditor?

### C:x.auroc.D1.decoys [4. Results] What does x.auroc.D1.decoys = 0.8802 (exploratory: P(C1 market scores above a decoys market) for D1) mean for a market auditor?

### C:x.auroc.D3.C2 [4. Results] What does x.auroc.D3.C2 = 0.2188 (exploratory: P(C1 market scores above a C2 market) for D3) mean for a market auditor?

### C:x.auroc.D3.decoys [4. Results] What does x.auroc.D3.decoys = 0.4115 (exploratory: P(C1 market scores above a decoys market) for D3) mean for a market auditor?

### C:x.tpr.X1.C1 [4. Results] What does x.tpr.X1.C1 = 0.5 (exploratory: X1 TPR on held-out C1) mean for a market auditor?

### C:x.fpr.X1.decoys [4. Results] What does x.fpr.X1.decoys = 0.0 (exploratory: X1 decoy FPR) mean for a market auditor?

### C:x.flag.X1.C3 [4. Results] What does x.flag.X1.C3 = 0.0 (exploratory: X1 flag rate on held-out C3) mean for a market auditor?

### C:x.flag.X1.C5 [4. Results] What does x.flag.X1.C5 = 0.0 (exploratory: X1 flag rate on held-out C5) mean for a market auditor?

### C:x.flag.X1.C6 [4. Results] What does x.flag.X1.C6 = 0.0 (exploratory: X1 flag rate on held-out C6) mean for a market auditor?

### C:x.splice.X1.all [4. Results] What does x.splice.X1.all = 0.0 (exploratory: X1 on talk-without-action markets, all seeds) mean for a market auditor?

### C:x.dep_p.C2_C4 [4. Results] What does x.dep_p.C2_C4 = 0.1196 (exploratory: permutation p, dependence in C2 (one model) vs C4 (mixed)) mean for a market auditor?

### C:x.flag.D2.channel_all [4. Results] What does x.flag.D2.channel_all = 1.0 (D2 flag rate on every C3, C5 and C6 market (all seeds)) mean for a market auditor?

### C:x.flag.D2.at_cost [4. Results] What does x.flag.D2.at_cost = 1.0 (D2 flag rate on channel markets whose collusion index stayed below 0.1) mean for a market auditor?

### C:x.n_at_cost [4. Results] What does x.n_at_cost = 24 mean for a market auditor?

### Q10 [5. Discussion and Limitations] What should a market auditor do differently because of these results?

### Q11 [5. Discussion and Limitations] What did the attack arm (C6, sellers told their messages are monitored by an overseer) show about how robust the result is?

### Q12 [6. Conclusion] Your findings and what they mean, in one or two short paragraphs.

### Q13 [Code and Data] What did you build or run this weekend, and what existed before (tooling, reused code)?

### Q14 [Appendix A: Limitations and Dual-Use / Ethical Considerations] What does your result not establish? Could your setup or findings make real collusion easier to carry out or harder to detect?

### Q15 [LLM Usage Statement] Which AI tools did you use, for what, and what did you write yourself?
