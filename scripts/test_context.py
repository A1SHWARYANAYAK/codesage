from github_utils.client import get_github_client
from github_utils.repository import (
    build_repository_context,
)

client = get_github_client()

repo = client.get_repo(
    "langchain-ai/langgraph"
)

context = build_repository_context(repo)

print(context.keys())

print("\nMetadata:")
print(context["metadata"])

print("\nLanguages:")
print(context["languages"])

print("\nREADME length:")
print(len(context["readme"]))