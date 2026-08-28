# Article Brief: Sim-to-Real Transfer Benchmarks for Military/Robotics

> **Ranked research-gap topic #4** in the C2-AI corpus (11,750 papers, 112 taxonomy cells). Target cell `sim-to-real/evaluation` = **7 paper(s)**; parent category `sim-to-real` = 742 papers. Trend anchor: domain randomization 1.55x; sim-to-real hottest category (159.6% growth).

---

## 1. Thesis

Sim-to-real is the fastest-growing category (159.6%) yet its evaluation cell has only 7 papers (86% recent). This article frames reproducible transfer benchmarks for military and robotics simulators, centering domain randomization and sim-to-sim gaps.

## 2. Gap evidence (from statistics.json)

| Cell | Papers | Note |
|------|------:|------|
| `sim-to-real/evaluation` | 7 | target cell (gap) |
| `sim-to-real` (parent) | 742 | evidence base to build on |
| trend anchor | — | domain randomization 1.55x; sim-to-real hottest category (159.6% growth) |

## 3. Seed papers (corpus-grounded)

- **Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models** (sim-to-real/evaluation) — 2026 — [2607.04546](https://arxiv.org/abs/2607.04546)
  Action-conditioned world models allow robots to predict the future consequences of candidate actions without additional physical interaction, supporting policy evaluation, planning, and data augmentation. We present Mask2Real-WM, a two-stage…
- **Cross-Embodiment Transfer via Behavior-Aligned Representations** (sim-to-real/evaluation) — 2026 — [2607.27549](https://arxiv.org/abs/2607.27549)
  Recent progress in large-scale imitation learning for robot manipulation has been driven by leveraging datasets across a wide range of robot embodiments. However, achieving significant cross-embodiment transfer is often still challenging. In this work, we…
- **3D Point World Models: Point Completion Enables More Accurate Dynamics Learning** (sim-to-real/evaluation) — 2026 — [2607.00148](https://arxiv.org/abs/2607.00148)
  Learning predictive models of the world enables robotic control through planning, potentially allowing robots to improvise solutions on new tasks. However, large video-based dynamics models lack explicit 3D spatial structure and suffer from geometrically…
- **Geometric Action Model for Robot Policy Learning** (sim-to-real/evaluation) — 2026 — [2606.17046](https://arxiv.org/abs/2606.17046)
  Generalist robot policies must follow user instructions while reasoning about how objects, cameras, and robot actions interact in the 3D physical world. Recent vision-language-action models (VLAs) and video world-action models (WAMs) inherit strong semantic…
- **Equivalence and Divergence of Bayesian Log-Odds and Dempster's Combination Rule for 2D Occupancy Grids** (sim-to-real/evaluation) — 2026 — [2602.18872](https://arxiv.org/abs/2602.18872)
  We introduce a pignistic-transform-based methodology for fair comparison of Bayesian log-odds and Dempster's combination rule in occupancy grid mapping, matching per-observation decision probabilities to isolate the fusion rule from sensor parameterization.…
- **DROPO: Sim-to-real transfer with offline domain randomization** (sim-to-real/evaluation) — 2023 — [https://doi.org/10.1016/j.robot.2023.104432](https://doi.org/10.1016/j.robot.2023.104432)
  In recent years, domain randomization over dynamics parameters has gained a lot of traction as a method for sim-to-real transfer of reinforcement learning policies in robotic manipulation; however,…
- **Reinforcement Learning Integration in Vision-Language-Action Models for Sim-to-Real Transfer** (sim-to-real/evaluation) — 2026 — [https://doi.org/10.5281/zenodo.20577236](https://doi.org/10.5281/zenodo.20577236)
  This report synthesises findings from 3 peer-reviewed papers addressing the following research question: Can the integration of reinforcement learning with vision-language-action models improve…
- **DexSim2Real: Foundation Model-Guided Sim-to-Real Transfer for Generalizable Dexterous Manipulation** (sim-to-real/application) — 2026 — [2605.05241](https://arxiv.org/abs/2605.05241)
  Sim-to-real transfer remains a critical bottleneck for deploying dexterous manipulation policies learned in simulation to real-world robots. Existing approaches rely on manually designed domain randomization or task-specific adaptation, limiting their…
- **Grounding Sim-to-Real Generalization in Robotic Manipulation: An Empirical Study with Vision-Language-Action Models** (sim-to-real/application) — 2026 — [2603.22876](https://arxiv.org/abs/2603.22876)
  Learning a generalist control policy for robotic manipulation typically relies on large-scale datasets. Given the high cost of real-world data collection, a practical alternative is to generate synthetic data through simulation. However, the resulting…
- **Benchmarking Sim2Real Gap: High-fidelity Digital Twinning of Agile Manufacturing** (sim-to-real/application) — 2024 — [2409.10784](https://arxiv.org/abs/2409.10784)
  As the manufacturing industry shifts from mass production to mass customization, there is a growing emphasis on adopting agile, resilient, and human-centric methodologies in line with the directives of Industry 5.0. Central to this transformation is the…

## 4. Proposed structure

- **H1 — Introduction & gap framing.** Lead with the cell count vs. category size.
- **H2 — Background.** Method/trend anchor + domain (C2/wargaming/simulation).
- **H3 — Taxonomy.** Map existing corpus work; flag the empty quadrant.
- **H4 — Research agenda / contributions.** Concrete proposals tied to the gap.
- **H5 — Evaluation.** Metrics & a reproducible testbed (the evaluation cell is itself thin).
- **H6 — Open challenges & conclusion.**

## 5. Suggested venues

CoRL, ICRA, IROS, IEEE Robotics and Automation Letters, RSS

_Generated by scripts-style gap-brief generator from papers.yaml + statistics.json._