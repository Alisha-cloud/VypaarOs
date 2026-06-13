from typing import TypedDict


class BusinessState(TypedDict, total=False):

    # User Goal
    goal: str

    # Planner Output
    plan: dict

    # Agent Outputs
    research_data: dict

    inventory_data: dict

    pricing_data: dict

    listing_data: dict

    marketing_data: dict

    recommendation: dict

    listing_data: dict

    analytics_data: dict

    simulation_data: dict

    festival_data: dict

    # Final Report
    advisor_report: str