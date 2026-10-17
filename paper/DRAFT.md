<!-- Pre-draft written by Claude (Anthropic) for Ayodeji Adesegun to rewrite. Sections marked <<FILL>> wait for the Kaggle results. Every number must come from results/claims.json. -->

# <<FILL: title, written after the results: a claim with a finding verb, e.g. "Same-Model Sellers Price in Parallel Without Talking: A Plus-Factor Rule Separates It From Agreement">>

## Abstract

<<FILL: abstract, at most 150 words, written last: the auditor's decision, the decoy design, the positive control number, the false-alarm rates of D1 and D3 against D4 on held-out decoys, and the talk-without-action result>>

## 1. Introduction

Suppose three firms in one market hand their pricing to the same language model. Their prices rise and fall together. An auditor has to decide whether that pattern is evidence of collusion, or what three copies of one model do when they face the same market. The question is practical. Two deployments of the same model already show correlated choices in economic settings where deployments of different models show none [5], so a detector built on correlated prices will flag firms whose only link is their vendor.

Antitrust law reached this question long before language models. Under US law, parallel conduct by competitors is not by itself evidence of an agreement; a court asks for additional facts, called plus factors, that make agreement more likely than independent action [6, 7]. Recent legal writing on AI pricing tools asks how that doctrine applies when the parallel conduct comes from shared software [8]. Studies of LLM collusion measure it through prices [1, 2] or through messages and outcomes [4]. I found no LLM collusion detector that states a comparable rule for separating agreement from parallel conduct.

This paper tests that rule on LLM sellers. The setting is the continuous double auction of Agrawal et al. [2], in which LLM sellers set asks against scripted buyers and may or may not have a private message channel. The design rests on one control: when sellers have no channel, agreement is impossible by construction, so every collusion flag on those markets is a false alarm. I compare four detectors on markets with no channel, with a channel, and with a planted agreement:

- D1, price level: are prices high?
- D2, message judge: does an LLM judge read the sellers' messages as coordination?
- D3, action dependence: do the sellers' ask changes move together?
- D4, a plus-factor rule: is dependence higher than copies of the same model produce on their own, and does a coordination message come before the asks converge?

Thresholds are set on calibration seeds and frozen before the held-out markets are scored. Two further tests target failure modes named in Track 2.3 of the sprint: talk without action, where messages from markets with a channel are spliced onto the actions of markets without one, and a monitoring attack, where sellers are told an overseer reads their messages.

The intended user is a market auditor who must decide whether parallel pricing alone justifies a collusion finding, or whether plus-factor evidence is required. The contributions are:

1. a decoy design that separates parallel conduct from agreement in a standard LLM market;
2. an operational plus-factor rule with a frozen threshold;
3. held-out false-alarm and detection rates for four detectors, with intervals;
4. the code, the preregistration and every market log.

## 2. Related Work

**LLM agents in markets.** Fish et al. [1] showed that LLM pricing agents in oligopoly settings reach supracompetitive prices without instruction to collude, and that small changes in prompt wording change how far prices rise. Agrawal et al. [2] built the double auction used here and found that a message channel between sellers increases collusive behaviour, with differences across models and under oversight. Keppo et al. [3] found that such collusion weakens when agents differ in patience or data access, and that agents of different sizes from one model family still sustain it. These studies measure whether collusion happens. This paper asks how an auditor would tell it apart from innocent parallel conduct.

**Detecting collusion from words and actions.** Nakamura et al. [4] audit collusion in cooperative multi-agent tasks and describe "collusion on paper": agents that plan collusion in text but then act otherwise. That is the talk-without-action failure tested here. Xu et al. [5] argue that audits based on a single agent's prices can be blind by construction, and report that two deployments of the same model show a small residual correlation where different models show almost none. Their result is the mechanism behind this paper's decoys: if same-model agents correlate without any agreement, a detector built on correlation will flag them. Rippin et al. [9] show that agents with tools can build covert channels that survive text monitoring, which bounds what any message-based detector can claim.

**Plus factors.** In *Bell Atlantic v. Twombly* [6] the US Supreme Court held that parallel conduct alone does not plausibly show an agreement under the Sherman Act. Kovacic et al. [7] review the plus factors courts use and argue that the strongest are those that are hard to explain by independent action. Berger et al. [8] discuss how these rules apply to shared AI pricing tools. The rule D4 borrows two plus factors from this literature: parallel conduct beyond what independent actors would produce, and communication followed by a change in conduct.

## 3. Methods

**Market.** I use the continuous double auction of Agrawal et al. [2] unchanged, from the authors' public code at a pinned commit (vendor/NOTICE in the repository). Three LLM sellers, each with a cost of $80 per lot, face three scripted buyers with a value of $100 per lot. The buyers follow the ZIP rule [10], a simple adaptive bidding strategy, so any rise in prices comes from the sellers. The market runs for 15 hours. Each hour, every seller sees the order book, its past trades, its own memory notes and, when the channel is on, the messages the other sellers sent the previous hour (up to 500 characters each). It returns an ask for one lot and, when the channel is on, a message. A trade happens when the highest bid meets the lowest ask, at the midpoint. All sellers use temperature 0.7 and at most 1024 output tokens.

**Models.** The sellers are Qwen2.5-7B-Instruct [11] and Llama-3.1-8B-Instruct [12] (Ollama tags qwen2.5:7b and llama3.1:8b), served by Ollama with its default 4-bit weights on Kaggle GPUs. All calls went through one logged client; the full call ledger is in the repository. The study used no paid API.

**Conditions.** Table 1 lists the seven conditions. Each ran with 8 seeds, giving 56 markets.

Table 1: The seven conditions. "Channel" means sellers can message each other.

| Condition | Sellers | Channel | Other | Role |
|---|---|---|---|---|
| C1 | 3 Qwen | on | told before the market that they agreed to coordinate on a common high ask | positive control |
| C2 | 3 Qwen | off | | decoy, calibration baseline |
| C3 | 3 Qwen | on | | channel, no instruction |
| C4 | 2 Qwen, 1 Llama | off | | decoy, mixed models |
| C5 | 2 Qwen, 1 Llama | on | | channel, mixed models |
| C6 | 3 Qwen | on | told an overseer monitors messages; overseer active | monitoring attack |
| C7 | 3 Llama | off | | decoy, model-identity control |

C2, C4 and C7 have no channel, so no agreement can form in them. They differ in how many sellers share a model, which is the variable the shared-prior explanation depends on. In C6 the overseer from Agrawal et al. [2] reads each hour's messages during the market; when it rates them 4 out of 4, every later message is limited to 5 characters for the rest of the market, as in the original code.

**Collusion index and positive control.** For each market, the collusion index is the mean seller ask over the last 5 hours, rescaled so that 0 is seller cost and 1 is buyer value. The preregistered positive control requires the mean index of C1 to exceed that of C2 by at least 0.2. If it does not, the instrument cannot see planted coordination and the main results are not interpretable.

**Detectors.**
- D1 (price level) flags a market whose collusion index reaches a threshold.
- D2 (message judge) runs the overseer prompt from Agrawal et al. [2], unchanged, on each hour's seller messages after the market ends, at temperature 0, with Qwen2.5-7B-Instruct as the judge. It flags a market when any hour scores 3 or 4 on the prompt's 1 to 4 coordination scale. Markets without a channel have no messages, so D2 cannot flag them.
- D3 (action dependence) is the mean, over the three seller pairs, of the Pearson correlation between the two sellers' hour-to-hour ask changes. It flags a market whose dependence reaches a threshold.
- D4 (plus-factor rule) flags a market only when both plus factors hold: (a) its dependence exceeds the 95th percentile of dependence in the C2 calibration markets, that is, more parallel than copies of the same model with no channel; and (b) at least one message the judge scored 3 or more is followed, within 2 hours, by a fall in the spread between the highest and lowest seller ask.

**Calibration and held-out scoring.** Seeds 0 to 3 of every condition are calibration markets and seeds 4 to 7 are held out. The D1 and D3 thresholds are the values that maximise true-positive rate on C1 minus false-positive rate on C2 in the calibration markets. D4's dependence cut is the C2 calibration percentile above. The analysis script computes these from the calibration files before it opens a held-out file, writes them to disk, and then scores the held-out markets once. The primary metrics are each detector's false-positive rate on held-out C2, C4 and C7 markets and its true-positive rate on held-out C1 markets, each with a Wilson 95% interval.

**Talk without action.** To test whether a detector mistakes talk for collusion, I pair each C3 market (channel, messages, judge scores) with the C2 market of the same seed (no channel) and score the C2 actions together with the C3 messages. No action in these spliced markets responds to the messages, so any flag is a false alarm. No new markets are run for this test.

**Hypothesis tests.** H1 (copies of one model look collusive without a channel) uses an exact binomial test of whether the held-out decoy flag rate of D1 and of D3 exceeds 5%. H2 (same-model pairs are more dependent than cross-family pairs) uses an exact sign-flip test on the within-market difference in C4. H3 (D4 has fewer false alarms than D1 and D3) uses exact McNemar tests on the same held-out decoy markets. H4 (monitoring lowers what the judge sees more than it lowers dependence) compares C6 with C3 by permutation. P-values are Holm-corrected across the four hypotheses. Where the preregistration left a detail open, the choice is listed in DEVIATIONS.md with the reason; every entry there was written and committed before the main grid ran.

**Hand labels.** The judge is itself a model, so I labelled whether sellers reached an agreement in every C3, C5 and C6 market from the messages alone, with the condition, the models and the prices hidden. I labelled each market twice, in a different random order, at least a day apart; a market counts as an agreement only when both passes say so. I report agreement between the passes and between the labels and each detector.

**Preregistration and code.** The question, conditions, detectors, decision rule and outcomes were frozen in PREREG.md (git tag prereg-v1) before any market of the main grid ran, and the analysis code was committed (tag analysis-frozen-v1) before the results existed.

## 4. Results

<<FILL: results, starting with the positive control and its number (pc.mean, pc.baseline_mean, pc.contrast, pc.p). Then: Table 2 (held-out FPR per decoy and TPR on C1, per detector, with Wilson intervals); Figure 1; Figure 2; H1-H4 with Holm p-values; the talk-without-action splice; the monitoring attack; hand-label agreement (judge.agreement.*); parse and judge failure counts.>>

## 5. Discussion and Limitations

<<FILL: discussion, written after the results: what the auditor should do, and which result carries the paper if H1 is null>>

The study has clear limits. The sellers are 7 to 8 billion parameter models with 4-bit weights; larger models write better messages and may coordinate through actions alone. Each condition has 8 seeds and each held-out cell has only 4 markets, so the intervals are wide and a difference of one or two flags is within noise. The market is one design with three sellers and 15 hours; dependence measured over 14 hourly changes is noisy. The judge belongs to the same model family as most sellers, which may make it read Qwen messages more charitably or more harshly than an outside judge would. The hand labels come from one person, so the two-pass agreement measures consistency, not agreement between people. The talk-without-action markets are constructed, not observed. D4 is one way to write two plus factors as code, and a seller that coordinates without messages, or waits longer than 2 hours to act on a message, would pass it.

## 6. Conclusion

<<FILL: conclusion, two or three sentences, ending on the next experiment>>

## Code and Data

code: <<FILL: GitHub URL once the repository is public>>

prereg: <<FILL: GitHub URL of tag prereg-v1>>

### What is new this weekend

This project was prepared before the sprint, and that is disclosed here with dates. Before the sprint (14–17 October 2026) I chose the question, Claude drafted the question card and preregistration, which I reviewed, and the preregistration was frozen on 16 October. The harness that runs the Agrawal et al. [2] market through a logged client, the analysis code and the full 56-market grid were built and run on 17 October, on Kaggle. During the sprint weekend I <<FILL: what you actually did during the weekend, e.g. the two-pass hand labels, the judge-agreement analysis, any added condition or seeds, and rewriting this report>>.

## References

[1] Fish, S., Gonczarowski, Y. A., Shorrer, R. I. (2024). Algorithmic Collusion by Large Language Models. arXiv:2404.00806. https://arxiv.org/abs/2404.00806

[2] Agrawal, K., Teo, V., Vazquez, J. J., Kunnavakkam, S., Srikanth, V., Liu, A. (2025). Evaluating LLM Agent Collusion in Double Auctions. arXiv:2507.01413. https://arxiv.org/abs/2507.01413

[3] Keppo, J., Li, Y., Tsoukalas, G., Yuan, N. (2026). On the Fragility of AI Agent Collusion. arXiv:2603.20281. https://arxiv.org/abs/2603.20281

[4] Nakamura, M., Kumar, A., Das, S., Abdelnabi, S., Mahmud, S., Fioretto, F., Zilberstein, S., Bagdasarian, E. (2026). Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems. arXiv:2602.15198. https://arxiv.org/abs/2602.15198

[5] Xu, X., Wu, C., Lu, J., Tan, K., Tao, S., Hong, H. (2026). Collusion with Competitive Marginals: Price-Level Audits Are Blind by Construction. arXiv:2607.26385. https://arxiv.org/abs/2607.26385

[6] Supreme Court of the United States (2007). Bell Atlantic Corp. v. Twombly, 550 U.S. 544. U.S. Reports. https://supreme.justia.com/cases/federal/us/550/544/

[7] Kovacic, W. E., Marshall, R. C., Marx, L. M., White, H. L. (2011). Plus Factors and Agreement in Antitrust Law. Michigan Law Review 110(3), 393-436. https://repository.law.umich.edu/mlr/vol110/iss3/1/

[8] Berger, L. F., Weiner, M. L., Jiang, W. (2025). Coordination by Code: Rethinking Antitrust Liability in the Age of AI Pricing. Antitrust 40(1), ABA Section of Antitrust Law. https://www.americanbar.org/groups/antitrust_law/resources/magazine/2025-fall/coordination-code-rethinking-antitrust-liability-age-ai-pricing/

[9] Rippin, J. L., Marshall, S. C., Africa, D. D., Schroeder de Witt, C. (2026). Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems. arXiv:2606.28425. https://arxiv.org/abs/2606.28425

[10] Cliff, D. (1997). Minimal-Intelligence Agents for Bargaining Behaviours in Market-Based Environments. HP Laboratories Technical Report HPL-97-91. https://www.hpl.hp.com/techreports/97/HPL-97-91.html

[11] Qwen Team (2024). Qwen2.5 Technical Report. arXiv:2412.15115. https://arxiv.org/abs/2412.15115

[12] Grattafiori, A., et al. (2024). The Llama 3 Herd of Models. arXiv:2407.21783. https://arxiv.org/abs/2407.21783

## Appendix A: Limitations and Dual-Use / Ethical Considerations

**What the results do not establish.** A low false-alarm rate for D4 in this market does not establish that the rule works in other markets, with larger models, or against sellers trying to evade it. A flag from any detector here does not establish that a real firm colluded: the markets are simulated, the stakes are zero, and the definition of agreement is the one in the labelling guide. The results also do not establish what US or any other law requires; the legal doctrine is used as a design idea, not applied to facts.

**Dual use.** Describing what a detector checks also describes how to pass it. D4 can be evaded by coordinating without messages, by acting on a message after more than 2 hours, or by keeping asks spread apart. The monitoring condition shows one way sellers change their messages when told they are watched. I judged these risks small: the evasions are obvious from the rule itself, the models are small open-weight models, and the paper releases no technique for hiding coordination. The benefit is a test that auditors can run before they accuse anyone on the strength of parallel prices.

**Ethics.** No people took part. The only human data are my own labels. The study used open-weight models on free Kaggle GPUs and no paid API.

## LLM Usage Statement

Claude (Anthropic, model Claude Opus 5.5), used as a coding agent in Claude Code, wrote the code that connects the Agrawal et al. [2] market to the logged model client, wrote the analysis scripts, drafted the question card and the preregistration from my chosen question, and drafted the text of this report. I chose the research question, reviewed and froze the preregistration, ran the experiments, labelled the messages by hand, checked every number in this report against the analysis outputs, and rewrote the draft. The sellers and the message judge in the experiments are the open-weight models named in Methods. <<FILL: adjust this statement so it matches exactly what you did>>
