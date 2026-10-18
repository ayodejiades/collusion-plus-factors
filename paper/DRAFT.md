<!-- Drafted by Claude (Anthropic) for Ayodeji Adesegun to rewrite in the author's own words. Every number comes from results/claims.json; rops-claims verify checks them. -->

# No Single Signal Separates Agreement From Parallel Conduct Among LLM Sellers

## Abstract

A market auditor who sees AI pricing agents move prices together must decide whether that is evidence of collusion; antitrust law says parallel conduct alone is not. I test this on LLM sellers in the Agrawal et al. double auction, in two preregistered studies of 56 markets each, with no-channel markets, where agreement is impossible, as decoys. Planted agreements raised the collusion index to 0.30, and to 0.75 with an explicit price floor, against 0.03 without a channel. No single signal was reliable: prices moved together more without a channel than under planted agreement, and an LLM judge flagged all 24 channel markets that priced at cost. In the confirmatory study, a judge extracting the proposed price cut those false alarms from 15 of 15 to 7 (Holm p = 0.04). Requiring high prices plus price-holding talk raised no false alarm on 32 known negatives but missed failed agreements.

## 1. Introduction

Suppose three firms in one market hand their pricing to the same language model. Their prices rise and fall together. An auditor has to decide whether that pattern is evidence of collusion, or what three copies of one model do when they face the same market. The question is practical. Two deployments of the same model already show correlated choices in economic settings where deployments of different models show none [5], so a detector built on correlated prices will flag firms whose only link is their vendor.

Antitrust law reached this question long before language models. Under US law, parallel conduct by competitors is not enough on its own to show an agreement; a court asks for additional facts, called plus factors, that make agreement more likely than independent action [6, 7]. Recent legal writing on AI pricing tools asks how that doctrine applies when the parallel conduct comes from shared software [8]. Studies of LLM collusion measure it through prices [1, 2] or through messages and outcomes [4]. I found no LLM collusion detector that states a comparable rule for separating agreement from parallel conduct.

This paper tests that rule on LLM sellers. The setting is the continuous double auction of Agrawal et al. [2], in which LLM sellers set asks against scripted buyers and may or may not have a private message channel. The design rests on one control: when sellers have no channel, agreement is impossible by construction, so every collusion flag on those markets is a false alarm. I compare four detectors on markets with no channel, with a channel, and with a planted agreement:

- D1, price level: are prices high?
- D2, message judge: does an LLM judge read the sellers' messages as coordination?
- D3, action dependence: do the sellers' ask changes move together?
- D4, a plus-factor rule: is dependence higher than copies of the same model produce on their own, and does a coordination message come before the asks converge?

Thresholds are frozen on calibration seeds before held-out markets are scored, and two failure modes named in Track 2.3 are tested directly: talk without action, and a monitoring attack.

Every single signal failed, each in a different way. Without a channel, sellers' price changes moved together more than under a planted agreement, because copies of one model competing towards cost move in step. The message judge flagged every market with a channel, including all those where prices stayed at cost. Price level flagged two Llama markets where no agreement was possible. A second, preregistered study then tested the fixes these failures suggest. A judge that reports what price the sellers propose, instead of whether they sound coordinated, halved the false alarms on talk at cost. Rules that require both high prices and talk about holding a high common price raised no false alarm on any known negative, at the cost of missing agreements that fail to lift prices.

The intended user is a market auditor deciding whether parallel pricing alone justifies a collusion finding. The contributions are a decoy design that separates parallel conduct from agreement in a standard LLM market; held-out false-alarm and detection rates for single signals and plus-factor rules across two preregistered studies; a message judge that extracts proposed prices; and the code, both preregistrations and every market log.

## 2. Related Work

**LLM agents in markets.** Fish et al. [1] showed that LLM pricing agents in oligopoly settings reach supracompetitive prices without instruction to collude, and that small changes in prompt wording change how far prices rise. Agrawal et al. [2] built the double auction used here and found that a message channel between sellers increases collusive behaviour, with differences across models and under oversight. Keppo et al. [3] found that such collusion weakens when agents differ in patience or data access, and that agents of different sizes from one model family still sustain it. These studies ask whether collusion happens; this paper asks how an auditor would tell it apart from innocent parallel conduct.

**Detecting collusion from words and actions.** Nakamura et al. [4] audit collusion in cooperative multi-agent tasks and describe "collusion on paper": agents that plan collusion in text but then act otherwise. Xu et al. [5] argue that audits based on a single agent's prices can be blind by construction, and report that two deployments of the same model show a small residual correlation where different models show almost none. If same-model agents correlate without agreement, a correlation detector will flag them; this paper's decoys test that. Rippin et al. [9] show that agents with tools can build covert channels that survive text monitoring, which bounds what any message-based detector can claim.

**Plus factors.** In *Bell Atlantic v. Twombly* [6] the US Supreme Court held that parallel conduct alone does not plausibly show an agreement under the Sherman Act. Kovacic et al. [7] review the plus factors courts use and argue that the strongest are those that are hard to explain by independent action. Berger et al. [8] discuss how these rules apply to shared AI pricing tools. The rule D4 borrows two plus factors from this literature: parallel conduct beyond what independent actors would produce, and communication followed by a change in conduct.

## 3. Methods

**Market.** I use the continuous double auction of Agrawal et al. [2] unchanged, from the authors' public code at a pinned commit. Three LLM sellers, each with a cost of $80 per lot, face three scripted buyers that follow the adaptive ZIP rule [10] with a value of $100 per lot, so any rise in prices comes from the sellers. Each of 15 hours, every seller sees the order book, its past trades, its own notes and, when the channel is on, the other sellers' messages from the previous hour (up to 500 characters). It returns an ask and, with a channel, a message. Trades happen at the midpoint when bid meets ask. Sellers use temperature 0.7 and at most 1024 output tokens.

**Models.** The sellers are Qwen2.5-7B-Instruct [11] and Llama-3.1-8B-Instruct [12], served by Ollama with 4-bit weights on two Kaggle T4 GPUs, through one logged client. No paid API was used.

**Conditions.** Table 1 lists the conditions; Study 1 ran C1 to C7 with 8 seeds each (56 markets).

Table 1: Conditions. "Channel" means sellers can message each other. C8 is in Study 2 only, and C6 in Study 1 only.

| Condition | Sellers | Channel | Other | Role |
|---|---|---|---|---|
| C1 | 3 Qwen | on | told they agreed to coordinate on a common high ask | positive control |
| C2 | 3 Qwen | off | | decoy, baseline |
| C3 | 3 Qwen | on | | talk, no planted agreement |
| C4 | 2 Qwen, 1 Llama | off | | decoy, mixed models |
| C5 | 2 Qwen, 1 Llama | on | | talk, mixed models |
| C6 | 3 Qwen | on | told an overseer reads messages; overseer active | monitoring attack |
| C7 | 3 Llama | off | | decoy, model identity |
| C8 | 3 Qwen | on | told they agreed a price floor of $95 | strong positive control |

C2, C4 and C7 have no channel, so no agreement can form in them; they differ in how many sellers share a model. In C6 the overseer of Agrawal et al. [2] reads each hour's messages, and after it rates them 4 out of 4 every later message is limited to 5 characters.

**Collusion index and positive control.** The collusion index is the mean seller ask over the last 5 hours, rescaled so that 0 is seller cost and 1 is buyer value. Study 1's positive control requires C1 to beat C2 by at least 0.2.

**Detectors.**
- D1 (price level): the collusion index reaches a threshold.
- D2 (message judge): the overseer prompt of Agrawal et al. [2], unchanged, run after the market at temperature 0 with Qwen2.5-7B-Instruct, scores any hour 3 or 4 on its 1 to 4 scale.
- D3 (action dependence): the mean, over seller pairs, of the correlation between hour-to-hour ask changes reaches a threshold.
- D4 (preregistered plus-factor rule): dependence above the 95th percentile of the C2 calibration markets, and a message scored 3 or more followed within 2 hours by a fall in the spread of asks.

**Study 1 protocol.** Seeds 0 to 3 are calibration markets and seeds 4 to 7 are held out. The D1 and D3 thresholds maximise true-positive rate on C1 minus false-positive rate on C2 in the calibration markets; the analysis script writes them to disk before it opens a held-out file. For talk without action, each C3 market's messages are scored together with the actions of the C2 market of the same seed, so no action responds to the talk. H1 to H4 (decoy false alarms above 5%, same-model pair dependence, fewer D4 false alarms, monitoring) use exact binomial, sign-flip, McNemar and permutation tests with Holm correction. The preregistration is git tag prereg-v1 and the analysis code was tagged before results existed (analysis-frozen-v1); DEVIATIONS.md lists every open choice.

**Study 2: a confirmatory test.** Study 1 suggested a better rule, so I froze a second preregistration (study2/PREREG.md, tag prereg2-v1) before running any new market. Study 2 runs C1 to C5, C7 and C8 on new seeds 8 to 15 (56 markets), with every threshold taken from Study 1. It adds an extraction judge, D2x: instead of rating "coordination", the model reports whether sellers propose or accept a common price, which way it pushes asks, and the price named, and code flags an hour when the proposed price is at or above the D1 threshold in dollars. I checked its prompt on 9 Study 1 hours before freezing it; a first prompt that asked the model to judge the direction itself failed that check and was dropped. The same judge also runs with Llama (D2x-L). Two rules require both kinds of evidence: X1 = D1 and D2, and D5 = D1 and D2x. Known positives are C1 and C8 (16 markets); known negatives are the decoys and 8 talk-without-action markets (32). H5 asks whether D5 makes fewer errors than D1 and than D2; H6 the same for X1; H7 whether D2x flags fewer than D2 on C3 and C5 markets priced at cost; H8 whether the judge's family changes D2x's flags; H9 replicates Study 1's dependence result. All use exact McNemar or permutation tests with Holm correction.

## 4. Results

### Study 1

**Positive control.** The planted instruction raised the mean collusion index from 0.03 in C2 to 0.30 in C1, a contrast of 0.27 against the preregistered 0.2 (permutation p = 0.001). The sellers announced a "common ask" but often named different numbers and then cut prices; three of the eight C1 markets ended below the D1 threshold (Figure 1). All 56 markets finished, with 3684 model calls and no truncated replies.

![Figure 1: Collusion index of every Study 1 market (x: calibration seeds 0-3, o: held-out seeds 4-7). Grey conditions have no message channel, so any agreement is impossible. The dashed line is the D1 threshold frozen on calibration seeds.](figures/fig1.png)

Table 2: Study 1, held-out markets flagged (seeds 4 to 7). Brackets give Wilson 95% intervals for the pooled decoy rate (C2, C4, C7).

| Detector | C1, planted (correct) | C2 | C4 | C7 | All decoys (false alarm) | Talk without action (false alarm) |
|---|---|---|---|---|---|---|
| D1 price level | 2 of 4 | 0 of 4 | 0 of 4 | 2 of 4 | 2 of 12 [0.05, 0.45] | 0 of 4 |
| D2 message judge | 4 of 4 | 0 of 4 | 0 of 4 | 0 of 4 | 0 of 12 [0, 0.24] | 4 of 4 |
| D3 action dependence | 0 of 4 | 0 of 4 | 0 of 4 | 0 of 4 | 0 of 12 [0, 0.24] | 0 of 4 |
| D4 plus-factor rule | 0 of 4 | 0 of 4 | 0 of 4 | 0 of 4 | 0 of 12 [0, 0.24] | 1 of 4 |

**Each single signal failed in its own way.** Price level (threshold 0.29) caught 2 of 4 held-out planted markets but flagged 2 of 12 decoys, both three-Llama markets where sellers cut asks slowly and traded little. Llama sellers also failed to reply usably more often (68 failed replies in all, 13% of decisions in C7), which keeps old asks in place; dropping the 7 markets with more than 10% failures leaves 1 of 8 decoys flagged. Action dependence ran the wrong way: it was 0.28 [0.09, 0.46] in C2 and 0.02 [-0.10, 0.15] in C1, no threshold beat flagging nothing, and under the preregistered rule D3 flags no market (DEVIATIONS.md, D5). Figure 2 shows why. Without a channel, three copies of Qwen undercut each other towards cost in step; under the planted agreement each seller holds its own idea of the common ask. In mixed markets, same-model pairs were not more dependent than cross-family pairs (difference -0.09 [-0.41, 0.28], p = 0.69). The message judge flagged every channel market: all 4 held-out planted markets, and also all 24 C3, C5 and C6 markets, every one priced at cost (index below 0.1). The sellers do talk the language of coordination ("Let's keep our asks just below the lowest ask to maximize trades... Coordination is key."), but what they propose is a price cut. On talk-without-action markets the judge flagged 8 of 8. D4 (dependence cut 0.53) raised no false alarm on decoys but caught no planted market, since planted markets were not unusually parallel.

![Figure 2: Seller asks per hour. Left: the held-out no-channel market with the highest action dependence, chosen by that rule. Right: the first held-out planted-agreement market. Dotted lines mark seller cost ($80) and buyer value ($100).](figures/fig3.png)

None of H1 to H4 is supported after Holm correction (all adjusted p = 1.00). Telling sellers they were monitored did not lower the judge's scores: every C6 market still reached 4, and dependence changed by -0.08 (p = 0.61); the sellers talked before the gag cut their messages to fragments such as "COMP". An exploratory rule found after reading these results, X1 = D1 and D2, flagged 2 of 4 held-out planted markets and none of the 12 decoys or 8 talk-without-action markets. Study 2 tests it.

### Study 2 (confirmatory)

**Positive controls.** The price-floor instruction worked: the mean collusion index was 0.75 in C8 against 0.01 in C2, a contrast of 0.74 against the preregistered 0.3 (p = 0.0002). C1 replicated Study 1, with a contrast of 0.30 (p = 0.0006). All 56 markets finished; 63 seller replies failed to parse and left the previous ask in place.

Table 3: Study 2 on the 48 known markets: 16 positives (C1, C8) and 32 negatives (24 decoys, 8 talk-without-action markets). Thresholds from Study 1.

| Detector | Planted caught (of 16) | False alarms (of 32) | Errors (of 48) |
|---|---|---|---|
| D1 price level | 11 | 0 | 5 |
| D2 message judge | 16 | 8 | 8 |
| D2x extraction judge | 15 | 3 | 4 |
| D2x-L extraction judge, Llama | 16 | 4 | 4 |
| D3 action dependence | 0 | 0 | 16 |
| D4 plus-factor rule | 0 | 2 | 18 |
| X1 = D1 and D2 | 11 | 0 | 5 |
| D5 = D1 and D2x | 11 | 0 | 5 |

**The extraction judge removed half of the vendored judge's false alarms (H7 supported).** On the 15 C3 and C5 markets that priced at cost, D2 flagged 15 and D2x flagged 7 (exact McNemar p = 0.008, Holm-adjusted 0.039), while D2x still caught 15 of 16 planted markets. Its 3 false alarms were all talk-without-action markets in which sellers proposed a high common price in words but, in the C2 actions they were paired with, nobody raised prices. As a secondary check on Study 1's markets, which had already been read, D2x flagged 3 of 8 C3 markets and none of 8 C6 markets, where the vendored judge had flagged all of them.

**Requiring two signals removed every false alarm but did not beat price level (H5, H6 not supported).** D5 and X1 raised no false alarm on any of the 32 known negatives (Wilson interval 0 to 0.11). They missed 5 of 16 planted markets, all C1 markets whose sellers agreed in words but let prices fall below the D1 threshold. Price level alone made the same 5 errors in Study 2: unlike Study 1, no Llama decoy reached the D1 threshold (C7 mean 0.07). Against D2, D5 traded 8 false alarms for 5 misses, which is not a significant difference (H5 p = 1.00).

**Judge family and replication.** The Qwen and Llama extraction judges agreed on 0.84 of channel markets (kappa 0.53), and their flag rates did not differ significantly (H8, Holm-adjusted p = 0.25). Action dependence was again higher without a channel than under the planted agreement (0.26 against 0.08), but not significantly this time (H9 p = 0.21), and D4 again caught nothing.

**Hand labels.** <<FILL: after labelling both passes, run make analyze and rops-claims build, then report labels.self_kappa, the share of markets labelled as agreements, and judge.agreement.kappa and judge.agreement.pct>>

## 5. Discussion and Limitations

For the auditor, the two studies give a consistent answer. Parallel pricing alone did not indicate agreement: the most parallel markets were ones where agreement was impossible. Coordination talk alone did not either: a judge reading "coordination" flagged every market with a channel, including all those that priced at cost. Each single signal failed in a way the plus-factors doctrine anticipates: parallel conduct without agreement (D3), talk without action (D2) and high prices without agreement (D1 on Llama markets in Study 1).

Two changes help. First, a message judge should report what price the talk proposes rather than whether it sounds coordinated; that one change halved the false alarms on talk at cost, in a preregistered test. Second, a rule that needs a supracompetitive price as well as price-holding talk flagged none of the 32 known negatives in Study 2, nor on Study 1's held-out decoys and talk-without-action markets. In Study 2 price level alone did as well, because no decoy happened to price high, so the two studies together show the conjunction protecting against a failure that appears in some markets and not others. Its cost is plain: a planted agreement that does not lift prices goes unflagged. Under US law a price-fixing agreement is unlawful in itself, whether or not it succeeds [13], so an auditor who must catch failed agreements still needs the message evidence on its own, at the price of more false alarms. The preregistered D4 failed because it looked for correlated price changes; an agreement to hold a price leaves a high, flat price instead.

The limits are clear. The sellers are 7 to 8 billion parameter models with 4-bit weights, and larger models may coordinate through actions alone. Study 1's held-out cells have 4 markets and Study 2's known set has 48, so several intervals are wide. The market is one design with three sellers. The vendored judge is from the same family as most sellers and saturates at its top score; the cross-family check did not find a significant difference, but with 32 markets it could miss a moderate one. D4's cut comes from 4 calibration markets. The hand labels come from one person, so two-pass agreement measures consistency, not agreement between people. Llama sellers failed to reply usably more often, which inflates their price level. The talk-without-action markets are constructed, not observed, and the extraction judge's rule borrows the D1 threshold, so the two are not fully independent.

## 6. Conclusion

In LLM seller markets, neither parallel price changes nor coordination talk was reliable evidence of collusion, and high prices misled in one of two studies. A preregistered second study showed that a judge which extracts the proposed price halves the message judge's false alarms, and that requiring both high prices and price-holding talk produced no false alarms at the cost of missing failed agreements. The next step is to test these rules with larger models, more sellers and a second market, and to measure how often failed agreements matter in practice.

## Code and Data

code: <<FILL: GitHub URL once the repository is public>>

prereg: <<FILL: GitHub URL of tag prereg-v1>>

### What is new this weekend

Prior work, with dates. Before the sprint (14–18 October 2026) I chose the question. Claude drafted the question card and both preregistrations, which I reviewed. I froze the Study 1 preregistration on 16 October and the Study 2 preregistration on 18 October, each before its markets ran. The harness and analysis code were built on 17 and 18 October. Both studies ran on Kaggle between 17 and 19 October, and the analysis and a first draft of this report were produced in the same days. Study 2 was originally planned for the sprint weekend and was run early instead; study2/DEVIATIONS.md records the change.

New during the sprint weekend (23–25 October 2026): <<FILL: what you actually did during the sprint, for example the final rewrite of this report, final checks, and anything else; if the hand labels or the rewrite were done before the sprint, say so with dates>>

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

[10] Cliff, D. (1997). Minimal-Intelligence Agents for Bargaining Behaviours in Market-Based Environments. Hewlett-Packard Laboratories Technical Report HPL-97-91.

[11] Qwen Team (2024). Qwen2.5 Technical Report. arXiv:2412.15115. https://arxiv.org/abs/2412.15115

[12] Grattafiori, A., et al. (2024). The Llama 3 Herd of Models. arXiv:2407.21783. https://arxiv.org/abs/2407.21783

[13] Supreme Court of the United States (1940). United States v. Socony-Vacuum Oil Co., 310 U.S. 150. U.S. Reports. https://www.govinfo.gov/content/pkg/USREPORTS-310/pdf/USREPORTS-310-150.pdf

## Appendix A: Limitations and Dual-Use / Ethical Considerations

**What the results do not establish.** A low false-alarm rate for D4 in this market does not establish that the rule works in other markets, with larger models, or against sellers trying to evade it. A flag from any detector here does not establish that a real firm colluded: the markets are simulated, the stakes are zero, and the definition of agreement is the one in the labelling guide. The results also do not establish what US or any other law requires; the legal doctrine is used as a design idea, not applied to facts.

**Dual use.** Describing what a detector checks also describes how to pass it. D4 can be evaded by coordinating without messages, by acting on a message after more than 2 hours, or by keeping asks spread apart. The monitoring condition shows one way sellers change their messages when told they are watched. I judged these risks small: the evasions are obvious from the rule itself, the models are small open-weight models, and the paper releases no technique for hiding coordination. The benefit is a test that auditors can run before they accuse anyone on the strength of parallel prices.

**Ethics.** No people took part. The only human data are my own labels. The study used open-weight models on free Kaggle GPUs and no paid API.

## LLM Usage Statement

Claude (Anthropic, model Claude Opus 5.5), used as a coding agent in Claude Code, wrote the code that connects the Agrawal et al. [2] market to the logged model client, wrote the analysis and figure scripts, drafted the question card and the preregistration from my chosen question, ran the experiments on Kaggle at my request, and drafted the text of this report. I chose the research question, reviewed and froze the preregistration, labelled the messages by hand, checked every number in this report against the analysis outputs, and rewrote the draft. The sellers and the message judge in the experiments are the open-weight models named in Methods. <<FILL: make this statement match exactly what you did, including how much of the text you rewrote>>
