# CodeSage

CodeSage is a multi-agent repository analysis system that uses GitHub data and Large Language Models (LLMs) to automatically analyze software repositories.

Given a GitHub repository URL, CodeSage extracts repository metadata, README content, and project structure, then uses specialized AI agents to generate architecture, quality, and security assessments.

## Features

* GitHub repository intelligence
* Repository metadata extraction
* README analysis
* Architecture analysis agent
* Quality analysis agent
* Security analysis agent
* Parallel multi-agent execution
* Structured outputs using Pydantic
* Multi-agent orchestration workflow
* Markdown report generation
* Command-line interface (CLI)
* Execution time tracking

## Architecture

```text
GitHub Repository
        │
        ▼
Repository Context Builder
        │
        ▼
 ┌───────────────────┐
 │ Architecture Agent│
 └───────────────────┘
        │
 ┌───────────────────┐
 │   Quality Agent   │
 └───────────────────┘
        │
 ┌───────────────────┐
 │  Security Agent   │
 └───────────────────┘
        │
        ▼
 Parallel Orchestrator
        │
        ▼
   Final Analysis
        │
        ▼
 Markdown Report
```

## Project Structure

```text
codesage/
│
├── agents/
│   ├── architecture_agent.py
│   ├── quality_agent.py
│   ├── security_agent.py
│   ├── orchestrator.py
│   └── schemas.py
│
├── github_utils/
│   ├── client.py
│   ├── parser.py
│   ├── repository.py
│   ├── llm.py
│   └── report_generator.py
│
├── reports/
│
├── scripts/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/A1SHWARYANAYAK/codesage.git

cd codesage

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token
GEMINI_API_KEY=your_gemini_api_key
```

## Usage

```bash
python main.py https://github.com/langchain-ai/langgraph
```

## Example Workflow

```text
Repository URL
      ↓
GitHub API
      ↓
Repository Context
      ↓
 ┌────────────────┐
 │ Architecture   │
 └────────────────┘
      ↓
 ┌────────────────┐
 │ Quality        │
 └────────────────┘
      ↓
 ┌────────────────┐
 │ Security       │
 └────────────────┘
      ↓
Parallel Aggregation
      ↓
Combined Report
```

## Current Agents

### Architecture Agent

Analyzes:

* Project type
* Software architecture
* Primary technologies
* Key technical observations

### Quality Agent

Analyzes:

* Maintainability
* Documentation quality
* Code organization
* Strengths
* Weaknesses

### Security Agent

Analyzes:

* Security posture
* Dependency risks
* Secret exposure risks
* Repository hygiene
* Security recommendations

## Example Output

```text
==================================================
CodeSage Repository Analysis
==================================================

Repository:
https://github.com/langchain-ai/langgraph

Execution Time: 3.42 seconds

ARCHITECTURE
--------------------------------------------------
Project Type: AI Agent Framework
...

QUALITY
--------------------------------------------------
Maintainability Score: 9.0
...

SECURITY
--------------------------------------------------
Security Score: 8.5
...

==================================================
Analysis Complete
==================================================
```

## Tech Stack

* Python
* Gemini API
* PyGithub
* Pydantic
* python-dotenv
* concurrent.futures

## Future Improvements

* Dependency analysis agent
* License compliance agent
* JSON export
* PDF report generation
* LangGraph orchestration
* Web dashboard
* Additional repository intelligence agents

## License

MIT
