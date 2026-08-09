# C2-AI Research — Literature Review

**Generated:** 2026-08-10  
**Corpus:** 6,081 papers across 14 categories

> Synthesis of the autonomous decision-making & deep-RL research corpus. Category insights are drawn from title/abstract analysis of the papers themselves.

---

## Corpus Overview

| Rank | Category | Papers |
|------|----------|--------|
| 1 | Human–AI Teaming | 1721 |
| 2 | Deep Reinforcement Learning | 988 |
| 3 | Autonomous Decision-Making | 582 |
| 4 | Multi-Agent Reinforcement Learning | 448 |
| 5 | Simulation-to-Reality Transfer | 425 |

**Time span:** 2017–2026 (median year 2022)
**Dominant aspects:** Application (1692), Development (1526), Theory (1106)

---

## 📈 Research Momentum (Last 12 Months)

Categories ranked by a momentum score combining recent output density with year-over-year growth.

| Category | Total | Last 12m | Prior 12m | Growth | 12-m share | Papers/mo |
|----------|------:|---------:|----------:|-------:|----------:|----------:|
| Command & Control (C2) | 361 | 165 | 58 | +184.5% | 46% | 13.8 |
| Opponent & Cognitive Modeling | 165 | 165 | 0 | — | 100% | 13.8 |
| Wargaming | 4 | 4 | 0 | — | 100% | 0.3 |
| Probabilistic & Uncertainty Reasoning | 328 | 328 | 0 | — | 100% | 27.3 |
| Mission Planning | 145 | 145 | 0 | — | 100% | 12.1 |
| Simulation-to-Reality Transfer | 425 | 425 | 0 | — | 100% | 35.4 |
| Autonomous Decision-Making | 582 | 581 | 0 | — | 100% | 48.4 |
| Decision Support | 403 | 402 | 0 | — | 100% | 33.5 |
| Deep Reinforcement Learning | 988 | 984 | 0 | — | 100% | 82.0 |
| Multi-Agent Reinforcement Learning | 448 | 446 | 0 | — | 100% | 37.2 |
| Mathematical Optimization | 259 | 258 | 0 | — | 100% | 21.5 |
| Hierarchical Planning | 127 | 126 | 0 | — | 99% | 10.5 |
| Military Simulation | 125 | 124 | 0 | — | 99% | 10.3 |
| Human–AI Teaming | 1721 | 673 | 446 | +50.9% | 39% | 56.1 |

---

## 🕳️ Research Gaps & White Space

**Thinnest taxonomy cells:**

| Cell | Papers |
|------|--------|
| `wargaming/theory` | 1 |
| `wargaming/review` | 1 |
| `command-and-control/evaluation` | 1 |
| `mission-planning/method` | 1 |
| `mission-planning/evaluation` | 1 |
| `multi-agent-rl/review` | 2 |
| `wargaming/application` | 2 |
| `mathematical-optimization/review` | 2 |

**White-space cells** (low total but fast-growing):

| Cell | Total | Last-12m | 12-m share |
|------|-------:|---------:|-----------:|
| `autonomous-decision-making/mechanism` | 24 | 24 | 100% |
| `opponent-modeling/application` | 23 | 23 | 100% |
| `hierarchical-planning/application` | 23 | 23 | 100% |
| `mission-planning/development` | 23 | 23 | 100% |
| `mathematical-optimization/systems` | 22 | 22 | 100% |
| `autonomous-decision-making/method` | 21 | 21 | 100% |
| `mission-planning/theory` | 20 | 20 | 100% |
| `hierarchical-planning/theory` | 19 | 19 | 100% |

---


## Category Insights

### Human–AI Teaming (`human-ai-teaming`)

Trust, explainability and mixed-initiative control are the acceptance criteria — an autonomous system that no human trusts is not deployable.

**Corpus size:** 1721 papers

**Papers:**

- [2026-08] Securing Agentic AI: From Per-Action Checks to Trajectory Assurance — https://arxiv.org/abs/2608.01558v1
- [2026-08] Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent — https://arxiv.org/abs/2608.03979v1
- [2026-08] SCP-NL2TL: Selective Conformal Prediction with Semantic Verification for Natural Language to Tempora — https://arxiv.org/abs/2608.05439v1

---

### Deep Reinforcement Learning (`deep-reinforcement-learning`)

DRL is the methodological core of the corpus: value/policy gradients, benchmark algorithms (PPO, DQN/Rainbow) and sample-efficiency methods form the substrate every downstream planning/decision task builds on.

**Corpus size:** 988 papers

**Papers:**

- [2026-08] MA-HEAD-Net: Adaptive Rule-Guided Multi-Agent DRL for AoI Minimization in UAV-Assisted Emergency Net — https://arxiv.org/abs/2608.01128v1
- [2026-08] Analytic Planning under Uncertainty with Moment Closure — https://arxiv.org/abs/2608.02519v1
- [2026-08] Trident : How to Break Deep Reinforcement Learning Cyber Defenses (Agentic) — https://arxiv.org/abs/2608.04317v1

---

### Autonomous Decision-Making (`autonomous-decision-making`)

End-to-end perception-then-action pipelines (e.g. decision transformers, MCTS planners) encode the target capability for autonomous planning and decision-making in high-stakes, partially structured environments.

**Corpus size:** 582 papers

**Papers:**

- [2026-08] Seeing Is Not Deciding: Can Multimodal LLMs Act as Effective CEOs? — https://arxiv.org/abs/2608.05864v1
- [2026-08] OPERA: Operator-residual feedback for reliable autonomous optical experiments with language-model ag — https://arxiv.org/abs/2608.05990v1
- [2026-08] From AI Technical Debt to Agentic Technical Debt: A Systematic Mapping of Root Causes and Manifestat — https://arxiv.org/abs/2608.01001v1

---

### Multi-Agent Reinforcement Learning (`multi-agent-rl`)

Cooperative/competitive multi-agent RL is the bridge from single-agent learning to unit/force-level coordination — the core of adversarial and maneuver scenarios in simulation.

**Corpus size:** 448 papers

**Papers:**

- [2026-08] History Matters: Meta-policy Delegation with Heterogeneous Multi-agent Reinforcement Learning — https://arxiv.org/abs/2608.03833v1
- [2026-08] Is Inter-Seed Cross-Play Enough? Evaluating the Robustness of Zero-Shot Coordination Algorithms to I — https://arxiv.org/abs/2608.03644v1
- [2026-08] Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity in Multi-Ag — https://arxiv.org/abs/2608.03648v1

---

### Simulation-to-Reality Transfer (`sim-to-real`)

Domain randomization and sim-to-sim/sim-to-real transfer are the mechanisms that make policies learned in simulations usable on real systems.

**Corpus size:** 425 papers

**Papers:**

- [2026-08] Bridging the Sim-to-Real Gap in Parallel-Link Leg Mechanisms via Simulator-Side Dynamics Normalizati — https://arxiv.org/abs/2608.01697v2
- [2026-08] TRACE: Learned Proprioceptive Odometry for Legged Robots under Unreliable Contact Conditions — https://arxiv.org/abs/2608.05975v1
- [2026-08] RORA: Realistic Object Reconstruction with Articulation — https://arxiv.org/abs/2608.04842v1

---

### Decision Support (`decision-support`)

Decision support fuses statistics, ML and optimization to augment human decisions — explicitly including recommendation and interpretability for warfighters and operators.

**Corpus size:** 403 papers

**Papers:**

- [2026-08] Neuro-Symbolic Participation Governance for Verifiable AI Agents in Open Digital Twin Ecosystems — https://arxiv.org/abs/2608.00937v1
- [2026-08] Stability of Ranking-dependent Pair-wise Comparison Patterns in the Analytic Hierarchy Process — https://arxiv.org/abs/2608.05958v1
- [2026-08] Predictive Maintenance: Deep Learning-Based Remaining Useful Life Prediction for Combat Aircraft Eng — https://arxiv.org/abs/2608.01819v1

---

### Command & Control (C2) (`command-and-control`)

C2 research connects autonomy to human-machine teaming, situational awareness and decision support at the operational seam between computation and command.

**Corpus size:** 361 papers

**Papers:**

- [2026-07] Cyber-Capable AI Agents: Vulnerabilities, Evaluation Containment, and Defensive Response — https://arxiv.org/abs/2607.25379v2
- [2026-07] Clinical Translation of Brain-Computer Interface in China: A Landscape Analysis of Investigator-Init — https://arxiv.org/abs/2607.07185v3
- [2026-07] FleetScape: A Mixed Reality Sandtable for Spatial Supervision and Control of Scalable Drone Fleets — https://arxiv.org/abs/2607.26423v1

---

### Probabilistic & Uncertainty Reasoning (`probabilistic-uncertainty`)

Bayesian, POMDP and uncertainty-quantified reasoning is essential where observation is partial and risk must be quantified before committing to an action.

**Corpus size:** 328 papers

**Papers:**

- [2026-08] AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning — https://arxiv.org/abs/2608.05987v1
- [2026-08] ReBRAC-v2: The Return of the King — https://arxiv.org/abs/2608.01205v1
- [2026-08] Reward Structure Shapes the Interaction Between Episodic Exploration and Neural Memory in Reinforcem — https://arxiv.org/abs/2608.05111v1

---

### Mathematical Optimization (`mathematical-optimization`)

Constrained/convex/DP optimization is the formal bridge between RL objectives and provable mission-planning guarantees.

**Corpus size:** 259 papers

**Papers:**

- [2026-08] Heterogeneous Multi-Agent Reinforcement Learning for Radio Resource Management under Coupled Finite- — https://arxiv.org/abs/2608.01745v1
- [2026-08] Hybrid-Adaptive Thread Tuning to Mitigate Simulation Execution Bottlenecks in High-Performance Reinf — https://arxiv.org/abs/2608.06025v1
- [2026-08] Generative Optimization for Incentivized Advertising with Global Level Constraints — https://arxiv.org/abs/2608.04421v1

---

### Opponent & Cognitive Modeling (`opponent-modeling`)

Inferring adversary intent and strategy (game theory, adversarial RL, counterfactual regret) is the differentiator for decision support that reasons about an opponent, not just the environment.

**Corpus size:** 165 papers

**Papers:**

- [2026-08] IFlowNets: Extending Generative Samplers to Learn Strategies in Incomplete Information Games — https://arxiv.org/abs/2608.05422v1
- [2026-08] Reputation-driven Cooperation in Lattice-based Decentralized Federated Learning through Evolutionary — https://arxiv.org/abs/2608.01197v1
- [2026-07] Agents That Certify Their Own Exploits: Confidence-Scheduled Restricted Responses for Safe Opponent  — https://arxiv.org/abs/2607.28520v1

---

### Mission Planning (`mission-planning`)

Task allocation, routing, path planning and scheduling are the concrete optimization problems behind an autonomous mission plan.

**Corpus size:** 145 papers

**Papers:**

- [2026-08] Passively Safe Convex Guidance for Cislunar Rendezvous and Proximity Operations — https://arxiv.org/abs/2608.03060v1
- [2026-08] A Forward-Inverse Dynamic Game Framework for Enhanced Multi-Agent Trajectory Planning — https://arxiv.org/abs/2608.01636v1
- [2026-07] End-to-End LLM Flight Planning with RAG-based Memory and Multi-modal Coach Agent — https://arxiv.org/abs/2607.06964v1

---

### Hierarchical Planning (`hierarchical-planning`)

Hierarchical and abductive planning tackles the combinatorial depth of complex operational tasks by decomposing goals into options and sub-plans.

**Corpus size:** 127 papers

**Papers:**

- [2026-08] Beyond Flat Policies: Hierarchical Post-Training for Embodied Agents in Robotic Manipulation — https://arxiv.org/abs/2608.05999v1
- [2026-07] Two-Timescale Hierarchical Reinforcement Learning for Resilient Operations — https://arxiv.org/abs/2607.23434v1
- [2026-07] Hierarchical Soft Actor-Critic for Sparse-Reward Long-Horizon Reinforcement Learning — https://arxiv.org/abs/2607.23726v1

---

### Military Simulation (`military-simulation`)

Simulation environments (constructive, game-engine, entity-level) are the training and test bed for RL in military settings; assessment and fidelity criteria matter as much as the learners themselves.

**Corpus size:** 125 papers

**Papers:**

- [2026-08] Training a Conditioned Video Game Agent on a VLM Annotated Dataset — https://arxiv.org/abs/2608.05954v1
- [2026-07] Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds — https://arxiv.org/abs/2607.18135v1
- [2026-07] Learning Safe Agent Behaviour from Human Preferences and Justifications via World Models — https://arxiv.org/abs/2607.13172v1

---

### Wargaming (`wargaming`)

Red-vs-blue wargaming is the canonical adversarial setting where RL, opponent modeling and optimization collide under realistic scenario constraints.

**Corpus size:** 4 papers

**Papers:**

- [2026-08] No One Wins in Nuclear War: A Social Simulation of Military Decision-making — https://arxiv.org/abs/2608.01868v1
- [2026-08] Steganalysis of Adaptive Covert Collusion in Tool-Using Agent Populations: A Black-Box, Cross-Princi — https://arxiv.org/abs/2608.02698v1
- [2025-11] Superhuman AI for Stratego Using Self-Play Reinforcement Learning and Test-Time Search — https://arxiv.org/abs/2511.07312v1

---

## Methodology

1. Papers are discovered via taxonomy-aware arXiv/OpenAlex queries and auto-classified into the 14×8 taxonomy.
2. Category insights above are editorially curated but grounded in corpus statistics.
3. Regenerate this document with `scripts/analysis/generate_reports.py`.
