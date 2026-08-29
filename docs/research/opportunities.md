# Research Gaps & Business Opportunities

**Generated:** 2026-08 (manual synthesis, grounded in `statistics.json`, `docs/research/*`, and `papers.json`)
**Corpus:** 11,596 papers · 14 categories × 8 aspects = 112 cells (100% saturation)

This document reasons about two things the rest of the repo does not yet connect:
**where the literature is thin (research gaps)** and **where that thinness, plus
the momentum data, points to defensible commercial value (business
opportunities)**. It is deliberately opinionated.

---

## 1. The single most important finding

**The field builds systems but almost never benchmarks them.**

The `evaluation` research aspect is **202 / 11,596 = 1.7%** of the entire corpus —
the thinnest of all eight aspects (next thinnest: `review` at 4.2%; `application`
dominates at 29.6%). This is not a one-off gap; it is *systematic*. Evaluation
volume per category:

| Category | `*/evaluation` papers | Category total | Eval share |
|----------|----------------------:|---------------:|-----------:|
| Deep RL | 54 | 1,737 | 3.1% |
| Human–AI Teaming | 31 | 1,972 | 1.6% |
| Probabilistic & Uncertainty | 17 | 694 | 2.4% |
| Opponent Modeling | 13 | 461 | 2.8% |
| Mathematical Optimization | 15 | 578 | 2.6% |
| Decision Support | 10 | 801 | 1.2% |
| Sim-to-Real | 7 | 742 | 0.9% |
| Hierarchical Planning | 7 | 453 | 1.5% |
| Multi-Agent RL | 9 | 946 | 0.9% |
| **Command & Control** | **5** | 684 | **0.7%** |
| **Military Simulation** | **5** | 464 | **1.1%** |
| **Mission Planning** | **3** | 490 | **0.6%** |
| **Wargaming** | **1** | 433 | **0.2%** |

Every defense-relevant category (C2, military-sim, mission-planning, wargaming)
sits at **≤5 evaluation papers**. The thinnest cells overall are
`wargaming/evaluation` (1), `wargaming/mechanism` (1), `mission-planning/evaluation` (3),
`military-simulation/evaluation` (5), `command-and-control/evaluation` (5).

> **Interpretation:** there is no standardized testbed, benchmark suite, or
> evaluation culture for autonomous C2 / wargaming / mission-planning. That is
> both the #1 research gap *and* the most defensible business wedge (see §3.1).

---

## 2. Research gaps (academic)

### 2.1 Evaluation & benchmarking vacuum (cross-cutting)
- No reproducible benchmarks for C2, wargaming, mission-planning, or
  military-simulation decision policies.
- Even `sim-to-real/evaluation` (7) and `probabilistic-uncertainty/evaluation` (17)
  are tiny despite both being hot (sim-to-real is the #1 momentum cell).
- *White-space with momentum:* `probabilistic-uncertainty/evaluation` (17 papers,
  88% from the last 12 months), `sim-to-real/evaluation` (7, 86%),
  `military-simulation/evaluation` (5, 80%) — emerging but still thin → first-mover
  research advantage for anyone who builds the benchmark *now*.

### 2.2 Scarcity of synthesis (reviews & surveys)
- `review` = 492 (4.2%). Several categories have ≤5 reviews:
  mathematical-optimization/review (5), command-and-control/review (17),
  wargaming/review (12), opponent-modeling/review (11), hierarchical-planning/review (6).
- The field is in rapid expansion with almost no consolidation → high-value
  survey opportunities, especially **"RL for C2: a decade in review"** and
  **"Benchmarks for autonomous military decision-making."**

### 2.3 Structurally thin / cooling categories
- **Wargaming** (433 total) is the shallowest *large* category: application-heavy
  (254) but mechanism=1, evaluation=1, development=7, theory=48. Grew fast
  recently (+7.9% momentum) but depth is hollow.
- **Mission Planning** is *stagnant*: +2.2% momentum and 2026 actuals (87) collapsed
  vs 2025 (226). evaluation=3, review=8. Cooling + under-evaluated.
- **Hierarchical Planning** is the only *negative* momentum (-5.2%). review=6,
  evaluation=7. Arguably oversaturated / consolidating.

### 2.4 Hot themes that lack dedicated treatment
Burst keywords with momentum but no dedicated taxonomy cell:
`agentic` (burst 1.75, 416 papers), `offline` RL (1.34, 465),
`domain randomization` (1.34, 163), `constrained` optimization (853),
`pomdp` (223), `mcts` (115), `adversarial` (497). These are ripe for spin-out
sub-areas / workshops.

### 2.5 Meta-gap: the reporting loop is broken
- `concept_graph_analysis.json` has **5 nodes, 0 edges** — the concept graph
  produces no co-occurrence edges, so the "bridge" cross-cutting signal that
  `tools/topic_planner.py` is supposed to surface is **always 0**.
- The README's **"Research Gaps"** section is an empty placeholder (`—`)
  even though `statistics.json` already contains a `gaps` object. The data
  exists; the regeneration step is missing.

### 2.6 Data-quality caveat (affects both research and any product)
- **71.9% of papers are arXiv preprints** (8,335), not peer-reviewed.
- Author field contains obvious AI-generated / non-person entries:
  `Gemini 3.1 (Flash)` (12 papers), `Chatterbox TTS` (12),
  `Daniel Rosehill` (12). Provenance noise is real and must be filtered before
  any quantitative claim (including this one) is treated as authoritative.

---

## 3. Business opportunities (commercial)

The corpus is themed "military simulation," but the *methods* it catalogs
(RL, optimization, sim-to-real, uncertainty reasoning, decision support) are
broadly dual-use. The venue mix confirms the civilian adjacency:
**IEEE Vehicular Technology, Intelligent Transportation Systems, IoT Journal,
Drones, Applied Energy, Robotics & Automation Letters.** The same algorithms
transfer to mobility, logistics, energy, and industrial autonomy.

### 3.1 Benchmark / testbed-as-a-service for high-stakes autonomy  ★ strongest
- **Gap it exploits:** evaluation is 1.7% of the field and near-zero for
  C2/wargaming/mission-planning (§1).
- **Wedge:** a neutral, reproducible evaluation suite — "MLPerf for command &
  control" — for decision policies in simulation. Defensible via network effects
  (everyone benchmarks on the same suite) and data moats.
- **Buyers:** defense primes, simulation vendors, gov eval labs, and (later)
  autonomous-mobility / robotics companies needing assurance benchmarks.

### 3.2 Sim-to-real / digital-twin transfer tooling
- **Gap it exploits:** #1 momentum cell (score 221.9, +159.6% growth), yet
  `sim-to-real/evaluation` = 7 and `sim-to-real/mechanism` = 10.
- **Wedge:** domain-randomization + transfer tooling, "sim-to-real certification"
  for autonomy. Directly monetizable as SDK/services to robotics & drone firms.

### 3.3 Assured / trustworthy autonomy (regulation-driven)
- **Gap it exploits:** `probabilistic-uncertainty/evaluation` (17, 88% recent),
  `pomdp` (223), `bayesian` (363), `uncertainty` (832) are all surging, but the
  evaluation layer is missing.
- **Wedge:** safety-case / certification tooling for high-risk autonomy
  (EU/US AI acts, defense airworthiness). A compliance-adjacent moat.

### 3.4 Decision-support copilots for high-stakes ops
- **Gap it exploits:** Decision Support is the #2 momentum cell (221.7),
  801 papers, 59% recent, with `benchmark` + `agentic` bursting.
- **Wedge:** operator-facing decision copilots — not just defense, but emergency
  response, logistics dispatch, grid operations. Human–AI teaming (1,972 papers,
  the largest category) supplies the trust/UX literature to build on.

### 3.5 Specialist defense-R&D consultancy (thin-literature = low competition)
- **Gap it exploits:** wargaming / C2 / military-sim are strategically sensitive
  *and* academically thin (§2.3).
- **Wedge:** SBIR / framework-style applied R&D where thin literature means few
  competitors and high willingness-to-pay. The corpus itself is the competitive
  intelligence asset.

### 3.6 Research-intelligence subscription (monetize the pipeline directly)
- This repo's pipeline (arXiv + OpenAlex + Zenodo discovery → momentum/gap/burst
  analysis) is reusable and already auto-generates `ARTICLE_TOPICS.md`,
  briefs, and landscape docs.
- **Wedge:** a "research radar" SaaS for defense/AI R&D teams that tracks
  momentum, white-space, and thin cells on a rolling basis — turning the corpus
  into a continuously-updated intelligence product rather than a static repo.

### 3.7 Agentic literature intelligence / RAG over the corpus
- **Gap it exploits:** `agentic` is the single hottest burst (1.75).
- **Wedge:** an agent that answers "what's the state of the art in X, and where
  are the gaps?" over the 11.6k-paper corpus — the natural productization of the
  `topic_planner` / `brief_generator` tooling already in `tools/`.

---

## 4. Gap → Opportunity map (one line each)

| Research gap | Momentum signal | Business opportunity |
|--------------|-----------------|----------------------|
| No C2/wargaming/mission-planning benchmarks | eval = 1.7% of corpus | Benchmark / testbed-as-a-service (§3.1) |
| Sim-to-real hot but un-evaluated | #1 momentum (221.9) | Transfer / certification tooling (§3.2) |
| Uncertainty surging, no assurance layer | pomdp/bayesian bursting | Trusted-autonomy certification (§3.3) |
| Decision support 2nd-hottest, applied | agentic/benchmark bursting | Decision copilots (§3.4) |
| Wargaming/C2 thin but strategic | small but growing | Specialist defense R&D (§3.5) |
| Corpus has momentum/gap data, static | pipeline exists | Research-radar SaaS (§3.6) |
| No synthesis / few reviews | review = 4.2% | Survey products + RAG agent (§2.2, §3.7) |

---

## 5. Recommended next actions (in-repo)

1. **Fix the reporting loop:** populate the README "Research Gaps" section from
   `statistics.json → gaps` (the data is already there).
2. **Repair the concept graph:** `analyze_concept_graph.py` yields 0 edges,
   killing the `topic_planner` bridge signal. Investigate co-occurrence extraction.
3. **Filter provenance noise:** drop non-person authors (Gemini/Chatterbox) and
   flag arXiv-only vs peer-reviewed before any metric is quoted externally.
4. **Spin a `business_opportunities.md` / strategy brief** from §3 for stakeholders.

---

*Methodology: counts from `statistics.json` (`by_cell`, `momentum`,
`keyword_bursts`, `source_breakdown`). Venue signal from `statistics.json →
venues`. Data-quality flags from manual inspection of `papers.json` author
fields. All percentages computed on the 11,596-paper total.*
