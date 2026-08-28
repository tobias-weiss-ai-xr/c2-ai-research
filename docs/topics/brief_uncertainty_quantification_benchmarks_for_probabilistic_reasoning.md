# Article Brief: Uncertainty-Quantification Benchmarks for Probabilistic Reasoning

> **Ranked research-gap topic #6** in the C2-AI corpus (11,750 papers, 112 taxonomy cells). Target cell `probabilistic-uncertainty/evaluation` = **17 paper(s)**; parent category `probabilistic-uncertainty` = 694 papers. Trend anchor: uncertainty 1.45x; bayesian 1.44x.

---

## 1. Thesis

Probabilistic/uncertainty reasoning is the white-space cell with the highest recent share (88%), yet only 17 evaluation papers. This article proposes calibration and UQ benchmarks for decision-making under uncertainty, bridging Bayesian and deep-RL uncertainty.

## 2. Gap evidence (from statistics.json)

| Cell | Papers | Note |
|------|------:|------|
| `probabilistic-uncertainty/evaluation` | 17 | target cell (gap) |
| `probabilistic-uncertainty` (parent) | 694 | evidence base to build on |
| trend anchor | — | uncertainty 1.45x; bayesian 1.44x |

## 3. Seed papers (corpus-grounded)

- **SymQNet: Amortized Acquisition for Low-Latency Adaptive Hamiltonian Learning** (probabilistic-uncertainty/evaluation) — 2026 — [2606.12808](https://arxiv.org/abs/2606.12808)
  Adaptive Hamiltonian learning is central to calibrating and characterizing quantum devices. In an adaptive controller, choosing the next experiment is itself a computation. Bayesian design rules are recomputed after every posterior update, and that step can…
- **Cross-Epoch Adaptive Rollout Optimization for RL Post-Training** (probabilistic-uncertainty/evaluation) — 2026 — [2606.05606](https://arxiv.org/abs/2606.05606)
  LLM post-training often relies on reinforcement learning methods that sample multiple rollouts per prompt, yet most existing approaches use a fixed rollout budget for every prompt, despite large differences in the training signal different prompts provide. In…
- **Lighthouse RL: Sample-Efficient Circuit Optimization via Strategic Reset Points** (probabilistic-uncertainty/evaluation) — 2026 — [2607.14008](https://arxiv.org/abs/2607.14008)
  In this paper, we introduce Lighthouse RL, a sample-efficient reinforcement learning (RL) approach for analog circuit sizing. Traditional methods lack generalization across different performance targets, while standard RL approaches waste resources exploring…
- **Understanding Diversity Collapse in RLVR via the Lens of Overtraining** (probabilistic-uncertainty/evaluation) — 2026 — [2606.15455](https://arxiv.org/abs/2606.15455)
  Reinforcement learning with verifiable rewards (RLVR) has become a key approach for enhancing the reasoning abilities of large language models. However, RLVR often suffers from diversity collapse: Pass@1 improves while high-k Pass@k degrades, which is viewed…
- **Towards Reliable Zero-Shot Crowd Forecasting: Evaluating Time Series Foundation Models for Special Event Pedestrian Forecasting** (probabilistic-uncertainty/evaluation) — 2026 — [2607.17758](https://arxiv.org/abs/2607.17758)
  Managing massive crowds during infrequent special events requires reliable real-time pedestrian-flow forecasting to ensure public safety and operational efficiency. However, supervised forecasting methods face limitations in these contexts due to scarce…
- **Hierarchical Latent Prediction for Language Models** (probabilistic-uncertainty/evaluation) — 2026 — [2608.05806](https://arxiv.org/abs/2608.05806)
  While standard Next-Token Prediction (NTP) lays the foundation of language model pre- training, its teacher-forced training paradigm may not be optimal for long-horizon reasoning and planning. Recent works such as Multi-Token Prediction (MTP) and Next-Latent…
- **Pruning Strategies for Backdoor Defense in LLMs** (probabilistic-uncertainty/evaluation) — 2025 — [2508.20032](https://arxiv.org/abs/2508.20032)
  Backdoor attacks are a significant threat to the performance and integrity of pre-trained language models. Although such models are routinely fine-tuned for downstream NLP tasks, recent work shows they remain vulnerable to backdoor attacks that survive…
- **Long-Horizon Model-Based Offline Reinforcement Learning Without Explicit Conservatism** (probabilistic-uncertainty/evaluation) — 2025 — [2512.04341](https://arxiv.org/abs/2512.04341)
  Popular offline reinforcement learning (RL) methods rely on explicit conservatism, penalizing out-of-dataset actions or restricting rollout horizons. We question the universality of this principle and revisit a complementary Bayesian perspective for test-time…
- **Small Generalizable Prompt Predictive Models Can Steer Efficient RL Post-Training of Large Reasoning Models** (probabilistic-uncertainty/evaluation) — 2026 — [2602.01970](https://arxiv.org/abs/2602.01970)
  Reinforcement learning enhances the reasoning capabilities of large language models but often involves high computational costs due to rollout-intensive optimization. Online prompt selection presents a plausible solution by prioritizing informative prompts to…
- **Efficient RLVR Training via Weighted Mutual Information Data Selection** (probabilistic-uncertainty/evaluation) — 2026 — [2603.01907](https://arxiv.org/abs/2603.01907)
  Reinforcement learning (RL) plays a central role in improving the reasoning and alignment of large language models, yet its efficiency critically depends on how training data are selected. Existing online selection strategies predominantly rely on…

## 4. Proposed structure

- **H1 — Introduction & gap framing.** Lead with the cell count vs. category size.
- **H2 — Background.** Method/trend anchor + domain (C2/wargaming/simulation).
- **H3 — Taxonomy.** Map existing corpus work; flag the empty quadrant.
- **H4 — Research agenda / contributions.** Concrete proposals tied to the gap.
- **H5 — Evaluation.** Metrics & a reproducible testbed (the evaluation cell is itself thin).
- **H6 — Open challenges & conclusion.**

## 5. Suggested venues

UAI, AISTATS, NeurIPS, ICML, International Journal of Approximate Reasoning

_Generated by scripts-style gap-brief generator from papers.yaml + statistics.json._