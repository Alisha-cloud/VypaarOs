from services.gemini import ask_gemini


def marketing_agent(state):

    prompt = f"""
Create a marketing campaign.

Product:
{state['research_data']['top_trending']}

Recommended Price:
₹{state['pricing_data']['recommended_price']}

Generate:

1. Campaign Name
2. Instagram Caption
3. WhatsApp Message
4. Festival Offer

Keep it concise.
"""

    marketing_content = ask_gemini(
        prompt
    )

    state["marketing_data"] = {
        "content": marketing_content
    }

    return state