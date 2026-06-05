import os

from dotenv import load_dotenv
from github import Github

load_dotenv()


def get_github_client():
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise ValueError(
            "GITHUB_TOKEN not found in environment variables"
        )

    return Github(token)