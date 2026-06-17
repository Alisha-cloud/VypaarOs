def forecast_agent(state):

    analytics = state.get(
        "analytics_data",
        {}
    )

    current_sales = analytics.get(
        "total_sales",
        70
    )

    current_revenue = analytics.get(
        "total_revenue",
        62930
    )

    projected_sales = round(
        current_sales * 1.20
    )

    projected_revenue = round(
        current_revenue * 1.20
    )

    state["forecast_data"] = {

        "current_sales":
        current_sales,

        "projected_sales":
        projected_sales,

        "current_revenue":
        current_revenue,

        "projected_revenue":
        projected_revenue,

        "growth":
        "20%"
    }

    return state