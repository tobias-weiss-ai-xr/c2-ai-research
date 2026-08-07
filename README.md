# C2-AI Research Corpus

**Evidence base for autonomous decision-making & deep reinforcement learning in
military simulations** — 11 papers across 14 categories
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
| **Papers Analyzed** | 11 |
| **Categories** | 14 |
| **Research Aspects** | 8 |
| **Taxonomy Cells** | 112 |
| **Saturation** | 9.8% (11/112 cells) |
| **Time Span** | 2017-2022 |

---

## 📊 The 14-Category Taxonomy

| Category | Papers |
|----------|-------:|
| Deep Reinforcement Learning | 4 |
| Multi-Agent Reinforcement Learning | 2 |
| Hierarchical Planning | 1 |
| Autonomous Decision-Making | 1 |
| Decision Support | 1 |
| Military Simulation | 1 |
| Mathematical Optimization | 1 |

### Research Aspects (Subcategories)

| Aspect | Papers |
|--------|-------:|
| Reviews & Surveys | 2 |
| Method | 2 |
| Evaluation & Benchmarks | 2 |
| Theory | 2 |
| Systems & Technology | 1 |
| Mechanism | 1 |
| Application | 1 |

### Distribution by Year

| Year | Papers |
|------|-------:|
| 2017 | 4 |
| 2018 | 2 |
| 2019 | 3 |
| 2020 | 1 |
| 2022 | 1 |


---

## 🕳️ Research Gaps

Prime opportunities for further investigation — **uncovered categories**:

Opponent & Cognitive Modeling, Wargaming, Command & Control (C2), Probabilistic & Uncertainty Reasoning, Mission Planning, Human–AI Teaming, Simulation-to-Reality Transfer

**Uncovered aspects:**

Development

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
│   ├── research/                      # Taxonomy, literature review, trends
│   └── topics/                        # Generated article topics
│
├── tools/                             # Article planning tools
│   ├── topic_planner.py               # Evidence-based topic planner
│   ├── trend_scanner.py               # Emergent-trend scanner
│   └── brief_generator.py             # Article brief generator
│
├── scripts/
│   ├── build_corpus.py               # Rebuild corpus from curated seed (arXiv)
│   ├── validate_papers.py             # Corpus validation
│   ├── generate_readme.py             # README generator
│   ├── visualize_statistics.py        # Chart generation
│   └── analysis/generate_analysis.py # Statistics + JSON export
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

### 3. Article Brief Generator
```bash
cd tools && python3 brief_generator.py "Deep RL for wargaming" --papers 5
```

---

## 🔄 Research Pipeline

1. **Discover** — add papers to `papers.yaml` (or run `scripts/build_corpus.py`)
2. **Validate** — `python3 scripts/validate_papers.py`
3. **Analyse** — `python3 scripts/analysis/generate_analysis.py`
4. **Visualise** — `python3 scripts/visualize_statistics.py`
5. **Generate** — `python3 scripts/generate_readme.py`

CI (``.github/workflows/validate.yml`) validates and regenerates on every push.

---

## 🔗 Related Repositories

- [graph-research](https://github.com/tobias-weiss-ai-xr/graph-research) — graph / GNN corpus
- [learning-research](https://github.com/tobias-weiss-ai-xr/learning-research) — agent learning corpus

---

## 📄 License

**© 2026 C2-AI Research | Tobias Weiss**

- **Research corpus:** Proprietary
- **Tools / scripts:** MIT License

---

**Want to plan topics?** `cd tools && python3 topic_planner.py`
