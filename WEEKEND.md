# Plan: finish before the sprint, so the hackathon weekend is light

Deadline: Mon 26 Oct 12:59 Lagos (Sun 25 Oct 23:59 AoE). Both studies run before the sprint and
the paper discloses it with dates ("What is new this weekend").

| When (Lagos time) | What | Who | Your time |
|---|---|---|---|
| Sun 18 Oct | Study 2 ran on Kaggle (56/56 markets), was analysed, and is written into the paper | done | 0 |
| Any day this week | Hand labels, pass 1: fill `labels/pass1.csv` from `labels/markets/` (rubric at the top of `analysis/labels.py`; do not open `labels/key.json`) | you | 45–60 min |
| At least 24 h after pass 1 | Hand labels, pass 2: `labels/pass2.csv`; then tell Claude "labels done" (it runs `make analyze`, rebuilds claims and fills the Hand labels paragraph) | you | 45–60 min |
| This week, in short sessions | Rewrite the paper in your own words, section by section, from `paper/FACTS.md` (Apart does not score reports that read as generated) | you | 3–4 h |
| Before Fri 23 Oct | Publish the repo (NEXT_STEPS.md step 3), upload `paper/DRAFT.docx` to Google Docs, check the page count | you, with Claude | 1 h |
| Sprint weekend | Final read, fill "What is new this weekend" with what you actually did, `rops-preflight .`, submit | you | 1 h |

## If something goes wrong with the Kaggle run
- **ERROR status:** ask Claude to read the log and fix it; finished markets are kept and the grid resumes.
- **Pull fails with 429 Too Many Requests:** download `rops-output.tar.gz` from the kernel's Output
  tab and run `rops-kaggle pull study2 --from ~/Downloads/rops-output.tar.gz`.
