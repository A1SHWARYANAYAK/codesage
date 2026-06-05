from agents.schemas import (
    SecurityAnalysis,
)

analysis = SecurityAnalysis(
    security_score=8.5,
    findings=[
        "No exposed secrets detected"
    ],
    recommendations=[
        "Enable dependency scanning"
    ],
)

print(analysis)