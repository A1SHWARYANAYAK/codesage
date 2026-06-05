from github_utils.client import get_github_client
from github_utils.parser import (
    parse_repository_url,
)
from github_utils.repository import (
    build_repository_context,
)
from github_utils.llm import (
    get_gemini_client,
)


def analyze_repository(repo_url: str):
    github_client = get_github_client()

    parsed = parse_repository_url(repo_url)

    repo = github_client.get_repo(
        f"{parsed['owner']}/{parsed['repo']}"
    )

    context = build_repository_context(repo)

    client = get_gemini_client()

    prompt = f"""
You are a software architecture reviewer.

Repository Metadata:
{context["metadata"]}

Languages:
{context["languages"]}

README:
{context["readme"][:1000]}

Analyze this repository.

Rules:
1. Return ONLY valid JSON.
2. Do not use markdown.
3. Do not use code fences.
4. Do not add explanations before or after the JSON.

Required format:

{{
  "project_type": "",
  "architecture": "",
  "primary_technologies": [],
  "key_observations": [],
  "confidence_score": 0
}}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return {
            "error": str(e)
        }