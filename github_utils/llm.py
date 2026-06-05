import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_gemini_client():
    api_key = os.getenv(
        "GEMINI_API_KEY"
    )

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found"
        )

    return genai.Client(
        api_key=api_key
    )


def clean_json_response(
    text: str
) -> str:
    text = text.strip()

    if text.startswith(
        "```json"
    ):
        text = text.replace(
            "```json",
            "",
            1,
        )

    if text.endswith(
        "```"
    ):
        text = text[:-3]

    return text.strip()