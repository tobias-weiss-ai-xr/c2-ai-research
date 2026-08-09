#!/usr/bin/env python3
"""Targeted expansion fetch for C2 and Human-AI Teaming categories.

Broader queries, longer time window (--months 60), additional keyword
combinations not in the main fetch_new_papers.py query list.

Usage:
    python3 scripts/fetch/fetch_expand_c2_hai.py --months 60
"""

import argparse
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_new_papers import (  # noqa: E402
    ARXIV_ID_PATTERN,
    classify_subcategory,
    load_existing_papers,
    append_papers,
)

ARXIV_SEARCH_API = (
    "https://export.arxiv.org/api/query?search_query={}&start={}&max_results={}"
)

# Expanded queries for C2 — broader terms, OR combinations, adjacent fields
C2_QUERIES = [
    # Broader C2 terms
    ('(cat:cs.AI OR cat:cs.HC OR cat:cs.CY) AND abs:"command and control"', "command-and-control", "application"),
    ('abs:"C2" AND abs:"decision" AND abs:"system"', "command-and-control", "systems"),
    ('abs:"battle management" AND abs:"aid"', "command-and-control", "systems"),
    ('abs:"operational command" AND abs:"intelligence"', "command-and-control", "application"),
    ('abs:"command" AND abs:"control" AND abs:"autonomy"', "command-and-control", "application"),
    ('abs:"force employment" AND abs:"decision"', "command-and-control", "application"),
    ('abs:"situational awareness" AND abs:"machine learning"', "command-and-control", "mechanism"),
    ('abs:"common operational picture" AND abs:"AI"', "command-and-control", "systems"),
    ('abs:"mission command" AND abs:"artificial intelligence"', "command-and-control", "application"),
    ('abs:"battlefield management"', "command-and-control", "application"),
    ('abs:"human-machine teaming" AND abs:"decision"', "command-and-control", "application"),
    ('abs:"mixed-initiative" AND abs:"control"', "command-and-control", "mechanism"),
    ('abs:"supervisory control" AND abs:"autonomous"', "command-and-control", "systems"),
    ('abs:"shared autonomy" AND abs:"decision"', "command-and-control", "mechanism"),
    ('abs:"joint all-domain command" AND abs:"control"', "command-and-control", "application"),
    ('abs:"multi-domain operations" AND abs:"artificial intelligence"', "command-and-control", "application"),
    ('abs:"OODA" AND abs:"artificial intelligence"', "command-and-control", "theory"),
    # C2 with RL/learning
    ('abs:"command and control" AND abs:"reinforcement learning"', "command-and-control", "method"),
    ('abs:"command and control" AND abs:"machine learning"', "command-and-control", "development"),
    ('abs:"command and control" AND abs:"deep learning"', "command-and-control", "development"),
    ('abs:"command and control" AND abs:"agent"', "command-and-control", "theory"),
    ('abs:"command and control" AND abs:"planning"', "command-and-control", "method"),
    # C2 evaluation/benchmarking
    ('abs:"command and control" AND abs:"benchmark"', "command-and-control", "evaluation"),
    ('abs:"command and control" AND abs:"evaluation"', "command-and-control", "evaluation"),
    ('abs:"command and control" AND abs:"survey"', "command-and-control", "review"),
    ('abs:"command and control" AND abs:"review"', "command-and-control", "review"),
    ('abs:"command and control" AND abs:"framework"', "command-and-control", "development"),
    ('abs:"command and control" AND abs:"architecture"', "command-and-control", "systems"),
    # C2 x cybersecurity
    ('abs:"cyber command" AND abs:"automation"', "command-and-control", "systems"),
    ('abs:"cyber" AND abs:"command and control" AND abs:"AI"', "command-and-control", "systems"),
]

# Expanded queries for Human-AI Teaming
HAI_QUERIES = [
    # Direct human-AI teaming
    ('(cat:cs.HC OR cat:cs.AI OR cat:cs.LG) AND abs:"human-AI teaming"', "human-ai-teaming", "mechanism"),
    ('abs:"human-AI collaboration" AND abs:"autonomous"', "human-ai-teaming", "mechanism"),
    ('abs:"human-machine teaming"', "human-ai-teaming", "mechanism"),
    ('abs:"human-robot teaming" AND abs:"learning"', "human-ai-teaming", "application"),
    ('abs:"human-agent teaming" AND abs:"autonomous"', "human-ai-teaming", "mechanism"),
    ('abs:"human-autonomy teaming"', "human-ai-teaming", "mechanism"),
    ('abs:"ad hoc teamwork" AND abs:"learning"', "human-ai-teaming", "method"),
    ('abs:"adaptive autonomy" AND abs:"human"', "human-ai-teaming", "mechanism"),
    # Trust and explainability
    ('abs:"trust" AND abs:"autonomous system"', "human-ai-teaming", "mechanism"),
    ('abs:"trust calibration" AND abs:"AI"', "human-ai-teaming", "mechanism"),
    ('abs:"trust" AND abs:"machine learning" AND abs:"decision"', "human-ai-teaming", "mechanism"),
    ('abs:"explainable AI" AND abs:"decision"', "human-ai-teaming", "mechanism"),
    ('abs:"XAI" AND abs:"decision support"', "human-ai-teaming", "mechanism"),
    ('abs:"interpretable" AND abs:"autonomous agent"', "human-ai-teaming", "mechanism"),
    ('abs:"transparency" AND abs:"autonomous system"', "human-ai-teaming", "mechanism"),
    # Human-in-the-loop
    ('abs:"human-in-the-loop" AND abs:"learning"', "human-ai-teaming", "mechanism"),
    ('abs:"human-in-the-loop" AND abs:"reinforcement"', "human-ai-teaming", "method"),
    ('abs:"human-on-the-loop" AND abs:"autonomous"', "human-ai-teaming", "mechanism"),
    ('abs:"human-on-the-loop" AND abs:"AI"', "human-ai-teaming", "mechanism"),
    ('abs:"learning from human feedback" AND abs:"decision"', "human-ai-teaming", "method"),
    ('abs:"RLHF" AND abs:"autonomous"', "human-ai-teaming", "method"),
    # Cognitive/affective aspects
    ('abs:"cognitive load" AND abs:"automation"', "human-ai-teaming", "mechanism"),
    ('abs:"cognitive modeling" AND abs:"autonomous"', "human-ai-teaming", "theory"),
    ('abs:"mental model" AND abs:"AI agent"', "human-ai-teaming", "theory"),
    ('abs:"shared mental model" AND abs:"team"', "human-ai-teaming", "theory"),
    ('abs:"situation awareness" AND abs:"AI"', "human-ai-teaming", "mechanism"),
    ('abs:"team cognition" AND abs:"artificial"', "human-ai-teaming", "theory"),
    # Reviews and surveys
    ('abs:"human-AI teaming" AND abs:"survey"', "human-ai-teaming", "review"),
    ('abs:"human-machine collaboration" AND abs:"survey"', "human-ai-teaming", "review"),
    ('abs:"human-autonomy interaction" AND abs:"review"', "human-ai-teaming", "review"),
    ('abs:"trust in AI" AND abs:"survey"', "human-ai-teaming", "review"),
    ('abs:"explainable AI" AND abs:"survey"', "human-ai-teaming", "review"),
    # Application domains
    ('abs:"human-AI teaming" AND abs:"defense"', "human-ai-teaming", "application"),
    ('abs:"human-AI teaming" AND abs:"healthcare"', "human-ai-teaming", "application"),
    ('abs:"human-AI teaming" AND abs:"manufacturing"', "human-ai-teaming", "application"),
    ('abs:"collaborative robot" AND abs:"learning"', "human-ai-teaming", "application"),
    ('abs:"cobot" AND abs:"reinforcement learning"', "human-ai-teaming", "application"),
    # Frameworks/benchmarks
    ('abs:"human-AI teaming" AND abs:"benchmark"', "human-ai-teaming", "evaluation"),
    ('abs:"human-AI teaming" AND abs:"framework"', "human-ai-teaming", "development"),
    ('abs:"human-AI interaction" AND abs:"evaluation"', "human-ai-teaming", "evaluation"),
    ('abs:"human-AI teaming" AND abs:"evaluation"', "human-ai-teaming", "evaluation"),
]


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
                wait = 10 * (attempt + 1)
                print(f"    rate-limited (429), waiting {wait}s...", flush=True)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            break
        if resp is None or resp.status_code != 200:
            return []
        entries = []
        for match in re.finditer(r"<entry>(.*?)</entry>", resp.text, re.DOTALL):
            xml = match.group(1)
            entry = {}
            t = re.search(r"<title>(.*?)</title>", xml, re.DOTALL)
            if t:
                entry["title"] = re.sub(r"\s+", " ", t.group(1).strip())
            i = re.search(r"<id>(.*?)</id>", xml)
            if i:
                entry["url"] = i.group(1).strip().replace("http://", "https://")
            p = re.search(r"<published>(.*?)</published>", xml)
            if p:
                entry["date"] = p.group(1).strip()[:7]
            s = re.search(r"<summary>(.*?)</summary>", xml, re.DOTALL)
            if s:
                entry["abstract"] = re.sub(r"\s+", " ", s.group(1).strip())
            a = re.findall(r"<name>(.*?)</name>", xml)
            if a:
                entry["authors"] = [x.strip() for x in a][:3]
            if entry.get("title") and entry.get("url"):
                entries.append(entry)
        return entries
    except Exception as e:
        print(f"  WARNING: {e}", flush=True)
        return []


def main():
    parser = argparse.ArgumentParser(description="Expand C2 & Human-AI Teaming corpus")
    parser.add_argument("--months", type=int, default=60)
    parser.add_argument("--sleep", type=float, default=3.0)
    parser.add_argument("--max-results", type=int, default=100)
    parser.add_argument("--categories", default="both",
                        choices=["both", "c2", "hai"])
    args = parser.parse_args()

    yaml_path = Path(__file__).resolve().parent.parent.parent / "papers.yaml"
    by_id, titles_lower = load_existing_papers(yaml_path)
    print(f"Loaded {len(by_id)} existing papers", flush=True)

    queries = []
    if args.categories in ("both", "c2"):
        queries.extend(C2_QUERIES)
    if args.categories in ("both", "hai"):
        queries.extend(HAI_QUERIES)

    all_new = []
    for qi, (query, category, hint) in enumerate(queries):
        print(f"Query {qi+1}/{len(queries)} [{category}] {query[:80]}", flush=True)
        entries = search_arxiv(query, args.months, max_results=args.max_results)
        for entry in entries:
            m = ARXIV_ID_PATTERN.search(entry.get("url", ""))
            key = m.group(1) if m else None
            if key and key in by_id:
                continue
            t_lower = entry.get("title", "").lower().strip()
            if any(t_lower == t for t in titles_lower):
                continue
            if any(e.get("url") == entry["url"] for e in all_new):
                continue
            entry["category"] = category
            entry["subcategory"] = classify_subcategory(
                entry.get("title", ""), entry.get("abstract", "")
            )
            all_new.append(entry)
            by_id[key] = entry
            titles_lower.append(t_lower)
        time.sleep(args.sleep)

        if all_new and (qi + 1) % 10 == 0:
            append_papers(yaml_path, all_new)
            print(f"  [checkpoint] saved {len(all_new)} papers", flush=True)
            all_new = []
            by_id, titles_lower = load_existing_papers(yaml_path)

    print(f"\nFound {len(all_new)} new papers total", flush=True)

    if all_new:
        append_papers(yaml_path, all_new)
        print(f"Appended {len(all_new)} papers to papers.yaml", flush=True)


if __name__ == "__main__":
    main()
