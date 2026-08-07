#!/usr/bin/env python3
"""Regenerate papers.yaml and papers.json from the curated seed data.

This is the one-time/update builder for the research corpus. It holds the
curated list of verified papers (from the arXiv API) plus each paper's
taxonomy assignment. Running it rewrites `papers.yaml` (source of truth)
and `papers.json` (JSON export).

Usage:
    python3 scripts/build_corpus.py
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

# (arxiv_id, category, subcategory)
SEED = [
    ("1701.07274", "deep-reinforcement-learning", "review"),
    ("1707.06347", "deep-reinforcement-learning", "method"),
    ("1710.02298", "deep-reinforcement-learning", "systems"),
    ("1712.00006", "deep-reinforcement-learning", "evaluation"),
    ("1909.07528", "multi-agent-rl", "mechanism"),
    ("2203.08975", "multi-agent-rl", "review"),
    ("1806.10792", "hierarchical-planning", "method"),
    ("1911.08265", "autonomous-decision-making", "theory"),
    ("1810.00829", "decision-support", "application"),
    ("2004.09340", "military-simulation", "evaluation"),
    ("1910.08476", "mathematical-optimization", "theory"),
]


def normalize_abstract(text: str) -> str:
    text = (text or "").strip()
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return " ".join(lines)


def fetch_arxiv(ids):
    """Fetch metadata for a list of arxiv ids and return a map id -> paper."""
    import urllib.parse
    import urllib.request
    import re

    url = "https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(
        ",".join(p[0].split("v")[0] for p in ids)
    ) + "&max_results=100"
    data = urllib.request.urlopen(url, timeout=30).read().decode()
    out = {}
    for blk in re.findall(r"<entry>(.*?)</entry>", data, re.S):
        m = re.search(r"<id>http://arxiv.org/abs/([^<]+)</id>", blk)
        base = m.group(1).split("v")[0] if m else None
        tt = re.search(r"<title>(.*?)</title>", blk, re.S)
        pub = re.search(r"<published>(\d{4}-\d{2})", blk)
        au = re.findall(r"<name>([^<]+)</name>", blk)
        ab = re.search(r"<summary>(.*?)</summary>", blk, re.S)
        if base is None or tt is None:
            continue
        out[base] = {
            "arxiv_id": base,
            "title": " ".join(tt.group(1).replace("\n", " ").split()),
            "date": pub.group(1) if pub else "0000-00",
            "authors": [a.strip() for a in au],
            "abstract": normalize_abstract(ab.group(1)) if ab else "",
        }
    return out


def main():
    import yaml

    meta = fetch_arxiv(SEED)
    papers = []
    for arxiv_id, category, subcategory in SEED:
        base = arxiv_id.split("v")[0]
        info = meta.get(base)
        if info is None:
            raise SystemExit(f"arxiv metadata missing for {base}")
        url = f"https://arxiv.org/abs/{base}"
        if arxiv_id not in (base, f"{base}v1", info.get("arxiv_id") + "v1"):
            url = f"https://arxiv.org/abs/{arxiv_id}"
        papers.append(
            {
                "title": info["title"],
                "date": info["date"],
                "url": url,
                "category": category,
                "subcategory": subcategory,
                "arxiv_id": base,
                "authors": info["authors"],
                "abstract": info["abstract"],
            }
        )

    (BASE / "papers.yaml").write_text(
        yaml.safe_dump({"papers": papers}, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    (BASE / "papers.json").write_text(
        json.dumps({"papers": papers}, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote {len(papers)} papers to papers.yaml / papers.json")


if __name__ == "__main__":
    main()