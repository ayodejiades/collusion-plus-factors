# Facts for writing the paper in your own words

Write each section from these bullets, in your own sentences, without looking at DRAFT.md. Every
number here is in results/claims.json; `rops-claims verify . --paper paper/paper.md` checks
yours. Study 2 ran on 18 October (study2/DEVIATIONS.md D1).

## Title
- Must contain a finding verb. Current: "No Single Signal Separates Agreement From Parallel
  Conduct Among LLM Sellers". Revisit after Study 2 (if D5 works, the title can say so).

## Abstract (max 150 words)
- User: a market auditor deciding whether parallel AI pricing is evidence of collusion.
- Law: parallel conduct alone is not enough; courts ask for plus factors [6, 7].
- Design: Agrawal et al. double auction; no-channel markets are decoys (agreement impossible).
- Positive control: planted coordination index 0.30 vs 0.03 (0 = cost, 1 = buyer value).
- Findings: no single detector works (D3 inverted, D2 flags all 24 talk-at-cost markets, D1 2 of
  12 decoys); preregistered D4 caught nothing.
- Study 2: price floor 0.75; extraction judge cuts talk-at-cost false alarms 15 of 15 -> 7 of 15
  (Holm p = 0.04); high price + price-holding talk: 0 false alarms on 32 negatives, misses failed
  agreements.

## 1. Introduction
- Problem: firms using the same model may price in parallel without agreement; Xu et al. [5]
  found same-model deployments correlate (different models do not).
- Law reached this first: Twombly [6], plus factors [7], shared AI pricing tools [8].
- LLM collusion work measures prices [1, 2] or messages/outcomes [4]; no detector states such a rule.
- What you did: four detectors (D1 price, D2 judge, D3 dependence, D4 plus-factor rule) on markets
  with no channel, a channel, and a planted agreement; frozen thresholds; held-out scoring; talk
  without action; monitoring attack; Study 2 confirmatory test during the sprint.
- Result preview: every single signal failed in a different way (see Results).

## 2. Related Work
- Fish et al. [1]: LLM pricing agents reach supracompetitive prices; prompt wording matters.
- Agrawal et al. [2]: built this market; a channel increases collusion; differs by model.
- Keppo et al. [3]: collusion fragile under heterogeneity; size differences within a family do not break it.
- Nakamura et al. [4]: "collusion on paper", agents plan collusion in text but act otherwise.
- Xu et al. [5]: price-level audits blind by construction; same-model residual correlation.
- Rippin et al. [9]: tool-using agents can build covert channels (limits message monitoring).
- Twombly [6], Kovacic et al. [7] (strongest plus factors are hard to explain by independent
  action), Berger et al. [8] (shared AI pricing tools).

## 3. Methods (Study 1)
- 3 LLM sellers (cost $80), 3 ZIP buyers [10] (value $100), 15 hours, temperature 0.7, 1024
  tokens, messages up to 500 characters read the next hour, trades at the midpoint.
- Models: Qwen2.5-7B-Instruct [11], Llama-3.1-8B-Instruct [12], Ollama 4-bit, Kaggle T4 GPUs, no paid API.
- Seven conditions C1–C7 (Table 1), 8 seeds each, 56 markets.
- Collusion index = mean ask in the last 5 hours, 0 = cost, 1 = value. Positive control: C1 minus C2 >= 0.2.
- D1 index >= threshold; D2 vendored overseer prompt, Qwen judge, temperature 0, any hour >= 3;
  D3 mean pairwise correlation of ask changes; D4 dependence above the C2 95th percentile plus a
  judged message followed within 2 hours by a falling spread.
- Thresholds on seeds 0–3 (Youden on C1 vs C2), scored once on seeds 4–7, Wilson intervals.
- Talk without action: C3 messages spliced onto C2 actions (same seed).
- Tests: H1 binomial vs 5%, H2 sign-flip, H3 McNemar, H4 permutation, Holm.
- Prereg tag prereg-v1; analysis tag analysis-frozen-v1; DEVIATIONS.md D1–D5 (D5 after results).

## 4. Results (Study 1)
- Positive control: 0.30 vs 0.03, contrast 0.27 (bar 0.2), p = 0.001; weak (three of eight C1
  markets end below the D1 threshold); C1 sellers "agree" but name different prices.
- 56/56 markets, 3684 calls, no truncation, no judge parse failure; 68 seller parse failures
  (13% of decisions in C7, none in Qwen-only conditions).
- D1: threshold 0.29; 2 of 4 planted, 2 of 12 decoys (both C7 Llama, slow price cuts, few
  trades; seed 6 no trades); 1 of 8 after dropping the 7 high-failure markets; AUROC 0.95 vs C2.
- D3: dependence 0.28 in C2 vs 0.02 in C1; no threshold beat flagging nothing; AUROC 0.22.
  Mechanism (Figure 2): no-channel copies undercut to cost together; planted sellers hold
  different "common" asks.
- H2: same-model vs cross-family pairs in C4, difference -0.09, p = 0.69; market level C4 0.04
  vs C2 0.28, exploratory p = 0.12.
- D2: flags every channel market; all 24 C3/C5/C6 priced at cost (index < 0.1); quote "Let's keep
  our asks just below the lowest ask ... Coordination is key."; 8 of 8 talk-without-action.
- D4: cut 0.53; 0 of 12 decoys, 0 of 4 planted, 2 of 8 talk-without-action (0.25).
- Hypotheses: none supported after Holm; H4: C6 still scored 4 everywhere, dependence -0.08,
  p = 0.61; the gag cut messages to 5 characters ("COMP").
- Exploratory X1 = D1 and D2: 2 of 4 planted, 0 of 12 decoys, 0 C3/C5/C6, 0 of 8 splices.

## 5. Discussion
- Decision: parallel pricing alone is not evidence of agreement here; nor is coordination talk alone.
- Each single signal fails as the doctrine predicts: parallel conduct, talk without action, high
  prices without agreement.
- Your D4 used the wrong conduct trace; agreement shows as a held high price. Study 2 tests the fix.
- The vendored judge counts proposals to cut prices as coordination; direction matters.
- Limits: weak positive control, 7–8B models, 4 markets per held-out cell, one market design,
  same-family saturated judge, D4 cut from 4 markets, one labeller, Llama parse failures,
  constructed splice markets, D4 is one encoding.

## Appendix and LLM statement
- "does not establish" sentence is required (lint L13).
- Dual use: detector rules describe how to evade them; risks small; no evasion technique released.
- LLM Usage Statement: say plainly that Claude drafted text and code, and what you did.

## 4. Results (Study 2, confirmatory; tag prereg2-v1; seeds 8-15; thresholds from Study 1)
- Positive controls: C8 (price floor $95) 0.75 vs C2 0.01, contrast 0.74 (bar 0.3), p = 0.0002;
  C1 replicates, contrast 0.30, p = 0.0006. 56/56 markets; 63 seller parse failures.
- Known set: 16 positives (C1, C8), 32 negatives (24 decoys, 8 talk-without-action). Table 3:
  caught / false alarms / errors: D1 11/0/5, D2 16/8/8, D2x 15/3/4, D2x-L 16/4/4, D3 0/0/16,
  D4 0/2/18, X1 11/0/5, D5 11/0/5.
- H7 supported: on 15 C3/C5 markets at cost, D2 flagged 15, D2x 7 (p = 0.008, Holm 0.039).
  D2x's 3 false alarms were all talk-without-action (high price proposed in words, no action).
  Secondary on Study 1: D2x flagged 3 of 8 C3 and 0 of 8 C6 (vendored judge: all).
- H5, H6 not supported: D5 and X1 had 0 false alarms (Wilson 0 to 0.11) but missed 5 C1
  markets (agreed in words, prices fell); D1 alone also had 0 false alarms in Study 2 (C7 mean
  0.07), so the rules tied with D1. vs D2: 8 false alarms traded for 5 misses (p = 1.00).
- H8: Qwen and Llama extraction judges agree 0.84 (kappa 0.53), Holm p = 0.25.
- H9: dependence C2 0.26 vs C1 0.08, p = 0.21 (direction replicates, not significant); D4 again 0.

## 5. Discussion (both studies)
- Fix 1: ask the judge for the proposed price, not for "coordination" (halves talk-at-cost false alarms).
- Fix 2: require high price plus price-holding talk; no false alarms across both studies'
  negatives; protects against high-price false alarms that appear in some markets (Study 1 Llama).
- Cost: misses failed agreements; under US law a price-fixing agreement is unlawful even if it
  fails [13] (Socony-Vacuum), so an auditor who must catch those still needs message evidence.
