def recommendation_agent(state):

    trending = state[
        "research_data"
    ]["top_trending"]

    price = state[
        "pricing_data"
    ]["recommended_price"]

    state["recommendation"] = {

        "action":
        f"Promote {trending}",

        "recommended_price":
        price,

        "reason":
        f"{trending} is trending and should be sold at ₹{price}"
    }

    return state