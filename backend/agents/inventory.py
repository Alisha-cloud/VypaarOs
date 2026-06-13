import pandas as pd

def inventory_agent(state):

    if "inventory" not in state["plan"]["tasks"]:
        return state


    df = pd.read_csv(
        "data/inventory.csv"
    )

    state["inventory_data"] = {
        "top_inventory":
        df.sort_values(
            by="stock",
            ascending=False
        )
        .head(3)
        .to_dict(
            orient="records"
        )
    }

    return state