"""Figures for the paper, from results/detectors.json and runs/. Re-runs itself under
`uv run --with matplotlib` when matplotlib is not installed. Writes figures/fig*.png and
figures/captions.json. Run after analysis/detect.py (make analyze skips this file)."""
import json
import os
import pathlib
import shutil
import subprocess
import sys

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    if os.environ.get("FIGURES_REEXEC") or not shutil.which("uv"):
        print("figures: SKIP (matplotlib not available and uv not found)")
        sys.exit(0)
    env = dict(os.environ, FIGURES_REEXEC="1")
    sys.exit(subprocess.call(["uv", "run", "-q", "--with", "matplotlib", "python", __file__], env=env))

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import markets as M  # noqa: E402

FIG = M.PROJECT / "figures"
LABEL = {"C1": "C1 planted", "C2": "C2 Qwen×3\nno channel", "C3": "C3 Qwen×3\nchannel",
         "C4": "C4 mixed\nno channel", "C5": "C5 mixed\nchannel", "C6": "C6 monitored\nchannel",
         "C7": "C7 Llama×3\nno channel"}
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
                     "savefig.dpi": 200, "savefig.bbox": "tight"})


def wilson(k, n, z=1.96):
    if n == 0:
        return 0, 0, 0
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return p, c - h, c + h


def main():
    det = json.loads((M.PROJECT / "results" / "detectors.json").read_text())
    cfg = M.config()
    conds = [c["id"] for c in cfg["conditions"]]
    rows = det["markets"]
    FIG.mkdir(exist_ok=True)
    captions = {}

    # Figure 1: collusion index (D1 score) per market
    fig, ax = plt.subplots(figsize=(6.4, 2.8))
    for i, c in enumerate(conds):
        for r in rows:
            if r["condition"] == c and r["scores"]["D1"] is not None:
                ax.scatter(i + (0.12 if r["split"] == "heldout" else -0.12), r["scores"]["D1"], s=14,
                           marker="o" if r["split"] == "heldout" else "x",
                           color="#c0392b" if c == "C1" else ("#7f8c8d" if c in ("C2", "C4", "C7") else "#2c3e50"))
    t1 = det["thresholds"]["D1"]["threshold"]
    if t1 is not None:
        ax.axhline(t1, ls="--", lw=0.8, color="#555")
        ax.text(len(conds) - 0.5, t1, " D1 cut", va="center", fontsize=7)
    ax.set_xticks(range(len(conds)), [LABEL[c] for c in conds], fontsize=7)
    ax.set_ylabel("collusion index\n(0 = cost, 1 = buyer value)")
    ax.set_ylim(-0.03, 1.03)
    fig.savefig(FIG / "fig1.png")
    plt.close(fig)
    captions["fig1.png"] = ("Figure 1: Collusion index of every market (x: calibration seeds 0-3, o: held-out "
                            "seeds 4-7). Grey conditions have no message channel, so any agreement is impossible. "
                            "The dashed line is the D1 threshold frozen on calibration seeds.")

    # Figure 2: held-out flag rates per detector
    groups = [("C1 (planted)", lambda r: r["condition"] == "C1" and r["split"] == "heldout", rows),
              ("No-channel decoys", lambda r: r["condition"] in ("C2", "C4", "C7") and r["split"] == "heldout", rows),
              ("Talk without action", lambda s: s["split"] == "heldout", det["splice"])]
    dets = ["D1", "D2", "D3", "D4", "X1"]
    names = {"D1": "D1 price level", "D2": "D2 message judge", "D3": "D3 action dependence",
             "D4": "D4 plus-factor rule", "X1": "D1 and D2 (exploratory)"}
    colors = ["#95a5a6", "#3498db", "#e67e22", "#27ae60", "#ffffff"]
    fig, ax = plt.subplots(figsize=(6.4, 2.8))
    width = 0.16
    for j, d in enumerate(dets):
        for g, (gname, pick, source) in enumerate(groups):
            sel = [r for r in source if pick(r)]
            k = sum(r["flags"][d] for r in sel)
            p, lo, hi = wilson(k, len(sel))
            x = g + (j - 2) * width
            ax.bar(x, p, width * 0.92, color=colors[j], label=names[d] if g == 0 else None,
                   edgecolor="#333" if d == "X1" else colors[j], hatch="///" if d == "X1" else None, lw=0.6)
            ax.errorbar(x, p, yerr=[[max(0.0, p - lo)], [max(0.0, hi - p)]], color="#333", lw=0.7, capsize=1.5)
    sizes = [len([r for r in source if pick(r)]) for _, pick, source in groups]
    ax.set_xticks(range(len(groups)), ["%s\n(n = %d)" % (g[0], n) for g, n in zip(groups, sizes)])
    ax.set_ylabel("share of markets flagged")
    ax.set_ylim(0, 1.05)
    ax.legend(fontsize=7, frameon=False, ncol=3, loc="lower center", bbox_to_anchor=(0.5, 1.0))
    fig.savefig(FIG / "fig2.png")
    plt.close(fig)
    captions["fig2.png"] = ("Figure 2: Share of held-out markets each detector flags, with Wilson 95% intervals. "
                            "On C1 a flag is correct; on the no-channel decoys and on talk-without-action "
                            "markets (C3 messages spliced onto C2 actions) a flag is a false alarm. D3 flags no market because no "
                            "calibration threshold beat flagging nothing. The hatched bar is an exploratory rule added after "
                            "the results were read.")

    # Figure 3: the most parallel held-out no-channel market next to a held-out planted market
    decoys = [r for r in rows if r["condition"] in ("C2", "C4", "C7") and r["split"] == "heldout" and r["scores"]["D3"] is not None]
    planted = [r for r in rows if r["condition"] == "C1" and r["split"] == "heldout"]
    if decoys and planted:
        worst = max(decoys, key=lambda r: r["scores"]["D3"])
        example = sorted(planted, key=lambda r: r["seed"])[0]
        fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.4), sharey=True)
        for ax, r, title in ((axes[0], worst, "%s seed %d: no channel" % (worst["condition"], worst["seed"])),
                             (axes[1], example, "C1 seed %d: planted agreement" % example["seed"])):
            m = M.load_markets([r["condition"]])[(r["condition"], r["seed"])]
            for i, (sid, series) in enumerate(M.ask_series(m).items(), 1):
                ax.plot(range(1, len(series) + 1), series, lw=1.1, label="S%d %s" % (i, m["seller_models"][sid]))
            ax.legend(fontsize=6, frameon=False)
            ax.axhline(80, color="#999", lw=0.6, ls=":")
            ax.axhline(100, color="#999", lw=0.6, ls=":")
            ax.set_title("%s (D3 = %.2f)" % (title, r["scores"]["D3"] or 0), fontsize=8)
            ax.set_xlabel("hour")
        axes[0].set_ylabel("seller ask ($)")
        fig.savefig(FIG / "fig3.png")
        plt.close(fig)
        captions["fig3.png"] = ("Figure 3: Seller asks per hour. Left: the held-out no-channel market with the highest "
                                "action dependence, chosen by that rule rather than by eye. Right: the first held-out "
                                "planted-agreement market. Dotted lines mark seller cost ($80) and buyer value ($100).")
    (FIG / "captions.json").write_text(json.dumps(captions, indent=2) + "\n")
    print("figures: %d written" % len(captions))
    return 0


if __name__ == "__main__":
    sys.exit(main())
