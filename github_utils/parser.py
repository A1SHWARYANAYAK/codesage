from urllib.parse import urlparse


def parse_repository_url(url: str) -> dict:
    """
    Parse a GitHub repository URL.

    Example:
    https://github.com/langchain-ai/langgraph

    Returns:
    {
        "owner": "langchain-ai",
        "repo": "langgraph"
    }
    """

    parsed = urlparse(url)

    path_parts = parsed.path.strip("/").split("/")

    if len(path_parts) < 2:
        raise ValueError("Invalid GitHub repository URL")

    return {
        "owner": path_parts[0],
        "repo": path_parts[1]
    }

def parse_issue_url(url: str) -> dict:
    """
    Parse a GitHub issue URL.

    Example:
    https://github.com/langchain-ai/langgraph/issues/102

    Returns:
    {
        "owner": "langchain-ai",
        "repo": "langgraph",
        "issue_number": 102
    }
    """

    parsed = urlparse(url)

    path_parts = parsed.path.strip("/").split("/")

    if len(path_parts) < 4:
        raise ValueError("Invalid GitHub issue URL")

    if path_parts[2] != "issues":
        raise ValueError("URL is not a GitHub issue URL")

    return {
        "owner": path_parts[0],
        "repo": path_parts[1],
        "issue_number": int(path_parts[3]),
    }