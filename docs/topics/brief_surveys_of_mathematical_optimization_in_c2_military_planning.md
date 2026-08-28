# Article Brief: Surveys of Mathematical Optimization in C2/Military Planning

> **Ranked research-gap topic #7** in the C2-AI corpus (11,750 papers, 112 taxonomy cells). Target cell `mathematical-optimization/review` = **5 paper(s)**; parent category `mathematical-optimization` = 578 papers. Trend anchor: optimization 1.39x.

---

## 1. Thesis

Mathematical optimization has 578 corpus papers but only 5 reviews. This survey synthesizes combinatorial/continuous optimization for C2 and military planning, and maps open problems.

## 2. Gap evidence (from statistics.json)

| Cell | Papers | Note |
|------|------:|------|
| `mathematical-optimization/review` | 5 | target cell (gap) |
| `mathematical-optimization` (parent) | 578 | evidence base to build on |
| trend anchor | — | optimization 1.39x |

## 3. Seed papers (corpus-grounded)

- **Trustworthy Machine Learning through the Lens of Combinatorial Optimization: Survey and Research Perspectives** (mathematical-optimization/review) — 2026 — [2607.07762](https://arxiv.org/abs/2607.07762)
  Modern machine learning (ML) increasingly relies on complex models whose behavior is difficult to characterize beyond empirical performance metrics. Across a wide range of tasks, including prediction, generation, and decision-making, models with similar…
- **A survey of the orienteering problem: model evolution, algorithmic advances, and future directions** (mathematical-optimization/review) — 2025 — [2512.16865](https://arxiv.org/abs/2512.16865)
  The orienteering problem (OP) is a combinatorial optimization problem that seeks a path visiting a subset of locations to maximize collected rewards under a limited resource budget. This article presents a systematic PRISMA-based review of OP research…
- **Reinforcement Learning Methods for Computation Offloading: A Systematic Review** (mathematical-optimization/review) — 2023 — [https://doi.org/10.1145/3603703](https://doi.org/10.1145/3603703)
  Today, cloud computation offloading may not be an appropriate solution for delay-sensitive applications due to the long distance between end-devices and remote datacenters. In addition, offloading…
- **Neural combinatorial optimization with reinforcement learning in industrial engineering: a survey** (mathematical-optimization/review) — 2025 — [https://doi.org/10.1007/s10462-024-11045-1](https://doi.org/10.1007/s10462-024-11045-1)
  In recent trends, machine learning is widely used to support decision-making in various domains and industrial operations. Because of the increasing complexity of modern industries, industrial…
- **Reinforcement Learning for Prompt Optimization in Language Models: A Comprehensive Survey of Methods, Representations, and Evaluation Challenges** (mathematical-optimization/review) — 2025 — [https://doi.org/10.62762/tetai.2025.790504](https://doi.org/10.62762/tetai.2025.790504)
  The growing prominence of prompt engineering as a means of controlling large language models has given rise to a diverse set of methods, ranging from handcrafted templates to embedding-level tuning.…
- **Combinatorial Optimization Augmented Machine Learning** (deep-reinforcement-learning/review) — 2026 — [2601.10583](https://arxiv.org/abs/2601.10583)
  Combinatorial optimization augmented machine learning (COAML) has recently emerged as a powerful paradigm for integrating predictive models with combinatorial decision-making. By embedding combinatorial optimization oracles into learning pipelines, COAML…
- **A Survey of Freshness-Aware Wireless Networking with Reinforcement Learning** (deep-reinforcement-learning/review) — 2025 — [2512.21412](https://arxiv.org/abs/2512.21412)
  The age of information (AoI) has become a central measure of data freshness in modern wireless systems, yet existing surveys either focus on classical AoI formulations or provide broad discussions of reinforcement learning (RL) in wireless networks without…
- **Deep RL for Fast Long-Horizon Operations Scheduling on NASA's Carruthers Geocorona Observatory Mission** (deep-reinforcement-learning/application) — 2026 — [2606.22159](https://arxiv.org/abs/2606.22159)
  Spacecraft operations scheduling is a highly constrained, long-horizon combinatorial optimization problem that traditionally relies on heuristics, constraint programming, or manual planning. We present a scalable deep reinforcement learning framework…
- **Toward Human-Centered Multi-Agent Systems: Integrating Cognition, Culture, Values, and Cooperation in AI Agents** (multi-agent-rl/development) — 2026 — [2606.08274](https://arxiv.org/abs/2606.08274)
  The emergence of large language model (LLM)-based agents and multi-agent systems has enabled a shift from narrow task automation to more autonomous decision-making. Despite progress in language generation, planning, tool use, and coordination, most agents…
- **RELIC: Revealed Principles for Learning Interpretable Composable Skills in Multi-Agent Planning** (decision-support/development) — 2026 — [2607.16745](https://arxiv.org/abs/2607.16745)
  Multi-agent planning becomes substantially harder when agents must improve specialized decision-making skills while keeping their executable implementations private. This setting arises when independently developed agents expose heterogeneous interfaces,…

## 4. Proposed structure

- **H1 — Introduction & gap framing.** Lead with the cell count vs. category size.
- **H2 — Background.** Method/trend anchor + domain (C2/wargaming/simulation).
- **H3 — Taxonomy.** Map existing corpus work; flag the empty quadrant.
- **H4 — Research agenda / contributions.** Concrete proposals tied to the gap.
- **H5 — Evaluation.** Metrics & a reproducible testbed (the evaluation cell is itself thin).
- **H6 — Open challenges & conclusion.**

## 5. Suggested venues

European Journal of Operational Research, INFORMS JOCS, IEEE Transactions on Systems, Man, and Cybernetics

_Generated by scripts-style gap-brief generator from papers.yaml + statistics.json._