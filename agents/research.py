import json


def research_agent(state):

    if "research" not in state["plan"]["tasks"]:
        return state

    # existing code below

    with open(
        "data/market_data.json"
    ) as file:

        market_data = json.load(file)

    top_product = max(
        market_data,
        key=lambda x:
        market_data[x][
            "trend_score"
        ]
    )

    state["research_data"] = {
        "market_data":
        market_data,

        "top_trending":
        top_product
    }

    return state