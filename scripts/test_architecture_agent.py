from agents.architecture_agent import (
    analyze_repository,
)

result = analyze_repository(
    "https://github.com/langchain-ai/langgraph"
)

print(type(result))
print(result)