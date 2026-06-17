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
from agents.analytics import analytics_agent
from agents.simulation import simulation_agent
from agents.festival import festival_agent
from agents.forecast import (
    forecast_agent
)
from agents.competitor import (
    competitor_agent
)


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

builder.add_node(
    "analytics",
    analytics_agent
)

builder.add_node(
    "simulation",
    simulation_agent
)

builder.add_node(
    "festival",
    festival_agent
)

builder.add_node(
    "forecast",
    forecast_agent
)
builder.add_node(
    "competitor",
    competitor_agent
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
    "analytics"
)

builder.add_edge(
    "analytics",
    "forecast"
)

builder.add_edge(
    "forecast",
    "pricing"
)

builder.add_edge(
    "pricing",
    "simulation"
)

builder.add_edge(
    "simulation",
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
    "festival"
)

builder.add_edge(
    "festival",
    "competitor"
)

builder.add_edge(
    "competitor",
    "advisor"
)

builder.add_edge(
    "advisor",
    END
)
# Compile

workflow = builder.compile()