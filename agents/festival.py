import json
from datetime import datetime


def festival_agent(state):

    if "festival" not in state["plan"]["tasks"]:
        return state


    with open(
        "data/festivals.json"
    ) as file:

        festivals = json.load(file)

    current_month = datetime.now().month

    upcoming = None

    for festival in festivals:

        if festival["month"] >= current_month:

            upcoming = festival
            break

    if upcoming is None:

        upcoming = festivals[0]

    state["festival_data"] = {

        "festival":
        upcoming["festival"],

        "recommended_products":
        upcoming[
            "recommended_products"
        ],

        "marketing_theme":
        upcoming[
            "marketing_theme"
        ]
    }

    return state