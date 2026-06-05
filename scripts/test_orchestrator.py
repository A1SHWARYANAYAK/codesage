from agents.orchestrator import (
    run_analysis,
)

result = run_analysis(
    "https://github.com/langchain-ai/langgraph"
)

print(type(result))

print("\nARCHITECTURE:")
print(result["architecture"])

print("\nQUALITY:")
print(result["quality"])