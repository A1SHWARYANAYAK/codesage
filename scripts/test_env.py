import os

from dotenv import load_dotenv

load_dotenv()

print(
    "GitHub Key Loaded:",
    bool(os.getenv("GITHUB_TOKEN"))
)

print(
    "Gemini Key Loaded:",
    bool(os.getenv("GEMINI_API_KEY"))
)