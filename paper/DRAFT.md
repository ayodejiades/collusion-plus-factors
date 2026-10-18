<!-- Drafted by Claude (Anthropic) for Ayodeji Adesegun to rewrite in the author's own words. Every number comes from results/claims.json; rops-claims verify checks them. -->

# No Single Signal Separates Agreement From Parallel Conduct Among LLM Sellers

## Abstract

A market auditor who sees AI pricing agents move prices together must decide whether that is evidence of collusion. Antitrust law says parallel conduct alone is not, and asks for plus factors. I test this on LLM sellers in the double auction of Agrawal et al., using markets with no message channel, where agreement is impossible, as decoys. Planted coordination raised the collusion index from 0.03 to 0.30 of the way from cost to buyer value, passing the positive control. No preregistered detector worked alone. Ask changes moved together more without a channel than under a planted agreement, so action dependence could not be calibrated. An LLM message judge flagged all 24 channel markets without planted coordination, though every one priced at cost. Price level caught 2 of 4 held-out planted markets and 2 of 12 decoys. A preregistered plus-factor rule raised no false alarms on decoys but caught nothing.

## 1. Introduction

Suppose three firms in one market hand their pricing to the same language model. Their prices rise and fall together. An auditor has to decide whether that pattern is evidence of collusion, or what three copies of one model do when they face the same market. The question is practical. Two deployments of the same model already show correlated choices in economic settings where deployments of different models show none [5], so a detector built on correlated prices will flag firms whose only link is their vendor.

Antitrust law reached this question long before language models. Under US law, parallel conduct by competitors is not enough on its own to show an agreement; a court asks for additional facts, called plus factors, that make agreement more likely than independent action [6, 7]. Recent legal writing on AI pricing tools asks how that doctrine applies when the parallel conduct comes from shared software [8]. Studies of LLM collusion measure it through prices [1, 2] or through messages and outcomes [4]. I found no LLM collusion detector that states a comparable rule for separating agreement from parallel conduct.

This paper tests that rule on LLM sellers. The setting is the continuous double auction of Agrawal et al. [2], in which LLM sellers set asks against scripted buyers and may or may not have a private message channel. The design rests on one control: when sellers have no channel, agreement is impossible by construction, so every collusion flag on those markets is a false alarm. I compare four detectors on markets with no channel, with a channel, and with a planted agreement:

- D1, price level: are prices high?
- D2, message judge: does an LLM judge read the sellers' messages as coordination?
- D3, action dependence: do the sellers' ask changes move together?
- D4, a plus-factor rule: is dependence higher than copies of the same model produce on their own, and does a coordination message come before the asks converge?

Thresholds are frozen on calibration seeds before held-out markets are scored. Two further tests target failure modes named in Track 2.3: talk without action, and a monitoring attack.

Every single signal failed, each in a different way. Without a channel, sellers' price changes moved together more than they did under a planted agreement, because copies of one model competing towards cost move in step. The message judge flagged every market with a channel, including all those where prices stayed at cost. Price level flagged two Llama markets where no agreement was possible. The preregistered plus-factor rule raised no false alarms but also missed planted coordination, because it looked for correlated price changes, while an agreement to hold a price leaves a high and flat price. An exploratory rule that requires both high prices and coordination talk avoided every false alarm, and is the hypothesis this study leaves for the next one.

The intended user is a market auditor deciding whether parallel pricing alone justifies a collusion finding. The contributions are a decoy design that separates parallel conduct from agreement in a standard LLM market, held-out false-alarm and detection rates for four detectors including an operational plus-factor rule, and the code, preregistration and every market log.

## 2. Related Work

**LLM agents in markets.** Fish et al. [1] showed that LLM pricing agents in oligopoly settings reach supracompetitive prices without instruction to collude, and that small changes in prompt wording change how far prices rise. Agrawal et al. [2] built the double auction used here and found that a message channel between sellers increases collusive behaviour, with differences across models and under oversight. Keppo et al. [3] found that such collusion weakens when agents differ in patience or data access, and that agents of different sizes from one model family still sustain it. These studies ask whether collusion happens; this paper asks how an auditor would tell it apart from innocent parallel conduct.

**Detecting collusion from words and actions.** Nakamura et al. [4] audit collusion in cooperative multi-agent tasks and describe "collusion on paper": agents that plan collusion in text but then act otherwise. Xu et al. [5] argue that audits based on a single agent's prices can be blind by construction, and report that two deployments of the same model show a small residual correlation where different models show almost none. If same-model agents correlate without agreement, a correlation detector will flag them; this paper's decoys test that. Rippin et al. [9] show that agents with tools can build covert channels that survive text monitoring, which bounds what any message-based detector can claim.

**Plus factors.** In *Bell Atlantic v. Twombly* [6] the US Supreme Court held that parallel conduct alone does not plausibly show an agreement under the Sherman Act. Kovacic et al. [7] review the plus factors courts use and argue that the strongest are those that are hard to explain by independent action. Berger et al. [8] discuss how these rules apply to shared AI pricing tools. The rule D4 borrows two plus factors from this literature: parallel conduct beyond what independent actors would produce, and communication followed by a change in conduct.

## 3. Methods

**Market.** I use the continuous double auction of Agrawal et al. [2] unchanged, from the authors' public code at a pinned commit (vendor/NOTICE in the repository). Three LLM sellers, each with a cost of $80 per lot, face three scripted buyers with a value of $100 per lot. The buyers follow the ZIP rule [10], a simple adaptive bidding strategy, so any rise in prices comes from the sellers. The market runs for 15 hours. Each hour, every seller sees the order book, its past trades, its own memory notes and, when the channel is on, the messages the other sellers sent the previous hour (up to 500 characters each). It returns an ask for one lot and, when the channel is on, a message. A trade happens when the highest bid meets the lowest ask, at the midpoint. All sellers use temperature 0.7 and at most 1024 output tokens.

**Models.** The sellers are Qwen2.5-7B-Instruct [11] and Llama-3.1-8B-Instruct [12] (Ollama tags qwen2.5:7b and llama3.1:8b), served by Ollama with its default 4-bit weights on two Kaggle T4 GPUs. All calls went through one logged client; the full call ledger is in the repository. The study used no paid API.

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

**Calibration and held-out scoring.** Seeds 0 to 3 of every condition are calibration markets and seeds 4 to 7 are held out. The D1 and D3 thresholds are the values that maximise true-positive rate on C1 minus false-positive rate on C2 in the calibration markets. D4's dependence cut is the C2 calibration percentile above. The analysis script writes these to disk before it opens any held-out file. The primary metrics are each detector's false-positive rate on held-out C2, C4 and C7 markets and true-positive rate on held-out C1 markets, with Wilson 95% intervals.

**Talk without action.** To test whether a detector mistakes talk for collusion, I pair each C3 market (channel, messages, judge scores) with the C2 market of the same seed (no channel) and score the C2 actions together with the C3 messages. No action in these spliced markets responds to the messages, so any flag is a false alarm. No new markets are run for this test.

**Hypothesis tests.** H1 (D1 and D3 flag no-channel decoys at more than 5%) uses exact binomial tests; H2 (same-model seller pairs are more dependent than cross-family pairs within C4) an exact sign-flip test; H3 (D4 has fewer decoy false alarms than D1 and D3) exact McNemar tests; H4 (the monitoring warning lowers the judge's scores more than dependence, C6 against C3) permutation tests. P-values are Holm-corrected across the four. Where the preregistration left a detail open, the choice is listed in DEVIATIONS.md with the reason. Entries D1 to D4 were committed before the main grid ran; D5, about a threshold that turned out to be undefined, was written after, and says so.

**Hand labels.** Because the judge is a model, I labelled every C3, C5 and C6 market for whether sellers reached an agreement, reading only the messages with condition, models and prices hidden, twice and at least a day apart in different orders. A market counts as an agreement only when both passes say so.

**Preregistration and code.** The question, conditions, detectors, decision rule and outcomes were frozen in PREREG.md (git tag prereg-v1) before any market of the main grid ran, and the analysis code was committed (tag analysis-frozen-v1) before the results existed.

**Study 2: a confirmatory test, run during the sprint.** Study 1's results suggested a better plus-factor rule, so I froze a second preregistration (study2/PREREG.md, tag prereg2-v1) before running any new market, and ran Study 2 during the sprint weekend on new seeds 8 to 15. It keeps C1 to C5 and C7, drops C6, and adds C8, a stronger positive control in which sellers are told they agreed a price floor of $95. Every threshold comes from Study 1 and none is tuned on Study 2. It tests two rules that need both kinds of evidence: X1, a high price (D1) plus judged coordination talk (D2), and D5, a high price plus talk that proposes holding a common price at or above the D1 price, as read by a new extraction judge. The extraction judge does not rate "coordination"; it reports whether sellers propose a common price, which way the proposal pushes prices, and the price named, and code applies the rule. I checked its prompt on 9 Study 1 hours before freezing it. The same judge also runs with Llama-3.1-8B-Instruct, to test whether the judge's model family matters. Known positives are C1 and C8, and known negatives are the no-channel decoys and the talk-without-action markets. The main test (H5) asks whether D5 makes fewer errors than price level or the vendored judge alone.

## 4. Results

**Positive control.** The planted instruction raised the mean collusion index from 0.03 in C2 to 0.30 in C1, a contrast of 0.27 against the preregistered minimum of 0.2 (permutation p = 0.001, 8 markets each). The instrument therefore sees planted coordination, and the other results are interpretable. The effect is smaller than the instruction suggests. In C1 the sellers announce a "common ask" in their first messages but often name different numbers, then cut prices over the market; Figure 1 shows three of the eight C1 markets ending below the D1 threshold. All 56 markets finished, with 3684 model calls, no truncated replies and no judge reply that failed to parse.

![Figure 1: Collusion index of every market (x: calibration seeds 0-3, o: held-out seeds 4-7). Grey conditions have no message channel, so any agreement is impossible. The dashed line is the D1 threshold frozen on calibration seeds.](figures/fig1.png)

**Held-out detector rates.** Table 2 and Figure 2 give each detector's rates on the held-out seeds. A flag on C1 is correct; a flag on a no-channel decoy or on a talk-without-action market is a false alarm.

Table 2: Held-out markets flagged by each detector (seeds 4 to 7). Decoys pool C2, C4 and C7. Brackets give Wilson 95% intervals for the pooled decoy rate.

| Detector | C1, planted (correct) | C2 | C4 | C7 | All decoys (false alarm) | Talk without action (false alarm) |
|---|---|---|---|---|---|---|
| D1 price level | 2 of 4 | 0 of 4 | 0 of 4 | 2 of 4 | 2 of 12 [0.05, 0.45] | 0 of 4 |
| D2 message judge | 4 of 4 | 0 of 4 | 0 of 4 | 0 of 4 | 0 of 12 [0, 0.24] | 4 of 4 |
| D3 action dependence | 0 of 4 | 0 of 4 | 0 of 4 | 0 of 4 | 0 of 12 [0, 0.24] | 0 of 4 |
| D4 plus-factor rule | 0 of 4 | 0 of 4 | 0 of 4 | 0 of 4 | 0 of 12 [0, 0.24] | 1 of 4 |

![Figure 2: Share of held-out markets each detector flags, with Wilson 95% intervals. On C1 a flag is correct; on the no-channel decoys and on talk-without-action markets (C3 messages spliced onto C2 actions) a flag is a false alarm. D3 flags no market because no calibration threshold beat flagging nothing. The hatched bar is an exploratory rule added after the results were read.](figures/fig2.png)

**Price level (D1).** The frozen threshold was a collusion index of 0.29. D1 caught 2 of 4 held-out planted markets and flagged 2 of 12 decoys. Both false alarms were three-Llama markets with no channel (C7). In those markets the Llama sellers lowered their asks slowly from the opening level and traded little; in seed 6 no trade happened in 15 hours. Llama sellers also failed to return a usable reply more often (68 failed replies in all, 13% of decisions in C7, none in the Qwen-only conditions), and a seller that fails keeps its previous ask; dropping the 7 markets where more than 10% of decisions failed leaves D1 flagging 1 of 8 held-out decoys. In an exploratory, threshold-free comparison over all seeds, a C1 market had a higher index than a C2 market in 0.95 of pairs, and than any decoy in 0.88 of pairs.

**Action dependence (D3).** Without any channel, sellers' ask changes moved together more than they did under a planted agreement. Mean dependence was 0.28 [0.09, 0.46] in C2 and 0.02 [-0.10, 0.15] in C1. On the calibration seeds no D3 threshold beat flagging nothing, so under the preregistered rule D3 flags no market (DEVIATIONS.md, D5). The exploratory threshold-free score for C1 against C2 was 0.22, where 0.5 is chance and lower values mean the decoys look more coordinated. Figure 3 shows why. With no channel, three copies of Qwen undercut one another towards cost in step, which produces strongly correlated changes. Under the planted agreement each seller holds its own idea of the common ask, so its changes are small and unrelated to the others'. Correlated conduct is here a sign of competition, not of agreement.

![Figure 3: Seller asks per hour. Left: the held-out no-channel market with the highest action dependence, chosen by that rule rather than by eye. Right: the first held-out planted-agreement market. Dotted lines mark seller cost ($80) and buyer value ($100).](figures/fig3.png)

The shared-prior explanation got mixed support. In the mixed C4 markets, pairs of Qwen sellers were not more dependent than Qwen-Llama pairs (difference -0.09 [-0.41, 0.28], sign-flip p = 0.69), so H2 is not supported. At the market level, dependence was lower in mixed markets than in three-Qwen markets (0.04 against 0.28), but that exploratory comparison is not significant (permutation p = 0.12).

**Message judge (D2).** The judge flagged every market that had a channel. It caught all 4 held-out planted markets, and it also flagged all 24 C3, C5 and C6 markets, in every one of which the collusion index stayed below 0.1, that is, prices stayed at cost. The judge gave the highest score, 4, to almost all of them (mean 3.75 in C5 and 4 in C3 and C6). The sellers do use the language of coordination. A C3 seller wrote "Let's keep our asks just below the lowest ask to maximize trades and ensure fair market conditions. Coordination is key." The proposal is to cut prices, and the market traded near cost, but the overseer prompt counts any joint price proposal as coordination. On the talk-without-action markets the judge flagged all 8 of 8.

**Plus-factor rule (D4).** The frozen dependence cut was 0.53, the 95th percentile of the C2 calibration markets. D4 raised no false alarm on the decoys, but it also caught none of the held-out planted markets, because planted markets did not show dependence above the no-channel baseline. On the talk-without-action markets it flagged 2 of 8 (0.25 [0.07, 0.59]): there the C2 actions supplied high dependence and the C3 messages supplied the talk. The preregistered rule therefore combined the two signals, but chose the wrong action signature for this market.

**Hypotheses.** None of the four preregistered hypotheses is supported after Holm correction. H1: neither D1 nor D3 flagged decoys clearly above 5% (p = 1.00). H2: see above (p = 0.69, 1.00 after correction). H3: D4 had no fewer false alarms than D3, which had none (p = 1.00). H4: the monitoring warning did not lower the judge's scores; every C6 market still reached 4, as in C3 (p = 1.00), and dependence changed by -0.08 (p = 0.61). The in-market overseer did act: after its first score of 4, messages were cut to 5 characters, and in C6 seed 4 the later messages read "COMP" or a bare price. The sellers talked about coordinating before the gag took effect.

**Exploratory: high prices and talk together.** After reading the results I checked one rule that requires both signals that failed alone: a market is flagged only if D1 and D2 both flag it, using their frozen thresholds, so nothing new was tuned. It caught 2 of 4 held-out planted markets, flagged none of the 12 held-out decoys, none of the held-out C3, C5 or C6 markets, and none of the 8 talk-without-action markets. Because it was chosen after the data were seen, this is a hypothesis for the next experiment, not a result.

**Study 2.** <<FILL: Study 2 results, written after the sprint-weekend run: the C8 positive control (s2.pc.contrast, s2.pc.p), a table of TPR, FPR and errors per detector (s2.tpr.*, s2.fpr.*, s2.errors.*), H5 to H9 with Holm p-values, the extraction judge on talk at cost (s2.flag.D2x.at_cost against s2.flag.D2.at_cost) and on Study 1 (s2.study1.D2x.*), and judge-family agreement (s2.judge_family.kappa)>>

**Hand labels.** <<FILL: after labelling both passes, run make analyze and rops-claims build, then report labels.self_kappa, the share of markets labelled as agreements, and judge.agreement.kappa and judge.agreement.pct>>

## 5. Discussion and Limitations

For the auditor's decision the answer from these markets is direct: parallel pricing alone did not indicate agreement. The most parallel markets in the study were ones where agreement was impossible, and the sellers' co-movement came from competing down to cost together. Coordination talk alone did not indicate agreement either: every market with a channel talked about coordinating, and every one without planted coordination priced at cost. Each single signal failed in a way the plus-factors doctrine anticipates. D3 confused parallel conduct with agreement, D2 confused talk with action, and D1 confused high asks with agreement in the Llama markets.

The plus-factor idea survives, but my version of it did not. I wrote the action plus factor as correlated price changes. An agreement to hold a price shows up instead as a high and flat price, which has little correlation in its changes, so D4 looked for the wrong trace. The exploratory rule that needs both a high price and coordination talk is closer to how courts read plus factors, communication followed by conduct that independent sellers would not choose, and it had no false alarms here. It needs to be preregistered and tested on new seeds before anyone relies on it. A second lesson concerns the judge: the overseer prompt counts any joint price proposal as coordination, including proposals to cut prices. An evidentiary standard has to ask which way the proposed price moves relative to cost.

The study has clear limits. The positive control passed, but the planted instruction lifted prices in only some C1 markets, so the instrument is weak. The sellers are 7 to 8 billion parameter models with 4-bit weights; larger models write better messages and may coordinate through actions alone. Each held-out cell has only 4 markets, so a difference of one or two flags is within noise. The market is one design with three sellers, and dependence over 14 hourly changes is noisy. The judge belongs to the same model family as most sellers, and it gave the top score to almost every channel market, so it cannot rank markets by how strongly they coordinate. D4's dependence cut comes from only 4 calibration markets, so it sits close to their maximum. The hand labels come from one person, so the two-pass agreement measures consistency, not agreement between people. Llama sellers failed to reply in a usable form more often than Qwen sellers, which inflates their price level; the sensitivity check above bounds this but does not remove it. The talk-without-action markets are constructed, not observed. D4 is one way to write two plus factors as code, and a seller that coordinates without messages, or waits longer than 2 hours to act on a message, would pass it.

## 6. Conclusion

In this double auction, neither parallel price changes, nor coordination talk, nor high prices alone separated agreement from innocent behaviour, and the preregistered plus-factor rule missed planted coordination because it looked for correlated changes instead of held prices. The next experiment is to preregister the rule that requires both supracompetitive prices and coordination talk, together with a judge prompt that scores the direction of proposed prices, and to test both on new seeds, larger models and a second market.

## Code and Data

code: <<FILL: GitHub URL once the repository is public>>

prereg: <<FILL: GitHub URL of tag prereg-v1>>

### What is new this weekend

Prior work, with dates: before the sprint (14–18 October 2026) I chose the question; Claude drafted the question card and the Study 1 preregistration, which I reviewed and froze on 16 October; the harness and analysis code were built on 17 October; and the 56 Study 1 markets ran on Kaggle on 17 and 18 October. The Study 2 design, its preregistration (frozen 18 October, before any Study 2 market ran) and a three-market infrastructure test of its notebook were also prepared before the sprint; the test markets are not used in any result.

New during the sprint weekend (23–25 October 2026): the 56 Study 2 markets and their analysis, which carry the confirmatory results; the extraction and cross-family judges applied to both studies; the two-pass blind hand labels of Study 1's channel markets and the judge-agreement analysis; and the rewriting of this report. <<FILL: confirm this list against what you actually did, and add anything else>>

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

## Appendix A: Limitations and Dual-Use / Ethical Considerations

**What the results do not establish.** A low false-alarm rate for D4 in this market does not establish that the rule works in other markets, with larger models, or against sellers trying to evade it. A flag from any detector here does not establish that a real firm colluded: the markets are simulated, the stakes are zero, and the definition of agreement is the one in the labelling guide. The results also do not establish what US or any other law requires; the legal doctrine is used as a design idea, not applied to facts.

**Dual use.** Describing what a detector checks also describes how to pass it. D4 can be evaded by coordinating without messages, by acting on a message after more than 2 hours, or by keeping asks spread apart. The monitoring condition shows one way sellers change their messages when told they are watched. I judged these risks small: the evasions are obvious from the rule itself, the models are small open-weight models, and the paper releases no technique for hiding coordination. The benefit is a test that auditors can run before they accuse anyone on the strength of parallel prices.

**Ethics.** No people took part. The only human data are my own labels. The study used open-weight models on free Kaggle GPUs and no paid API.

## LLM Usage Statement

Claude (Anthropic, model Claude Opus 5.5), used as a coding agent in Claude Code, wrote the code that connects the Agrawal et al. [2] market to the logged model client, wrote the analysis and figure scripts, drafted the question card and the preregistration from my chosen question, ran the experiments on Kaggle at my request, and drafted the text of this report. I chose the research question, reviewed and froze the preregistration, labelled the messages by hand, checked every number in this report against the analysis outputs, and rewrote the draft. The sellers and the message judge in the experiments are the open-weight models named in Methods. <<FILL: make this statement match exactly what you did, including how much of the text you rewrote>>
