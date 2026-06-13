def recommendation_agent(state):

    if (
        "research" not in state["plan"]["tasks"]
        and
        "pricing" not in state["plan"]["tasks"]
    ):
        return state

    trending = "Floral Kurti"
    price = 799

    if "research_data" in state:
        trending = state[
            "research_data"
        ]["top_trending"]

    if "pricing_data" in state:
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