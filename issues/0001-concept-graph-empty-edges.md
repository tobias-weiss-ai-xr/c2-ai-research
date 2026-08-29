# Issue #0001 — Concept graph has 0 edges (bridge signal is dead)

**Status:** Open · **Severity:** Medium · **Area:** `tools/` concept pipeline
**GitHub:** https://github.com/tobias-weiss-ai-xr/c2-ai-research/issues/1

## Symptom

`concept_graph_analysis.json` reports:

```
"stats": { "nodes": 5, "edges": 0, "components": 0, "communities": 0, "modularity": 0.0 }
```

Consequently `tools/topic_planner.py` reads `betweenness` for every taxonomy
node as `0.0`, so its "bridge" cross-cutting signal — the whole point of the
integrative-topic ranking — is **always 0**. The planner silently degrades to
plain paper-count ranking.

## Root cause (two compounding factors)

1. **`config/extraction.yaml` is `mode: selective`.**
   `tools/extract_concepts.py` then emits *only* the taxonomy + curated seed
   concepts and skips emergent bigrams. `concepts.json` therefore contains just
   5 concepts (3 taxonomy: C2 / Opponent Modeling / Wargaming; 2 curated:
   "Survey", "Method" with `df: 0`). There is nothing to connect.

2. **Taxonomy concepts can never co-occur by construction.**
   In `tools/relate_concepts.py`, a taxonomy concept's paper-set is matched
   STRUCTURALLY (`paper.category == value`). Every paper has exactly one
   category, so the 3 taxonomy seeds have **disjoint** paper-sets → 0 shared
   papers → 0 edges. The 2 curated seeds have `df: 0`, i.e. empty paper-sets.
   Net result: `edges: []` regardless.

   → `selective` mode is fundamentally incompatible with producing a
   non-trivial concept graph. Edges can only arise from text-matched
   (emergent / curated) concepts co-occurring in papers.

## Proposed fix

- Switch `config/extraction.yaml` to `mode: broad` (or delete the file to fall
  back to `broad`), then re-run the pipeline:
  ```bash
  python3 tools/extract_concepts.py --papers papers.yaml > concepts.json
  python3 tools/relate_concepts.py --papers papers.yaml --concepts concepts.json --write-doc
  python3 tools/analyze_concept_graph.py --graph concept_graph.json --write-doc
  ```
- Optionally lower `--min-df` in `extract_concepts.py` (default 8) if the
  corpus is large and emergent concepts are sparse.
- Verify `concept_graph_analysis.json` now has `edges > 0` and that
  `topic_planner.py` bridge scores become non-zero.
- Consider a CI assertion (or `generate_readme.py --check` style guard) that
  fails if `edges == 0`, so this regression can't recur silently.

## Acceptance

- `concept_graph.json` has > 0 edges after regeneration.
- `topic_planner.py --top 10` prints at least one `bridge >= 0.5` category.
- `docs/research/concept_graph_analysis.md` lists real bridge nodes/edges.
