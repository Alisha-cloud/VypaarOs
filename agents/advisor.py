from services.gemini import ask_gemini


def advisor_agent(state):

    tasks = state.get(
        "plan",
        {}
    ).get(
        "tasks",
        []
    )

    research_data = state.get(
        "research_data",
        {}
    )

    inventory_data = state.get(
        "inventory_data",
        {}
    )

    pricing_data = state.get(
        "pricing_data",
        {}
    )

    recommendation = state.get(
        "recommendation",
        {}
    )

    listing_data = state.get(
        "listing_data",
        {}
    )

    marketing_data = state.get(
        "marketing_data",
        {}
    )

    analytics_data = state.get(
        "analytics_data",
        {}
    )

    simulation_data = state.get(
        "simulation_data",
        {}
    )

    festival_data = state.get(
        "festival_data",
        {}
    )

    prompt = f"""

You are an expert business consultant.

Goal:
{state['goal']}

Executed Agents:
{tasks}

Research Data:
{research_data}

Inventory Data:
{inventory_data}

Analytics Data:
{analytics_data}

Pricing Data:
{pricing_data}

Recommendation:
{recommendation}

Listing Data:
{listing_data}

Marketing Data:
{marketing_data}

Simulation Data:
{simulation_data}

Festival Data:
{festival_data}

Generate a detailed report with:

1. Executive Summary

2. Business Insights

3. Pricing Strategy

4. Inventory Strategy

5. Listing Strategy

6. Marketing Strategy

7. Risks

8. Growth Opportunities

9. Expected Impact

Important:
Only use the data that is available.
Do not mention missing data.
Keep the report professional and actionable.

"""

    state["advisor_report"] = ask_gemini(
        prompt
    )

    return state