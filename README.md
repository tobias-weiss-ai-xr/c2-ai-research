<h1 align="center">
  <strong>C2-AI Research Corpus</strong>
</h1>
<h3 align="center">Autonomous decision-making & deep reinforcement learning for military simulations</h3>

### 🔗 Links

- **GitHub**: https://github.com/tobias-weiss-ai-xr/c2-ai-research
- **License**: https://github.com/tobias-weiss-ai-xr/c2-ai-research/blob/main/LICENSE
- **CI**: https://github.com/tobias-weiss-ai-xr/c2-ai-research/actions/workflows/validate.yml
- **Decision-Making**: https://github.com/tobias-weiss-ai-xr/dm-research
- **Robotics**: https://github.com/tobias-weiss-ai-xr/robotics-research
- **Bayesian Stats**: https://github.com/tobias-weiss-ai-xr/bayesian-statistics-research


> 🎯 **C2-AI research corpus:** command & control AI, autonomous decision-making,
> deep reinforcement learning in military simulations — 14 categories across
> 8 research aspects. Part of the family of `*-research` corpora.

<p align="center">
  <img src="https://raw.githubusercontent.com/tobias-weiss-ai-xr/c2-ai-research/main/assets/visualizations/category_distribution.png" alt="Teaser" width="600" />
</p>

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
| **Papers Analyzed** | 11596 |
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
| Simulation-to-Reality Transfer | 742 |
| Probabilistic & Uncertainty Reasoning | 694 |
| Command & Control (C2) | 684 |
| Mathematical Optimization | 578 |
| Mission Planning | 490 |
| Military Simulation | 464 |
| Opponent & Cognitive Modeling | 461 |
| Hierarchical Planning | 453 |
| Wargaming | 433 |

### Research Aspects (Subcategories)

| Aspect | Papers |
|--------|-------:|
| Application | 3427 |
| Development | 2314 |
| Theory | 2051 |
| Systems & Technology | 1395 |
| Method | 920 |
| Mechanism | 795 |
| Reviews & Surveys | 492 |
| Evaluation & Benchmarks | 202 |

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
| 2026 | 3987 |


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
## 📊 Corpus Statistics

**11,596 papers** across **14 categories**.  
Sources: **arXiv** 8,335 (71%) · **DOI** 3,138 (27%) · **Other** 123 (1%).  
Full paper list: [GitHub Pages site](https://tobias-weiss-ai-xr.github.io/c2-ai-research).

### Top categories

| Category | Papers | Recent | |
|----------|--------|--------|-|
| human-ai-teaming | **1,972** | 0 | ████████████ |
| deep-reinforcement-learning | **1,737** | 0 | ██████████░░ |
| autonomous-decision-making | **1,141** | 0 | ██████░░░░░░ |
| multi-agent-rl | **946** | 0 | █████░░░░░░░ |
| decision-support | **801** | 0 | ████░░░░░░░░ |
| sim-to-real | **742** | 0 | ████░░░░░░░░ |
| probabilistic-uncertainty | **694** | 0 | ████░░░░░░░░ |
| command-and-control | **684** | 0 | ████░░░░░░░░ |
| mathematical-optimization | **578** | 0 | ███░░░░░░░░░ |
| mission-planning | **490** | 0 | ██░░░░░░░░░░ |
| *other* | **1,811** | | |


### By year

| Year | Papers | |
|------|--------|-|
| 2024 | 1,650 | ████░░░░░░░░ |
| 2025 | 3,798 | ███████████░ |
| 2026 | 3,987 | ████████████ |


### Momentum (hottest categories)

| Category | Total | Rate | Recent | Score |
|----------|-------|------|--------|-------|
| Simulation-to-Reality Transfer | 742 | 38.5/mo | 62% | 222 |
| Decision Support | 801 | 39.6/mo | 59% | 222 |
| Deep Reinforcement Learning | 1,737 | 91.2/mo | 63% | 200 |
| Mathematical Optimization | 578 | 25.7/mo | 53% | 192 |
| Probabilistic & Uncertainty Reasoning | 694 | 33.7/mo | 58% | 186 |


### Trending keywords

| Keyword | Papers | Burst |
|---------|--------|-------|
| agentic | 416 | 1.75 |
| benchmark | 1,624 | 1.53 |
| policy gradient | 321 | 1.51 |
| uncertainty | 832 | 1.41 |
| simulator | 353 | 1.41 |
| bayesian | 363 | 1.40 |
| pomdp | 223 | 1.39 |
| optimization | 2,140 | 1.35 |


### Top venues

| Venue | Papers |
|-------|--------|
| arXiv | 98 |
| IEEE Transactions on Vehicular Technology | 61 |
| IEEE Transactions on Intelligent Transportation Systems | 59 |
| IEEE Access | 56 |
| IEEE Internet of Things Journal | 44 |
| Zenodo (CERN European Organization for Nuclear Research) | 43 |
| IEEE Robotics and Automation Letters | 41 |
| Lecture notes in computer science | 38 |


### Research gaps (thinnest cells)

| Cell | Papers |
|------|--------|
| `wargaming/mechanism` | 1 |
| `wargaming/evaluation` | 1 |
| `mission-planning/evaluation` | 3 |
| `military-simulation/evaluation` | 5 |
| `mathematical-optimization/review` | 5 |



*Generated 2026-08 by `scripts/standard_stats.py`.*

## 📊 Corpus Statistics

**11,596 papers** across **14 categories**.  
Sources: **arXiv** 8,335 (71%) · **DOI** 3,138 (27%) · **Other** 123 (1%).  
Full paper list: [GitHub Pages site](https://tobias-weiss-ai-xr.github.io/c2-ai-research).

### Top categories

| Category | Papers | Recent | |
|----------|--------|--------|-|
| human-ai-teaming | **1,972** | 0 | ████████████ |
| deep-reinforcement-learning | **1,737** | 0 | ██████████░░ |
| autonomous-decision-making | **1,141** | 0 | ██████░░░░░░ |
| multi-agent-rl | **946** | 0 | █████░░░░░░░ |
| decision-support | **801** | 0 | ████░░░░░░░░ |
| sim-to-real | **742** | 0 | ████░░░░░░░░ |
| probabilistic-uncertainty | **694** | 0 | ████░░░░░░░░ |
| command-and-control | **684** | 0 | ████░░░░░░░░ |
| mathematical-optimization | **578** | 0 | ███░░░░░░░░░ |
| mission-planning | **490** | 0 | ██░░░░░░░░░░ |
| *other* | **1,811** | | |


### By year

| Year | Papers | |
|------|--------|-|
| 2024 | 1,650 | ████░░░░░░░░ |
| 2025 | 3,798 | ███████████░ |
| 2026 | 3,987 | ████████████ |


### Momentum (hottest categories)

| Category | Total | Rate | Recent | Score |
|----------|-------|------|--------|-------|
| Simulation-to-Reality Transfer | 742 | 38.5/mo | 62% | 222 |
| Decision Support | 801 | 39.6/mo | 59% | 222 |
| Deep Reinforcement Learning | 1,737 | 91.2/mo | 63% | 200 |
| Mathematical Optimization | 578 | 25.7/mo | 53% | 192 |
| Probabilistic & Uncertainty Reasoning | 694 | 33.7/mo | 58% | 186 |


### Trending keywords

| Keyword | Papers | Burst |
|---------|--------|-------|
| agentic | 416 | 1.75 |
| benchmark | 1,624 | 1.53 |
| policy gradient | 321 | 1.51 |
| uncertainty | 832 | 1.41 |
| simulator | 353 | 1.41 |
| bayesian | 363 | 1.40 |
| pomdp | 223 | 1.39 |
| optimization | 2,140 | 1.35 |


### Top venues

| Venue | Papers |
|-------|--------|
| arXiv | 98 |
| IEEE Transactions on Vehicular Technology | 61 |
| IEEE Transactions on Intelligent Transportation Systems | 59 |
| IEEE Access | 56 |
| IEEE Internet of Things Journal | 44 |
| Zenodo (CERN European Organization for Nuclear Research) | 43 |
| IEEE Robotics and Automation Letters | 41 |
| Lecture notes in computer science | 38 |


### Research gaps (thinnest cells)

| Cell | Papers |
|------|--------|
| `wargaming/mechanism` | 1 |
| `wargaming/evaluation` | 1 |
| `mission-planning/evaluation` | 3 |
| `military-simulation/evaluation` | 5 |
| `mathematical-optimization/review` | 5 |



*Generated 2026-08 by `scripts/standard_stats.py`.*


## 📄 License

**© 2026 C2-AI Research | Tobias Weiss**

- **Research corpus:** Proprietary
- **Tools / scripts:** MIT License

---

**Want to plan topics?** `cd tools && python3 topic_planner.py`
