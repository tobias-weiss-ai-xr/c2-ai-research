# C2-AI Research Corpus

**Evidence base for autonomous decision-making & deep reinforcement learning in
military simulations** — 6277 papers across 14 categories
and 8 research aspects.

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
| **Papers Analyzed** | 6277 |
| **Categories** | 14 |
| **Research Aspects** | 8 |
| **Taxonomy Cells** | 112 |
| **Saturation** | 99.1% (111/112 cells) |
| **Time Span** | – |

---

## 📊 The 14-Category Taxonomy

| Category | Papers |
|----------|-------:|
| Human–AI Teaming | 1721 |
| Deep Reinforcement Learning | 988 |
| Autonomous Decision-Making | 582 |
| Multi-Agent Reinforcement Learning | 448 |
| Simulation-to-Reality Transfer | 425 |
| Decision Support | 403 |
| Command & Control (C2) | 401 |
| Probabilistic & Uncertainty Reasoning | 328 |
| Mathematical Optimization | 259 |
| Opponent & Cognitive Modeling | 176 |
| Wargaming | 149 |
| Mission Planning | 145 |
| Hierarchical Planning | 127 |
| Military Simulation | 125 |

### Research Aspects (Subcategories)

| Aspect | Papers |
|--------|-------:|
| Application | 1769 |
| Development | 1533 |
| Theory | 1110 |
| Systems & Technology | 701 |
| Mechanism | 524 |
| Method | 270 |
| Reviews & Surveys | 237 |
| Evaluation & Benchmarks | 133 |

### Distribution by Year

| Year | Papers |
|------|-------:|
| 1978 | 2 |
| 1985 | 1 |
| 1989 | 1 |
| 1997 | 1 |
| 1999 | 2 |
| 2000 | 1 |
| 2001 | 1 |
| 2002 | 3 |
| 2003 | 1 |
| 2004 | 1 |
| 2005 | 1 |
| 2007 | 1 |
| 2008 | 2 |
| 2009 | 5 |
| 2010 | 4 |
| 2012 | 3 |
| 2013 | 1 |
| 2014 | 2 |
| 2015 | 3 |
| 2016 | 11 |
| 2017 | 7 |
| 2018 | 6 |
| 2019 | 6 |
| 2020 | 12 |
| 2021 | 73 |
| 2022 | 194 |
| 2023 | 298 |
| 2024 | 397 |
| 2025 | 1866 |
| 2026 | 3371 |


---

## 🕳️ Research Gaps

Prime opportunities for further investigation — **uncovered categories**:

—

**Uncovered aspects:**

—

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
