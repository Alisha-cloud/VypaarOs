def competitor_agent(state):

    state["competitor_data"] = {

        "competitors": [

            {
                "name": "Myntra",
                "strength": "Large product catalog",
                "weakness": "Less personalized shopping experience"
            },

            {
                "name": "Ajio",
                "strength": "Aggressive discounting",
                "weakness": "Lower product variety in some categories"
            },

            {
                "name": "Meesho",
                "strength": "Low-cost pricing",
                "weakness": "Perceived quality concerns"
            }

        ],

        "recommendation":
        "Differentiate through trending products, faster delivery, and festival-focused marketing campaigns."
    }

    return state