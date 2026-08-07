#!/usr/bin/env python3
"""Compute statistics.json and rewrite papers.json from papers.yaml.

Produces machine-readable statistics used by generate_readme.py and the
reporting tools.

Usage:
    python3 scripts/analysis/generate_analysis.py
"""

import collections
import json
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import domain  # noqa: E402


def main():
    papers = yaml.safe_load((BASE / "papers.yaml").read_text(encoding="utf-8"))["papers"]

    by_cat = collections.Counter(p["category"] for p in papers)
    by_sub = collections.Counter(p["subcategory"] for p in papers)
    by_year = collections.Counter(p["date"][:4] for p in papers)
    cells = collections.Counter((p["category"], p["subcategory"]) for p in papers)

    years = sorted(by_year)
    time_span = (years[0] + "-" + years[-1]) if years else ""

    # Last-12-months window (relative to the most recent published date).
    latest = sorted({p["date"] for p in papers})[-1] if papers else "0000-00"
    cut = str(int(latest[:4]) - 1)  # include the previous calendar year
    by_cat_12m = collections.Counter(
        p["category"] for p in papers if p["date"][:4] >= cut
    )

    n_cats = len(domain.CATEGORIES)
    n_subs = len(domain.SUBCATEGORIES)
    total_cells = n_cats * n_subs
    filled_cells = len(cells)

    # Saturation per aspect-cell depth for reporting
    depth = {
        "dense": filled_cells,
        "saturation": round(filled_cells / total_cells * 100, 1) if total_cells else 0.0,
    }

    stats = {
        "metadata": {
            "topic": "Autonomous Decision-Making & Deep Reinforcement Learning "
                     "for Military Simulations",
            "total_papers": len(papers),
            "categories": n_cats,
            "aspects": n_subs,
            "taxonomy": {
                "total_cells": total_cells,
                "filled_cells": filled_cells,
                "saturation": depth["saturation"],
            },
        },
        "by_category": dict(by_cat),
        "by_subcategory": dict(by_sub),
        "by_year": dict(by_year),
        "by_category_last_12m": dict(by_cat_12m),
        "cells": [{"category": c, "subcategory": s, "count": n}
                  for (c, s), n in sorted(cells.items())],
    }
    stats["metadata"]["time_span"] = time_span

    (BASE / "statistics.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    # papers.json is rebuilt from papers.yaml to stay in sync.
    (BASE / "papers.json").write_text(
        json.dumps({"papers": papers}, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"stats written: {len(papers)} papers, {filled_cells}/{total_cells} cells "
          f"({depth['saturation']}% saturated)")


if __name__ == "__main__":
    main()