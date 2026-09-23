"""Day 2 - ReAct agent."""

import json

from config import client, MODEL, QUESTIONS, banner
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a student study-planning assistant.

You follow the ReAct pattern:

Thought:
Decide what information or calculation is needed.

Action:
Call the appropriate tool.

Observation:
Read the tool result.

Repeat when necessary.

Finally provide a concise answer.

Use get_exam_schedule whenever you need actual exam dates
or study-hour requirements.

Use calculator for arithmetic.

Available subjects:
PYTHON
AI
DBMS
"""


def react_agent(question, max_steps=6, verbose=True):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        # THOUGHT / DECISION
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        # FINAL ANSWER
        if not message.tool_calls:
            return message.content.strip()

        messages.append(
            {
                "role": "assistant",
                "content": message.content or "",
                "tool_calls": [
                    {
                        "id": call.id,
                        "type": "function",
                        "function": {
                            "name": call.function.name,
                            "arguments": call.function.arguments
                        }
                    }
                    for call in message.tool_calls
                ]
            }
        )

        # ACTION + OBSERVATION
        for call in message.tool_calls:

            name = call.function.name

            arguments = json.loads(
                call.function.arguments or "{}"
            )

            function = TOOL_FUNCTIONS.get(name)

            if function:
                result = function(**arguments)
            else:
                result = f"Unknown tool: {name}"

            if verbose:
                print(
                    f" step {step}: "
                    f"{name}({arguments}) -> {result}"
                )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": result
                }
            )

    return "Stopped: maximum steps reached."


if __name__ == "__main__":

    banner("REACT AGENT")

    for question in QUESTIONS:

        print("Q:", question)
        print("A:", react_agent(question))
        print("-" * 70)