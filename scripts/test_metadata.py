from github_utils.client import get_github_client
from github_utils.repository import (
    extract_repository_metadata,
    extract_readme,
    extract_languages,
)

client = get_github_client()

repo = client.get_repo(
    "langchain-ai/langgraph"
)

metadata = extract_repository_metadata(repo)

print(metadata)

readme = extract_readme(repo)

print(f"README length: {len(readme)}")
print(readme[:300])

languages = extract_languages(repo)

print("\nLanguages:")
print(languages)