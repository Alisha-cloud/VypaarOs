def planner_agent(state):

    goal = state["goal"].lower()

    # Simulation Goals

    if (
        "what if" in goal
        or "reduce price" in goal
        or "price by" in goal
        or "forecast" in goal
        or "simulation" in goal
    ):

        state["plan"] = {
            "tasks": [
                "pricing",
                "simulation"
            ]
        }

    # Listing Goals

    elif (
        "listing" in goal
        or "seo" in goal
        or "product description" in goal
    ):

        state["plan"] = {
            "tasks": [
                "listing"
            ]
        }

    # Marketing Goals

    elif (
        "marketing" in goal
        or "campaign" in goal
        or "instagram" in goal
        or "whatsapp" in goal
        or "festival" in goal
    ):

        state["plan"] = {
            "tasks": [
                "marketing"
            ]
        }

    # Pricing Goals

    elif (
        "pricing" in goal
        or "price" in goal
        or "profit" in goal
    ):

        state["plan"] = {
            "tasks": [
                "research",
                "inventory",
                "pricing"
            ]
        }

    # Inventory Goals

    elif (
        "inventory" in goal
        or "stock" in goal
    ):

        state["plan"] = {
            "tasks": [
                "inventory"
            ]
        }

    elif (
        "raksha bandhan" in goal
        or "diwali" in goal
        or "navratri" in goal
        or "eid" in goal
        or "onam" in goal
        or "pongal" in goal
    ):
        state["plan"] = {
            "tasks": [
                "festival",
                "marketing"
            ]
        }

    elif (
        "marketing" in goal
        or "campaign" in goal
        or "instagram" in goal
        or "whatsapp" in goal
    ):
        state["plan"] = {
            "tasks": [
                "marketing"
            ]
        }

    # Business Growth Goals

    else:

        state["plan"] = {
            "tasks": [
                "research",
                "inventory",
                "pricing",
                "listing",
                "marketing"
            ]
        }

    return state