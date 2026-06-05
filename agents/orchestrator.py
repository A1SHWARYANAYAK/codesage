from graphs.repository_graph import (
    repository_graph,
)


def run_analysis(
    repo_url: str,
):
    return repository_graph.invoke(
        {
            "repo_url": repo_url
        }
    )