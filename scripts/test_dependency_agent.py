from agents.dependency_agent import (
    analyze_dependencies,
)

result = analyze_dependencies(
    "https://github.com/langchain-ai/langgraph"
)

print(type(result))
print(result)