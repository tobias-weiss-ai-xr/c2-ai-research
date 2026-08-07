# C2-AI Research — Documentation Index

Research corpus for autonomous decision-making, deep reinforcement learning
and decision support in military simulation environments.

## Research

| Document | Purpose |
|----------|---------|
| [`research/taxonomy.md`](research/taxonomy.md) | The 14×8 category/aspect taxonomy definition |
| [`research/literature_review.md`](research/literature_review.md) | Annotated synthesis of the corpus |
| [`research/trends.md`](research/trends.md) | 12-month trend / keyword-burst report |
| [`research/landscape_report.md`](research/landscape_report.md) | Full landscape (YoY, venues, authors, hot/thin cells) |
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
| `../statistics.json` | Machine-readable statistics (+ momentum, bursts, gaps, venues) |
| `../paper/references.bib` | BibTeX export of the corpus |

## Regenerating

```bash
python3 scripts/validate_papers.py                # validate the corpus
python3 scripts/analysis/generate_analysis.py     # statistics.json + papers.json + viz data
python3 scripts/analysis/generate_reports.py      # literature review + trends
python3 scripts/export_bibtex.py                  # paper/references.bib
python3 scripts/visualize_statistics.py           # PNG chart(s)
python3 tools/trend_scanner.py --months 12        # burst/trend report
python3 tools/landscape_analyzer.py --write-doc   # landscape_report.md
python3 tools/topic_planner.py --top 10           # ARTICLE_TOPICS.md
python3 scripts/generate_readme.py                # README.md
```

## Discovery & Enrichment

```bash
python3 scripts/fetch/fetch_new_papers.py --months 6 --dry-run     # arXiv discovery (77 taxonomy queries)
python3 scripts/fetch/fetch_openalex.py --months 36 --dry-run      # OpenAlex discovery (same queries)
python3 scripts/fetch/fetch_openalex_bulk.py --per-category 100     # OpenAlex bulk bootstrap
python3 scripts/fetch/fetch_metadata_bulk.py                        # enrich authors/venue via arXiv id_list
python3 scripts/reclassify_papers.py --dry-run                      # re-run subcategory classification
```