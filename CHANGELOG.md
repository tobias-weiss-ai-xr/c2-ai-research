# Changelog

## [0.1.0] — 2026-08-07

### Added
- Initial corpus: 11 curated papers across 7/14 categories (seed corpus).
- 14×8 taxonomy (`scripts/domain.py`, `docs/research/taxonomy.md`).
- Research pipeline:
  - `scripts/build_corpus.py` — rebuild corpus from curated arXiv seed.
  - `scripts/validate_papers.py` — corpus validation.
  - `scripts/analysis/generate_analysis.py` — `statistics.json` + `papers.json`.
  - `scripts/analysis/generate_reports.py` — literature review & gaps.
  - `scripts/visualize_statistics.py` — chart generation.
  - `scripts/generate_readme.py` — auto-generated README.
- Planning tools: `topic_planner.py`, `trend_scanner.py`, `brief_generator.py`.
- CI workflow: validate + regenerate README on push.
- Docs: taxonomy, literature review, research gaps, article topics.
- License: MIT (tools/scripts); research corpus proprietary.