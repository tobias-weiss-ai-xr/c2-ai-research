# Article Brief: Multi-Agent RL Failure Modes & Reproducibility Benchmarks

> **Ranked research-gap topic #9** in the C2-AI corpus (11,750 papers, 112 taxonomy cells). Target cell `multi-agent-rl/evaluation` = **9 paper(s)**; parent category `multi-agent-rl` = 946 papers. Trend anchor: multi-agent 1.10x.

---

## 1. Thesis

Multi-agent RL has 946 papers but only 9 evaluation papers. This article catalogs failure modes of deep MARL and proposes reproducibility/evaluation benchmarks — a live, emerging angle with seed work already in the corpus.

## 2. Gap evidence (from statistics.json)

| Cell | Papers | Note |
|------|------:|------|
| `multi-agent-rl/evaluation` | 9 | target cell (gap) |
| `multi-agent-rl` (parent) | 946 | evidence base to build on |
| trend anchor | — | multi-agent 1.10x |

## 3. Seed papers (corpus-grounded)

- **LLM-Guided Communication for Cooperative Multi-Agent Reinforcement Learning** (multi-agent-rl/evaluation) — 2026 — [2605.18077](https://arxiv.org/abs/2605.18077)
  Communication is a key component in multi-agent reinforcement learning (MARL) for mitigating partial observability, yet prior approaches often rely on inefficient information exchange or fail to transmit sufficient state information. To address this, we…
- **Failure Modes of Deep Multi-Agent RL in Asynchronous Pricing: Reproducible Triggers, Trace Diagnostics, and a Partial Fix** (multi-agent-rl/evaluation) — 2026 — [2606.09884](https://arxiv.org/abs/2606.09884)
  We study two reproducible failure modes of deep multi-agent reinforcement learning in continuous-time pricing markets: (i) tacit cartel formation between competing DDPG agents, and (ii) actor--critic instability at high event rates. We instantiate both inside…
- **Adaptive TD-Lambda for Cooperative Multi-agent Reinforcement Learning** (multi-agent-rl/evaluation) — 2026 — [2605.11880](https://arxiv.org/abs/2605.11880)
  TD(λ) in value-based MARL algorithms or the Temporal Difference critic learning in Actor-Critic-based (AC-based) algorithms synergistically integrate elements from Monte-Carlo simulation and Q function bootstrapping via dynamic programming, which effectively…
- **Safe Equilibrium Policy Optimization for Strategic Agent Policies** (multi-agent-rl/evaluation) — 2026 — [2605.30854](https://arxiv.org/abs/2605.30854)
  Language models fine-tuned with reinforcement learning typically optimize for task reward, ignoring multi-agent strategic structure. Because these agents condition on natural language game-state descriptions and emit actions through free-form generation,…
- **Single-Agent Scaling Fails Multi-Agent Intelligence: Towards Foundation Models with Native Multi-Agent Intelligence** (multi-agent-rl/evaluation) — 2025 — [2512.08743](https://arxiv.org/abs/2512.08743)
  Foundation models (FMs) are increasingly assuming the role of the ''brain'' of AI agents. While recent efforts have begun to equip FMs with native single-agent abilities -- such as GUI interaction or integrated tool use -- we argue that the next frontier is…
- **Episodic Multi-agent Reinforcement Learning with Curiosity-Driven Exploration** (multi-agent-rl/evaluation) — 2021 — [2111.11032](https://arxiv.org/abs/2111.11032)
  Efficient exploration in deep cooperative multi-agent reinforcement learning (MARL) still remains challenging in complex coordination problems. In this paper, we introduce a novel Episodic…
- **Multi-Agent Reinforcement Learning With Policy Clipping and Average Evaluation for UAV-Assisted Communication Markov Game** (multi-agent-rl/evaluation) — 2023 — [https://doi.org/10.1109/tits.2023.3296769](https://doi.org/10.1109/tits.2023.3296769)
  Unmanned aerial vehicle (UAV)-assisted communication is a significant technology in 6G communication. In order to cope with the dynamic trajectory optimization problem of the air-ground network, the…
- **Self-Supervised Neuron Segmentation with Multi-Agent Reinforcement Learning** (multi-agent-rl/evaluation) — 2023 — [2310.04148](https://arxiv.org/abs/2310.04148)
  The performance of existing supervised neuron segmentation methods is highly dependent on the number of accurate annotations, especially when applied to large scale electron microscopy (EM) data. By…
- **SMACv2: An Improved Benchmark for Cooperative Multi-Agent Reinforcement Learning** (multi-agent-rl/evaluation) — 2022 — [2212.07489](https://arxiv.org/abs/2212.07489)
  The availability of challenging benchmarks has played a key role in the recent progress of machine learning. In cooperative multi-agent reinforcement learning, the StarCraft Multi-Agent Challenge…
- **Decoupled Delay Compensation: Enhancing Pre-trained MARL Policies via Learned Dynamics Filtering** (multi-agent-rl/application) — 2026 — [2605.26286](https://arxiv.org/abs/2605.26286)
  Real-world multi-agent reinforcement learning (MARL) systems must often operate under stale observations, stochastic communication delays, and intermittent packet loss. Policies trained under idealized synchronous conditions frequently exhibit significant…

## 4. Proposed structure

- **H1 — Introduction & gap framing.** Lead with the cell count vs. category size.
- **H2 — Background.** Method/trend anchor + domain (C2/wargaming/simulation).
- **H3 — Taxonomy.** Map existing corpus work; flag the empty quadrant.
- **H4 — Research agenda / contributions.** Concrete proposals tied to the gap.
- **H5 — Evaluation.** Metrics & a reproducible testbed (the evaluation cell is itself thin).
- **H6 — Open challenges & conclusion.**

## 5. Suggested venues

AAMAS, ICLR, NeurIPS (Multi-Agent), JAAMAS, ICML

_Generated by scripts-style gap-brief generator from papers.yaml + statistics.json._