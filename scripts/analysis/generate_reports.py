#!/usr/bin/env python3
"""Generate research reports from the corpus:
  - docs/research/literature_review.md   (synthesis + top papers per category)
  - docs/research/trends.md              (trend report from trend scanner)

Adopted & adapted from graph-research corpus tooling.

Usage:
    python3 scripts/analysis/generate_reports.py
"""

import json
import os
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE / "scripts"))
import domain  # noqa: E402

sys.path.insert(0, str(BASE / "tools"))
from trend_scanner import scan as scan_trends  # noqa: E402

CATEGORY_DISPLAY = domain.CATEGORY_DISPLAY
SUBCATEGORY_DISPLAY = domain.SUBCATEGORY_DISPLAY

KEY_INSIGHTS = {
    "deep-reinforcement-learning": (
        "DRL is the methodological core of the corpus: value/policy gradients, "
        "benchmark algorithms (PPO, DQN/Rainbow) and sample-efficiency methods "
        "form the substrate every downstream planning/decision task builds on."
    ),
    "autonomous-decision-making": (
        "End-to-end perception-then-action pipelines (e.g. decision transformers, "
        "MCTS planners) encode the target capability for autonomous planning and "
        "decision-making in high-stakes, partially structured environments."
    ),
    "multi-agent-rl": (
        "Cooperative/competitive multi-agent RL is the bridge from single-agent "
        "learning to unit/force-level coordination — the core of adversarial and "
        "maneuver scenarios in simulation."
    ),
    "opponent-modeling": (
        "Inferring adversary intent and strategy (game theory, adversarial RL, "
        "counterfactual regret) is the differentiator for decision support that "
        "reasons about an opponent, not just the environment."
    ),
    "hierarchical-planning": (
        "Hierarchical and abductive planning tackles the combinatorial depth of "
        "complex operational tasks by decomposing goals into options and sub-plans."
    ),
    "military-simulation": (
        "Simulation environments (constructive, game-engine, entity-level) are "
        "the training and test bed for RL in military settings; assessment and "
        "fidelity criteria matter as much as the learners themselves."
    ),
    "wargaming": (
        "Red-vs-blue wargaming is the canonical adversarial setting where RL, "
        "opponent modeling and optimization collide under realistic scenario "
        "constraints."
    ),
    "command-and-control": (
        "C2 research connects autonomy to human-machine teaming, situational "
        "awareness and decision support at the operational seam between "
        "computation and command."
    ),
    "decision-support": (
        "Decision support fuses statistics, ML and optimization to augment "
        "human decisions — explicitly including recommendation and "
        "interpretability for warfighters and operators."
    ),
    "mathematical-optimization": (
        "Constrained/convex/DP optimization is the formal bridge between RL "
        "objectives and provable mission-planning guarantees."
    ),
    "probabilistic-uncertainty": (
        "Bayesian, POMDP and uncertainty-quantified reasoning is essential where "
        "observation is partial and risk must be quantified before committing to "
        "an action."
    ),
    "mission-planning": (
        "Task allocation, routing, path planning and scheduling are the concrete "
        "optimization problems behind an autonomous mission plan."
    ),
    "human-ai-teaming": (
        "Trust, explainability and mixed-initiative control are the acceptance "
        "criteria — an autonomous system that no human trusts is not deployable."
    ),
    "sim-to-real": (
        "Domain randomization and sim-to-sim/sim-to-real transfer are the "
        "mechanisms that make policies learned in simulations usable on real "
        "systems."
    ),
}


def render_literature_review(papers, now, stats=None):
    total = len(papers)
    lines = [
        "# C2-AI Research — Literature Review",
        "",
        f"**Generated:** {now}  ",
        f"**Corpus:** {total:,} papers across {len(CATEGORY_DISPLAY)} categories",
        "",
        "> Synthesis of the autonomous decision-making & deep-RL research corpus. "
        "Category insights are drawn from title/abstract analysis of the papers "
        "themselves.",
        "",
        "---",
        "",
        "## Corpus Overview",
        "",
    ]
    cat_counter = Counter(p.get("category", "unknown") for p in papers)
    sub_counter = Counter(p.get("subcategory", "unknown") for p in papers)
    year_counter = Counter(p.get("date", "")[:4] for p in papers if p.get("date"))
    top_cats = sorted(cat_counter.items(), key=lambda kv: -kv[1])[:5]

    lines.append("| Rank | Category | Papers |")
    lines.append("|------|----------|--------|")
    for i, (c, n) in enumerate(top_cats, 1):
        lines.append(f"| {i} | {CATEGORY_DISPLAY.get(c, c)} | {n} |")

    years = sorted(y for y in year_counter if y)
    lines += [
        "",
        f"**Time span:** {years[0]}–{years[-1]} (median year {years[len(years)//2] if years else '—'})",
        f"**Dominant aspects:** {', '.join(f'{SUBCATEGORY_DISPLAY.get(s, s)} ({n})' for s, n in sub_counter.most_common(3))}",
        "",
        "---",
        "",
    ]

    if isinstance(stats, dict):
        mom = stats.get("momentum", [])
        if mom:
            lines += [
                "## 📈 Research Momentum (Last 12 Months)",
                "",
                "Categories ranked by a momentum score combining recent output "
                "density with year-over-year growth.",
                "",
                "| Category | Total | Last 12m | Prior 12m | Growth | 12-m share | Papers/mo |",
                "|----------|------:|---------:|----------:|-------:|----------:|----------:|",
            ]
            for m in mom:
                g = f"{m['growth_pct']:+}%" if m['growth_pct'] is not None else "—"
                lines.append(
                    f"| {m['name']} | {m['total']} | {m['recent']} | {m['prior']} | {g} | "
                    f"{m['recent_share']*100:.0f}% | {m['papers_per_month']} |"
                )
            lines += ["", "---", ""]

        gaps = stats.get("gaps", {})
        if gaps:
            lines += ["## 🕳️ Research Gaps & White Space", ""]
            thinnest = gaps.get("thinnest_cells", [])[:8]
            if thinnest:
                lines += ["**Thinnest taxonomy cells:**", "", "| Cell | Papers |", "|------|--------|"]
                for g in thinnest:
                    lines.append(f"| `{g['cell']}` | {g['papers']} |")
                lines.append("")
            ws = gaps.get("white_space", [])[:8]
            if ws:
                lines += ["**White-space cells** (low total but fast-growing):", "",
                          "| Cell | Total | Last-12m | 12-m share |",
                          "|------|-------:|---------:|-----------:|"]
                for w in ws:
                    lines.append(f"| `{w['cell']}` | {w['total']} | {w['recent']} | {w['recent_share']*100:.0f}% |")
                lines.append("")
            lines += ["---", ""]

        if stats.get("venues"):
            lines += ["## Publishing Venues", "",
                      "Top venues by paper count (where present in the metadata):", "",
                      "| Venue | Papers |", "|-------|--------|"]
            for v in stats["venues"][:10]:
                lines.append(f"| {v['name']} | {v['papers']} |")
            lines += ["", "---", ""]

    lines += ["", "## Category Insights", ""]
    for c in sorted(cat_counter, key=lambda c: -cat_counter[c]):
        if cat_counter[c] == 0:
            continue
        insight = KEY_INSIGHTS.get(c,
            "Category still saturating — see `statistics.json` for cell counts.")
        lines += [f"### {CATEGORY_DISPLAY.get(c, c)} (`{c}`)", "", insight,
                  "", f"**Corpus size:** {cat_counter[c]} papers"]
        cat_papers = sorted((p for p in papers if p.get("category") == c),
                            key=lambda p: p.get("date", ""), reverse=True)[:3]
        if cat_papers:
            lines += ["", "**Papers:**", ""]
            for p in cat_papers:
                lines.append(f"- [{p.get('date','')}] {p['title'][:100]} — {p.get('url', '')}")
        lines += ["", "---", ""]

    lines += [
        "## Methodology",
        "",
        "1. Papers are discovered via taxonomy-aware arXiv/OpenAlex queries and "
        "auto-classified into the 14×8 taxonomy.",
        "2. Category insights above are editorially curated but grounded in "
        "corpus statistics.",
        "3. Regenerate this document with `scripts/analysis/generate_reports.py`.",
        "",
    ]
    return "\n".join(lines)


def render_trend_report(papers, now, stats=None):
    result = scan_trends(papers, months=12, top=15)
    lines = [
        "# C2-AI Research Trends (12-Month View)",
        "",
        f"**Generated:** {now}  ",
        f"**Window:** since {result['cutoff']} — {result['recent_papers']} of {len(papers)} papers",
        "",
        "## 🔥 Keyword Bursts",
        "",
        "| Keyword | Recent | Total | Burst |",
        "|---------|--------|-------|-------|",
    ]
    for t in result["trends"]:
        lines.append(f"| {t['keyword']} | {t['recent_papers']} | {t['total_papers']} | {t['burst_score']}× |")

    lines += ["", "## 📈 Fastest-Growing Cells", "",
              "| Cell | Recent | Total | Recent Share |",
              "|------|--------|-------|--------------|"]
    for g in result["growing_cells"]:
        lines.append(f"| `{g['cell']}` | {g['recent']} | {g['total']} | {g['recent_share']*100:.0f}% |")
    lines += ["", "Regenerate with `python3 tools/trend_scanner.py --months 12`.", ""]
    return "\n".join(lines)


def main():
    with open(BASE / "papers.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    papers = data.get("papers", [])
    now = datetime.now().isoformat()[:10]

    stats_path = BASE / "statistics.json"
    stats = json.loads(stats_path.read_text(encoding="utf-8")) if stats_path.exists() else None

    out = BASE / "docs" / "research"
    out.mkdir(parents=True, exist_ok=True)
    (out / "literature_review.md").write_text(render_literature_review(papers, now, stats), encoding="utf-8")
    (out / "trends.md").write_text(render_trend_report(papers, now, stats), encoding="utf-8")
    print("wrote docs/research/literature_review.md & docs/research/trends.md")


if __name__ == "__main__":
    main()