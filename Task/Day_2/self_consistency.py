"""Day 2 - Self-consistency experiment."""

from collections import Counter

from config import client, MODEL


QUESTION = (
    "If I study 4 hours per day for 3 days, "
    "is that enough to complete the 12 hours needed for Python?"
)


def ask(question, temperature):

    prompt = f"""
Solve this problem carefully.

Give a brief reasoning summary followed by
the final answer.

Question:
{question}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a careful mathematical reasoning assistant."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    print("\n=== SELF-CONSISTENCY EXPERIMENT ===\n")

    answers = []

    temperature = 0.7

    for i in range(5):

        answer = ask(
            QUESTION,
            temperature
        )

        answers.append(answer)

        print(f"RUN {i + 1}")
        print(answer)
        print("-" * 70)

    print("\n=== TEMPERATURE 0 ===\n")

    zero_answer = ask(
        QUESTION,
        0
    )

    print(zero_answer)

    print("\n=== OBSERVATION ===")

    # Exact full-response counting is mainly illustrative because
    # wording can vary even when the answer is equivalent.
    normalized = [
        answer.lower().strip()
        for answer in answers
    ]

    counts = Counter(normalized)

    print("\nMost repeated exact response:")
    print(counts.most_common(1)[0])