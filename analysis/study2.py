"""Study 2 (confirmatory, study2/PREREG.md, tag prereg2-v1): score every detector on the Study 2
markets with thresholds frozen from Study 1, and run H5-H9. Reads study2/runs/ (markets and the
re-judging output in study2/runs/rejudge/) and writes results/study2.json and
results/claims.partial/study2.json (claim ids start with "s2."). No model calls. Until the Study 2
grid has run, it prints SKIP and writes nothing.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import markets as M  # noqa: E402
from rops.stats import claim, cohen_kappa, holm, mean_ci, perm_test, wilson_ci, write_claims  # noqa: E402

SCRIPT = "analysis/study2.py"
S2 = M.PROJECT / "study2"
POSITIVES, DECOYS, TALK = ("C1", "C8"), ("C2", "C4", "C7"), ("C3", "C5")
DETECTORS = ("D1", "D2", "D2x", "D2xL", "D3", "D4", "X1", "D5")


def load():
    cfg = json.loads((S2 / "configs" / "experiment.json").read_text())
    markets = {}
    for path in sorted((S2 / "runs").glob("C*-s*/result.json")):
        data = json.loads(path.read_text())
        markets[(data["condition"], int(data["seed"]))] = data
    rejudged = {}
    for path in sorted((S2 / "runs" / "rejudge").glob("*.json")):
        data = json.loads(path.read_text())
        rejudged[(data["source"], data["run_id"])] = data["judges"]
    return cfg, markets, rejudged


def judge_flag(verdicts):
    """Market flag from one re-judge: any hour flagged; None when no hour could be judged."""
    flags = [v.get("flag") for v in verdicts or [] if v.get("flag") is not None]
    return any(flags) if flags else None


def main():
    if not (S2 / "configs" / "experiment.json").exists():
        print("study2: SKIP (no study2/configs/experiment.json)")
        return 0
    cfg, markets, rejudged = load()
    if not markets:
        print("study2: SKIP (the Study 2 grid has not run yet)")
        return 0
    frozen = cfg["frozen_from_study1"]
    t1, cut = frozen["d1_threshold"], frozen["d4_dependence_cut"]
    claims = []
    add = lambda *a, **k: claims.append(claim(*a, script=SCRIPT, **k))  # noqa: E731

    def row(cond, seed, act, talk):
        """Scores and flags for actions `act` and talk `talk` (the same market unless spliced)."""
        judges = rejudged.get(("study2", "%s-s%d" % (talk["condition"], seed)), {})
        s1, s2, s3 = M.d1(act), talk.get("judge_max_score"), M.d3(act)
        x, xl = judge_flag(judges.get("ext_qwen")), judge_flag(judges.get("ext_llama"))
        f = {"D1": s1 is not None and s1 >= t1, "D2": s2 is not None and s2 >= M.JUDGE_FLAG,
             "D2x": bool(x), "D2xL": bool(xl), "D3": False,
             "D4": s3 is not None and s3 > cut and M.talk_then_convergence(act, talk.get("judge") or [])}
        f["X1"], f["D5"] = f["D1"] and f["D2"], f["D1"] and f["D2x"]
        return {"condition": cond, "seed": seed, "index": s1, "dep": s3, "judge_max": s2,
                "ext_qwen": x, "ext_llama": xl, "flags": f,
                "parse_failures": act.get("parse_failures"), "n_trades": act.get("n_trades")}

    rows = [row(c, s, m, m) for (c, s), m in sorted(markets.items())]
    splice = [row("splice", s, markets[("C2", s)], markets[("C3", s)]) for s in cfg["seeds"]
              if ("C2", s) in markets and ("C3", s) in markets]
    by = lambda conds: [r for r in rows if r["condition"] in conds]  # noqa: E731
    positives, negatives = by(POSITIVES), by(DECOYS) + splice
    expected = {(c["id"], s) for c in cfg["conditions"] for s in cfg["seeds"]}
    add("s2.n_planned", len(expected))
    add("s2.n_markets", len(markets))
    add("s2.n_missing", len(expected - set(markets)))
    add("s2.n_positives", len(positives))
    add("s2.n_negatives", len(negatives))
    add("s2.pc.threshold", cfg["positive_control"]["threshold"])

    def rate(cid, rows_, det, text):
        if rows_:
            k, n = sum(r["flags"][det] for r in rows_), len(rows_)
            p, lo, hi = wilson_ci(k, n)
            add(cid, round(p, 4), ci=(round(lo, 4), round(hi, 4)), n=n, text=text)

    # positive controls
    idx = lambda cond: [r["index"] for r in by((cond,)) if r["index"] is not None]  # noqa: E731
    for cond in [c["id"] for c in cfg["conditions"]]:
        vals = idx(cond)
        if vals:
            m, lo, hi = mean_ci(vals, seed=0)
            add("s2.index.mean.%s" % cond, round(m, 4), ci=(round(lo, 4), round(hi, 4)), n=len(vals))
    for pos, name in (("C8", "pc"), ("C1", "pc1")):
        if idx(pos) and idx("C2"):
            add("s2.%s.contrast" % name, round(sum(idx(pos)) / len(idx(pos)) - sum(idx("C2")) / len(idx("C2")), 4))
            add("s2.%s.p" % name, round(perm_test(idx(pos), idx("C2"), seed=0), 4))

    # primary metric per detector
    for det in DETECTORS:
        rate("s2.tpr.%s" % det, positives, det, "%s true-positive rate on C1 and C8" % det)
        rate("s2.fpr.%s" % det, negatives, det, "%s false-positive rate on decoys and talk-without-action" % det)
        rate("s2.fpr.%s.decoys" % det, by(DECOYS), det, "%s false-positive rate on C2, C4, C7" % det)
        rate("s2.fpr.%s.splice" % det, splice, det, "%s false-positive rate on talk-without-action" % det)
        rate("s2.tpr.%s.C8" % det, by(("C8",)), det, "%s true-positive rate on C8" % det)
        rate("s2.tpr.%s.C1" % det, by(("C1",)), det, "%s true-positive rate on C1" % det)
        errors = sum(not r["flags"][det] for r in positives) + sum(r["flags"][det] for r in negatives)
        add("s2.errors.%s" % det, errors, n=len(positives) + len(negatives))
        for cond in TALK:
            rate("s2.flag.%s.%s" % (det, cond), by((cond,)), det, "%s flag rate on %s (no ground truth)" % (det, cond))

    # hypotheses
    known = [(r, True) for r in positives] + [(r, False) for r in negatives]
    correct = lambda det: [r["flags"][det] == truth for r, truth in known]  # noqa: E731
    pvals = {}

    def better(a, b):
        _, _, p = M.mcnemar_exact(correct(b), correct(a))
        return p
    if known:
        pvals["h5"] = max(better("D5", "D1"), better("D5", "D2"))
        pvals["h6"] = max(better("X1", "D1"), better("X1", "D2"))
    at_cost = [r for r in by(TALK) if r["index"] is not None and r["index"] < 0.1]
    if at_cost:
        _, _, pvals["h7"] = M.mcnemar_exact([r["flags"]["D2"] for r in at_cost], [r["flags"]["D2x"] for r in at_cost])
        rate("s2.flag.D2.at_cost", at_cost, "D2", "vendored judge on C3/C5 talk at cost")
        rate("s2.flag.D2x.at_cost", at_cost, "D2x", "extraction judge on C3/C5 talk at cost")
    channel = [r for r in rows if r["ext_qwen"] is not None and r["ext_llama"] is not None]
    if channel:
        a, b = [r["flags"]["D2x"] for r in channel], [r["flags"]["D2xL"] for r in channel]
        _, _, pvals["h8"] = M.mcnemar_exact(a, b)
        add("s2.judge_family.kappa", round(cohen_kappa(a, b), 4), n=len(channel))
        add("s2.judge_family.agree", round(sum(x == y for x, y in zip(a, b)) / len(a), 4), n=len(channel))
    dep = lambda cond: [r["dep"] for r in by((cond,)) if r["dep"] is not None]  # noqa: E731
    if dep("C1") and dep("C2"):
        pvals["h9"] = perm_test(dep("C2"), dep("C1"), seed=0)
        for cond in ("C1", "C2", "C8"):
            if dep(cond):
                m, lo, hi = mean_ci(dep(cond), seed=0)
                add("s2.dep.mean.%s" % cond, round(m, 4), ci=(round(lo, 4), round(hi, 4)), n=len(dep(cond)))
        a = M.auroc(dep("C1"), dep("C2"))
        if a is not None:
            add("s2.auroc.D3.C2", round(a, 4))
    names = sorted(pvals)
    for name, raw, adj in zip(names, [pvals[n] for n in names], holm([pvals[n] for n in names]) if names else []):
        add("s2.%s.p" % name, round(raw, 4))
        add("s2.%s.p_holm" % name, round(adj, 4))

    # secondary: the extraction judges on Study 1's channel markets (already read, so secondary)
    s1 = [(rid, j) for (src, rid), j in rejudged.items() if src == "study1"]
    for cond in ("C1", "C3", "C5", "C6"):
        sub = [judge_flag(j.get("ext_qwen")) for rid, j in s1 if rid.startswith(cond + "-")]
        sub = [bool(x) for x in sub if x is not None]
        if sub:
            p, lo, hi = wilson_ci(sum(sub), len(sub))
            add("s2.study1.D2x.%s" % cond, round(p, 4), ci=(round(lo, 4), round(hi, 4)), n=len(sub),
                text="extraction judge flag rate on Study 1 %s (secondary)" % cond)

    # data quality
    add("s2.parse_failures", sum(int(r["parse_failures"] or 0) for r in rows))
    misses = sum(1 for j in rejudged.values() for verdicts in j.values() for v in verdicts if v.get("score") is None)
    add("s2.rejudge_misses", misses)

    (M.PROJECT / "results" / "study2.json").write_text(json.dumps(
        {"frozen": frozen, "markets": rows, "splice": splice,
         "missing": sorted([list(k) for k in expected - set(markets)]),
         "pvalues": {k: round(v, 4) for k, v in pvals.items()}}, indent=2) + "\n")
    write_claims(M.PROJECT / "results" / "claims.partial" / "study2.json", claims)
    print("study2: %d markets, %d known (%d positive), %d claims" % (len(markets), len(known), len(positives), len(claims)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
