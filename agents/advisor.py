from services.gemini import ask_gemini


def advisor_agent(state):

    prompt = f"""

You are an expert business consultant.

Goal:
{state['goal']}

Research Data:
{state['research_data']}

Inventory Data:
{state['inventory_data']}

Pricing Data:
{state['pricing_data']}

Recommendation:
{state['recommendation']}

Listing Data:
{state['listing_data']}

Marketing Data:
{state['marketing_data']}

Generate:

1. Business Summary

2. Pricing Strategy

3. Inventory Strategy

4. Listing Strategy

5. Marketing Strategy

6. Risks

7. Expected Impact

Keep the response professional, actionable, and suitable for a small ecommerce seller.

"""

    state["advisor_report"] = ask_gemini(
        prompt
    )

    return state