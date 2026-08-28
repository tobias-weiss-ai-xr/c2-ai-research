# Article Brief: Mission-Planning Evaluation Benchmarks

> **Ranked research-gap topic #5** in the C2-AI corpus (11,750 papers, 112 taxonomy cells). Target cell `mission-planning/evaluation` = **3 paper(s)**; parent category `mission-planning` = 490 papers. Trend anchor: evaluation 1.36x.

---

## 1. Thesis

Mission planning has 490 corpus papers but only 3 in evaluation. This article proposes standardized mission-planning benchmarks and scoring protocols for autonomous task/route planning under constraints.

## 2. Gap evidence (from statistics.json)

| Cell | Papers | Note |
|------|------:|------|
| `mission-planning/evaluation` | 3 | target cell (gap) |
| `mission-planning` (parent) | 490 | evidence base to build on |
| trend anchor | — | evaluation 1.36x |

## 3. Seed papers (corpus-grounded)

- **DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale** (mission-planning/evaluation) — 2026 — [2604.00813](https://arxiv.org/abs/2604.00813)
  End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilitate planning. In this paper, we propose…
- **Bounomodes: the grazing ox algorithm for exploration of clustered anomalies** (mission-planning/evaluation) — 2025 — [2507.06960](https://arxiv.org/abs/2507.06960)
  A common class of algorithms for informative path planning (IPP) follows boustrophedon ("as the ox turns") patterns, which aim to achieve uniform area coverage. However, IPP is often applied in scenarios where anomalies, such as plant diseases, pollution, or…
- **UEVAVD: A Dataset for Developing UAV's Eye View Active Object Detection** (mission-planning/evaluation) — 2024 — [2411.04348](https://arxiv.org/abs/2411.04348)
  Occlusion is a longstanding difficulty that challenges the UAV-based object detection. Many works address this problem by adapting the detection model. However, few of them exploit that the UAV could fundamentally improve detection performance by changing its…
- **SKYSURF: A Self-learning Framework for Persistent Surveillance using Cooperative Aerial Gliders** (mission-planning/application) — 2026 — [2602.12838](https://arxiv.org/abs/2602.12838)
  The success of surveillance applications involving small unmanned aerial vehicles (UAVs) depends on how long the limited on-board power would persist. To cope with this challenge, alternative renewable sources of lift are sought. One promising solution is to…
- **Adapting Reinforcement Learning for Path Planning in Constrained Parking Scenarios** (mission-planning/application) — 2026 — [2601.22545](https://arxiv.org/abs/2601.22545)
  Real-time path planning in constrained environments remains a fundamental challenge for autonomous systems. Traditional classical planners, while effective under perfect perception assumptions, are often sensitive to real-world perception constraints and rely…
- **Path Planning Using Deep Deterministic Policy Gradient: A Reinforcement Learning Approach** (mission-planning/application) — 2026 — [2606.07855](https://arxiv.org/abs/2606.07855)
  Path-planning for autonomous vehicles in threat-laden environments is a fundamental challenge because the problem is nonlinear and nonconvex even in simplest scenarios. While traditional optimal control methods can be used to find ideal paths, the…
- **PEACE: A Planner-Executor Agent with Constraint Enforcement for UAVs** (mission-planning/application) — 2026 — [2606.00104](https://arxiv.org/abs/2606.00104)
  Foundation models are increasingly used to drive autonomous systems, yet existing approaches either keep the model in a tight control loop, raising latency and hallucination risk, or compile natural language into opaque end-to-end policies that are hard to…
- **Think Like a Pilot: Fine-Grained Long-Horizon UAV Navigation** (mission-planning/application) — 2026 — [2606.06836](https://arxiv.org/abs/2606.06836)
  Language-guided UAV agents must execute long-horizon semantic instructions while producing smooth, physically feasible continuous flight commands, yet existing Vision-Language Navigation (VLN) benchmarks typically use discrete or coarse actions and existing…
- **Benchmarking Empirical and Learning-Based Approaches for Feedforward Steering Control in Autonomous Racing** (mission-planning/application) — 2026 — [2605.21111](https://arxiv.org/abs/2605.21111)
  Feedforward steering control is a key component of hierarchical control architectures for autonomous racing. The goal is to reduce steering corrections from the feedback controllers by predicting the vehicle's inverse lateral dynamics. This paper presents a…
- **Optimizing Mission Planning for Multi-Debris Rendezvous Using Reinforcement Learning with Refueling and Adaptive Collision Avoidance** (mission-planning/application) — 2026 — [2602.05075](https://arxiv.org/abs/2602.05075)
  As the orbital environment around Earth becomes increasingly crowded with debris, active debris removal (ADR) missions face significant challenges in ensuring safe operations while minimizing the risk of in-orbit collisions. This study presents a…

## 4. Proposed structure

- **H1 — Introduction & gap framing.** Lead with the cell count vs. category size.
- **H2 — Background.** Method/trend anchor + domain (C2/wargaming/simulation).
- **H3 — Taxonomy.** Map existing corpus work; flag the empty quadrant.
- **H4 — Research agenda / contributions.** Concrete proposals tied to the gap.
- **H5 — Evaluation.** Metrics & a reproducible testbed (the evaluation cell is itself thin).
- **H6 — Open challenges & conclusion.**

## 5. Suggested venues

IEEE ICUAS, AAMAS, IJCAI, Autonomous Agents and Multi-Agent Systems, IEEE Access

_Generated by scripts-style gap-brief generator from papers.yaml + statistics.json._