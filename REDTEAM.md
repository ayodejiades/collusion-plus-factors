# Red team

Responses drafted by Claude on 18 October 2026 against the results; Ayodeji to check each one.

### A1: What decision changes, and for whom, if this result is true?
Status: fixed
Response: A market auditor should not treat parallel price changes, or coordination talk, as evidence of agreement on its own: in these markets the most parallel conduct came from no-channel competition, and every market with a channel talked coordination while pricing at cost. The Discussion's first paragraph states this.

### A2: Where is the positive control, what number did it give, and is it in Results?
Status: fixed
Response: First paragraph of Results: mean collusion index 0.30 in C1 against 0.03 in C2, contrast 0.27 against the preregistered 0.2, permutation p = 0.001. Its weakness (only some C1 markets rose) led to Study 2's explicit price floor (C8), which raised the index to 0.75 (contrast 0.74, p = 0.0002).

### A3: Does any comparison change more than one variable at once?
Status: limited
Response: C1 against C2 changes both the channel and the planted instruction, as intended for a positive control; the channel-only comparison is C3 against C2. C7 changes model identity only. The splice markets hold actions fixed and swap in messages.

### A4: Could the headline be an artefact of a token cap, truncation, parser, prompt format or judge?
Status: limited
Response: No reply was truncated and no judge reply failed to parse. Llama sellers failed to parse in 13% of decisions in C7, which inflates their price level; excluding markets with more than 10% failures cuts D1's decoy false alarms from 2 of 12 to 1 of 8, and this is reported. The judge's saturation at score 4 comes from the vendored prompt and is discussed.

### A5: Does the abstract state anything that Limitations takes back or narrows?
Status: fixed
Response: The abstract reports the negative results and the positive control, without the exploratory rule, which appears only in Results and Discussion and is labelled exploratory. Limitations narrows scope (small models, one market, 4 markets per held-out cell) without contradicting the abstract.

### A6: Do the prereg URL and code URL load, and does the code reproduce the headline numbers?
Status: limited
Response: make analyze rebuilds every number from runs/ with no model calls, and rops-claims verify matches every number in the draft except the pending judge-agreement claim. The URLs exist only once the repository is public (owner step); the vendored market code is fetched by harness/fetch_vendor.sh because its repository has no license.

### A7: What was built or run before the weekend, and is it disclosed?
Status: fixed
Response: Everything except the hand labels and the rewrite: question, preregistration, harness, analysis code and the 56-market grid (14–18 October). Disclosed with dates under "What is new this weekend" and in the README.

### A8: If an LLM judge scored anything, what is its agreement with hand labels?
Status: limited
Response: Label sheets for all 24 C3, C5 and C6 markets are exported to labels/; the agreement numbers follow the owner's two passes. Until then rops-claims verify fails its judge rule, by design.

### A9: How many seeds or samples per cell, and is variance reported?
Status: fixed
Response: Study 1: 8 seeds per condition, 4 calibration and 4 held out. Study 2: 8 new seeds per condition, 48 known markets for the confirmatory tests. Every rate has a Wilson 95% interval and every mean a bootstrap interval; the small cells are named as a limitation.

### A10: Does every reported metric have a scale a non-specialist can read?
Status: fixed
Response: The collusion index is defined as 0 at seller cost and 1 at buyer value, Table 2 gives rates as "k of n", and the threshold-free score is explained as chance at 0.5.

### A11: Does Methods describe exactly what ran, with settings identical to configs/?
Status: fixed
Response: Models, temperature 0.7, 1024 tokens, 15 hours, 8 seeds, the judge model at temperature 0 and the C6 gag rule all match configs/experiment.json and the harness; rops-claims verify checks the config numbers.

### A12: Is any section a second paper that should be cut?
Status: fixed
Response: The exploratory D1-and-D2 rule is one paragraph and one hatched bar, labelled as a hypothesis for the next study rather than developed as a second contribution.

### A13: Which three paragraphs read most like generated text, and did a human rewrite each one in their own words?
Status: limited
Response: rops-lint reports no L18 or L19 warning, but Claude wrote the whole draft and the paper discloses it. Before submission the owner must rewrite it in their own words, starting with the first two paragraphs of the Introduction and the Discussion, which carry the argument.

### N1: The positive control only just works, so maybe nothing could have been detected.
Status: limited
Response: Study 1's contrast (0.27) only just clears the bar, so Study 2 added an explicit price floor (C8), whose contrast is 0.74. C1 replicated at 0.30 in Study 2.

### N2: D3's failure might be a quirk of the correlation measure, not of parallel conduct.
Status: limited
Response: The threshold-free score (0.22) and the mean dependences (0.28 against 0.02) agree, and Figure 3 shows the mechanism. A dependence measure on price levels might behave differently; the Discussion proposes a held high price as the action plus factor instead.

### N3: The judge prompt counts proposals to cut prices as coordination, so D2's false alarms may say more about the prompt than about message-based detection.
Status: limited
Response: Agreed. Study 2 tested an extraction judge that reports the proposed price; it flagged 7 of 15 talk-at-cost markets against 15 of 15 for the vendored prompt (Holm p = 0.039), so much of D2's failure was the prompt.
