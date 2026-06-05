from agents.orchestrator import (
    run_analysis,
)

from github_utils.report_generator import (
    generate_markdown_report,
)

result = run_analysis(
    "https://github.com/langchain-ai/langgraph"
)

generate_markdown_report(
    result,
    "reports/langgraph_report.md",
)

print(
    "Report generated successfully."
)