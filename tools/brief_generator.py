#!/usr/bin/env python3
"""Turn a research topic into a ready-to-write article brief.

Usage:
    tools/brief_generator.py "Deep RL for wargaming" --papers 5
    tools/brief_generator.py "opponent modeling" --as-doc
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import domain  # noqa: E402


def slugify(topic):
    return re.sub(r"[^a-z0-9]+", "_", topic.lower()).strip("_") or "brief"


def find_papers(papers, topic):
    terms = [t for t in topic.lower().split()
             if t not in {"for", "in", "the", "and", "with"}]
    scored = []
    for p in papers:
        hay = " ".join([p["title"], p["category"], p["subcategory"],
                        p.get("abstract", "")]).lower()
        matches = sum(1 for t in terms if t in hay)
        if matches:
            scored.append((matches, p))
    scored.sort(key=lambda x: -x[0])
    return [p for _, p in scored]


def main():
    parser = argparse.ArgumentParser(description="Brief generator")
    parser.add_argument("topic", help="e.g. 'Deep RL for wargaming'")
    parser.add_argument("--papers", type=int, default=5)
    parser.add_argument("--as-doc", action="store_true", help="write a .md brief")
    args = parser.parse_args()

    papers = yaml.safe_load(
        (BASE / "papers.yaml").read_text(encoding="utf-8")
    )["papers"]
    hits = find_papers(papers, args.topic)[:args.papers]

    lines = [f"# Article Brief: {args.topic}\n"]
    if not hits:
        lines.append("No corpus papers matched the topic. Consider expanding the corpus.")
    for p in hits:
        category = domain.CATEGORY_DISPLAY.get(p["category"], p["category"])
        lines.append(f"- **{p['title']}** ({category} / {p['subcategory']}) — "
                     f"{p['date']} — [{p['url'].split('/abs/')[-1]}]({p['url']})")
        if p.get("abstract"):
            lines.append(f"  {p['abstract'][:600].rsplit(' ', 1)[0]}…\n")

    print("\n".join(lines))

    if args.as_doc:
        out_dir = BASE / "docs" / "topics"
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / f"brief_{slugify(args.topic)}.md"
        out.write_text("\n".join(lines), encoding="utf-8")
        print(f"\nWrote {out}")


if __name__ == "__main__":
    main()