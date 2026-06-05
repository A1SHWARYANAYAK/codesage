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

def get_repository_contents(repo):
    return repo.get_contents("")

def extract_repository_structure(repo):
    contents = repo.get_contents("")

    structure = {
        "files": [],
        "directories": [],
    }

    for item in contents:
        if item.type == "file":
            structure["files"].append(item.name)

        elif item.type == "dir":
            structure["directories"].append(item.name)

    return structure

def detect_dependency_files(repo):
    contents = repo.get_contents("")

    dependency_files = []

    targets = {
        "requirements.txt",
        "pyproject.toml",
        "setup.py",
        "package.json",
        "Dockerfile",
        "docker-compose.yml",
    }

    for item in contents:
        if item.name in targets:
            dependency_files.append(item.name)

    return dependency_files

def extract_repository_map(repo):
    repo_map = {}

    root_contents = repo.get_contents("")

    for item in root_contents:

        if item.type == "file":
            repo_map[item.name] = "file"

        elif item.type == "dir":
            repo_map[item.name] = []

            try:
                children = repo.get_contents(item.path)

                for child in children:
                    repo_map[item.name].append(
                        child.name
                    )

            except Exception:
                pass

    return repo_map