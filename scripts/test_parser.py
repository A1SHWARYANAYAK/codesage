from github.parser import (
    parse_repository_url,
    parse_issue_url,
)

repo_url = "https://github.com/langchain-ai/langgraph"

issue_url = (
    "https://github.com/"
    "langchain-ai/"
    "langgraph/"
    "issues/102"
)

print(parse_repository_url(repo_url))
print(parse_issue_url(issue_url))