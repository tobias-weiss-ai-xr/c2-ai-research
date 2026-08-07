# C2-AI Research — Literature Review

**Generated:** 2026-08-07  
**Corpus:** 11 papers across 14 categories

> Synthesis of the autonomous decision-making & deep-RL research corpus. Category insights are drawn from title/abstract analysis of the papers themselves.

---

## Corpus Overview

| Rank | Category | Papers |
|------|----------|--------|
| 1 | Deep Reinforcement Learning | 4 |
| 2 | Multi-Agent Reinforcement Learning | 2 |
| 3 | Hierarchical Planning | 1 |
| 4 | Autonomous Decision-Making | 1 |
| 5 | Decision Support | 1 |

**Time span:** 2017–2022 (median year 2019)
**Dominant aspects:** Reviews & Surveys (2), Method (2), Evaluation & Benchmarks (2)

---

## 📈 Research Momentum (Last 12 Months)

Categories ranked by a momentum score combining recent output density with year-over-year growth.

| Category | Total | Last 12m | Prior 12m | Growth | 12-m share | Papers/mo |
|----------|------:|---------:|----------:|-------:|----------:|----------:|
| Autonomous Decision-Making | 1 | 0 | 0 | — | 0% | 0.0 |
| Deep Reinforcement Learning | 4 | 0 | 0 | — | 0% | 0.0 |
| Multi-Agent Reinforcement Learning | 2 | 0 | 0 | — | 0% | 0.0 |
| Opponent & Cognitive Modeling | 0 | 0 | 0 | — | 0% | 0.0 |
| Hierarchical Planning | 1 | 0 | 0 | — | 0% | 0.0 |
| Military Simulation | 1 | 0 | 0 | — | 0% | 0.0 |
| Wargaming | 0 | 0 | 0 | — | 0% | 0.0 |
| Command & Control (C2) | 0 | 0 | 0 | — | 0% | 0.0 |
| Decision Support | 1 | 0 | 0 | — | 0% | 0.0 |
| Mathematical Optimization | 1 | 0 | 0 | — | 0% | 0.0 |
| Probabilistic & Uncertainty Reasoning | 0 | 0 | 0 | — | 0% | 0.0 |
| Mission Planning | 0 | 0 | 0 | — | 0% | 0.0 |
| Human–AI Teaming | 0 | 0 | 0 | — | 0% | 0.0 |
| Simulation-to-Reality Transfer | 0 | 0 | 0 | — | 0% | 0.0 |

---

## 🕳️ Research Gaps & White Space

**Thinnest taxonomy cells:**

| Cell | Papers |
|------|--------|
| `deep-reinforcement-learning/review` | 1 |
| `deep-reinforcement-learning/method` | 1 |
| `deep-reinforcement-learning/systems` | 1 |
| `deep-reinforcement-learning/evaluation` | 1 |
| `multi-agent-rl/mechanism` | 1 |
| `multi-agent-rl/review` | 1 |
| `hierarchical-planning/method` | 1 |
| `autonomous-decision-making/theory` | 1 |

---


## Category Insights

### Deep Reinforcement Learning (`deep-reinforcement-learning`)

DRL is the methodological core of the corpus: value/policy gradients, benchmark algorithms (PPO, DQN/Rainbow) and sample-efficiency methods form the substrate every downstream planning/decision task builds on.

**Corpus size:** 4 papers

**Papers:**

- [2017-11] Comparing Deep Reinforcement Learning and Evolutionary Methods in Continuous Control — https://arxiv.org/abs/1712.00006
- [2017-10] Rainbow: Combining Improvements in Deep Reinforcement Learning — https://arxiv.org/abs/1710.02298
- [2017-07] Proximal Policy Optimization Algorithms — https://arxiv.org/abs/1707.06347

---

### Multi-Agent Reinforcement Learning (`multi-agent-rl`)

Cooperative/competitive multi-agent RL is the bridge from single-agent learning to unit/force-level coordination — the core of adversarial and maneuver scenarios in simulation.

**Corpus size:** 2 papers

**Papers:**

- [2022-03] A Survey of Multi-Agent Deep Reinforcement Learning with Communication — https://arxiv.org/abs/2203.08975
- [2019-09] Emergent Tool Use From Multi-Agent Autocurricula — https://arxiv.org/abs/1909.07528

---

### Hierarchical Planning (`hierarchical-planning`)

Hierarchical and abductive planning tackles the combinatorial depth of complex operational tasks by decomposing goals into options and sub-plans.

**Corpus size:** 1 papers

**Papers:**

- [2018-06] Hierarchical Reinforcement Learning with Abductive Planning — https://arxiv.org/abs/1806.10792

---

### Autonomous Decision-Making (`autonomous-decision-making`)

End-to-end perception-then-action pipelines (e.g. decision transformers, MCTS planners) encode the target capability for autonomous planning and decision-making in high-stakes, partially structured environments.

**Corpus size:** 1 papers

**Papers:**

- [2019-11] Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model — https://arxiv.org/abs/1911.08265

---

### Decision Support (`decision-support`)

Decision support fuses statistics, ML and optimization to augment human decisions — explicitly including recommendation and interpretability for warfighters and operators.

**Corpus size:** 1 papers

**Papers:**

- [2018-10] Adaptive Game-Theoretic Decision Making for Autonomous Vehicle Control at Roundabouts — https://arxiv.org/abs/1810.00829

---

### Military Simulation (`military-simulation`)

Simulation environments (constructive, game-engine, entity-level) are the training and test bed for RL in military settings; assessment and fidelity criteria matter as much as the learners themselves.

**Corpus size:** 1 papers

**Papers:**

- [2020-04] On the Evaluation of Military Simulations: Towards A Taxonomy of Assessment Criteria — https://arxiv.org/abs/2004.09340

---

### Mathematical Optimization (`mathematical-optimization`)

Constrained/convex/DP optimization is the formal bridge between RL objectives and provable mission-planning guarantees.

**Corpus size:** 1 papers

**Papers:**

- [2019-10] On Connections between Constrained Optimization and Reinforcement Learning — https://arxiv.org/abs/1910.08476

---

## Methodology

1. Papers are discovered via taxonomy-aware arXiv/OpenAlex queries and auto-classified into the 14×8 taxonomy.
2. Category insights above are editorially curated but grounded in corpus statistics.
3. Regenerate this document with `scripts/analysis/generate_reports.py`.
