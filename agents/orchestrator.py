from agents.architecture_agent import (
    analyze_repository,
)

from agents.quality_agent import (
    analyze_quality,
)


def run_analysis(repo_url: str):
    result = {}

    try:
        result["architecture"] = (
            analyze_repository(repo_url)
        )
    except Exception as e:
        result["architecture"] = {
            "error": str(e)
        }

    try:
        result["quality"] = (
            analyze_quality(repo_url)
        )
    except Exception as e:
        result["quality"] = {
            "error": str(e)
        }

    return result