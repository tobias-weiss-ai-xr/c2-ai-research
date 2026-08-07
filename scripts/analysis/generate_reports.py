#!/usr/bin/env python3
"""Generate review & gap-analysis markdown docs from the corpus.

Usage:
    python3 scripts/analysis/generate_reports.py
"""

import collections
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import domain  # noqa: E402

OUT = BASE / "docs" / "research"


def build_literature(papers):
    by_cat = collections.Counter(p["category"] for p in papers)
    lines = ["# Literature Review\n",
             "Evidence synthesis from the curated seed corpus of autonomous "
             "decision-making & deep RL in military simulation environments.\n"]
    for category in sorted(by_cat, key=lambda c: -by_cat[c]):
        lines.append(f"\n## {domain.CATEGORY_DISPLAY.get(category, category)}\n")
        for p in sorted((x for x in papers if x["category"] == category),
                        key=lambda x: x["date"], reverse=True):
            authors = ", ".join(p["authors"])
            lines.append(f"- **{p['title']}** — {p['date']} — "
                         f"[arXiv]({p['url']}) · {authors}")
            abstract = p["abstract"]
            if len(abstract) > 320:
                abstract = abstract[:320].rsplit(" ", 1)[0] + " …"
            lines.append(f"\n  {abstract}\n")
    (OUT / "literature_review.md").write_text("\n".join(lines), encoding="utf-8")


def build_gaps(papers):
    by_cat = collections.Counter(p["category"] for p in papers)
    covered = set(by_cat)
    gaps = [domain.CATEGORY_DISPLAY.get(c, c) for c in domain.CATEGORIES if c not in covered]

    out = ["# Research Gaps\n",
           "Categories and aspects with no curated papers yet — candidate "
           "areas for new investigations or corpus expansion.\n",
           "\n## Uncovered Categories\n"]
    out += [f"- **{g}**" for g in gaps] or ["- (none)"]
    out.append("\n_Auto-generated. No content here should be read as policy or "
               "operational guidance._\n")
    (OUT / "research_gaps.md").write_text("\n".join(out), encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    papers = yaml.safe_load(
        (BASE / "papers.yaml").read_text(encoding="utf-8")
    )["papers"]
    build_literature(papers)
    build_gaps(papers)
    print("wrote docs/research/literature_review.md & docs/research/research_gaps.md")


if __name__ == "__main__":
    main()