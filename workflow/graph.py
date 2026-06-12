from langgraph.graph import (
    StateGraph,
    END
)

from workflow.state import BusinessState

from agents.research import research_agent
from agents.inventory import inventory_agent
from agents.pricing import pricing_agent
from agents.recommendation import recommendation_agent
from agents.listing import listing_agent
from agents.marketing import marketing_agent
from agents.advisor import advisor_agent
from agents.planner import planner_agent


builder = StateGraph(
    BusinessState
)

# Nodes

builder.add_node(
    "research",
    research_agent
)

builder.add_node(
    "inventory",
    inventory_agent
)

builder.add_node(
    "pricing",
    pricing_agent
)

builder.add_node(
    "recommendation",
    recommendation_agent
)

builder.add_node(
    "listing",
    listing_agent
)

builder.add_node(
    "marketing",
    marketing_agent
)

builder.add_node(
    "advisor",
    advisor_agent
)

builder.add_node(
    "planner",
    planner_agent
)
# Entry Point

builder.set_entry_point(
    "planner"
)

# Flow

builder.add_edge(
    "planner",
    "research"
)

builder.add_edge(
    "research",
    "inventory"
)

builder.add_edge(
    "inventory",
    "pricing"
)

builder.add_edge(
    "pricing",
    "recommendation"
)

builder.add_edge(
    "recommendation",
    "listing"
)

builder.add_edge(
    "listing",
    "marketing"
)

builder.add_edge(
    "marketing",
    "advisor"
)

builder.add_edge(
    "advisor",
    END
)
# Compile

workflow = builder.compile()