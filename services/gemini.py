import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)


def ask_gemini(prompt):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print(
            f"Gemini Error: {str(e)}"
        )

        return """
# AI Advisor (Fallback Mode)

Gemini is currently unavailable.

Business Recommendations:

• Focus on promoting top-performing products.

• Monitor inventory levels to avoid stockouts.

• Optimize pricing based on demand and sales trends.

• Run targeted marketing campaigns during festivals.

• Improve product listings with better titles,
  descriptions, and keywords.

• Track sales, revenue, and average order value
  regularly.

• Use customer feedback to improve product
  selection and future campaigns.

Fallback report generated successfully.
"""