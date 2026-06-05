from agents.schemas import (
    DependencyAnalysis,
)

analysis = DependencyAnalysis(
    dependency_risk_score=8.5,
    major_dependencies=[
        "langchain",
        "pydantic",
    ],
    observations=[
        "Uses mature libraries"
    ],
    recommendations=[
        "Pin dependency versions"
    ],
)

print(analysis)