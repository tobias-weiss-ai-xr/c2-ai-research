# Contributing to c2-ai-research

Thanks for helping build the evidence base for autonomous decision-making and
deep reinforcement learning in military simulation environments.

> ⚠️ **Ethical note:** This corpus is a public-research evidence base about
> algorithms and simulation methodology. Nothing here is intended as, and
> nothing should be used as, operational military guidance. Keep submissions
> academic and reproducible.

## Ways to Contribute

### 1. Add Papers

1. Fork the repository.
2. Edit `papers.yaml` — append entries in this format:

```yaml
- title: "A great RL paper"
  date: "2026-07"
  url: https://arxiv.org/abs/2607.12345
  category: deep-reinforcement-learning
  subcategory: method
  arxiv_id: '2607.12345'
  authors: ["First Author"]
  abstract: "Short abstract..."
```

3. Open a PR. The CI workflow validates the corpus.

### Taxonomy Reference

**Categories (14):** `autonomous-decision-making`, `deep-reinforcement-learning`,
`multi-agent-rl`, `opponent-modeling`, `hierarchical-planning`,
`military-simulation`, `wargaming`, `command-and-control`, `decision-support`,
`mathematical-optimization`, `probabilistic-uncertainty`, `mission-planning`,
`human-ai-teaming`, `sim-to-real`

**Subcategories (8):** `theory`, `mechanism`, `method`, `application`,
`development`, `systems`, `evaluation`, `review`

### 2. Improve Tools / Scripts

- Scripts and tools are Python 3.10+ with type hints and logging where possible.
- Run `python3 scripts/validate_papers.py` and the relevant tool before opening a PR.
- Keep `scripts/domain.py` and `scripts/validate_papers.py` in sync when the
  taxonomy changes.

### 3. Report Issues

- Wrong categories / metadata → open a paper-metadata issue.
- Broken pipeline → open a tooling issue.

## Development Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/validate_papers.py
```

## Code Style

- PEP 8, 4-space indentation.
- F-strings for formatting.
- Keep scripts deterministic (no network calls in `validate_papers.py`).