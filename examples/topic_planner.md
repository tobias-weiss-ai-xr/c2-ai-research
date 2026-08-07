# Example: turning evidence into a topic plan

```bash
cd /c2-ai-research

# 1. Validate the corpus
python3 scripts/validate_papers.py

# 2. Refresh statistics + README
python3 scripts/analysis/generate_analysis.py
python3 scripts/generate_readme.py

# 3. Plan topics
python3 tools/topic_planner.py --top 10
# writes docs/topics/ARTICLE_TOPICS.md

# 4. Draft a brief for a chosen topic
python3 tools/brief_generator.py "adaptive decision-making in simulation" --as-doc
# writes docs/topics/brief_adaptive_decision_making_in_simulation.md
```

### Sample output (topic_planner)

```
1. Multi-Agent Reinforcement Learning (papers=2, score=1.182)
2. Deep Reinforcement Learning (papers=4, score=0.364)
3. Hierarchical Planning (papers=1, score=0.091)
...
```

Run this against a larger corpus (via `scripts/build_corpus.py` and continued
curation) for statistically meaningful momentum and gap analysis.