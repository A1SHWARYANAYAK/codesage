# CodeSage

CodeSage is a multi-agent AI system that analyzes GitHub repositories using specialized LLM-powered agents.

The platform extracts repository intelligence from GitHub and produces structured architecture and software quality assessments through an orchestrated agent workflow.

Built to demonstrate:

* Agent orchestration
* Structured LLM outputs
* GitHub intelligence pipelines
* Multi-agent software analysis
* Repository understanding workflows

---

## Features

* GitHub repository intelligence
* Repository metadata extraction
* README analysis
* Architecture analysis agent
* Quality analysis agent
* Structured outputs using Pydantic
* Multi-agent orchestration workflow
* Command-line interface (CLI)
* Extensible agent architecture

---

## Quick Demo

```bash
python main.py https://github.com/langchain-ai/langgraph
```

Example Output:

```text
==================================================
CodeSage Repository Analysis
==================================================

Repository:
https://github.com/langchain-ai/langgraph

ARCHITECTURE
--------------------------------------------------
Project Type:
AI Agent Orchestration Framework

QUALITY
--------------------------------------------------
Maintainability Score: 95
Documentation Score: 90

==================================================
Analysis Complete
==================================================
```

---

## Why CodeSage?

Modern repositories contain valuable architectural and engineering signals that are difficult to evaluate quickly.

CodeSage automates repository understanding by combining GitHub intelligence with specialized AI agents that focus on different aspects of software analysis.

Instead of generating a single generic summary, CodeSage uses multiple agents to produce structured assessments that can be extended over time.

---

## Architecture

```text
GitHub Repository
        │
        ▼
Repository Context Builder
        │
        ▼
 ┌─────────────────────┐
 │ Architecture Agent  │
 └─────────────────────┘
        │
        ▼
 ┌─────────────────────┐
 │   Quality Agent     │
 └─────────────────────┘
        │
        ▼
     Orchestrator
        │
        ▼
   Final Analysis
```

---

## Project Structure

```text
codesage/
│
├── agents/
│   ├── architecture_agent.py
│   ├── quality_agent.py
│   ├── orchestrator.py
│   └── schemas.py
│
├── github_utils/
│   ├── client.py
│   ├── parser.py
│   ├── repository.py
│   └── llm.py
│
├── scripts/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/A1SHWARYANAYAK/codesage.git

cd codesage
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GITHUB_TOKEN=your_github_token
GEMINI_API_KEY=your_gemini_api_key
```

### GitHub Token

Generate a Personal Access Token from GitHub and provide access to public repositories.

### Gemini API Key

Generate an API key from Google AI Studio and add it to your environment file.

---

## Usage

Analyze a repository:

```bash
python main.py https://github.com/langchain-ai/langgraph
```

---

## Example Workflow

```text
Repository URL
      ↓
GitHub API
      ↓
Repository Context
      ↓
Architecture Analysis
      ↓
Quality Analysis
      ↓
Combined Report
```

---

## Current Agents

### Architecture Agent

Analyzes:

* Project type
* Software architecture
* Primary technologies
* Key technical observations
* Architecture confidence score

Returns:

```json
{
  "project_type": "...",
  "architecture": "...",
  "primary_technologies": [],
  "key_observations": [],
  "confidence_score": 0
}
```

### Quality Agent

Analyzes:

* Maintainability
* Documentation quality
* Code organization
* Strengths
* Weaknesses

Returns:

```json
{
  "maintainability_score": 0,
  "documentation_score": 0,
  "code_organization_score": 0,
  "strengths": [],
  "weaknesses": []
}
```

---

## Tech Stack

* Python
* Gemini API
* PyGithub
* Pydantic
* python-dotenv

---

## Future Improvements

* Security Analysis Agent
* Dependency Risk Agent
* Parallel Agent Execution
* Markdown Report Generation
* JSON Export
* LangGraph-based Agent Workflow
* Web Dashboard
* Repository Comparison Mode

---

## Skills Demonstrated

This project demonstrates:

* AI Agent Design
* Multi-Agent Systems
* LLM Integration
* Structured Output Generation
* GitHub API Integration
* Software Architecture Analysis
* Python Backend Development
* Prompt Engineering
* Pydantic Data Validation
* Workflow Orchestration

---

## License

MIT License
