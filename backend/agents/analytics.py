import pandas as pd


def analytics_agent(state):

    df = pd.read_csv(
        "data/sales.csv"
    )

    total_sales = df["sales"].sum()

    total_revenue = df[
        "revenue"
    ].sum()

    average_order_value = (
        total_revenue / total_sales
    )

    state["analytics_data"] = {

        "total_sales":
        int(total_sales),

        "total_revenue":
        round(total_revenue),

        "average_order_value":
        round(
            average_order_value
        )
    }

    return state