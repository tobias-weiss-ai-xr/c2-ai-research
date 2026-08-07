# C2-AI Research — Documentation Index

Research corpus for autonomous decision-making & deep reinforcement learning
in military simulation environments.

## Research

| Document | Purpose |
|----------|---------|
| [`research/taxonomy.md`](research/taxonomy.md) | The 14×8 category/aspect taxonomy definition |
| [`research/literature_review.md`](research/literature_review.md) | Annotated synthesis of the corpus |
| [`research/research_gaps.md`](research/research_gaps.md) | Uncovered categories & opportunities |

## Topics (Generated)

| Document | Purpose |
|----------|---------|
| [`topics/ARTICLE_TOPICS.md`](topics/ARTICLE_TOPICS.md) | Evidence-ranked article topics (from `topic_planner.py`) |

## Data Files

| File | Description |
|------|-------------|
| `../papers.yaml` | Source of truth (paper metadata) |
| `../papers.json` | JSON export of all papers |
| `../statistics.json` | Machine-readable statistics |

## Regenerating

```bash
python3 scripts/validate_papers.py                # validate the corpus
python3 scripts/analysis/generate_analysis.py     # statistics.json + papers.json
python3 scripts/analysis/generate_reports.py      # literature review + gaps
python3 scripts/visualize_statistics.py           # PNG chart(s)
python3 tools/trend_scanner.py --months 12        # trend report
python3 tools/topic_planner.py --top 10           # ARTICLE_TOPICS.md
python3 scripts/generate_readme.py                # README.md
```