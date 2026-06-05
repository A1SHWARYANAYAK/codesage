def extract_repository_metadata(repo):
    return {
        "name": repo.name,
        "full_name": repo.full_name,
        "description": repo.description,
        "stars": repo.stargazers_count,
        "language": repo.language,
        "topics": repo.get_topics(),
    }

def extract_readme(repo):
    try:
        readme = repo.get_readme()

        return readme.decoded_content.decode(
            "utf-8",
            errors="ignore"
        )

    except Exception:
        return ""
    
def extract_languages(repo):
    return repo.get_languages()    

def build_repository_context(repo):
    return {
        "metadata": extract_repository_metadata(repo),
        "readme": extract_readme(repo),
        "languages": {
            key: value
            for key, value in extract_languages(repo).items()
            if key != "url"
        },
    }