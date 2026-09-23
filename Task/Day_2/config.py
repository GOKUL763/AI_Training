"""Shared configuration for Day 2."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-120b")

else:
    raise SystemExit("This Day 2 project is configured for Groq.")

if not API_KEY:
    raise SystemExit("GROQ_API_KEY is missing from .env")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

# Scenario data
EXAMS = {
    "PYTHON": {
        "date": "2026-10-10",
        "study_hours": 12
    },
    "AI": {
        "date": "2026-10-14",
        "study_hours": 15
    },
    "DBMS": {
        "date": "2026-10-18",
        "study_hours": 10
    }
}

QUESTIONS = [
    "If I study 3 hours per day, how many days do I need for AI if it requires 15 hours?",
    "I can study 4 hours per day for 3 days. Is that enough for Python?",
    "Which exam comes first, Python or AI, and how many days are between them?",
    "I need to plan my study order for Python, AI and DBMS based on their exam dates. What order should I follow?"
]


def banner(name):
    print(
        f"\n=== {name} | "
        f"provider: {PROVIDER} | "
        f"model: {MODEL} ===\n"
    )