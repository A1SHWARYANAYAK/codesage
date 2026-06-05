from github_utils.llm import (
    get_gemini_client,
)

client = get_gemini_client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Reply with exactly: CodeSage Working",
)

print(response.text)