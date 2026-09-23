"""Tools available to the AI agent."""

import ast
import operator

from config import ATTENDANCE


def get_attendance(course_code: str) -> str:
    """Get attendance information for one course."""

    course = course_code.strip().upper()

    data = ATTENDANCE.get(course)

    if data is None:
        return f"Unknown course: {course_code}"

    return (
        f"{course}: "
        f"{data['attended']} attended out of "
        f"{data['total']} classes"
    )


_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def _evaluate(node):

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.left),
            _evaluate(node.right)
        )

    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.operand)
        )

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    """Calculate a mathematical expression safely."""

    try:
        result = _evaluate(
            ast.parse(expression, mode="eval").body
        )

        return str(result)

    except Exception as error:
        return f"Calculator error: {error}"


TOOL_FUNCTIONS = {
    "get_attendance": get_attendance,
    "calculator": calculator,
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_attendance",
            "description": (
                "Get attendance information for one course. "
                "Available courses: PYTHON, AI, DBMS."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string"
                    }
                },
                "required": ["course_code"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Evaluate arithmetic expressions using "
                "+, -, *, / and brackets."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },
                "required": ["expression"],
            },
        },
    },
]


if __name__ == "__main__":

    print(
        "get_attendance('PYTHON') ->",
        get_attendance("PYTHON")
    )

    print(
        "calculator('34 / 40 * 100') ->",
        calculator("34 / 40 * 100")
    )