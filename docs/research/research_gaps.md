# Research Gaps

Categories and taxonomy cells with the thinnest coverage — candidate areas for new investigations or targeted corpus expansion.

> Auto-generated from statistics.json on 2026-08-10.

---

## Corpus Summary

| Metric | Value |
|--------|-------|
| Total papers | 6,277 |
| Categories | 14 |
| Subcategories | 8 |
| Taxonomy cells | 112 |
| Filled cells | 111 (99.1%) |
| Empty cells | 1 |
| Sources | 6,082 arXiv · 195 DBLP/CrossRef/EuropePMC |

---

## Thinnest Taxonomy Cells (Single-Digit Coverage)

| Cell | Papers | Notes |
|------|--------:|-------|
| `command-and-control/evaluation` | 1 | Despite 401 C2 papers, no benchmarking culture |
| `mission-planning/method` | 1 | Formalized methods for mission planning are missing |
| `mission-planning/evaluation` | 1 | No standardized mission-planning benchmarks |
| `wargaming/mechanism` | 1 | Mechanism/explainability analysis absent |
| `wargaming/evaluation` | 1 | No wargaming benchmarks |
| `wargaming/development` | 2 | Very few open-source frameworks |
| `multi-agent-rl/review` | 2 | 448 papers, only 2 reviews |
| `mathematical-optimization/review` | 2 | 259 papers, only 2 reviews |
| `hierarchical-planning/review` | 2 | 127 papers, only 2 reviews |
| `mission-planning/review` | 2 | No comprehensive surveys |

---

## Empty Cells (0 Papers)

None — all 112 taxonomy cells are now filled except 1 remaining empty cell.

---

## White-Space Cells (Low Volume, Fast Growth — Emerging Areas)

| Cell | Total | Recent | 12-m Share |
|------|-------:|-------:|-----------:|
| `autonomous-decision-making/mechanism` | 24 | 24 | 100% |
| `opponent-modeling/application` | 23 | 23 | 100% |
| `hierarchical-planning/application` | 23 | 23 | 100% |
| `mission-planning/development` | 23 | 23 | 100% |
| `mathematical-optimization/systems` | 22 | 22 | 100% |
| `autonomous-decision-making/method` | 21 | 21 | 100% |
| `mission-planning/theory` | 20 | 20 | 100% |
| `hierarchical-planning/theory` | 19 | 19 | 100% |
| `military-simulation/systems` | 18 | 18 | 100% |
| `human-ai-teaming/evaluation` | 29 | 29 | 100% |

---

## Structural Observations

1. **Wargaming filled from 4 → 149 papers** via DBLP/CrossRef/EuropePMC — now a viable category with depth back to the 1970s. Still thin in reviews, development, and evaluation.

2. **Reviews remain scarce**: 237 review papers (3.8%) across 6,277 total. Most categories have ≤2 reviews. The field is still in rapid expansion, with few survey-type synthesis papers.

3. **C2 evaluation is a persistent gap**: 401 papers but only 1 benchmarking/evaluation paper. No standardized testbeds for command and control AI.

4. **Non-arXiv sources added 195 papers** (DBLP: ~100, CrossRef: ~50, EuropePMC: ~45). These include journals (IEEE Access, Information Sciences, J. Aerosp. Inf. Syst.), conferences (AAAI, AIES, CoG), and books/chapters. Many predate the arXiv era (back to 1978), adding historical depth.

5. **99.1% saturation** achieved — only 1 empty taxonomy cell remains.

---

_Regenerate with: `python3 scripts/analysis/generate_analysis.py && python3 scripts/analysis/generate_reports.py`_
