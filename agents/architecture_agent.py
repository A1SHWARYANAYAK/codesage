from github_utils.llm import (
    get_gemini_client,
)
import json

from agents.schemas import (
    ArchitectureAnalysis,
)


def analyze_repository(context: dict):
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

        data = json.loads(
            response.text
        )

        return ArchitectureAnalysis(
            **data
        )

    except Exception as e:
        return {
            "error": str(e)
        }