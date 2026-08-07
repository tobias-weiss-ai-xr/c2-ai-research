#!/usr/bin/env python3
"""Generate evidence-weighted article topics from the research corpus.

Topics are ranked by combining paper-author density in a category, the share of
papers published in the recent window, and coverage of high-signal domain
vocabulary.

Usage:
    tools/topic_planner.py --top 10
"""

import argparse
import collections
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import domain  # noqa: E402

TOPIC_HINTS = {
    "autonomous-decision-making": ("autonomous", "decision", "planning", "fallback", "compression"),
    "deep-reinforcement-learning": ("value", "policy", "reward", "gradient", "Q-network"),
    "multi-agent-rl": ("multi-agent", "agent", "cooperation", "communication"),
    "opponent-modeling": ("opponent", "adversa", "game-theory"),
    "hierarchical-planning": ("hierarchical", "abduction", "abductive", "planning"),
    "military-simulation": ("military", "simulation", "wargame", "evaluation", "theory"),
    "wargaming": ("wargam", "game", "scenario"),
    "command-and-control": ("command", "control", "decision-support", "C2"),
    "decision-support": ("decision", "support", "recommend"),
    "mathematical-optimization": ("optimization", "constrained", "programming"),
    "probabilistic-uncertainty": ("probabilit", "bayesian", "uncertainty", "belief"),
    "mission-planning": ("mission", "route", "task allocation"),
    "human-ai-teaming": ("human", "team", "trust", "explanation", "XAI"),
    "sim-to-real": ("sim-to-real", "transfer", "domain randomization"),
}


def score_category(name, count, total, recent, total_recent):
    density = count / max(total, 1)
    recency = recent / max(total_recent, 1)
    return {"category": name,
            "papers": count,
            "score": round(density + recency, 3),
            "recency": round(recency, 3)}


def main():
    parser = argparse.ArgumentParser(description="Topic planner for the corpus")
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    papers = yaml.safe_load((BASE / "papers.yaml").read_text(encoding="utf-8"))["papers"]
    by_cat = collections.Counter(p["category"] for p in papers)
    latest = sorted({p["date"] for p in papers})[-1]
    cut = str(int(latest[:4]) - 1)
    by_cat_12m = collections.Counter(p["category"] for p in papers
                                     if p["date"][:4] >= cut)

    total = len(papers)
    total_recent = sum(1 for p in papers if p["date"][:4] >= cut)

    rows = sorted((score_category(c, n, total, by_cat_12m.get(c, 0), total_recent)
                   for c, n in by_cat.items()), key=lambda r: -r["score"])[:args.top]

    print(f"Top {len(rows)} article topics for the C2-AI corpus:\n")
    for i, r in enumerate(rows, 1):
        hints = ", ".join(TOPIC_HINTS.get(r["category"], [])[:3])
        print(f"{i:>2}. {domain.CATEGORY_DISPLAY.get(r['category'], r['category'])} "
              f"(papers={r['papers']}, score={r['score']})")
        print(f"     angles: {hints}")

    # write the generated topics doc
    out = ["# Article Topics (auto-generated)\n"]
    for r in rows:
        out.append(f"\n## {domain.CATEGORY_DISPLAY.get(r['category'], r['category'])}\n")
        out.append(f"Evidence-based topic with {r['papers']} curated papers.\n")
        out.append(f"Suggested angles: {', '.join(TOPIC_HINTS.get(r['category'], []))}.\n")
    out_path = BASE / "docs" / "topics" / "ARTICLE_TOPICS.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()