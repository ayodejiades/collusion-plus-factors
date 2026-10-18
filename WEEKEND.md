# Sprint weekend plan (23–25 October 2026; deadline Mon 26 Oct 12:59 Lagos = Sun 23:59 AoE)

Everything below is new work done during the sprint, which is what "What is new this weekend"
in the paper reports. Nothing of Study 2 runs before kickoff.

| When (Lagos time) | What | Who | Time it takes you |
|---|---|---|---|
| Fri 23 Oct, 19:00 | Study 2 launches on Kaggle (scheduled task; or run `make study2-push`) | automatic | 0 |
| Fri evening | Hand labels, pass 1: fill `labels/pass1.csv` from `labels/markets/` | you | 45–60 min |
| Sat 24 Oct, ~05:00–07:00 | Study 2 finishes (about 9–10 h on Kaggle) | automatic | 0 |
| Sat morning | Tell Claude: "pull Study 2 and write it up". Claude runs `make study2-pull study2-analyze`, drafts the Study 2 results and updates the abstract, title and discussion | Claude | 5 min to ask |
| Sat | Rewrite the paper in your own words, section by section, using `paper/FACTS.md` | you | 3–4 h |
| Sun 25 Oct (24 h after pass 1) | Hand labels, pass 2: `labels/pass2.csv`, then `make analyze && rops-claims build .`; fill the Hand labels paragraph | you | 45–60 min |
| Sun | Publish the repo (NEXT_STEPS.md step 3), fill the links, upload `paper/DRAFT.docx` to Google Docs, check the page count, `rops-preflight .` | you | 1 h |
| Sun night | Submit on the sprint page | you | 15 min |

## If something goes wrong
- **Study 2 stays "Queued" on Kaggle for more than 45 minutes:** `make study2-push-alt`
  (a second kernel slug, which has started at once before). When one starts running, stop the
  other in Kaggle's "View Active Events" panel so the grid runs once.
- **`make study2-status` says ERROR:** download the log from the kernel's Logs tab and ask
  Claude to fix it; the grid resumes where it stopped (finished markets are kept).
- **`make study2-pull` fails with 429 Too Many Requests:** download `rops-output.tar.gz` from
  the kernel's Output tab and run `rops-kaggle pull study2 --from ~/Downloads/rops-output.tar.gz`.
- **Kaggle GPU quota:** Study 2 needs about 10 GPU hours; you had 22 left this week and the
  quota resets weekly.
