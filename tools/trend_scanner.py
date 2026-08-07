#!/usr/bin/env python3
"""Scan the corpus for emerging keywords (burden detection across years).

Chooses the most recent window size and reports terms whose usage increased
relative to the corpus average, limited to an allowed vocabulary set.

Usage:
    tools/trend_scanner.py --months 12
"""

import argparse
import collections
import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import domain  # noqa: E402

VOCAB = [
    "reinforcement", "policy", "value", "reward", "multi-agent", "actor",
    "critic", "planning", "hierarchical", "opponent", "adversarial", "wargame",
    "simulation", "decision", "optimization", "constraint", "sim2real", "transfer",
    "game-theory", "security", "command", "control", "mission", "team",
    "uncertainty", "probabilistic", "explanation", "trust",
]

STOP = {"the", "and", "for", "with", "from", "that", "this", "which", "are"}


def tokenize(text):
    return re.findall(r"[a-z][a-z0-9-]{2,}", text.lower())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--months", type=int, default=12)
    args = parser.parse_args()

    papers = yaml.safe_load((BASE / "papers.yaml").read_text(encoding="utf-8"))["papers"]
    dates = sorted({p["date"] for p in papers})
    if not dates:
        sys.exit("no papers")
    latest = dates[-1]
    last_year = int(latest[:4]) - 1
    recent = [p for p in papers if p["date"][:4] >= str(last_year)]
    baseline = [p for p in papers if p["date"][:4] < str(last_year)]

    def count(ps):
        c = collections.Counter()
        for p in ps:
            for w in tokenize(p["abstract"]):
                if w not in STOP:
                    c[w] += 1
        return c

    cr = count(recent)
    cb = count(baseline)
    bursts = []
    for w in VOCAB:
        r = cr.get(w, 0)
        b = cb.get(w, 0)
        if r + b == 0:
            continue
        share = r / (r + b)
        bursts.append((w, r, b, round(share, 2)))

    bursts.sort(key=lambda x: -x[3])
    print(f"Emergent signals (last {args.months} vs baseline), from {len(papers)} papers:\n")
    for w, r, b, share in bursts[:15]:
        print(f"  {w:<22} recent={r:<2} base={b:<2} recent-share={share}")

    if not bursts:
        print("  none detected — corpus too small; add more papers.")


if __name__ == "__main__":
    main()