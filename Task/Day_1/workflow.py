"""System 2: Rule-based attendance workflow."""

import re
from config import ATTENDANCE, QUESTIONS


def workflow(question):

    text = question.lower()

    # Find course name
    course = None

    for name in ATTENDANCE:
        if name.lower() in text:
            course = name
            break

    if course is None and "total" not in text:
        return "Sorry, I only have attendance data for Python, AI and DBMS."

    # Total attendance
    if "total" in text:
        total_classes = sum(
            data["total"]
            for data in ATTENDANCE.values()
        )

        attended_classes = sum(
            data["attended"]
            for data in ATTENDANCE.values()
        )

        percentage = attended_classes / total_classes * 100

        return f"Total attendance: {percentage:.2f}%"

    data = ATTENDANCE[course]

    # Attendance percentage
    if "percentage" in text:
        percentage = data["attended"] / data["total"] * 100

        return (
            f"{course} attendance percentage: "
            f"{percentage:.2f}%"
        )

    # Classes needed to reach 90%
    if "90%" in text or "90 percent" in text:
        attended = data["attended"]
        total = data["total"]

        additional = 0

        while (attended + additional) / (total + additional) < 0.90:
            additional += 1

        return (
            f"You need to attend "
            f"{additional} more {course} classes "
            f"to reach 90%."
        )

    # Basic attendance
    return (
        f"{course}: "
        f"{data['attended']} attended out of "
        f"{data['total']} classes."
    )


if __name__ == "__main__":

    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW ===\n")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)