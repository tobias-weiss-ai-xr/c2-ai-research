# C2-AI Research Corpus

**Evidence base for autonomous decision-making & deep reinforcement learning in
military simulations** — 11750 papers across 14 categories
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
| **Papers Analyzed** | 11750 |
| **Categories** | 14 |
| **Research Aspects** | 8 |
| **Taxonomy Cells** | 112 |
| **Saturation** | 100.0% (112/112 cells) |
| **Time Span** | – |

---

## 📊 The 14-Category Taxonomy

| Category | Papers |
|----------|-------:|
| Human–AI Teaming | 1972 |
| Deep Reinforcement Learning | 1737 |
| Autonomous Decision-Making | 1141 |
| Multi-Agent Reinforcement Learning | 946 |
| Decision Support | 801 |
| Command & Control (C2) | 752 |
| Simulation-to-Reality Transfer | 742 |
| Probabilistic & Uncertainty Reasoning | 694 |
| Mathematical Optimization | 578 |
| Opponent & Cognitive Modeling | 514 |
| Mission Planning | 490 |
| Wargaming | 466 |
| Military Simulation | 464 |
| Hierarchical Planning | 453 |

### Research Aspects (Subcategories)

| Aspect | Papers |
|--------|-------:|
| Application | 3478 |
| Development | 2338 |
| Theory | 2069 |
| Systems & Technology | 1413 |
| Method | 947 |
| Mechanism | 805 |
| Reviews & Surveys | 496 |
| Evaluation & Benchmarks | 204 |

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
| 2016 | 10 |
| 2017 | 7 |
| 2018 | 6 |
| 2019 | 6 |
| 2020 | 12 |
| 2021 | 287 |
| 2022 | 869 |
| 2023 | 928 |
| 2024 | 1650 |
| 2025 | 3798 |
| 2026 | 4141 |


---

## 🕳️ Research Gaps

The taxonomy is **100% saturated** (112/112 cells), so the open
questions are no longer *uncovered* topics but *under-examined* ones. The
`evaluation` research aspect is the thinnest at **204 papers
(1.7% of the corpus)** — the field builds systems but rarely
benchmarks them, especially in defense-relevant categories (C2, wargaming,
mission-planning and military-simulation each have ≤5 evaluation papers).

**Thinnest taxonomy cells**

| Cell | Papers |
|------|-------:|
| `wargaming/mechanism` | 1 |
| `wargaming/evaluation` | 2 |
| `mission-planning/evaluation` | 3 |
| `military-simulation/evaluation` | 5 |
| `mathematical-optimization/review` | 5 |
| `command-and-control/evaluation` | 5 |
| `military-simulation/mechanism` | 6 |
| `hierarchical-planning/review` | 6 |

**White-space cells** (low volume, fast recent growth — first-mover openings)

| Cell | Total | Recent | 12-m share |
|------|------:|-------:|-----------:|
| `probabilistic-uncertainty/evaluation` | 17 | 15 | 88% |
| `sim-to-real/evaluation` | 7 | 6 | 86% |
| `military-simulation/evaluation` | 5 | 4 | 80% |
| `sim-to-real/mechanism` | 10 | 7 | 70% |
| `mathematical-optimization/mechanism` | 24 | 16 | 67% |
| `mathematical-optimization/evaluation` | 15 | 10 | 67% |

> Full gap → opportunity analysis:
> [`docs/research/opportunities.md`](docs/research/opportunities.md)

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
