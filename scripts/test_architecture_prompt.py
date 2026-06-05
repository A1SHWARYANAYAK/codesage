from github_utils.client import get_github_client
from github_utils.repository import (
    build_repository_context,
)
from github_utils.llm import (
    get_gemini_client,
)

# GitHub Client
github_client = get_github_client()

repo = github_client.get_repo(
    "langchain-ai/langgraph"
)

# Build Repository Context
context = build_repository_context(repo)

# Gemini Client
client = get_gemini_client()

# Architecture Analysis Prompt
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
5. Confidence score must be an integer between 1 and 10.

Required format:

{{
  "project_type": "",
  "architecture": "",
  "primary_technologies": [],
  "key_observations": [],
  "confidence_score": 0
}}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)