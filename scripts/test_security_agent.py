from agents.security_agent import (
    analyze_security,
)

result = analyze_security(
    "https://github.com/langchain-ai/langgraph"
)

print(type(result))
print(result)