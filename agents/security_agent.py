import json

from github_utils.client import get_github_client
from github_utils.parser import (
    parse_repository_url,
)
from github_utils.repository import (
    build_repository_context,
)
from github_utils.llm import (
    get_gemini_client,
    clean_json_response,
)

from agents.schemas import (
    SecurityAnalysis,
)


def analyze_security(repo_url: str):
    github_client = get_github_client()

    parsed = parse_repository_url(
        repo_url
    )

    repo = github_client.get_repo(
        f"{parsed['owner']}/{parsed['repo']}"
    )

    context = build_repository_context(
        repo
    )

    client = get_gemini_client()

    prompt = f"""
You are a senior application security engineer.

Repository Metadata:
{context["metadata"]}

Languages:
{context["languages"]}

README:
{context["readme"][:1000]}

Evaluate the repository security posture.

Consider:
- dependency risks
- secret exposure risks
- CI/CD practices
- security maturity
- repository hygiene

Rules:
1. Return ONLY valid JSON.
2. Do not add markdown.
3. Do not add explanations.
4. Do not use code fences.

Required format:

{{
  "security_score": 0,
  "findings": [],
  "recommendations": []
}}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        cleaned = clean_json_response(
            response.text
        )

        data = json.loads(
            cleaned
        )

        return SecurityAnalysis(
            **data
        )

    except Exception as e:
        return {
            "error": str(e)
        }