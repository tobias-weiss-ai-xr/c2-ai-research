# Article Brief: Benchmark Suites for Wargaming AI

> **Ranked research-gap topic #2** in the C2-AI corpus (11,750 papers, 112 taxonomy cells). Target cell `wargaming/evaluation` = **2 paper(s)**; parent category `wargaming` = 466 papers. Trend anchor: benchmark 1.51x (#1 keyword).

---

## 1. Thesis

Wargaming has 466 corpus papers but only 2 in the evaluation cell and no shared benchmark. This article proposes a taxonomy of wargaming benchmarks and a reference testbed, porting the evaluation culture that is exploding elsewhere (benchmark is the single most-bursting keyword, 1.51x) into the wargaming domain.

## 2. Gap evidence (from statistics.json)

| Cell | Papers | Note |
|------|------:|------|
| `wargaming/evaluation` | 2 | target cell (gap) |
| `wargaming` (parent) | 466 | evidence base to build on |
| trend anchor | — | benchmark 1.51x (#1 keyword) |

## 3. Seed papers (corpus-grounded)

- **Guarding against malicious biased threats (GAMBiT) datasets: Revealing cognitive bias in human-subjects red-team cyber range operations.** (wargaming/evaluation) — 2026 — [https://doi.org/10.1016/j.dib.2026.112476](https://doi.org/10.1016/j.dib.2026.112476)
  We present datasets from three large-scale human-subject experiments involving red-team hacking in a cyber range in the Guarding Against Malicious Biased Threats (GAMBiT) project. Across Experiments 1-3 (July 2024-March 2025), 19-20 skilled attackers per…
- **Hardening the First Island Chain? a Wargaming Assessment of U.S. Forward Base Resilience under the 2025 National Security Strategy** (wargaming/evaluation) — 2026 — [https://doi.org/10.5281/zenodo.20282337](https://doi.org/10.5281/zenodo.20282337)
  Dataset for article "Hardening the First Island Chain? a Wargaming Assessment of U.S. Forward Base Resilience under the 2025 National Security Strategy" presented on June 6 2026 in Osaka at Workshop…
- **WGSR-Bench: Wargame-based Game-theoretic Strategic Reasoning Benchmark for Large Language Models** (wargaming/theory) — 2025 — [2506.10264](https://arxiv.org/abs/2506.10264)
  Recent breakthroughs in Large Language Models (LLMs) have led to a qualitative leap in artificial intelligence' s performance on reasoning tasks, particularly demonstrating remarkable capabilities in mathematical, symbolic, and commonsense reasoning. However,…
- **CalBench: Evaluating Coordination-Privacy Trade-offs in Multi-Agent LLMs** (multi-agent-rl/application) — 2026 — [2605.09823](https://arxiv.org/abs/2605.09823)
  Personal AI assistants are beginning to act as delegates with access to calendars, inboxes, and user preferences. Calendar scheduling makes the trust problem concrete: an assistant must coordinate with other assistants while deciding what to reveal about the…
- **α^3-SecBench: A Large-Scale Evaluation Suite of Security, Resilience, and Trust for LLM-based UAV Agents over 6G Networks** (autonomous-decision-making/application) — 2026 — [2601.18754](https://arxiv.org/abs/2601.18754)
  Autonomous unmanned aerial vehicle (UAV) systems are increasingly deployed in safety-critical, networked environments where they must operate reliably in the presence of malicious adversaries. While recent benchmarks have evaluated large language model…
- **Probing Dec-POMDP Reasoning in Cooperative MARL** (multi-agent-rl/theory) — 2026 — [2602.20804](https://arxiv.org/abs/2602.20804)
  Cooperative multi-agent reinforcement learning (MARL) is typically framed as a decentralised partially observable Markov decision process (Dec-POMDP), a setting whose hardness stems from two key challenges: partial observability and decentralised…
- **AVBench: Human-Aligned and Automated Evaluation Benchmark for Audio-Video Generative Models** (human-ai-teaming/application) — 2026 — [2605.24652](https://arxiv.org/abs/2605.24652)
  Rapid advances in audio-video (AV) generation have enabled high-fidelity synthesis with synchronized sound, particularly for human-related scenarios involving speech and interactions. Yet evaluation for AV generation remains at an early stage, with only a few…
- **UAVBench: An Open Benchmark Dataset for Autonomous and Agentic AI UAV Systems via LLM-Generated Flight Scenarios** (autonomous-decision-making/application) — 2025 — [2511.11252](https://arxiv.org/abs/2511.11252)
  Autonomous aerial systems increasingly rely on large language models (LLMs) for mission planning, perception, and decision-making, yet the lack of standardized and physically grounded benchmarks limits systematic evaluation of their reasoning capabilities. To…
- **HLSMAC: A New StarCraft Multi-Agent Challenge for High-Level Strategic Decision-Making** (autonomous-decision-making/systems) — 2025 — [2509.12927](https://arxiv.org/abs/2509.12927)
  Benchmarks are crucial for assessing multi-agent reinforcement learning (MARL) algorithms. While StarCraft II-related environments have driven significant advances in MARL, existing benchmarks like SMAC focus primarily on micromanagement, limiting…
- **CAMAR: Continuous Actions Multi-Agent Routing** (multi-agent-rl/development) — 2025 — [2508.12845](https://arxiv.org/abs/2508.12845)
  Multi-agent reinforcement learning (MARL) is a powerful paradigm for solving cooperative and competitive decision-making problems. While many MARL benchmarks have been proposed, few combine continuous state and action spaces with challenging coordination and…

## 4. Proposed structure

- **H1 — Introduction & gap framing.** Lead with the cell count vs. category size.
- **H2 — Background.** Method/trend anchor + domain (C2/wargaming/simulation).
- **H3 — Taxonomy.** Map existing corpus work; flag the empty quadrant.
- **H4 — Research agenda / contributions.** Concrete proposals tied to the gap.
- **H5 — Evaluation.** Metrics & a reproducible testbed (the evaluation cell is itself thin).
- **H6 — Open challenges & conclusion.**

## 5. Suggested venues

IEEE CIG/CoG, I/ITSEC, Journal of Defense Modeling and Simulation, IEEE Transactions on Games

_Generated by scripts-style gap-brief generator from papers.yaml + statistics.json._