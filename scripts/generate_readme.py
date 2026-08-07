#!/usr/bin/env python3
"""Generate README.md from statistics.json.

Usage:
    python3 scripts/generate_readme.py          # write README.md
    python3 scripts/generate_readme.py --check  # verify README is up to date (CI)
"""

import argparse
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import domain  # noqa: E402


def render_readme(stats):
    meta = stats["metadata"]
    total = meta["total_papers"]
    sat = meta["taxonomy"]["saturation"]
    filled = meta["taxonomy"]["filled_cells"]
    total_cells = meta["taxonomy"]["total_cells"]
    by_cat = stats["by_category"]
    by_sub = stats["by_subcategory"]
    by_year = stats["by_year"]
    time_span = meta.get("time_span", "–")

    cat_rows = "".join(
        f"| {domain.CATEGORY_DISPLAY.get(k, k)} | {v} |\n"
        for k, v in sorted(by_cat.items(), key=lambda x: -x[1])
    )
    sub_rows = "".join(
        f"| {domain.SUBCATEGORY_DISPLAY.get(k, k)} | {v} |\n"
        for k, v in sorted(by_sub.items(), key=lambda x: -x[1])
    )
    year_rows = "".join(
        f"| {k} | {v} |\n" for k, v in sorted(by_year.items())
    )

    gap_cats = [domain.CATEGORY_DISPLAY.get(c, c) for c in domain.CATEGORIES
                if c not in by_cat]
    gap_subs = [domain.SUBCATEGORY_DISPLAY.get(s, s) for s in domain.SUBCATEGORIES
                if s not in by_sub]
    gap_cats_txt = ", ".join(gap_cats) if gap_cats else "—"
    gap_subs_txt = ", ".join(gap_subs) if gap_subs else "—"

    readme = f"""# C2-AI Research Corpus

**Evidence base for autonomous decision-making & deep reinforcement learning in
military simulations** — {total} papers across {len(domain.CATEGORIES)} categories
and {len(domain.SUBCATEGORIES)} research aspects.

**Author:** Tobias Weiss · **License:** MIT (tools) / proprietary (corpus)

---

## 🎯 Overview

A research corpus and tooling harness for the intersection of **autonomous
planning & decision-making**, **deep reinforcement learning** and **decision
support** in military simulation environments. It mirrors the structure of the
established `*-research` corpora:
[graph-research](https://github.com/tobias-weiss-ai-xr/graph-research) and
[learning-research](https://github.com/tobias-weiss-ai-xr/learning-research).

### Research Scope

| Metric | Value |
|--------|-------|
| **Papers Analyzed** | {total} |
| **Categories** | {len(domain.CATEGORIES)} |
| **Research Aspects** | {len(domain.SUBCATEGORIES)} |
| **Taxonomy Cells** | {total_cells} |
| **Saturation** | {sat}% ({filled}/{total_cells} cells) |
| **Time Span** | {time_span} |

---

## 📊 The {len(domain.CATEGORIES)}-Category Taxonomy

| Category | Papers |
|----------|-------:|
{cat_rows}
### Research Aspects (Subcategories)

| Aspect | Papers |
|--------|-------:|
{sub_rows}
### Distribution by Year

| Year | Papers |
|------|-------:|
{year_rows}

---

## 🕳️ Research Gaps

Prime opportunities for further investigation — **uncovered categories**:

{gap_cats_txt}

**Uncovered aspects:**

{gap_subs_txt}

---

## 📁 Repository Structure

```
c2-ai-research/
├── README.md                          # This file (auto-generated)
├── papers.yaml                        # Paper metadata (source of truth)
├── papers.json                        # Paper metadata (JSON export)
├── statistics.json                    # Analysis statistics
├── requirements.txt
│
├── docs/
│   ├── research/                   # Taxonomy, review, trends, gaps, landscape
│   └── topics/                     # Generated article topics + briefs
│
├── tools/                          # Planning & analysis tools
│   ├── topic_planner.py            # Evidence-based topic planner
│   ├── trend_scanner.py            # Keyword-burst trend scanner
│   ├── landscape_analyzer.py       # Full landscape report
│   └── brief_generator.py          # Article brief generator
│
├── scripts/
│   ├── build_corpus.py            # Rebuild corpus from curated seed (arXiv)
│   ├── validate_papers.py          # Corpus validation
│   ├── export_bibtex.py            # paper/references.bib
│   ├── reclassify_papers.py        # Re-run subcategory classification
│   ├── generate_readme.py          # README generator
│   ├── visualize_statistics.py     # Chart generation
│   ├── analysis/
│   │   ├── generate_analysis.py    # statistics + momentum + bursts + gaps
│   │   └── generate_reports.py     # literature review + trends docs
│   └── fetch/
│       ├── fetch_new_papers.py     # arXiv discovery (77 taxonomy queries)
│       ├── fetch_openalex.py       # OpenAlex discovery (shared queries)
│       ├── fetch_openalex_bulk.py  # OpenAlex bulk bootstrap
│       └── fetch_metadata_bulk.py  # arXiv id_list metadata enrichment
│
└── examples/
```

---

## 🛠️ Tools

### 1. Article Topic Planner
```bash
cd tools && python3 topic_planner.py --top 10
```

### 2. Trend Scanner
```bash
cd tools && python3 trend_scanner.py --months 12
```

### 3. Landscape Analyzer
```bash
cd tools && python3 landscape_analyzer.py --write-doc
```

### 4. Article Brief Generator
```bash
cd tools && python3 brief_generator.py "Deep RL for wargaming" --papers 5
```

---

## 🔄 Research Pipeline

1. **Discover** — `python3 scripts/fetch/fetch_new_papers.py --months 6`
   (arXiv) or `python3 scripts/fetch/fetch_openalex_bulk.py` (OpenAlex bootstrap)
2. **Validate** — `python3 scripts/validate_papers.py`
3. **Analyse** — `python3 scripts/analysis/generate_analysis.py`
4. **Report** — `python3 scripts/analysis/generate_reports.py`
5. **Visualise** — `python3 scripts/visualize_statistics.py`
6. **Generate** — `python3 scripts/generate_readme.py`

CI (``.github/workflows/validate.yml`) validates and regenerates on every push.

---

## 🔗 Related Repositories

- [graph-research](https://github.com/tobias-weiss-ai-xr/graph-research) — the
  template corpus whose scripts & methods (arXiv/OpenAlex discovery, momentum,
  gaps, bursts, landscape analysis, BibTeX) were adopted here
- [learning-research](https://github.com/tobias-weiss-ai-xr/learning-research) — agent learning corpus

---

## 📄 License

**© 2026 C2-AI Research | Tobias Weiss**

- **Research corpus:** Proprietary
- **Tools / scripts:** MIT License

---

**Want to plan topics?** `cd tools && python3 topic_planner.py`
"""
    return readme


def main():
    parser = argparse.ArgumentParser(description="Generate README.md")
    parser.add_argument("--check", action="store_true",
                        help="exit non-zero if README.md is stale (for CI)")
    args = parser.parse_args()

    stats = json.loads((BASE / "statistics.json").read_text(encoding="utf-8"))
    readme = render_readme(stats)
    out_path = BASE / "README.md"

    if args.check:
        current = out_path.read_text(encoding="utf-8") if out_path.exists() else ""
        sys.exit(0 if current == readme else 1)
    out_path.write_text(readme, encoding="utf-8")
    print("README.md regenerated")


if __name__ == "__main__":
    main()