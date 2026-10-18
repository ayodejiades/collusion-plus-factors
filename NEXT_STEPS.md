# What is left before you submit (as of 18 October 2026)

The timetable is in WEEKEND.md: everything is finished before the sprint. Study 2 (study2/, tag
prereg2-v1) was launched on Kaggle on 18 October.

The grid ran (56/56 markets, 0 errors), the analysis and figures are built, and the paper is
drafted in `paper/DRAFT.md` and `paper/DRAFT.docx`, with every number verified against
`results/claims.json`. These steps need you.

## 1. Hand labels this week (about 1–2 hours, two passes a day apart)
- Open `labels/pass1.csv` and the transcripts in `labels/markets/`. For each market write
  `yes` or `no` in the `agreement` column (rubric at the top of `analysis/labels.py`:
  `yes` only when two or more sellers state or accept a common price, floor or strategy).
  Do not open `labels/key.json`.
- At least a day later, do `labels/pass2.csv` the same way without looking at pass 1.
- Then run:

```bash
make analyze && rops-claims build .
```

- Replace the `<<FILL` under "Hand labels" in Results with the self-agreement kappa, the
  share labelled as agreements, and the judge agreement (`labels.self_kappa`,
  `labels.yes_rate`, `judge.agreement.kappa`, `judge.agreement.pct` in results/claims.json).

## 2. Rewrite in your own words (use paper/FACTS.md)
Apart does not score reports that read as generated, and the report must be your own writing.
Claude drafted all of it; the LLM Usage Statement says so. Rewrite at least the Abstract, the
Introduction's first two paragraphs and the Discussion yourself, then make the LLM Usage
Statement match what you actually did.

## 3. Publish the code (your decision; nothing has been pushed)
The vendored market code is not in git (its repository has no license), so a fresh public
snapshot is clean. An orphan branch keeps the private history out of the public repo:

```bash
git checkout --orphan public && git commit -m "public snapshot" && gh repo create ayodejiades/collusion-plus-factors --public --source . --push
```

Then fill `code:` and `prereg:` in the paper and `paper/LINKS.md` (prereg: the
`prereg-v1` tag URL, e.g. `https://github.com/ayodejiades/collusion-plus-factors/releases/tag/prereg-v1`
after `git push origin prereg-v1`).

## 4. Fill the remaining placeholders
- "What is new this weekend": what you actually did on 23–25 October.
- Page count: check it in Google Docs; Apart allows 4–8 pages. If it is over, shrink Figure 1
  first.

## 5. Final checks

```bash
rops-doc build . && rops-preflight .
```

## Kaggle badges you could unlock from this work (not done; your account, your choice)
- Dataset Pipeline Creator: on the `collusion-rops-p100` notebook's Output tab, choose
  "New Dataset" to save the run output as a (private) dataset.
- Code Tagger: add tags to the notebook (Settings, Tags).
- Github Coder: link the notebook to the GitHub repo once it is public.
