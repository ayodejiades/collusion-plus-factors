# Parallel conduct is not agreement

Do collusion detectors mistake parallel pricing by copies of the same LLM for collusion, and does
a plus-factor rule from antitrust law separate agreement from shared priors? Entry by Ayodeji
Adesegun (Team discreet) to the Apart Research AI Collusion Research Sprint, 23–25 October 2026
(Track 2.3, with Track 1.3).

The market is the continuous double auction of Agrawal et al. (2025), arXiv:2507.01413, run
unchanged: three LLM sellers (cost $80) against three scripted ZIP buyers (value $100) for 15
hours. Seven conditions vary the seller message channel and the seller model mix. In the no-channel
conditions agreement is impossible by construction, so any collusion flag on them is a false
alarm. Four detectors are compared: price level (D1), an LLM message judge (D2), action
dependence (D3) and a plus-factor rule (D4).

## Files

| Path | What |
|---|---|
| `QUESTION.md`, `PREREG.md` | the question card and the preregistration (git tag `prereg-v1`) |
| `DEVIATIONS.md` | every choice the preregistration left open, committed before the main grid ran |
| `configs/experiment.json` | conditions, seeds, models, positive control |
| `harness/` | `run_one.py` (one market), `agrawal_bridge.py` (runs the vendored market through a logged client), `fetch_vendor.sh` |
| `analysis/` | `detect.py` (thresholds on calibration seeds, held-out scoring, H1–H4, talk without action), `labels.py` (blind two-pass hand labels), `figures.py` |
| `runs/` | one folder per market: `result.json` and the full market log; `runs/calls.jsonl` is the ledger of every model call |
| `results/` | `detectors.json`, `thresholds.json`, `positive_control.json`, `claims.json` (every number in the paper) |
| `kaggle/` | the notebook that ran the grid on Kaggle (2×T4, Ollama) |
| `paper/` | the report |

## Reproduce

Needs Python 3.11+, git, and the ResearchOps toolkit (`ROPS_HOME`, for `rops.llm` and
`rops.stats`). The market code is fetched, not redistributed (its repository has no license):

```bash
sh harness/fetch_vendor.sh
```

Run the grid on a GPU (the Kaggle notebook in `kaggle/`, or a local Ollama with `qwen2.5:7b`
and `llama3.1:8b` pulled):

```bash
rops-run grid . --provider ollama --force-main
```

Rebuild every number and figure from `runs/`, with no model calls:

```bash
make analyze
python3 analysis/figures.py
rops-claims build .
```

Hand labels: `python3 analysis/labels.py export` writes blind transcripts and two label sheets;
fill `labels/pass1.csv`, wait a day, fill `labels/pass2.csv`, then `make analyze` scores them.

## Disclosure

The question, preregistration, harness, analysis code and the 56-market grid were prepared and
run before the sprint (14–17 October 2026), with dates in the git history. Claude (Anthropic)
wrote the harness glue, the analysis code and a first draft of the report; see the LLM Usage
Statement in the paper.
