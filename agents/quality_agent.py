import json

from github_utils.llm import (
    get_gemini_client,
    clean_json_response,
)

from agents.schemas import (
    QualityAnalysis,
)

def analyze_quality(context: dict):
    client = get_gemini_client()

    prompt = f"""
You are a senior software engineer.

Repository Metadata:
{context["metadata"]}

Languages:
{context["languages"]}

README:
{context["readme"][:1000]}

Evaluate the repository quality.

Rules:
1. Return ONLY valid JSON.
2. Do not add explanations.
3. Do not add markdown.
4. Do not add code fences.

Required format:

{{
  "maintainability_score": 0,
  "documentation_score": 0,
  "code_organization_score": 0,
  "strengths": [],
  "weaknesses": []
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

        return QualityAnalysis(
            **data
        )

    except Exception as e:
        return {
            "error": str(e)
        }