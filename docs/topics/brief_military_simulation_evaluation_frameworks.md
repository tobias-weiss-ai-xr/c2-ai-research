# Article Brief: Military-Simulation Evaluation Frameworks

> **Ranked research-gap topic #8** in the C2-AI corpus (11,750 papers, 112 taxonomy cells). Target cell `military-simulation/evaluation` = **5 paper(s)**; parent category `military-simulation` = 464 papers. Trend anchor: evaluation 1.36x; simulation 1.20x.

---

## 1. Thesis

Military simulation has 464 papers, 80% recent in its evaluation cell, but only 5 evaluation papers. This article proposes an evaluation taxonomy and framework for military simulation AI, extending the canonical military-simulation assessment taxonomy.

## 2. Gap evidence (from statistics.json)

| Cell | Papers | Note |
|------|------:|------|
| `military-simulation/evaluation` | 5 | target cell (gap) |
| `military-simulation` (parent) | 464 | evidence base to build on |
| trend anchor | — | evaluation 1.36x; simulation 1.20x |

## 3. Seed papers (corpus-grounded)

- **Continuous-time Optimal Stopping through Deep Reinforcement Learning** (military-simulation/evaluation) — 2026 — [2606.17545](https://arxiv.org/abs/2606.17545)
  Simulation based solvers for optimal stopping problems must discretize the stopping decision. Under classical dynamic programming, a coarse exercise grid with only a few stopping opportunities can materially undervalue the optimal expected reward, whereas on…
- **ACCoRD: Actor-Critic Conflict Resolution with Deep learning for O-RAN xApps** (military-simulation/evaluation) — 2026 — [2605.22306](https://arxiv.org/abs/2605.22306)
  Conflict Mitigation (ConMit) is a crucial part of intelligent network control in Open Radio Access Networks (O-RAN). In this paper, we propose a method named ACCoRD to resolve detected control conflicts in Near-Real Time RAN Intelligent Controller using a…
- **Reinforcement Learning for LLM-based Event Forecasting** (military-simulation/evaluation) — 2026 — [2606.15917](https://arxiv.org/abs/2606.15917)
  We use Group Relative Policy Optimization (GRPO), a recently devised sample and memory efficient reinforcement learning method, to finetune pretrained LLMs in the range of 1.5B to 14B parameters equipped with the ability to get current information through the…
- **Towards Context-Aware Human-like Pointing Gestures with RL Motion Imitation** (military-simulation/evaluation) — 2025 — [2509.12880](https://arxiv.org/abs/2509.12880)
  Pointing is a key mode of interaction with robots, yet most prior work has focused on recognition rather than generation. We present a motion capture dataset of human pointing gestures covering diverse styles, handedness, and spatial targets. Using…
- **From discrete-time policies to continuous-time diffusion samplers: Asymptotic equivalences and faster training** (military-simulation/evaluation) — 2025 — [2501.06148](https://arxiv.org/abs/2501.06148)
  We study the problem of training neural stochastic differential equations, or diffusion models, to sample from a Boltzmann distribution without access to target samples. Existing methods for training such models enforce time-reversal of the generative and…
- **On the Evaluation of Military Simulations: Towards A Taxonomy of Assessment Criteria** (military-simulation/application) — 2020 — [2004.09340](https://arxiv.org/abs/2004.09340)
  In the area of military simulations, a multitude of different approaches is available. Close Combat Tactical Trainer, Joint Tactical Combat Training System, Battle Force Tactical Training or Warfighter's Simulation 2000 are just some examples within the…
- **Xiaomi-GUI-0 Technical Report** (military-simulation/application) — 2026 — [2606.31410](https://arxiv.org/abs/2606.31410)
  Graphical user interface (GUI) agents build on vision-language models to complete user tasks end-to-end in real applications through interface actions such as tapping, swiping, text entry, and navigation. However, existing GUI agents are trained and evaluated…
- **Measure the Sim-to-Real Gap: Designing an Affordable Real-World Benchmark Platform for Reinforcement Learning in AIoT Systems** (military-simulation/application) — 2026 — [2607.10309](https://arxiv.org/abs/2607.10309)
  Reinforcement learning (RL) is commonly employed to enhance the performance of autonomous systems, including the Autonomous Internet of Things (AIoT). However, the trial-and-error nature of RL, when conducted in real-world environments, is costly and…
- **One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents** (military-simulation/application) — 2026 — [2605.23652](https://arxiv.org/abs/2605.23652)
  On a 300-persona life-simulation benchmark, pcsp achieves compositional zero-shot persona identification up to 17x above chance, Spearman rho approx 0.73 semantic-behavioral alignment, and 22x faster inference than an LLM-as-policy baseline. Life simulation…
- **PHREEQC-MCQ-200: A Diagnostic Benchmark for Tool-Augmented Scientific Simulator Agents** (military-simulation/systems) — 2026 — [2607.00436](https://arxiv.org/abs/2607.00436)
  Large language model agents are increasingly connected to scientific software, yet it remains unclear when tool access makes scientific computation more reliable rather than merely more complex. We introduce PHREEQC-MCQ-200, a benchmark for evaluating…

## 4. Proposed structure

- **H1 — Introduction & gap framing.** Lead with the cell count vs. category size.
- **H2 — Background.** Method/trend anchor + domain (C2/wargaming/simulation).
- **H3 — Taxonomy.** Map existing corpus work; flag the empty quadrant.
- **H4 — Research agenda / contributions.** Concrete proposals tied to the gap.
- **H5 — Evaluation.** Metrics & a reproducible testbed (the evaluation cell is itself thin).
- **H6 — Open challenges & conclusion.**

## 5. Suggested venues

Journal of Defense Modeling and Simulation, I/ITSEC, SPIE Defense+Security, Simulation

_Generated by scripts-style gap-brief generator from papers.yaml + statistics.json._