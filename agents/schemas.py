from pydantic import BaseModel


class ArchitectureAnalysis(BaseModel):
    project_type: str
    architecture: str
    primary_technologies: list[str]
    key_observations: list[str]
    confidence_score: float

class QualityAnalysis(BaseModel):
    maintainability_score: float
    documentation_score: float
    code_organization_score: float

    strengths: list[str]
    weaknesses: list[str]    