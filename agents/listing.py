def listing_agent(state):

    if "listing" not in state["plan"]["tasks"]:
        return state

    # Try getting product from research

    if "research_data" in state:

        product = state[
            "research_data"
        ]["top_trending"]

    else:

        product = "Floral Kurti"

    state["listing_data"] = {

        "english_title":
        f"Premium {product} for Women",

        "hindi_title":
        f"महिलाओं के लिए प्रीमियम {product}",

        "description":
        f"""
Discover our latest {product}.
Designed for comfort and style.
Perfect for festive and casual wear.
""",

        "seo_keywords": [
            product,
            "Women Kurti",
            "Ethnic Wear",
            "Festival Fashion"
        ]
    }

    return state