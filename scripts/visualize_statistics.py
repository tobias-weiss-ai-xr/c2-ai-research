#!/usr/bin/env python3
"""Generate bar-chart visualizations from statistics.json.

Usage:
    python3 scripts/visualize_statistics.py          # write PNG charts
    python3 scripts/visualize_statistics.py --png    # (default)
"""

import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "assets" / "visualizations"
sys.path.insert(0, str(BASE / "scripts"))

import domain  # noqa: E402


def plot_ascii(title, items):
    """Fallback ASCII bar chart (also used when matplotlib is missing)."""
    max_v = max((v for _, v in items), default=1)
    scale = 40 / max_v if max_v else 1
    lines = [title]
    for label, v in items:
        bar = "█" * int(v * scale)
        lines.append(f"  {label:<34} {bar} {v}")
    return "\n".join(lines)


def main():
    stats = json.loads((BASE / "statistics.json").read_text(encoding="utf-8"))
    by_cat = stats["by_category"]

    items = [
        (domain.CATEGORY_DISPLAY.get(k, k), v)
        for k, v in sorted(by_cat.items(), key=lambda x: -x[1])
    ]

    could_plot = False
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        could_plot = True
    except Exception:
        could_plot = False

    if could_plot:
        fig, ax = plt.subplots(figsize=(9, 4.5))
        labels = [l for l, _ in items]
        vals = [v for _, v in items]
        ax.bar(labels, vals, color="#4C6EF5")
        ax.set_title("C2-AI Research Corpus — Papers per Category")
        ax.set_ylabel("Papers")
        ax.tick_params(axis="x", rotation=30)
        ax.grid(axis="y", alpha=0.3)
        fig.tight_layout()
        OUT.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUT / "category_distribution.png", dpi=140)
        print(f" wrote {OUT / 'category_distribution.png'}")
    else:
        print(plot_ascii("Papers per category:", items))


if __name__ == "__main__":
    main()