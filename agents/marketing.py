def marketing_agent(state):

    if "marketing" not in state["plan"]["tasks"]:
        return state

    # Safe defaults

    product = "Floral Kurti"
    price = 799

    # Use research output if available

    if "research_data" in state:
        product = state[
            "research_data"
        ]["top_trending"]

    # Use pricing output if available

    if "pricing_data" in state:
        price = state[
            "pricing_data"
        ]["recommended_price"]

    state["marketing_data"] = {

        "campaign_name":
        f"{product} Festival Sale",

        "instagram_caption":
        f"""
✨ Trending Now: {product}

Upgrade your wardrobe with our latest collection.

Starting at just ₹{price}

#KurtiFashion #EthnicWear #FestivalFashion
""",

        "whatsapp_message":
        f"""
🔥 Special Offer Alert 🔥

{product} now available at ₹{price}

Limited stock available.
Shop now before it's sold out!
""",

        "festival_offer":
        "Flat 20% OFF + Free Shipping"
    }

    return state