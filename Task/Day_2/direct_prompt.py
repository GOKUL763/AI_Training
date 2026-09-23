"""Day 2 - Direct prompting."""

from config import client, MODEL, QUESTIONS, banner


def direct_prompt(question):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a student study-planning assistant. "
                    "Answer the user's question directly. "
                    "Do not use external tools."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    banner("DIRECT PROMPTING")

    for question in QUESTIONS:

        print("Q:", question)
        print("A:", direct_prompt(question))
        print("-" * 70)