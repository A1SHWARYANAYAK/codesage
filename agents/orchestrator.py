import time

from concurrent.futures import (
    ThreadPoolExecutor,
)

from agents.architecture_agent import (
    analyze_repository,
)

from agents.quality_agent import (
    analyze_quality,
)

from agents.security_agent import (
    analyze_security,
)

from agents.dependency_agent import (
    analyze_dependencies,
)


def run_analysis(repo_url: str):
    start_time = time.time()

    result = {}

    with ThreadPoolExecutor(
        max_workers=4
    ) as executor:

        architecture_future = (
            executor.submit(
                analyze_repository,
                repo_url,
            )
        )

        quality_future = (
            executor.submit(
                analyze_quality,
                repo_url,
            )
        )

        security_future = (
            executor.submit(
                analyze_security,
                repo_url,
            )
        )

        dependency_future = (
            executor.submit(
                analyze_dependencies,
                repo_url,
            )
        )

        try:
            result["architecture"] = (
                architecture_future.result()
            )
        except Exception as e:
            result["architecture"] = {
                "error": str(e)
            }

        try:
            result["quality"] = (
                quality_future.result()
            )
        except Exception as e:
            result["quality"] = {
                "error": str(e)
            }

        try:
            result["security"] = (
                security_future.result()
            )
        except Exception as e:
            result["security"] = {
                "error": str(e)
            }

        try:
            result["dependency"] = (
                dependency_future.result()
            )
        except Exception as e:
            result["dependency"] = {
                "error": str(e)
            }    

    result["execution_time"] = round(
        time.time() - start_time,
        2,
    )

    return result