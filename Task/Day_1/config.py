"""Shared configuration for the Day 1 attendance task."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "ollama").strip().lower()

if PROVIDER == "ollama":
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"
    MODEL = os.getenv("MODEL", "qwen2.5:1.5b")

elif PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

elif PROVIDER == "huggingface":
    BASE_URL = "https://router.huggingface.co/v1"
    API_KEY = os.getenv("HF_TOKEN")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'. "
        "Use ollama, groq or huggingface."
    )

if not API_KEY:
    raise SystemExit(
        f"No API key found for PROVIDER={PROVIDER}."
    )

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

# PRIVATE STUDENT DATA
ATTENDANCE = {
    "PYTHON": {
        "total": 40,
        "attended": 34
    },
    "AI": {
        "total": 30,
        "attended": 24
    },
    "DBMS": {
        "total": 35,
        "attended": 28
    }
}

QUESTIONS = [
    "What is my attendance in Python?",
    "What is my attendance percentage in AI?",
    "How many more Python classes do I need to attend to reach 90%?",
    "What is my total attendance percentage?"
]


def banner(system_name):
    print(
        f"\n=== {system_name} | "
        f"provider: {PROVIDER} | model: {MODEL} ===\n"
    )