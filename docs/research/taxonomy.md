# C2-AI Research — 14×8 Taxonomy

Every paper in the corpus is classified along two orthogonal axes: a **category**
(research discipline) and an **aspect** (research activity). Together they form a
14×8 = 112-cell taxonomy.

## Categories

| Key | Label | Focus |
|-----|-------|-------|
| `autonomous-decision-making` | Autonomous Decision-Making | End-to-end perception → decision → action pipelines for autonomous agents |
| `deep-reinforcement-learning` | Deep Reinforcement Learning | DRL algorithms: value/policy/gradient methods, stabilisation, exploration |
| `multi-agent-rl` | Multi-Agent Reinforcement Learning | Cooperative, competitive, mixed-motive learning among multiple agents |
| `opponent-modeling` | Opponent & Cognitive Modeling | Inferring adversary intent/serials; game-theoretic & behavioural models |
| `hierarchical-planning` | Hierarchical Planning | Task & option hierarchies, curriculum, plan abstraction |
| `military-simulation` | Military Simulation | Simulators, physics/wargame engines, entity-level & engagement models |
| `wargaming` | Wargaming | Red-vs-blue diplomacy, scenario design, adjudication |
| `command-and-control` | Command & Control (C2) | C2 architectures, human-in-the-loop, situational awareness |
| `decision-support` | Decision Support | Tools & models that augment human decisions under workload |
| `mathematical-optimization` | Mathematical Optimization | Convex/SOC programming, DP connections to RL, combinatorial planning |
| `probabilistic-uncertainty` | Probabilistic & Uncertainty Reasoning | Bayesian models, belief states, robust decision-making |
| `mission-planning` | Mission Planning | Task allocation, routing, scheduling of resources |
| `human-ai-teaming` | Human–AI Teaming | Trust, explainability, shared autonomy, mixed-initiative control |
| `sim-to-real` | Simulation-to-Reality Transfer | Domain randomisation, sim-to-sim & sim-to-real transfer |

## Aspects (Subcategories)

| Key | Label |
|-----|-------|
| `theory` | Theory |
| `mechanism` | Mechanism |
| `method` | Method |
| `application` | Application |
| `development` | Development |
| `systems` | Systems & Technology |
| `evaluation` | Evaluation & Benchmarks |
| `review` | Reviews & Surveys |

## Conventions

- Categories and aspects are lowercase `kebab-case` keys; labels are human‑friendly.
- One paper = exactly one category + one aspect.
- New categories/relations must be added to `scripts/domain.py` **and** mirrored in
  `scripts/validate_papers.py` so the whole pipeline stays consistent.
- Gaps (empty cells) are first-class outputs: see `docs/research/research_gaps.md`.