from agents.quality_agent import (
    analyze_quality,
)

result = analyze_quality(
    "https://github.com/langchain-ai/langgraph"
)

print(type(result))
print(result)