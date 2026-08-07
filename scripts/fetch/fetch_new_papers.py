#!/usr/bin/env python3
"""Discover C2-AI / autonomous decision-making papers from the arXiv API
across all 14 taxonomy categories.

Runs a per-category arXiv query list (deep RL, multi-agent RL, opponent
modeling, hierarchical planning, military simulation, wargaming, C2, decision
support, optimization, uncertainty, mission planning, human-AI teaming, sim-to-
real). Each query carries a category (and keyword-derived subcategory) so new
papers are auto-classified into the 14x8 taxonomy on discovery.

Adopted & adapted from graph-research / agent-*-research corpus tooling.

Usage:
    python3 scripts/fetch/fetch_new_papers.py --months 3 --dry-run
    python3 scripts/fetch/fetch_new_papers.py --months 12 --max-results 50
"""

import argparse
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import domain  # noqa: E402

ARXIV_ID_PATTERN = re.compile(r"(\d{4}\.\d{4,5})")
ARXIV_SEARCH_API = (
    "https://export.arxiv.org/api/query?search_query={}&start={}&max_results={}"
)

# (query, category, subcategory-hint). Subcategory is refined by keyword scoring
# on title/abstract; the hint is used as a fallback when nothing matches.
QUERIES = [
    # --- deep-reinforcement-learning ---
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"deep reinforcement learning"', "deep-reinforcement-learning", "method"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"reinforcement learning" AND abs:"policy gradient"', "deep-reinforcement-learning", "method"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"proximal policy optimization"', "deep-reinforcement-learning", "method"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"Q-learning" AND abs:"deep"', "deep-reinforcement-learning", "method"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"distributional reinforcement learning"', "deep-reinforcement-learning", "theory"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"model-based reinforcement learning"', "deep-reinforcement-learning", "method"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"reinforcement learning" AND abs:"off-policy"', "deep-reinforcement-learning", "evaluation"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"reinforcement learning" AND abs:"survey"', "deep-reinforcement-learning", "review"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"reward" AND abs:"intrinsic" AND abs:"reinforcement"', "deep-reinforcement-learning", "mechanism"),
    # --- autonomous-decision-making ---
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"autonomous decision"', "autonomous-decision-making", "application"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"autonomous" AND abs:"decision-making"', "autonomous-decision-making", "application"),
    ('(cat:cs.AI OR cat:cs.LG) AND abs:"decision making" AND abs:"learning"', "autonomous-decision-making", "method"),
    ('(cat:cs.AI OR cat:cs.LG) AND abs:"sequential decision making"', "autonomous-decision-making", "theory"),
    ('(cat:cs.AI OR cat:cs.LG) AND abs:"planning" AND abs:"Monte Carlo tree search"', "autonomous-decision-making", "method"),
    ('(cat:cs.LG) AND abs:"decision transformer"', "autonomous-decision-making", "method"),
    # --- multi-agent-rl ---
    ('cat:cs.MA AND abs:"multi-agent reinforcement learning"', "multi-agent-rl", "method"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"multi-agent" AND abs:"reinforcement learning"', "multi-agent-rl", "method"),
    ('(cat:cs.LG OR cat:cs.MA) AND abs:"multi-agent deep reinforcement learning"', "multi-agent-rl", "method"),
    ('cat:cs.MA AND abs:"cooperative" AND abs:"reinforcement learning"', "multi-agent-rl", "method"),
    ('(cat:cs.LG OR cat:cs.MA) AND abs:"decentralized" AND abs:"reinforcement learning"', "multi-agent-rl", "method"),
    ('cat:cs.MA AND abs:"communication" AND abs:"multi-agent"', "multi-agent-rl", "mechanism"),
    ('(cat:cs.MA OR cat:cs.LG) AND abs:"multi-agent" AND abs:"reinforcement learning" AND abs:"survey"', "multi-agent-rl", "review"),
    # --- opponent-modeling ---
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"opponent modeling"', "opponent-modeling", "method"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"opponent modelling"', "opponent-modeling", "method"),
    ('(cat:cs.GT OR cat:cs.LG) AND abs:"game theory" AND abs:"reinforcement learning"', "opponent-modeling", "theory"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"counterfactual regret minimization"', "opponent-modeling", "method"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"adversarial" AND abs:"reinforcement learning"', "opponent-modeling", "method"),
    ('(cat:cs.GT) AND abs:"bounded rationality" AND abs:"game"', "opponent-modeling", "theory"),
    # --- hierarchical-planning ---
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"hierarchical reinforcement learning"', "hierarchical-planning", "method"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"option" AND abs:"reinforcement learning"', "hierarchical-planning", "method"),
    ('(cat:cs.AI) AND abs:"hierarchical task network"', "hierarchical-planning", "method"),
    ('(cat:cs.AI) AND abs:"abductive planning"', "hierarchical-planning", "method"),
    ('(cat:cs.AI OR cat:cs.RO) AND abs:"task planning" AND abs:"reinforcement learning"', "hierarchical-planning", "application"),
    ('(cat:cs.AI) AND abs:"automated planning" AND abs:"learning"', "hierarchical-planning", "method"),
    # --- military-simulation ---
    ('(cat:cs.MA OR cat:cs.AI) AND abs:"military simulation"', "military-simulation", "evaluation"),
    ('(cat:cs.AI OR cat:cs.LG) AND abs:"military" AND abs:"reinforcement learning"', "military-simulation", "application"),
    ('(cat:cs.AI OR cat:cs.LG) AND abs:"simulation" AND abs:"reinforcement learning" AND abs:"training"', "military-simulation", "systems"),
    ('(cat:cs.AI OR cat:cs.LG) AND abs:"constructive simulation" AND abs:"agent"', "military-simulation", "development"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"combat" AND abs:"reinforcement learning"', "military-simulation", "application"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"game engine" AND abs:"reinforcement learning"', "military-simulation", "systems"),
    # --- wargaming ---
    ('cat:cs.AI AND abs:"wargaming"', "wargaming", "method"),
    ('cat:cs.AI AND abs:"wargame"', "wargaming", "application"),
    ('(cat:cs.AI OR cat:cs.LG) AND abs:"wargaming" AND abs:"reinforcement learning"', "wargaming", "application"),
    ('cat:cs.AI AND abs:"red versus blue"', "wargaming", "application"),
    # --- command-and-control ---
    ('(cat:cs.AI OR cat:cs.HC) AND abs:"command and control"', "command-and-control", "application"),
    ('(cat:cs.AI OR cat:cs.HC) AND abs:"situation awareness" AND abs:"autonomous"', "command-and-control", "mechanism"),
    ('(cat:cs.AI OR cat:cs.HC) AND abs:"command and control" AND abs:"artificial intelligence"', "command-and-control", "application"),
    ('cat:cs.HC AND abs:"human-in-the-loop" AND abs:"decision"', "command-and-control", "systems"),
    # --- decision-support ---
    ('(cat:cs.AI OR cat:cs.LG) AND abs:"decision support"', "decision-support", "application"),
    ('(cat:cs.AI OR cat:cs.LG) AND abs:"decision support" AND abs:"reinforcement learning"', "decision-support", "application"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"recommendation" AND abs:"reinforcement learning"', "decision-support", "application"),
    ('(cat:cs.HC OR cat:cs.AI) AND abs:"interpretable" AND abs:"decision"', "decision-support", "mechanism"),
    # --- mathematical-optimization ---
    ('(cat:math.OC OR cat:cs.LG) AND abs:"constrained" AND abs:"reinforcement learning"', "mathematical-optimization", "theory"),
    ('(cat:math.OC OR cat:cs.LG) AND abs:"combinatorial optimization" AND abs:"learning"', "mathematical-optimization", "method"),
    ('(cat:math.OC OR cat:cs.LG) AND abs:"mixed-integer" AND abs:"reinforcement learning"', "mathematical-optimization", "method"),
    ('(cat:math.OC OR cat:cs.LG) AND abs:"convex optimization" AND abs:"decision"', "mathematical-optimization", "theory"),
    ('(cat:math.OC) AND abs:"assignment problem" AND abs:"learning"', "mathematical-optimization", "method"),
    # --- probabilistic-uncertainty ---
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"bayesian" AND abs:"reinforcement learning"', "probabilistic-uncertainty", "theory"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"partial observable" AND abs:"reinforcement learning"', "probabilistic-uncertainty", "theory"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"POMDP"', "probabilistic-uncertainty", "theory"),
    ('(cat:cs.LG OR cat:stat.ML) AND abs:"uncertainty quantification" AND abs:"decision"', "probabilistic-uncertainty", "method"),
    ('(cat:cs.AI OR cat:cs.LG) AND abs:"belief state" AND abs:"planning"', "probabilistic-uncertainty", "method"),
    # --- mission-planning ---
    ('(cat:cs.RO OR cat:cs.LG) AND abs:"mission planning"', "mission-planning", "application"),
    ('(cat:cs.RO OR cat:cs.AI) AND abs:"task allocation" AND abs:"autonomous"', "mission-planning", "method"),
    ('(cat:cs.RO OR cat:cs.LG) AND abs:"path planning" AND abs:"reinforcement learning"', "mission-planning", "application"),
    ('(cat:cs.RO OR cat:cs.LG) AND abs:"trajectory planning" AND abs:"learning"', "mission-planning", "application"),
    ('(cat:cs.RO OR cat:cs.LG) AND abs:"coverage planning" AND abs:"UAV"', "mission-planning", "application"),
    # --- human-ai-teaming ---
    ('(cat:cs.LG OR cat:cs.HC) AND abs:"human-AI teaming"', "human-ai-teaming", "mechanism"),
    ('(cat:cs.LG OR cat:cs.HC) AND abs:"human-ai" AND abs:"reinforcement learning"', "human-ai-teaming", "mechanism"),
    ('(cat:cs.LG OR cat:cs.AI) AND abs:"explainable reinforcement learning"', "human-ai-teaming", "mechanism"),
    ('cat:cs.HC AND abs:"robot teaming" AND abs:"autonomous"', "human-ai-teaming", "application"),
    ('(cat:cs.AI OR cat:cs.HC) AND abs:"trust" AND abs:"autonomous agent"', "human-ai-teaming", "mechanism"),
    # --- sim-to-real ---
    ('(cat:cs.LG OR cat:cs.RO) AND abs:"sim-to-real"', "sim-to-real", "method"),
    ('(cat:cs.LG OR cat:cs.RO) AND abs:"domain randomization"', "sim-to-real", "method"),
    ('(cat:cs.LG OR cat:cs.RO) AND abs:"simulation-to-real"', "sim-to-real", "method"),
    ('(cat:cs.LG OR cat:cs.RO) AND abs:"sim-to-real" AND abs:"reinforcement learning"', "sim-to-real", "evaluation"),
    ('(cat:cs.LG OR cat:cs.RO) AND abs:"sim-to-sim"', "sim-to-real", "evaluation"),
]

# Subcategory keyword rules, applied in order. First match wins.
# Each rule: (subcategory, keywords, title_only?) — title_only restricts
# matching to the paper title (for strong signals like "survey").
SUBCATEGORY_RULES = [
    ("review", ["survey", "systematic review", "state-of-the-art", "sota", "overview of"], True),
    ("review", ["a survey of", "review of", "bibliographic review", "overview"], False),
    ("theory", ["expressivity", "expressiveness", "theory", "theoretical", "complexity", "bounds",
                "fundamental limits", "axiomat", "computational complexity", "approximation guarantees",
                "convergence guarantee", "sample complexity"], False),
    ("application", ["application to", "application of", "case study", "real-world", "in practice",
                     "production", "military", "combat", "mission", "deployment", "wargame"], False),
    ("development", ["open-source", "library", "toolkit", "implementation of", "software package",
                     "benchmarking tool", "api for", "python library", "framework"], False),
    ("mechanism", ["interpretab", "explainab", "understanding why", "analysis of", "inner workings",
                   "attention analysis", "probing", "mechanism", "why", "trust"], False),
    ("systems", ["system", "engine", "platform", "infrastructure", "architecture", "pipeline",
                 "distributed", "scalable", "storage", "simulator", "engine", "environment"], False),
    ("evaluation", ["benchmark", "empirical study", "empirical comparison", "experimental evaluation",
                    "evaluating", "comparative", "dataset", "assessment"], False),
]

SUBCATEGORY_FALLBACK = "method"


def classify_subcategory(title, abstract):
    """Assign a subcategory using keyword rules against title + abstract."""
    t_lower = title.lower()
    text = f"{title} {abstract}".lower()
    for subcat, keywords, title_only in SUBCATEGORY_RULES:
        haystack = t_lower if title_only else text
        for kw in keywords:
            if kw in haystack:
                return subcat
    return SUBCATEGORY_FALLBACK


def load_existing_papers(yaml_path):
    if not yaml_path.exists():
        return {}, []
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f) or {}
    papers = data.get("papers", [])
    by_id = {}
    titles_lower = []
    for p in papers:
        url = p.get("url", "")
        match = ARXIV_ID_PATTERN.search(url)
        if match:
            by_id[match.group(1)] = p
        titles_lower.append(p.get("title", "").lower().strip())
    return by_id, titles_lower


def search_arxiv(query, months, start=0, max_results=100, max_retries=4):
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    cutoff = now - timedelta(days=months * 30)
    date_start = cutoff.strftime("%Y%m%d0000")
    date_end = now.strftime("%Y%m%d") + "2359"

    full_query = f"({query}) AND submittedDate:[{date_start} TO {date_end}]"
    try:
        resp = None
        for attempt in range(max_retries):
            resp = requests.get(
                ARXIV_SEARCH_API.format(
                    requests.utils.quote(full_query), start, max_results
                ),
                timeout=30,
            )
            if resp.status_code == 429:
                wait = 8 * (attempt + 1)
                print(f"    rate-limited (429), waiting {wait}s...", flush=True)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            break
        if resp is None:
            return []
        if resp.status_code != 200:
            print(f"  WARNING: arXiv returned HTTP {resp.status_code}", flush=True)
            return []
        entries = []
        for match in re.finditer(r"<entry>(.*?)</entry>", resp.text, re.DOTALL):
            entry_xml = match.group(1)
            entry = {}
            title_m = re.search(r"<title>(.*?)</title>", entry_xml, re.DOTALL)
            if title_m:
                entry["title"] = re.sub(r"\s+", " ", title_m.group(1).strip())
            id_m = re.search(r"<id>(.*?)</id>", entry_xml)
            if id_m:
                entry["url"] = id_m.group(1).strip().replace("http://", "https://")
            published_m = re.search(r"<published>(.*?)</published>", entry_xml)
            if published_m:
                entry["date"] = published_m.group(1).strip()[:7]
            summary_m = re.search(r"<summary>(.*?)</summary>", entry_xml, re.DOTALL)
            if summary_m:
                entry["abstract"] = re.sub(r"\s+", " ", summary_m.group(1).strip())
            authors_m = re.findall(r"<name>(.*?)</name>", entry_xml)
            if authors_m:
                entry["authors"] = [a.strip() for a in authors_m][:3]
            if entry.get("title") and entry.get("url"):
                entries.append(entry)
        return entries
    except Exception as e:
        print(f"  WARNING: arXiv search error: {e}", flush=True)
        return []


def format_yaml_entry(entry, category, subcategory):
    title = entry["title"].replace('"', '\\"')
    authors = ", ".join(entry.get("authors", [])[:3])
    lines = [
        f'  - title: "{title}"',
        f'    date: "{entry.get("date", "")}"',
        f'    url: "{entry.get("url", "")}"',
        f"    category: {category}",
        f"    subcategory: {subcategory}",
        f"    authors: [{authors}]",
    ]
    if entry.get("abstract"):
        abstract = entry["abstract"][:200].replace('"', '\\"')
        lines.append(f'    abstract: "{abstract}..."')
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Discover C2-AI/RL papers from arXiv across all categories"
    )
    parser.add_argument("--months", type=int, default=3)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--create-pr", action="store_true")
    parser.add_argument("--sleep", type=float, default=2.0)
    parser.add_argument("--max-results", type=int, default=100)
    parser.add_argument("--from", dest="from_idx", type=int, default=0)
    parser.add_argument("--to", dest="to_idx", type=int, default=None)
    args = parser.parse_args()

    yaml_path = Path(__file__).resolve().parent.parent.parent / "papers.yaml"
    by_id, titles_lower = load_existing_papers(yaml_path)

    print(f"Loaded {len(by_id)} existing papers from papers.yaml", flush=True)
    print(f"Searching arXiv ({len(QUERIES)} queries) for the last {args.months} month(s)...", flush=True)

    all_new = []
    CHECKPOINT_EVERY = 10
    to_idx = args.to_idx if args.to_idx is not None else len(QUERIES) - 1
    for qi, qdef in enumerate(QUERIES[args.from_idx:to_idx + 1], start=args.from_idx):
        if len(qdef) == 4:
            query, category, hint, force_sub = qdef
        else:
            query, category, hint = qdef
            force_sub = None
        print(f"Query {qi + 1}/{len(QUERIES)} [{category}] {query[:70]}", flush=True)
        entries = search_arxiv(query, args.months, max_results=args.max_results)
        for entry in entries:
            arxiv_id_match = ARXIV_ID_PATTERN.search(entry.get("url", ""))
            arxiv_id = arxiv_id_match.group(1) if arxiv_id_match else None
            if arxiv_id and arxiv_id in by_id:
                continue
            title_lower = entry.get("title", "").lower().strip()
            if any(title_lower == t for t in titles_lower):
                continue
            if arxiv_id and any(e.get("url", "") == entry["url"] for e in all_new):
                continue
            entry["category"] = category
            entry["subcategory"] = force_sub or classify_subcategory(
                entry.get("title", ""), entry.get("abstract", "")
            )
            all_new.append(entry)
            by_id[arxiv_id] = entry
            titles_lower.append(title_lower)

        if not args.dry_run and all_new and (qi + 1) % CHECKPOINT_EVERY == 0:
            append_papers(yaml_path, all_new)
            print(f"  [checkpoint] saved {len(all_new)} papers so far", flush=True)
            all_new = []
            by_id, titles_lower = load_existing_papers(yaml_path)
        time.sleep(args.sleep)

    print(f"\nFound {len(all_new)} new papers (<{len(by_id)} already present)", flush=True)
    if not all_new:
        print("No new papers to add.", flush=True)
        return

    print("\n--- New Papers (first 10) ---", flush=True)
    for entry in all_new[:10]:
        print(format_yaml_entry(entry, entry["category"], entry["subcategory"]), flush=True)
        print(flush=True)
    print(f"... and {max(0, len(all_new) - 10)} more", flush=True)

    if args.dry_run:
        print("\nDry run complete — no files modified", flush=True)
        return

    if args.create_pr:
        branch_name = f"add-new-papers-{datetime.now().strftime('%Y%m%d')}"
        try:
            subprocess.run(["git", "checkout", "-b", branch_name], check=True, cwd=yaml_path.parent)
            append_papers(yaml_path, all_new)
            subprocess.run(["git", "add", "papers.yaml"], check=True, cwd=yaml_path.parent)
            subprocess.run(["git", "commit", "-m", f"Add {len(all_new)} new papers from arXiv discovery"], check=True, cwd=yaml_path.parent)
            subprocess.run(["git", "push", "origin", branch_name], check=True, cwd=yaml_path.parent)
            subprocess.run(["gh", "pr", "create", "--title", f"Add {len(all_new)} new papers from arXiv discovery",
                            "--body", "Automatically discovered papers.\n\n**Please review taxonomy assignments.**"],
                           check=True, cwd=yaml_path.parent)
            print("PR created successfully!", flush=True)
        except subprocess.CalledProcessError as e:
            print(f"ERROR: Failed to create PR: {e}", flush=True)
            sys.exit(1)
    else:
        append_papers(yaml_path, all_new)
        print(f"\nAppended {len(all_new)} papers to papers.yaml", flush=True)


def append_papers(yaml_path, new_papers):
    if yaml_path.exists():
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f) or {}
    else:
        data = {}
    papers = data.get("papers", [])
    for entry in new_papers:
        papers.append({
            "title": entry.get("title", ""),
            "date": entry.get("date", ""),
            "url": entry.get("url", ""),
            "category": entry.get("category", ""),
            "subcategory": entry.get("subcategory", ""),
            "authors": entry.get("authors", []),
            "abstract": entry.get("abstract", ""),
        })
    data["papers"] = papers
    with open(yaml_path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


if __name__ == "__main__":
    main()