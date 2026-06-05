from agents.schemas import (
    QualityAnalysis,
)

analysis = QualityAnalysis(
    maintainability_score=8.5,
    documentation_score=9.0,
    code_organization_score=8.0,
    strengths=[
        "Good documentation",
        "Modular design",
    ],
    weaknesses=[
        "Limited tests",
    ],
)

print(analysis)