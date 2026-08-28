# Article Brief: LLM-Driven Agentic Wargaming

> **Ranked research-gap topic #13** in the C2-AI corpus (11,750 papers, 112 taxonomy cells). Target cell `wargaming/mechanism` = **1 paper(s)**; parent category `wargaming` = 466 papers. Trend anchor: agentic 1.54x.

---

## 1. Thesis

A narrow spin on the #1 gap: wargaming/mechanism has 1 paper while agentic is a top burst (1.54x). This article surveys LLM-driven agentic wargaming — strategy synthesis, scenario generation, and explainable commander agents.

## 2. Gap evidence (from statistics.json)

| Cell | Papers | Note |
|------|------:|------|
| `wargaming/mechanism` | 1 | target cell (gap) |
| `wargaming` (parent) | 466 | evidence base to build on |
| trend anchor | — | agentic 1.54x |

## 3. Seed papers (corpus-grounded)

- **Data analysis of tactical wargaming based on data mining.** (wargaming/mechanism) — 2024 — [https://dblp.org/rec/journals/jcmse/Wu24a](https://dblp.org/rec/journals/jcmse/Wu24a)
- **WGSR-Bench: Wargame-based Game-theoretic Strategic Reasoning Benchmark for Large Language Models** (wargaming/theory) — 2025 — [2506.10264](https://arxiv.org/abs/2506.10264)
  Recent breakthroughs in Large Language Models (LLMs) have led to a qualitative leap in artificial intelligence' s performance on reasoning tasks, particularly demonstrating remarkable capabilities in mathematical, symbolic, and commonsense reasoning. However,…
- **Stable and Expert-Aligned Evaluation of Wargaming Strategies via Optimized LLM Scoring Agents** (wargaming/application) — 2025 — [https://doi.org/10.1109/icmlca66850.2025.11336231](https://doi.org/10.1109/icmlca66850.2025.11336231)
  Wargaming is a simulation tool for strategy analysis and decision-making. As large language models (LLMs) improve, they can generate strategies in simulated wargames, but scalable and reliable…
- **Intelligent Multi-UAV Navigation in ITNTNs: A Hierarchical LLM Approach** (deep-reinforcement-learning/application) — 2026 — [2607.18604](https://arxiv.org/abs/2607.18604)
  The deployment of high-speed Uncrewed Aerial Vehicles (UAVs) in 3D aerial highways necessitates robust coordination of physical flight kinematics and multi-tier network handovers. While Deep Reinforcement Learning (DRL) offers rapid tactical control, it lacks…
- **Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning** (deep-reinforcement-learning/development) — 2026 — [2607.07508](https://arxiv.org/abs/2607.07508)
  Reinforcement learning (RL) is becoming increasingly important for post-training large language models (LLMs). Previous RL pipelines for LLMs were mostly synchronous and batch-interleaved, which is inefficient for long-horizon agentic tasks. Recently,…
- **RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems** (autonomous-decision-making/systems) — 2026 — [2606.23927](https://arxiv.org/abs/2606.23927)
  Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. Existing security evaluations are often tied to specific…
- **Towards Improving Sequential Decision-Making in LLM Agents via Experience Memory** (autonomous-decision-making/development) — 2026 — [2608.03420](https://arxiv.org/abs/2608.03420)
  Large language models have improved substantially on single-shot reasoning tasks, but their performance in sequential decision-making is less well understood. We study this on fully-observable two-player zero-sum games, which provide ground-truth evaluation:…
- **SciDataSailor: Deep Scientific Data Exploring** (autonomous-decision-making/development) — 2026 — [2607.28098](https://arxiv.org/abs/2607.28098)
  Scientific datasets are commonly organized as hierarchical repositories containing heterogeneous and interdependent files, making their inspection, integration, and analysis labor-intensive and reliant on domain expertise. Although large language model (LLM)…
- **Solvita: Enhancing Large Language Models for Competitive Programming via Agentic Evolution** (multi-agent-rl/development) — 2026 — [2605.15301](https://arxiv.org/abs/2605.15301)
  Large language models (LLMs) still struggle with the rigorous reasoning demands of hard competitive programming. While recent multi-agent frameworks attempt to bridge this reliability gap, they remain fundamentally stateless: they rely on static retrieval and…
- **Cattle Trade: A Multi-Agent Benchmark for LLM Bluffing, Bidding, and Bargaining** (opponent-modeling/application) — 2026 — [2605.14537](https://arxiv.org/abs/2605.14537)
  We introduce \textsc{Cattle Trade, a multi-agent benchmark for evaluating large language models (LLMs) as agents in strategic reasoning under imperfect information, adversarial interaction, and resource constraints. The benchmark combines auctions,…

## 4. Proposed structure

- **H1 — Introduction & gap framing.** Lead with the cell count vs. category size.
- **H2 — Background.** Method/trend anchor + domain (C2/wargaming/simulation).
- **H3 — Taxonomy.** Map existing corpus work; flag the empty quadrant.
- **H4 — Research agenda / contributions.** Concrete proposals tied to the gap.
- **H5 — Evaluation.** Metrics & a reproducible testbed (the evaluation cell is itself thin).
- **H6 — Open challenges & conclusion.**

## 5. Suggested venues

IEEE CIG/CoG, I/ITSEC, ACL (agent workshops), AAAI

_Generated by scripts-style gap-brief generator from papers.yaml + statistics.json._