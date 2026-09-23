"""Day 2 - Chain-of-Thought style prompting."""

from config import client, MODEL, QUESTIONS, banner


def cot(question):

    prompt = f"""
Solve the following problem carefully.

Break the problem into the necessary steps internally.
Then provide:
1. A brief reasoning summary.
2. The final answer.

Do not use any external tools.

Question:
{question}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a careful student study-planning assistant."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    banner("CHAIN-OF-THOUGHT STYLE PROMPTING")

    for question in QUESTIONS:

        print("Q:", question)
        print("A:", cot(question))
        print("-" * 70)