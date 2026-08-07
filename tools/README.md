# Planning & Analysis Tools

Dependency-light Python tools (adopted from the graph-research /
agent-*-research corpus tooling) that turn the research corpus into article
topics, trend signals, landscape analyses and writing briefs.

## topic_planner.py
Rank evidence-weighted topics and write `docs/topics/ARTICLE_TOPICS.md`.
```bash
python3 topic_planner.py --top 10
```

## trend_scanner.py
Detect rising keywords across the recent window vs. baseline (burst analysis)
and fastest-growing taxonomy cells. Exposes a reusable `scan()` used by the
report generator.
```bash
python3 trend_scanner.py --months 12
python3 trend_scanner.py --months 12 --json
```

## landscape_analyzer.py
Full landscape report: category growth/YoY, aspects, year trend, venue mix,
top authors, hot & thin cells, emerging themes.
```bash
python3 landscape_analyzer.py
python3 landscape_analyzer.py --json
python3 landscape_analyzer.py --write-doc   # docs/research/landscape_report.md
```

## brief_generator.py
Search the corpus and draft a ready-to-write brief.
```bash
python3 brief_generator.py "Deep RL for wargaming" --papers 5 --as-doc
```