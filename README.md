# 🔬 MCP Ecosystem Scanner

[![Daily Scan](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner/actions/workflows/scan.yml/badge.svg)](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner/actions/workflows/scan.yml)
[![MCP Servers](https://img.shields.io/badge/MCP_servers-453-blue)](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/mcp-ecosystem-scanner?style=social)](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner/stargazers)

> The most comprehensive automated registry of [Model Context Protocol](https://modelcontextprotocol.io/) servers.
> Discovers, validates, and quality-scores every MCP server on GitHub — daily.

> **453** servers catalogued | **10** categories | Last scan: **2026-07-27 10:54 UTC**

## Why This Exists

MCP is the open standard that lets AI agents (Claude, GPT, Gemini, etc.) connect to external tools and data.
The ecosystem is exploding — but discovery is fragmented. The official registry is young, awesome-lists are
manually curated, and there's no automated way to know which servers are well-maintained vs. abandoned.

This scanner crawls GitHub daily, validates each repo as a genuine MCP server, and scores its quality
based on documentation, tests, CI, maintenance activity, and community adoption.

---

## 📊 Ecosystem Overview

| Metric | Value |
|--------|-------|
| Total MCP Servers | **453** |
| Combined GitHub Stars | **1.3M** |
| Average Quality Score | **16.3/100** |
| New This Month | **0** |
| Categories | **10** |

**Languages:** **TypeScript**: 207 · **Python**: 202 · **Go**: 13 · **JavaScript**: 11 · **Unknown**: 8 · **C#**: 3

**Transports:** `stdio`: 237 · `sse`: 347 · `streamable-http`: 115 · `unknown`: 69

---

## 🏆 Top Servers by Quality Score

| Rank | Server | Quality | Stars | Description | Category | Transport |
|------|--------|---------|-------|-------------|----------|-----------|
| 1 | [private-gpt](https://github.com/zylon-ai/private-gpt) | █████████░ **90** | 57.4k | Complete API layer for private AI applications on local models: RAG, s | `ai-ml` | `SSE` |
| 2 | [ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | █████████░ **90** | 4.1k | The Unofficial and Awesome Home Assistant MCP Server | `dev-tools` | `stdio` `SSE` `HTTP` |
| 3 | [semiotic](https://github.com/nteract/semiotic) | █████████░ **90** | 2.7k | React data visualization library for streaming, networks, and AI-assis | `other` | `stdio` `SSE` |
| 4 | [playwright-mcp](https://github.com/microsoft/playwright-mcp) | █████████░ **90** | 35.5k | Playwright MCP server | `web` | `stdio` `SSE` |
| 5 | [gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli) | █████████░ **90** | 5.6k | Programmatic access to Gemini Notebook - via command-line interface (C | `other` | `SSE` |
| 6 | [mcporter](https://github.com/openclaw/mcporter) | █████████░ **90** | 4.8k | Call MCPs via TypeScript, masquerading as simple TypeScript API. Or pa | `other` | `stdio` `SSE` `HTTP` |
| 7 | [fast-agent](https://github.com/evalstate/fast-agent) | █████████░ **89** | 3.9k | Code, Build and Evaluate agents - excellent Model and Skills/MCP/ACP/A | `other` | `stdio` `SSE` `HTTP` |
| 8 | [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | █████████░ **89** | 6.5k | MCP Server for Computer Use in Windows | `other` | `stdio` `SSE` `HTTP` |
| 9 | [ghidra-mcp](https://github.com/bethington/ghidra-mcp) | █████████░ **89** | 3.0k | Ghidra MCP Server — 200+ MCP tools for AI-powered reverse engineering. | `dev-tools` | `stdio` `SSE` `HTTP` |
| 10 | [agent-scan](https://github.com/snyk/agent-scan) | █████████░ **89** | 2.8k | Security scanner for AI agents, MCP servers and agent skills. | `other` | `stdio` `SSE` |
| 11 | [context-mode](https://github.com/mksglu/context-mode) | █████████░ **89** | 19.4k | Context window optimization for AI coding agents. Sandboxes tool outpu | `files` | `stdio` `SSE` |
| 12 | [arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | █████████░ **89** | 3.0k | A Model Context Protocol server for searching and analyzing arXiv pape | `ai-ml` | `stdio` `HTTP` |
| 13 | [fastmcp](https://github.com/PrefectHQ/fastmcp) | █████████░ **89** | 26.9k | 🚀 The fast, Pythonic way to build MCP servers and clients. | `ai-ml` | `SSE` |
| 14 | [gpt-researcher](https://github.com/assafelovic/gpt-researcher) | █████████░ **88** | 28.7k | An autonomous agent that conducts deep research on any data using any  | `ai-ml` | `SSE` |
| 15 | [ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) | █████████░ **88** | 10.8k | AI-powered reverse engineering assistant that bridges IDA Pro with lan | `other` | `stdio` `SSE` |
| 16 | [csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | █████████░ **88** | 4.4k | The official C# SDK for Model Context Protocol servers and clients. Ma | `dev-tools` | `SSE` |
| 17 | [registry](https://github.com/modelcontextprotocol/registry) | █████████░ **88** | 7.1k | A community driven registry service for Model Context Protocol (MCP) s | `files` | `SSE` |
| 18 | [core](https://github.com/opensumi/core) | █████████░ **88** | 3.6k | A framework helps you quickly build AI Native IDE products. MCP Client | `other` | — |
| 19 | [python-sdk](https://github.com/modelcontextprotocol/python-sdk) | █████████░ **88** | 23.7k | The official Python SDK for Model Context Protocol servers and clients | `dev-tools` | `stdio` `SSE` `HTTP` |
| 20 | [CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | █████████░ **88** | 4.0k | An MCP server plus a CLI tool that indexes local code into a graph dat | `data` | `SSE` |
| 21 | [EvoScientist](https://github.com/EvoScientist/EvoScientist) | █████████░ **88** | 4.4k | 🔬 Harness Vibe Research with Self-evolving AI Scientists | `dev-tools` | `SSE` |
| 22 | [google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | █████████░ **88** | 2.9k | Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tas | `productivity` | `stdio` `SSE` `HTTP` |
| 23 | [linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server) | █████████░ **88** | 2.9k | Open-source MCP server for LinkedIn. Give Claude and any MCP-compatibl | `ai-ml` | `stdio` `SSE` `HTTP` |
| 24 | [critical](https://github.com/addyosmani/critical) | █████████░ **88** | 10.3k | Extract & Inline Critical-path CSS in HTML pages | `other` | `stdio` `SSE` |
| 25 | [optillm](https://github.com/algorithmicsuperintelligence/optillm) | █████████░ **88** | 4.2k | Optimizing inference proxy for LLMs | `ai-ml` | `stdio` `SSE` |
| 26 | [Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | █████████░ **87** | 15.5k | MCP server to provide Figma layout information to AI coding agents lik | `other` | `stdio` |
| 27 | [mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | █████████░ **87** | 5.6k | MCP server for Atlassian tools (Confluence, Jira) | `productivity` | `SSE` |
| 28 | [tabularis](https://github.com/TabularisDB/tabularis) | █████████░ **87** | 3.9k | Open-source desktop SQL workspace for PostgreSQL, MySQL/MariaDB, SQLit | `data` | `stdio` |
| 29 | [typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | █████████░ **87** | 13.0k | The official TypeScript SDK for Model Context Protocol servers and cli | `dev-tools` | `stdio` `HTTP` |
| 30 | [mcp-context-forge](https://github.com/IBM/mcp-context-forge) | █████████░ **87** | 4.1k | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, | `dev-tools` | `stdio` `SSE` `HTTP` |

---

## 📂 Servers by Category

### Ai Ml (79 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [headroom](https://github.com/headroomlabs-ai/headroom) | ⭐ 62.7k | 86 | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20 |
| [private-gpt](https://github.com/zylon-ai/private-gpt) | ⭐ 57.4k | 90 | Complete API layer for private AI applications on local models: RAG, skills, too |
| [gpt-researcher](https://github.com/assafelovic/gpt-researcher) | ⭐ 28.7k | 88 | An autonomous agent that conducts deep research on any data using any LLM provid |
| [fastmcp](https://github.com/PrefectHQ/fastmcp) | ⭐ 26.9k | 89 | 🚀 The fast, Pythonic way to build MCP servers and clients. |
| [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | ⭐ 16.9k | 70 | Agent framework and applications built upon Qwen>=3.0, featuring Function Callin |
| [DeepCode](https://github.com/HKUDS/DeepCode) | ⭐ 16.1k | 86 | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |
| [pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server) | ⭐ 11.7k | 72 | The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter  |
| [mcp-use](https://github.com/mcp-use/mcp-use) | ⭐ 10.4k | 74 | The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Serve |
| [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | ⭐ 8.5k | 71 | Build effective agents using Model Context Protocol and simple workflow patterns |
| [awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | ⭐ 6.0k | 36 | Tutorials, Guides and Agent Skills Directories |
| [awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) | ⭐ 5.7k | 32 | Awesome MCP Servers - A curated list of Model Context Protocol servers |
| [claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) | ⭐ 5.6k | 72 | The most comprehensive Claude Code guide: agentic workflows, hooks, skills, MCP  |
| [5ire](https://github.com/nanbingxyz/5ire) | ⭐ 5.3k | 87 | 5ire is a cross-platform desktop AI assistant, MCP client. It compatible with ma |
| [mcp-ui](https://github.com/MCP-UI-Org/mcp-ui) | ⭐ 5.0k | 66 | UI over MCP. Create next-gen UI experiences with the protocol and SDK! |
| [claude-code-guide](https://github.com/zebbern/claude-code-guide) | ⭐ 4.4k | 62 | Claude Code Guide - Setup, Commands, workflows, agents, skills & tips-n-tricks g |
| *...and 64 more* | | | |

### Cloud (7 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [mcp](https://github.com/awslabs/mcp) | ⭐ 9.5k | 72 | Open source MCP Servers for AWS |
| [mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | ⭐ 4.0k | 71 | — |
| [skills](https://github.com/microsoft/skills) | ⭐ 2.8k | 74 | Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents |
| [azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) | ⭐ 1.9k | 0 | The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to  |
| [mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) | ⭐ 381 | 0 | An MCP server for Azure DevOps |
| [sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers) | ⭐ 239 | 0 | Sample implementations of AI Agents and MCP Servers running on AWS Serverless co |
| [Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server) | ⭐ 234 | 0 | Creates a simple MCP tool server with "streaming" HTTP. |

### Data (30 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | ⭐ 4.0k | 88 | An MCP server plus a CLI tool that indexes local code into a graph database to p |
| [tabularis](https://github.com/TabularisDB/tabularis) | ⭐ 3.9k | 87 | Open-source desktop SQL workspace for PostgreSQL, MySQL/MariaDB, SQLite and 15+  |
| [dbhub](https://github.com/bytebase/dbhub) | ⭐ 3.2k | 75 | Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Se |
| [mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) | ⭐ 2.0k | 0 | A Model Context Protocol server that provides read-only access to MySQL database |
| [pg-aiguide](https://github.com/timescale/pg-aiguide) | ⭐ 1.8k | 0 | MCP server and Claude plugin for Postgres skills and documentation. Helps AI cod |
| [mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) | ⭐ 1.3k | 0 | A Model Context Protocol (MCP) server that enables secure interaction with MySQL |
| [nocturne_memory](https://github.com/Dataojitori/nocturne_memory) | ⭐ 1.3k | 0 | A lightweight, rollbackable, and visual Long-Term Memory Server for MCP Agents.  |
| [mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) | ⭐ 1.1k | 0 | A Model Context Protocol server to connect to MongoDB databases and MongoDB Atla |
| [yargi-mcp](https://github.com/saidsurucu/yargi-mcp) | ⭐ 1.1k | 0 | MCP Server For Turkish Legal Databases |
| [mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) | ⭐ 983 | 0 | Neo4j Labs Model Context Protocol servers |
| [mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry) | ⭐ 832 | 0 | Enterprise-ready MCP Gateway & Registry that centralizes AI development tools wi |
| [supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server) | ⭐ 830 | 0 | Query MCP enables end-to-end management of Supabase via chat interface: read & w |
| [mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) | ⭐ 752 | 0 | A growing collection of MCP servers bringing offensive security tools to AI assi |
| [mcp-for-security](https://github.com/cyproxio/mcp-for-security) | ⭐ 626 | 0 | MCP for Security: A collection of Model Context Protocol servers for popular sec |
| [mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) | ⭐ 619 | 0 | MCP server for interacting with Neon Management API and databases |
| *...and 15 more* | | | |

### Dev Tools (89 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [TrendRadar](https://github.com/sansan0/TrendRadar) | ⭐ 60.9k | 64 | ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS,  |
| [python-sdk](https://github.com/modelcontextprotocol/python-sdk) | ⭐ 23.7k | 88 | The official Python SDK for Model Context Protocol servers and clients |
| [typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | ⭐ 13.0k | 87 | The official TypeScript SDK for Model Context Protocol servers and clients |
| [hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) | ⭐ 10.5k | 41 | HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, G |
| [modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | ⭐ 8.7k | 74 | Specification and documentation for the Model Context Protocol |
| [git-mcp](https://github.com/idosal/git-mcp) | ⭐ 8.3k | 65 | Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP ser |
| [jscpd](https://github.com/kucherenko/jscpd) | ⭐ 5.9k | 74 | Copy/paste detector for programming source code, supports 223 formats. AI-ready  |
| [go-sdk](https://github.com/modelcontextprotocol/go-sdk) | ⭐ 4.9k | 74 | The official Go SDK for Model Context Protocol servers and clients. Maintained i |
| [aci](https://github.com/aipotheosis-labs/aci) | ⭐ 4.8k | 64 | ACI.dev is the open source tool-calling platform that hooks up 600+ tools into a |
| [notion-mcp-server](https://github.com/makenotion/notion-mcp-server) | ⭐ 4.6k | 68 | Official Notion MCP Server |
| [csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | ⭐ 4.4k | 88 | The official C# SDK for Model Context Protocol servers and clients. Maintained i |
| [EvoScientist](https://github.com/EvoScientist/EvoScientist) | ⭐ 4.4k | 88 | 🔬 Harness Vibe Research with Self-evolving AI Scientists |
| [mcp-context-forge](https://github.com/IBM/mcp-context-forge) | ⭐ 4.1k | 87 | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/g |
| [ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | ⭐ 4.1k | 90 | The Unofficial and Awesome Home Assistant MCP Server |
| [rust-sdk](https://github.com/modelcontextprotocol/rust-sdk) | ⭐ 3.7k | 74 | The official Rust SDK for the Model Context Protocol |
| *...and 74 more* | | | |

### Files (11 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [context-mode](https://github.com/mksglu/context-mode) | ⭐ 19.4k | 89 | Context window optimization for AI coding agents. Sandboxes tool output (98% red |
| [webiny-js](https://github.com/webiny/webiny-js) | ⭐ 8.0k | 73 | Open-source, self-hosted CMS platform on AWS serverless (Lambda, DynamoDB, S3).  |
| [registry](https://github.com/modelcontextprotocol/registry) | ⭐ 7.1k | 88 | A community driven registry service for Model Context Protocol (MCP) servers. |
| [sandbox](https://github.com/agent-infra/sandbox) | ⭐ 5.5k | 67 | All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSC |
| [spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp) | ⭐ 4.3k | 63 | A Model Context Protocol (MCP) server that provides structured spec-driven devel |
| [mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) | ⭐ 670 | 0 | Go server implementing Model Context Protocol (MCP) for filesystem operations. |
| [enrichmcp](https://github.com/featureform/enrichmcp) | ⭐ 646 | 0 | EnrichMCP is a python framework for building data driven MCP servers |
| [mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development) | ⭐ 435 | 0 | Spec-Driven Development MCP Server, not just Vibe Coding |
| [mcp-server](https://github.com/mapbox/mcp-server) | ⭐ 351 | 0 | Mapbox Model Context Protocol (MCP) server |
| [OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server) | ⭐ 174 | 0 | Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and  |
| [mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe) | ⭐ 156 | 0 | 小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an  |

### Finance (2 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate) | ⭐ 1.0k | 0 | A remote Cloudflare MCP server boilerplate with user authentication and Stripe f |
| [memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp) | ⭐ 915 | 0 | A Model Context Protocol (MCP) server implementation for remote memory bank mana |

### Other (164 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | ⭐ 91.4k | 65 | A collection of MCP servers. |
| [servers](https://github.com/modelcontextprotocol/servers) | ⭐ 88.9k | 72 | Model Context Protocol Servers |
| [activepieces](https://github.com/activepieces/activepieces) | ⭐ 23.4k | 74 | AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • A |
| [Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | ⭐ 15.5k | 87 | MCP server to provide Figma layout information to AI coding agents like Cursor |
| [aisuite](https://github.com/andrewyng/aisuite) | ⭐ 15.5k | 83 | Simple, unified interface to multiple Generative AI providers  |
| [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | ⭐ 14.9k | 65 | MCP for xiaohongshu.com |
| [ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) | ⭐ 10.8k | 88 | AI-powered reverse engineering assistant that bridges IDA Pro with language mode |
| [inspector](https://github.com/modelcontextprotocol/inspector) | ⭐ 10.5k | 73 | Visual testing tool for MCP servers |
| [critical](https://github.com/addyosmani/critical) | ⭐ 10.3k | 88 | Extract & Inline Critical-path CSS in HTML pages |
| [stitch-skills](https://github.com/google-labs-code/stitch-skills) | ⭐ 7.8k | 71 | A library of Agent Skills designed to work with the Stitch MCP server. Each skil |
| [Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH) | ⭐ 7.5k | 52 | MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients |
| [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | ⭐ 6.5k | 89 | MCP Server for Computer Use in Windows |
| [XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP) | ⭐ 6.2k | 74 | A Model Context Protocol (MCP) server and CLI that provides tools for agent use  |
| [mobile-mcp](https://github.com/mobile-next/mobile-mcp) | ⭐ 5.7k | 86 | Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android,  |
| [gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli) | ⭐ 5.6k | 90 | Programmatic access to Gemini Notebook - via command-line interface (CLI), Model |
| *...and 149 more* | | | |

### Productivity (18 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [SurfSense](https://github.com/MODSetter/SurfSense) | ⭐ 15.5k | 73 | Open-source NotebookLM alternative. Research the open web with live data(Reddit, |
| [mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | ⭐ 5.6k | 87 | MCP server for Atlassian tools (Confluence, Jira) |
| [NotFair](https://github.com/nowork-studio/NotFair) | ⭐ 3.3k | 76 | Goal-driven, loop-powered marketing agents that crush your business goals 24/7 |
| [google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | ⭐ 2.9k | 88 | Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search |
| [vexa](https://github.com/Vexa-ai/vexa) | ⭐ 2.6k | 0 | Open-source meeting transcription API for Google Meet, Microsoft Teams & Zoom. A |
| [slack-mcp-server](https://github.com/korotovsky/slack-mcp-server) | ⭐ 1.8k | 0 | The most powerful MCP Slack Server with no permission requirements, Apps support |
| [phantom](https://github.com/ghostwright/phantom) | ⭐ 1.5k | 0 | An AI co-worker with its own computer. Self-evolving, persistent memory, MCP ser |
| [keeper.sh](https://github.com/ridafkih/keeper.sh) | ⭐ 1.2k | 0 | Calendar sync tool & universal calendar MCP server. Aggregate, sync and control  |
| [mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) | ⭐ 960 | 0 | This MCP server integrates with your Google Drive and Google Sheets, to enable c |
| [colab-mcp](https://github.com/googlecolab/colab-mcp) | ⭐ 752 | 0 | An MCP server for interacting with Google Colab |
| [mcp-google-map](https://github.com/cablate/mcp-google-map) | ⭐ 403 | 0 | A powerful Model Context Protocol (MCP) server providing comprehensive Google Ma |
| [nanobanana-mcp-server](https://github.com/zhongweili/nanobanana-mcp-server) | ⭐ 383 | 0 | AI image generation MCP server powered by Google Gemini, with smart model select |
| [Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server) | ⭐ 381 | 0 | A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Goo |
| [mcp-email-server](https://github.com/Wh1isper/mcp-email-server) | ⭐ 293 | 0 | IMAP and SMTP via MCP Server |
| [mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc) | ⭐ 251 | 0 | A Model Context Protocol (MCP) server providing access to Google Search Console |
| *...and 3 more* | | | |

### Security (3 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [obsidian-local-rest-api](https://github.com/coddingtonbear/obsidian-local-rest-api) | ⭐ 2.7k | 75 | A secure REST API and Model Context Protocol (MCP) server for your vault. |
| [mcpvault](https://github.com/bitbonsai/mcpvault) | ⭐ 1.6k | 0 | A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access |
| [Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server) | ⭐ 1.2k | 0 | A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop wi |

### Web (50 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [playwright-mcp](https://github.com/microsoft/playwright-mcp) | ⭐ 35.5k | 90 | Playwright MCP server |
| [mcp-chrome](https://github.com/hangwin/mcp-chrome) | ⭐ 12.2k | 53 | Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) serve |
| [DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | ⭐ 8.9k | 84 | This is MCP server for Claude that gives it terminal control, file system search |
| [mcp](https://github.com/BrowserMCP/mcp) | ⭐ 6.9k | 32 | Browser MCP is a Model Context Provider (MCP) server that allows AI applications |
| [bb-browser](https://github.com/epiral/bb-browser) | ⭐ 6.0k | 64 | Your browser is the API. CLI + MCP server for AI agents to control Chrome with y |
| [mcp-playwright](https://github.com/executeautomation/mcp-playwright) | ⭐ 5.6k | 48 | Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in |
| [exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) | ⭐ 4.8k | 79 | Exa MCP for web search and web crawling! |
| [mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | ⭐ 3.4k | 83 | Allow LLMs to control a browser with Browserbase and Stagehand |
| [anything-analyzer](https://github.com/Mouseww/anything-analyzer) | ⭐ 3.4k | 78 | 全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE   |  All- |
| [brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | ⭐ 2.5k | 0 | A powerful Model Context Protocol (MCP) server that provides an all-in-one solut |
| [js-reverse-mcp](https://github.com/zhizhuodemao/js-reverse-mcp) | ⭐ 2.3k | 0 | AI Agent-first JS 逆向 MCP Server：有头 Chrome 调试、断点、网络/WebSocket 分析、Patchright 反检测，可 |
| [apify-mcp-server](https://github.com/apify/apify-mcp-server) | ⭐ 2.3k | 0 | The Apify MCP server enables your AI agents to extract data from social media, s |
| [DevDocs](https://github.com/cyberagiinc/DevDocs) | ⭐ 2.1k | 0 | Completely free, private, UI based Tech Documentation MCP server. Designed for c |
| [open-webSearch](https://github.com/Aas-ee/open-webSearch) | ⭐ 1.6k | 0 | Multi-engine MCP server, CLI, and local daemon for agent web search and content  |
| [jarvis](https://github.com/isair/jarvis) | ⭐ 1.5k | 0 | A 100% private AI voice assistant that lives on your computer (works offline). T |
| *...and 35 more* | | | |

---

## 🔍 Quality Breakdown — Top 10

| Server | README | License | Tests | CI | Releases | Stars | Recency | Issues | **Total** |
|--------|:------:|:-------:|:-----:|:--:|:--------:|:-----:|:-------:|:------:|:---------:|
| **private-gpt** | ✅ | ✅ | ✅ | ✅ | ✅ | 57.4k | today | 1241/1241 | **90** |
| **ha-mcp** | ✅ | ✅ | ✅ | ✅ | ✅ | 4.1k | today | 630/633 | **90** |
| **semiotic** | ✅ | ✅ | ✅ | ✅ | ✅ | 2.7k | today | 461/461 | **90** |
| **playwright-mcp** | ✅ | ✅ | ✅ | ✅ | ✅ | 35.5k | 2d ago | 873/877 | **90** |
| **gemini-notebook-mcp-cli** | ✅ | ✅ | ✅ | ✅ | ✅ | 5.6k | yesterday | 136/137 | **90** |
| **mcporter** | ✅ | ✅ | ✅ | ✅ | ✅ | 4.8k | today | 104/106 | **90** |
| **fast-agent** | ✅ | ✅ | ✅ | ✅ | ✅ | 3.9k | today | 237/253 | **89** |
| **Windows-MCP** | ✅ | ✅ | ✅ | ✅ | ✅ | 6.5k | 2d ago | 120/129 | **89** |
| **ghidra-mcp** | ✅ | ✅ | ✅ | ✅ | ✅ | 3.0k | 2d ago | 95/103 | **89** |
| **agent-scan** | ✅ | ✅ | ✅ | ✅ | ✅ | 2.8k | 5d ago | 60/63 | **89** |

---

## 💡 Key Insights

- **Most popular**: [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) with 91.4k stars
- **Highest quality**: [private-gpt](https://github.com/zylon-ai/private-gpt) with a score of 90/100
- **Largest category**: `other` with 164 servers
- **Archived/abandoned**: 13 servers are no longer maintained

---

## 🚀 Running the Scanner

```bash
git clone https://github.com/YOUR_USERNAME/mcp-ecosystem-scanner.git
cd mcp-ecosystem-scanner
pip install -r requirements.txt

# Set GitHub token (recommended for higher API limits)
export GITHUB_TOKEN=ghp_your_token_here

# Run the scanner
python scanner.py

# Generate the dashboard
python dashboard.py
```

## ⚙️ How Quality Scoring Works

Each server gets a score from 0–100 based on:

| Signal | Points | What It Checks |
|--------|--------|----------------|
| Has README | 10 | Documentation exists |
| Has License | 5 | Open source license present |
| Has Tests | 15 | Test directory found |
| Has CI/CD | 10 | GitHub Actions or similar configured |
| Has Releases | 10 | At least one tagged release |
| GitHub Stars | 15 | Community adoption (log scale) |
| Recent Activity | 15 | Days since last commit |
| Issue Health | 10 | Ratio of closed to total issues |

## 📋 Adding a Server Manually

Add repos to `config.yaml` under `discovery.seed_repos`:

```yaml
seed_repos:
  - owner/my-mcp-server
```

---

*Powered by GitHub Actions · Scanned daily · Last run: 2026-07-27 10:54 UTC*

*Built to solve the MCP ecosystem's [discovery gap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) — because the protocol's own roadmap says discoverability is a top priority.*