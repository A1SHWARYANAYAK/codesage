import sys

from agents.orchestrator import (
    run_analysis,
)

from agents.schemas import (
    ArchitectureAnalysis,
    QualityAnalysis,
)


def print_architecture(
    analysis: ArchitectureAnalysis,
):
    print("\nARCHITECTURE")
    print("-" * 50)

    print(
        f"Project Type: {analysis.project_type}"
    )

    print(
        f"\nConfidence Score: "
        f"{analysis.confidence_score}"
    )

    print(
        f"\nArchitecture:\n"
        f"{analysis.architecture}"
    )

    print(
        "\nPrimary Technologies:"
    )

    for tech in analysis.primary_technologies:
        print(f"- {tech}")

    print(
        "\nKey Observations:"
    )

    for observation in analysis.key_observations:
        print(f"- {observation}")


def print_quality(
    analysis: QualityAnalysis,
):
    print("\nQUALITY")
    print("-" * 50)

    print(
        f"Maintainability Score: "
        f"{analysis.maintainability_score}"
    )

    print(
        f"Documentation Score: "
        f"{analysis.documentation_score}"
    )

    print(
        f"Code Organization Score: "
        f"{analysis.code_organization_score}"
    )

    print("\nStrengths:")

    for strength in analysis.strengths:
        print(f"- {strength}")

    print("\nWeaknesses:")

    for weakness in analysis.weaknesses:
        print(f"- {weakness}")


def main():
    if len(sys.argv) != 2:
        print(
            "Usage: python main.py <github_repo_url>"
        )
        return

    repo_url = sys.argv[1]

    print("\n" + "=" * 50)
    print("CodeSage Repository Analysis")
    print("=" * 50)

    print(
        f"\nRepository:\n{repo_url}"
    )

    result = run_analysis(
        repo_url
    )

    architecture = result.get(
        "architecture"
    )

    architecture_success = False

    if isinstance(
        architecture,
        ArchitectureAnalysis,
    ):
        architecture_success = True

        print_architecture(
            architecture
        )

    quality = result.get(
        "quality"
    )

    quality_success = False

    if isinstance(
        quality,
        QualityAnalysis,
    ):
        quality_success = True

        print_quality(
            quality
        )

    successful = 0

    if architecture_success:
        successful += 1

    if quality_success:
        successful += 1

    failed = 2 - successful

    print("\n" + "-" * 50)

    if successful == 0:
        print(
            "All analyses are temporarily unavailable."
        )
        print(
            "Please try again in a minute."
        )

    else:
        print(
            f"{successful} analysis completed successfully"
        )

        if failed:
            print(
                f"{failed} analysis unavailable"
            ) 

    print("\n" + "=" * 50)
    print("Analysis Complete")
    print("=" * 50)


if __name__ == "__main__":
    main()