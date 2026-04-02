# 🔬 MCP Ecosystem Scanner

> The most comprehensive automated registry of [Model Context Protocol](https://modelcontextprotocol.io/) servers.
> Discovers, validates, and quality-scores every MCP server on GitHub — daily.

## Why This Exists

MCP is the open standard that lets AI agents (Claude, GPT, Gemini, etc.) connect to external tools and data.
The ecosystem is exploding — but discovery is fragmented. The official registry is young, awesome-lists are
manually curated, and there's no automated way to know which servers are well-maintained vs. abandoned.

This scanner crawls GitHub daily, validates each repo as a genuine MCP server, and scores its quality
based on documentation, tests, CI, maintenance activity, and community adoption.

**Run the first scan manually from the Actions tab to populate the dashboard.**

## How It Works

1. **Discovery** — Searches GitHub with multiple queries to find MCP server repos
2. **Validation** — Checks dependencies, README keywords, and repo metadata to confirm it's a real MCP server
3. **Analysis** — Scores each server on README, license, tests, CI, releases, stars, recency, and issue health
4. **Dashboard** — Generates this README with a ranked registry, category breakdowns, and trend data

## Running Locally

```bash
pip install -r requirements.txt
export GITHUB_TOKEN=ghp_your_token_here
python scanner.py
python dashboard.py
```

---

*Powered by GitHub Actions · Scanned daily*

*Built to solve the MCP ecosystem's [discovery gap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/).*
