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
    DependencyAnalysis,
)


def analyze_dependencies(
    repo_url: str,
):
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
You are a senior software architect.

Repository Metadata:
{context["metadata"]}

Languages:
{context["languages"]}

Dependency Files:
{context["dependency_files"]}

Repository Structure:
{context["structure"]}

Repository Map:
{context["repository_map"]}

Analyze the repository dependencies.

Evaluate:

- dependency complexity
- dependency maturity
- maintenance risk
- ecosystem stability
- dependency management practices

Rules:
1. Return ONLY valid JSON.
2. Do not use markdown.
3. Do not add explanations.
4. Do not use code fences.

Required format:

{{
  "dependency_risk_score": 0,
  "major_dependencies": [],
  "observations": [],
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

        return DependencyAnalysis(
            **data
        )

    except Exception as e:
        return {
            "error": str(e)
        }