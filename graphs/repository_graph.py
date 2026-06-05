from typing import TypedDict

from github_utils.client import (
    get_github_client,
)

from github_utils.parser import (
    parse_repository_url,
)

from github_utils.repository import (
    build_repository_context,
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

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

class RepositoryState(TypedDict):
    repo_url: str

    context: dict

    architecture: object
    quality: object
    security: object
    dependency: object

def build_context_node(
    state: RepositoryState,
):
    github_client = get_github_client()

    parsed = parse_repository_url(
        state["repo_url"]
    )

    repo = github_client.get_repo(
        f"{parsed['owner']}/{parsed['repo']}"
    )

    context = build_repository_context(
        repo
    )

    return {
        "context": context
    }    

def architecture_node(
    state: RepositoryState,
):
    return {
        "architecture": analyze_repository(
            state["context"]
        )
    }


def quality_node(
    state: RepositoryState,
):
    return {
        "quality": analyze_quality(
            state["context"]
        )
    }


def security_node(
    state: RepositoryState,
):
    return {
        "security": analyze_security(
            state["context"]
        )
    }


def dependency_node(
    state: RepositoryState,
):
    return {
        "dependency": analyze_dependencies(
            state["context"]
        )
    }

graph = StateGraph(
    RepositoryState
)

graph.add_node(
    "build_context",
    build_context_node,
)

graph.add_node(
    "architecture",
    architecture_node,
)

graph.add_node(
    "quality",
    quality_node,
)

graph.add_node(
    "security",
    security_node,
)

graph.add_node(
    "dependency",
    dependency_node,
)

graph.add_edge(
    START,
    "build_context",
)

graph.add_edge(
    "build_context",
    "architecture",
)

graph.add_edge(
    "architecture",
    "quality",
)

graph.add_edge(
    "quality",
    "security",
)

graph.add_edge(
    "security",
    "dependency",
)

graph.add_edge(
    "dependency",
    END,
)

repository_graph = graph.compile()