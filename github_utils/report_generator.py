from agents.schemas import (
    ArchitectureAnalysis,
    QualityAnalysis,
)


def generate_markdown_report(
    result: dict,
    output_file: str,
):
    lines = []

    lines.append("# CodeSage Analysis Report\n")

    architecture = result.get(
        "architecture"
    )

    if isinstance(
        architecture,
        ArchitectureAnalysis,
    ):
        lines.append("## Architecture\n")

        lines.append(
            f"**Project Type:** {architecture.project_type}\n"
        )

        lines.append(
            f"**Confidence Score:** {architecture.confidence_score}\n"
        )

        lines.append(
            f"**Architecture:**\n{architecture.architecture}\n"
        )

        lines.append(
            "### Primary Technologies\n"
        )

        for tech in architecture.primary_technologies:
            lines.append(f"- {tech}")

        lines.append("")

        lines.append(
            "### Key Observations\n"
        )

        for observation in architecture.key_observations:
            lines.append(
                f"- {observation}"
            )

        lines.append("")

    quality = result.get(
        "quality"
    )

    if isinstance(
        quality,
        QualityAnalysis,
    ):
        lines.append("## Quality\n")

        lines.append(
            f"**Maintainability Score:** {quality.maintainability_score}\n"
        )

        lines.append(
            f"**Documentation Score:** {quality.documentation_score}\n"
        )

        lines.append(
            f"**Code Organization Score:** {quality.code_organization_score}\n"
        )

        lines.append(
            "### Strengths\n"
        )

        for strength in quality.strengths:
            lines.append(
                f"- {strength}"
            )

        lines.append("")

        lines.append(
            "### Weaknesses\n"
        )

        for weakness in quality.weaknesses:
            lines.append(
                f"- {weakness}"
            )

        lines.append("")

    if len(lines) == 1:
        lines.append(
            "No analysis results were available."
        )    

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as f:
        f.write(
            "\n".join(lines)
        )