"""Tools available to the ReAct agent."""

from config import EXAMS


def get_exam_schedule(subject: str) -> str:
    """Look up the exam date and required study hours."""

    subject = subject.strip().upper()

    exam = EXAMS.get(subject)

    if exam is None:
        return f"Unknown subject: {subject}"

    return (
        f"{subject}: exam date {exam['date']}, "
        f"study requirement {exam['study_hours']} hours"
    )


def calculator(expression: str) -> str:
    """Perform basic arithmetic safely."""

    allowed = set("0123456789+-*/(). ")

    if not set(expression) <= allowed:
        return "Calculator error: invalid characters"

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)

    except Exception as error:
        return f"Calculator error: {error}"


TOOL_FUNCTIONS = {
    "get_exam_schedule": get_exam_schedule,
    "calculator": calculator,
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_exam_schedule",
            "description": (
                "Get the exam date and required study hours "
                "for Python, AI or DBMS."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "subject": {
                        "type": "string"
                    }
                },
                "required": ["subject"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Perform arithmetic calculations using "
                "numbers, +, -, *, / and parentheses."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


if __name__ == "__main__":

    print(
        get_exam_schedule("Python")
    )

    print(
        calculator("15 / 3")
    )