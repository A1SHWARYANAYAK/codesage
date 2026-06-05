from github_utils.client import get_github_client

client = get_github_client()

repo = client.get_repo(
    "langchain-ai/langgraph"
)

print(repo.full_name)
print(repo.description)
print(repo.stargazers_count)