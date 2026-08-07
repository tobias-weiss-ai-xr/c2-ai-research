#!/usr/bin/env python3
"""Validate papers.yaml structure, taxonomy values and URL/date formats.

Usage:
    python3 scripts/validate_papers.py
    python3 scripts/validate_papers.py --strict
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent

CATEGORIES = {
    "autonomous-decision-making", "deep-reinforcement-learning",
    "multi-agent-rl", "opponent-modeling", "hierarchical-planning",
    "military-simulation", "wargaming", "command-and-control",
    "decision-support", "mathematical-optimization",
    "probabilistic-uncertainty", "mission-planning",
    "human-ai-teaming", "sim-to-real",
}

SUBCATEGORIES = {
    "theory", "mechanism", "method", "application",
    "development", "systems", "evaluation", "review",
}

ARXIV_RE = re.compile(r"https?://arxiv\.org/abs/(\d{4}\.\d{4,5})")
DATE_RE = re.compile(r"^\d{4}-\d{2}$")


def main():
    parser = argparse.ArgumentParser(description="Validate papers.yaml")
    parser.add_argument("--strict", action="store_true", help="Fail on any issue")
    args = parser.parse_args()

    path = BASE / "papers.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    papers = data.get("papers", [])

    errors, warnings = [], []
    for i, p in enumerate(papers):
        label = f"paper[{i}]"
        if not isinstance(p, dict):
            errors.append(f"{label}: not a mapping")
            continue
        title = p.get("title", "<untitled>")
        for field in ("title", "date", "url", "category", "subcategory"):
            if not p.get(field):
                errors.append(f"{label} '{title}': missing '{field}'")
        if p.get("category") not in CATEGORIES:
            errors.append(f"{label} '{title}': bad category {p.get('category')!r}")
        if p.get("subcategory") not in SUBCATEGORIES:
            errors.append(f"{label} '{title}': bad subcategory {p.get('subcategory')!r}")
        if not DATE_RE.match(p.get("date", "")):
            errors.append(f"{label} '{title}': bad date {p.get('date')!r}")
        url = p.get("url", "")
        if not ARXIV_RE.match(url):
            warnings.append(f"{label} '{title}': url is not an arXiv abs link: {url!r}")

    seen = {}
    for p in papers:
        t = p.get("title", "").strip().lower()
        if t in seen:
            warnings.append(f"duplicate title: {t!r} (papers {seen[t]} and current)")
        seen[t] = papers.index(p)

    print(f"Checked {len(papers)} papers: {len(errors)} error(s), {len(warnings)} warning(s)")
    for e in errors:
        print("  ERROR  " + e)
    for w in warnings:
        print("  WARN   " + w)

    rc = 1 if errors else (0 if not (args.strict and warnings) else 1)
    sys.exit(rc)


if __name__ == "__main__":
    main()