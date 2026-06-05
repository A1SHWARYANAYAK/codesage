import sys

from agents.orchestrator import (
    run_analysis,
)


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

    print(f"\nRepository:\n{repo_url}")

    result = run_analysis(
        repo_url
    )

    print("\nARCHITECTURE")
    print("-" * 50)

    architecture = result.get(
        "architecture"
    )

    print(architecture)

    print("\nQUALITY")
    print("-" * 50)

    quality = result.get(
        "quality"
    )

    print(quality)

    print("\n" + "=" * 50)
    print("Analysis Complete")
    print("=" * 50)


if __name__ == "__main__":
    main()