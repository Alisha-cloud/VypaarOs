from services.gemini import ask_gemini
import json


def planner_agent(state):

    goal = state["goal"]

    prompt = f"""
You are an AI planner.

Goal:
{goal}

Available Agents:

- research
- inventory
- pricing
- listing
- marketing

Return ONLY valid JSON.

Example:

{{
    "tasks": [
        "research",
        "inventory",
        "pricing",
        "marketing"
    ]
}}
"""

    response = ask_gemini(prompt)

    try:
        state["plan"] = json.loads(response)

    except:
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