from services.gemini import ask_gemini


def listing_agent(state):

    product = state[
        "research_data"
    ]["top_trending"]

    prompt = f"""
Create an ecommerce listing.

Product:
{product}

Generate:

1. English Title

2. Hindi Title

3. Product Description

4. SEO Keywords

Return in structured format.
"""

    listing = ask_gemini(prompt)

    state["listing_data"] = {
        "content": listing
    }

    return state