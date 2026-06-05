import json

from github_utils.llm import (
    get_gemini_client,
    clean_json_response,
)

from agents.schemas import (
    SecurityAnalysis,
)


def analyze_security(context: dict):
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