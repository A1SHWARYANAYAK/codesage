from graphs.repository_graph import (
    repository_graph,
)

result = repository_graph.invoke(
    {
        "repo_url":
        "https://github.com/langchain-ai/langgraph"
    }
)

print(type(result))
print(result.keys())