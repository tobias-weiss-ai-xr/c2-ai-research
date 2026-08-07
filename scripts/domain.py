"""Shared domain config for the C2-AI research corpus.

Centralises the taxonomy constants so that validation, analysis, reporting,
README generation and the article-planning tools all agree on category names.
"""

# 14 research categories spanning the core job keywords:
# autonomous planning/decision-making, deep RL, military simulation, decision
# support via statistics / ML / mathematical optimization.
CATEGORIES = (
    "autonomous-decision-making",
    "deep-reinforcement-learning",
    "multi-agent-rl",
    "opponent-modeling",
    "hierarchical-planning",
    "military-simulation",
    "wargaming",
    "command-and-control",
    "decision-support",
    "mathematical-optimization",
    "probabilistic-uncertainty",
    "mission-planning",
    "human-ai-teaming",
    "sim-to-real",
)

CATEGORY_DISPLAY = {
    "autonomous-decision-making": "Autonomous Decision-Making",
    "deep-reinforcement-learning": "Deep Reinforcement Learning",
    "multi-agent-rl": "Multi-Agent Reinforcement Learning",
    "opponent-modeling": "Opponent & Cognitive Modeling",
    "hierarchical-planning": "Hierarchical Planning",
    "military-simulation": "Military Simulation",
    "wargaming": "Wargaming",
    "command-and-control": "Command & Control (C2)",
    "decision-support": "Decision Support",
    "mathematical-optimization": "Mathematical Optimization",
    "probabilistic-uncertainty": "Probabilistic & Uncertainty Reasoning",
    "mission-planning": "Mission Planning",
    "human-ai-teaming": "Human–AI Teaming",
    "sim-to-real": "Simulation-to-Reality Transfer",
}

# Eight research aspects reused across every category.
SUBCATEGORIES = (
    "theory", "mechanism", "method", "application",
    "development", "systems", "evaluation", "review",
)

SUBCATEGORY_DISPLAY = {
    "theory": "Theory",
    "mechanism": "Mechanism",
    "method": "Method",
    "application": "Application",
    "development": "Development",
    "systems": "Systems & Technology",
    "evaluation": "Evaluation & Benchmarks",
    "review": "Reviews & Surveys",
}

CATEGORY_SET = set(CATEGORIES)
SUBCATEGORY_SET = set(SUBCATEGORIES)