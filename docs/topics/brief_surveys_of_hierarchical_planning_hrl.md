# Article Brief: Surveys of Hierarchical Planning / HRL

> **Ranked research-gap topic #14** in the C2-AI corpus (11,750 papers, 112 taxonomy cells). Target cell `hierarchical-planning/review` = **6 paper(s)**; parent category `hierarchical-planning` = 453 papers. Trend anchor: hierarchical-planning momentum negative (-5.2%).

---

## 1. Thesis

Hierarchical planning has 453 papers but only 6 reviews, and category momentum is negative. This survey consolidates hierarchical RL / temporal-abstraction planning and flags where it meets C2 and mission planning.

## 2. Gap evidence (from statistics.json)

| Cell | Papers | Note |
|------|------:|------|
| `hierarchical-planning/review` | 6 | target cell (gap) |
| `hierarchical-planning` (parent) | 453 | evidence base to build on |
| trend anchor | — | hierarchical-planning momentum negative (-5.2%) |

## 3. Seed papers (corpus-grounded)

- **A Comprehensive Review of AI Agents: Transforming Possibilities in Technology and Beyond** (hierarchical-planning/review) — 2025 — [2508.11957](https://arxiv.org/abs/2508.11957)
  Artificial Intelligence (AI) agents have rapidly evolved from specialized, rule-based programs to versatile, learning-driven autonomous systems capable of perception, reasoning, and action in complex environments. The explosion of data, advances in deep…
- **Generative World Models of Tasks: LLM-Driven Hierarchical Scaffolding for Embodied Agents** (hierarchical-planning/review) — 2025 — [2509.04731](https://arxiv.org/abs/2509.04731)
  Recent advances in agent development have focused on scaling model size and raw interaction data, mirroring successes in large language models. However, for complex, long-horizon multi-agent tasks such as robotic soccer, this end-to-end approach often fails…
- **Hierarchical Reinforcement Learning: A Survey and Open Research Challenges** (hierarchical-planning/review) — 2022 — [https://doi.org/10.3390/make4010009](https://doi.org/10.3390/make4010009)
  Reinforcement learning (RL) allows an agent to solve sequential decision-making problems by interacting with an environment in a trial-and-error fashion. When these environments are very complex,…
- **Model-based Reinforcement Learning: A Survey** (hierarchical-planning/review) — 2023 — [https://doi.org/10.1561/2200000086](https://doi.org/10.1561/2200000086)
  Sequential decision making, commonly formalized as Markov Decision Process (MDP) optimization, is an important challenge in artificial intelligence. Two key approaches to this problem are…
- **Discovering Temporal Structure: An Overview of Hierarchical Reinforcement Learning** (hierarchical-planning/review) — 2025 — [2506.14045](https://arxiv.org/abs/2506.14045)
  Developing agents capable of exploring, planning and learning in complex open-ended environments is a grand challenge in artificial intelligence (AI). Hierarchical reinforcement learning (HRL) offers a promising solution to this challenge by discovering and…
- **Adaptive Trajectory Planning in Autonomous Vehicles: A Hierarchical Reinforcement Learning Approach with Soft Actor-Critic** (hierarchical-planning/review) — 2024 — [https://doi.org/10.1109/ants63515.2024.10898701](https://doi.org/10.1109/ants63515.2024.10898701)
  This study introduces a methodology enabling automated vehicles to perform lane changes effectively within complex road systems. It emphasizes a hierarchical driver behavior framework that…
- **Enhancing Hierarchical Reinforcement Learning through Change Point Detection in Time Series** (hierarchical-planning/theory) — 2025 — [2510.24988](https://arxiv.org/abs/2510.24988)
  Hierarchical Reinforcement Learning (HRL) enhances the scalability of decision-making in long-horizon tasks by introducing temporal abstraction through options-policies that span multiple timesteps. Despite its theoretical appeal, the practical implementation…
- **Learning Multi-Timescale Abstractions for Hierarchical Combinatorial Planning** (autonomous-decision-making/development) — 2026 — [2605.17058](https://arxiv.org/abs/2605.17058)
  The combination of exponentially large action spaces, stochastic dynamics, and long-horizon decision-making under limited resources makes Sequential Stochastic Combinatorial Optimization (SSCO) particularly challenging for reinforcement learning. Hierarchical…
- **DocHRL: A Hierarchical Reinforcement Learning Framework for Cost-Optimised Document Classification** (hierarchical-planning/theory) — 2026 — [2607.22644](https://arxiv.org/abs/2607.22644)
  Real-world document classification pipelines typically apply the same sequence of models to every incoming document, regardless of its complexity or type. This leads to inefficient use of compute and human resources: simple documents are over-processed while…
- **Hierarchical Reinforcement Learning for Sparse-Reward Search in Commutative Algebra** (hierarchical-planning/application) — 2026 — [2606.22922](https://arxiv.org/abs/2606.22922)
  Applying machine learning techniques to solving long-standing mathematical conjectures can be particularly challenging due to their extreme reward sparsity. As an illustrative example, we consider Kalai's algebraic Hirsch conjecture and recast the…

## 4. Proposed structure

- **H1 — Introduction & gap framing.** Lead with the cell count vs. category size.
- **H2 — Background.** Method/trend anchor + domain (C2/wargaming/simulation).
- **H3 — Taxonomy.** Map existing corpus work; flag the empty quadrant.
- **H4 — Research agenda / contributions.** Concrete proposals tied to the gap.
- **H5 — Evaluation.** Metrics & a reproducible testbed (the evaluation cell is itself thin).
- **H6 — Open challenges & conclusion.**

## 5. Suggested venues

JAIR, IEEE Transactions on Cognitive and Developmental Systems, ICRA, JMLR

_Generated by scripts-style gap-brief generator from papers.yaml + statistics.json._