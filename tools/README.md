# Planning Tools

Small, dependency-light Python tools that turn the research corpus into
article topics, trend signals and writing briefs.

## topic_planner.py
Rank evidence-weighted topics and write `docs/topics/ARTICLE_TOPICS.md`.
```bash
python3 topic_planner.py --top 10
```

## trend_scanner.py
Detect rising vocabulary across the recent window vs. baseline.
```bash
python3 trend_scanner.py --months 12
```

## brief_generator.py
Search the corpus and draft a ready-to-write brief.
```bash
python3 brief_generator.py "Deep RL for wargaming" --papers 5 --as-doc
```