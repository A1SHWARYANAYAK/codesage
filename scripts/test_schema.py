from agents.schemas import (
    ArchitectureAnalysis,
)

analysis = ArchitectureAnalysis(
    project_type="Framework",
    architecture="Monorepo",
    primary_technologies=[
        "Python",
        "Pydantic",
    ],
    key_observations=[
        "Uses agents",
    ],
    confidence_score=0.95,
)

print(analysis)