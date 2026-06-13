import pandas as pd


def simulation_agent(state):

    if "simulation" not in state["plan"]["tasks"]:
        return state

    goal = state["goal"].lower()

    if "reduce price" not in goal:
        return state

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

    reduction_amount = 50

    new_price = (
        current_price -
        reduction_amount
    )

    estimated_growth = 0.12

    projected_sales = (
        total_sales *
        (1 + estimated_growth)
    )

    projected_revenue = (
        projected_sales *
        new_price
    )

    revenue_change = (
        projected_revenue -
        total_revenue
    )

    state["simulation_data"] = {

        "current_price":
        round(current_price),

        "new_price":
        round(new_price),

        "price_reduction":
        reduction_amount,

        "estimated_sales_growth":
        "12%",

        "projected_revenue":
        round(projected_revenue),

        "revenue_change":
        round(revenue_change),

        "recommendation":
        (
            "Price reduction appears beneficial"
            if revenue_change > 0
            else
            "Price reduction may reduce revenue"
        )
    }

    return state