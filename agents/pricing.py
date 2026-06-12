import pandas as pd


def pricing_agent(state):

    df = pd.read_csv(
        "data/sales.csv"
    )

    total_sales = df["sales"].sum()

    total_revenue = df[
        "revenue"
    ].sum()

    current_price = (
        total_revenue /
        total_sales
    )

    recommended_price = (
        current_price - 100
    )

    state["pricing_data"] = {

        "current_price":
        round(current_price),

        "recommended_price":
        round(recommended_price),

        "confidence":
        0.84,

        "reason":
        "Lower pricing can improve conversions during high-demand festival periods."
    }

    return state