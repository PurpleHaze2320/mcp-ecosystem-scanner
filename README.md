# 🔬 MCP Ecosystem Scanner

[![Daily Scan](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner/actions/workflows/scan.yml/badge.svg)](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner/actions/workflows/scan.yml)
[![MCP Servers](https://img.shields.io/badge/MCP_servers-454-blue)](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/mcp-ecosystem-scanner?style=social)](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner/stargazers)

> The most comprehensive automated registry of [Model Context Protocol](https://modelcontextprotocol.io/) servers.
> Discovers, validates, and quality-scores every MCP server on GitHub — daily.

> **454** servers catalogued | **10** categories | Last scan: **2026-06-28 10:08 UTC**

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
| Total MCP Servers | **454** |
| Combined GitHub Stars | **1.2M** |
| Average Quality Score | **16.0/100** |
| New This Month | **0** |
| Categories | **10** |

**Languages:** **TypeScript**: 206 · **Python**: 203 · **Go**: 13 · **JavaScript**: 11 · **Unknown**: 8 · **C#**: 4

**Transports:** `stdio`: 236 · `sse`: 346 · `streamable-http`: 113 · `unknown`: 70

---

## 🏆 Top Servers by Quality Score

| Rank | Server | Quality | Stars | Description | Category | Transport |
|------|--------|---------|-------|-------------|----------|-----------|
| 1 | [semiotic](https://github.com/nteract/semiotic) | █████████░ **90** | 2.7k | React data visualization library for streaming, networks, and AI-assis | `other` | `stdio` `SSE` |
| 2 | [mcporter](https://github.com/openclaw/mcporter) | █████████░ **90** | 4.7k | Call MCPs via TypeScript, masquerading as simple TypeScript API. Or pa | `other` | `stdio` `SSE` `HTTP` |
| 3 | [ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | █████████░ **90** | 3.7k | The Unofficial and Awesome Home Assistant MCP Server | `dev-tools` | `stdio` `SSE` `HTTP` |
| 4 | [playwright-mcp](https://github.com/microsoft/playwright-mcp) | █████████░ **90** | 34.4k | Playwright MCP server | `web` | `stdio` `SSE` |
| 5 | [context-mode](https://github.com/mksglu/context-mode) | █████████░ **90** | 18.3k | Context window optimization for AI coding agents. Sandboxes tool outpu | `files` | `stdio` `SSE` |
| 6 | [notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | █████████░ **90** | 5.1k | Programmatic access to Google NotebookLM — via command-line interface  | `productivity` | `SSE` |
| 7 | [Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | █████████░ **89** | 15.2k | MCP server to provide Figma layout information to AI coding agents lik | `other` | `stdio` |
| 8 | [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | █████████░ **89** | 6.3k | MCP Server for Computer Use in Windows | `other` | `stdio` `SSE` `HTTP` |
| 9 | [fast-agent](https://github.com/evalstate/fast-agent) | █████████░ **89** | 3.8k | Code, Build and Evaluate agents - excellent Model and Skills/MCP/ACP S | `other` | `stdio` `SSE` `HTTP` |
| 10 | [fastmcp](https://github.com/PrefectHQ/fastmcp) | █████████░ **89** | 25.8k | 🚀 The fast, Pythonic way to build MCP servers and clients. | `ai-ml` | `SSE` |
| 11 | [EvoScientist](https://github.com/EvoScientist/EvoScientist) | █████████░ **89** | 3.9k | 🔬 Harness Vibe Research with Self-evolving AI Scientists | `dev-tools` | `SSE` |
| 12 | [ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) | █████████░ **88** | 9.7k | AI-powered reverse engineering assistant that bridges IDA Pro with lan | `other` | `stdio` `SSE` |
| 13 | [csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | █████████░ **88** | 4.4k | The official C# SDK for Model Context Protocol servers and clients. Ma | `dev-tools` | `SSE` |
| 14 | [linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server) | █████████░ **88** | 2.5k | Open-source MCP server for LinkedIn. Give Claude and any MCP-compatibl | `ai-ml` | `stdio` `SSE` `HTTP` |
| 15 | [gpt-researcher](https://github.com/assafelovic/gpt-researcher) | █████████░ **88** | 27.9k | An autonomous agent that conducts deep research on any data using any  | `ai-ml` | `SSE` |
| 16 | [python-sdk](https://github.com/modelcontextprotocol/python-sdk) | █████████░ **88** | 23.5k | The official Python SDK for Model Context Protocol servers and clients | `dev-tools` | `stdio` `SSE` `HTTP` |
| 17 | [brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | █████████░ **88** | 2.5k | A powerful Model Context Protocol (MCP) server that provides an all-in | `web` | `SSE` |
| 18 | [registry](https://github.com/modelcontextprotocol/registry) | █████████░ **88** | 7.0k | A community driven registry service for Model Context Protocol (MCP) s | `files` | `SSE` |
| 19 | [google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | █████████░ **88** | 2.8k | Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tas | `productivity` | `stdio` `SSE` `HTTP` |
| 20 | [agent-scan](https://github.com/snyk/agent-scan) | █████████░ **87** | 2.7k | Security scanner for AI agents, MCP servers and agent skills. | `other` | `stdio` `SSE` |
| 21 | [typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | █████████░ **87** | 12.7k | The official TypeScript SDK for Model Context Protocol servers and cli | `dev-tools` | `stdio` `HTTP` |
| 22 | [5ire](https://github.com/nanbingxyz/5ire) | █████████░ **87** | 5.3k | 5ire is a cross-platform desktop AI assistant, MCP client. It compatib | `ai-ml` | `SSE` |
| 23 | [mcp-context-forge](https://github.com/IBM/mcp-context-forge) | █████████░ **87** | 4.0k | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, | `dev-tools` | `stdio` `SSE` `HTTP` |
| 24 | [tabularis](https://github.com/TabularisDB/tabularis) | █████████░ **87** | 3.4k | Open-source desktop SQL workspace for PostgreSQL, MySQL/MariaDB, SQLit | `data` | `stdio` |
| 25 | [mobile-mcp](https://github.com/mobile-next/mobile-mcp) | █████████░ **86** | 5.3k | Model Context Protocol Server for Mobile Automation and Scraping (iOS, | `other` | `stdio` `SSE` |
| 26 | [mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | █████████░ **86** | 5.5k | MCP server for Atlassian tools (Confluence, Jira) | `productivity` | `SSE` |
| 27 | [headroom](https://github.com/headroomlabs-ai/headroom) | █████████░ **86** | 52.8k | Compress tool outputs, logs, files, and RAG chunks before they reach t | `ai-ml` | `SSE` |
| 28 | [CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | █████████░ **86** | 3.8k | An MCP server plus a CLI tool that indexes local code into a graph dat | `data` | `SSE` |
| 29 | [arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | ████████░░ **85** | 2.9k | A Model Context Protocol server for searching and analyzing arXiv pape | `ai-ml` | `stdio` `SSE` `HTTP` |
| 30 | [DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | ████████░░ **85** | 6.2k | This is MCP server for Claude that gives it terminal control, file sys | `web` | `SSE` |

---

## 📂 Servers by Category

### Ai Ml (81 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [headroom](https://github.com/headroomlabs-ai/headroom) | ⭐ 52.8k | 86 | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60 |
| [gpt-researcher](https://github.com/assafelovic/gpt-researcher) | ⭐ 27.9k | 88 | An autonomous agent that conducts deep research on any data using any LLM provid |
| [fastmcp](https://github.com/PrefectHQ/fastmcp) | ⭐ 25.8k | 89 | 🚀 The fast, Pythonic way to build MCP servers and clients. |
| [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | ⭐ 16.6k | 73 | Agent framework and applications built upon Qwen>=3.0, featuring Function Callin |
| [DeepCode](https://github.com/HKUDS/DeepCode) | ⭐ 15.9k | 82 | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |
| [pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server) | ⭐ 11.6k | 72 | The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter  |
| [mcp-use](https://github.com/mcp-use/mcp-use) | ⭐ 10.2k | 74 | The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Serve |
| [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | ⭐ 8.4k | 70 | Build effective agents using Model Context Protocol and simple workflow patterns |
| [awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | ⭐ 5.9k | 38 | Tutorials, Guides and Agent Skills Directories |
| [awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) | ⭐ 5.6k | 35 | Awesome MCP Servers - A curated list of Model Context Protocol servers |
| [5ire](https://github.com/nanbingxyz/5ire) | ⭐ 5.3k | 87 | 5ire is a cross-platform desktop AI assistant, MCP client. It compatible with ma |
| [claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) | ⭐ 5.2k | 73 | The most comprehensive Claude Code guide: agentic workflows, hooks, skills, MCP  |
| [mcp-ui](https://github.com/MCP-UI-Org/mcp-ui) | ⭐ 5.0k | 64 | UI over MCP. Create next-gen UI experiences with the protocol and SDK! |
| [claude-code-guide](https://github.com/zebbern/claude-code-guide) | ⭐ 4.3k | 64 | Claude Code Guide - Setup, Commands, workflows, agents, skills & tips-n-tricks g |
| [mcp-server-chart](https://github.com/antvis/mcp-server-chart) | ⭐ 4.2k | 84 | 🤖 A visualization mcp & skills contains 25+ visual charts using @antvis. Using f |
| *...and 66 more* | | | |

### Cloud (8 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [mcp](https://github.com/awslabs/mcp) | ⭐ 9.3k | 72 | Open source MCP Servers for AWS |
| [mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | ⭐ 3.9k | 71 | — |
| [skills](https://github.com/microsoft/skills) | ⭐ 2.6k | 75 | Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents |
| [azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) | ⭐ 1.9k | 0 | The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to  |
| [mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) | ⭐ 377 | 0 | An MCP server for Azure DevOps |
| [run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda) | ⭐ 373 | 0 | Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda func |
| [sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers) | ⭐ 239 | 0 | Sample implementations of AI Agents and MCP Servers running on AWS Serverless co |
| [Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server) | ⭐ 234 | 0 | Creates a simple MCP tool server with "streaming" HTTP. |

### Data (30 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | ⭐ 3.8k | 86 | An MCP server plus a CLI tool that indexes local code into a graph database to p |
| [tabularis](https://github.com/TabularisDB/tabularis) | ⭐ 3.4k | 87 | Open-source desktop SQL workspace for PostgreSQL, MySQL/MariaDB, SQLite and 12+  |
| [dbhub](https://github.com/bytebase/dbhub) | ⭐ 3.0k | 65 | Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Se |
| [mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) | ⭐ 1.9k | 0 | A Model Context Protocol server that provides read-only access to MySQL database |
| [pg-aiguide](https://github.com/timescale/pg-aiguide) | ⭐ 1.8k | 0 | MCP server and Claude plugin for Postgres skills and documentation. Helps AI cod |
| [mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) | ⭐ 1.3k | 0 | A Model Context Protocol (MCP) server that enables secure interaction with MySQL |
| [nocturne_memory](https://github.com/Dataojitori/nocturne_memory) | ⭐ 1.2k | 0 | A lightweight, rollbackable, and visual Long-Term Memory Server for MCP Agents.  |
| [mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) | ⭐ 1.1k | 0 | A Model Context Protocol server to connect to MongoDB databases and MongoDB Atla |
| [yargi-mcp](https://github.com/saidsurucu/yargi-mcp) | ⭐ 994 | 0 | MCP Server For Turkish Legal Databases |
| [mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) | ⭐ 972 | 0 | Neo4j Labs Model Context Protocol servers |
| [supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server) | ⭐ 827 | 0 | Query MCP enables end-to-end management of Supabase via chat interface: read & w |
| [mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry) | ⭐ 751 | 0 | Enterprise-ready MCP Gateway & Registry that centralizes AI development tools wi |
| [mcp-for-security](https://github.com/cyproxio/mcp-for-security) | ⭐ 621 | 0 | MCP for Security: A collection of Model Context Protocol servers for popular sec |
| [mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) | ⭐ 613 | 0 | MCP server for interacting with Neon Management API and databases |
| [mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) | ⭐ 594 | 0 | A growing collection of MCP servers bringing offensive security tools to AI assi |
| *...and 15 more* | | | |

### Dev Tools (85 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [TrendRadar](https://github.com/sansan0/TrendRadar) | ⭐ 60.0k | 64 | ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS,  |
| [python-sdk](https://github.com/modelcontextprotocol/python-sdk) | ⭐ 23.5k | 88 | The official Python SDK for Model Context Protocol servers and clients |
| [typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | ⭐ 12.7k | 87 | The official TypeScript SDK for Model Context Protocol servers and clients |
| [hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) | ⭐ 10.0k | 44 | HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, G |
| [modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | ⭐ 8.5k | 74 | Specification and documentation for the Model Context Protocol |
| [git-mcp](https://github.com/idosal/git-mcp) | ⭐ 8.2k | 68 | Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP ser |
| [jscpd](https://github.com/kucherenko/jscpd) | ⭐ 5.8k | 74 | Copy/paste detector for programming source code, supports 223 formats. AI-ready  |
| [aci](https://github.com/aipotheosis-labs/aci) | ⭐ 4.8k | 67 | ACI.dev is the open source tool-calling platform that hooks up 600+ tools into a |
| [go-sdk](https://github.com/modelcontextprotocol/go-sdk) | ⭐ 4.7k | 74 | The official Go SDK for Model Context Protocol servers and clients. Maintained i |
| [notion-mcp-server](https://github.com/makenotion/notion-mcp-server) | ⭐ 4.5k | 67 | Official Notion MCP Server |
| [csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | ⭐ 4.4k | 88 | The official C# SDK for Model Context Protocol servers and clients. Maintained i |
| [mcp-context-forge](https://github.com/IBM/mcp-context-forge) | ⭐ 4.0k | 87 | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/g |
| [EvoScientist](https://github.com/EvoScientist/EvoScientist) | ⭐ 3.9k | 89 | 🔬 Harness Vibe Research with Self-evolving AI Scientists |
| [ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | ⭐ 3.7k | 90 | The Unofficial and Awesome Home Assistant MCP Server |
| [rust-sdk](https://github.com/modelcontextprotocol/rust-sdk) | ⭐ 3.6k | 74 | The official Rust SDK for the Model Context Protocol |
| *...and 70 more* | | | |

### Files (11 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [context-mode](https://github.com/mksglu/context-mode) | ⭐ 18.3k | 90 | Context window optimization for AI coding agents. Sandboxes tool output (98% red |
| [webiny-js](https://github.com/webiny/webiny-js) | ⭐ 8.0k | 73 | Open-source, self-hosted CMS platform on AWS serverless (Lambda, DynamoDB, S3).  |
| [registry](https://github.com/modelcontextprotocol/registry) | ⭐ 7.0k | 88 | A community driven registry service for Model Context Protocol (MCP) servers. |
| [sandbox](https://github.com/agent-infra/sandbox) | ⭐ 5.3k | 70 | All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSC |
| [spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp) | ⭐ 4.2k | 60 | A Model Context Protocol (MCP) server that provides structured spec-driven devel |
| [mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) | ⭐ 661 | 0 | Go server implementing Model Context Protocol (MCP) for filesystem operations. |
| [enrichmcp](https://github.com/featureform/enrichmcp) | ⭐ 647 | 0 | EnrichMCP is a python framework for building data driven MCP servers |
| [mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development) | ⭐ 430 | 0 | Spec-Driven Development MCP Server, not just Vibe Coding |
| [mcp-server](https://github.com/mapbox/mcp-server) | ⭐ 348 | 0 | Mapbox Model Context Protocol (MCP) server |
| [OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server) | ⭐ 161 | 0 | Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and  |
| [mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe) | ⭐ 155 | 0 | 小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an  |

### Finance (2 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate) | ⭐ 1.0k | 0 | A remote Cloudflare MCP server boilerplate with user authentication and Stripe f |
| [memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp) | ⭐ 912 | 0 | A Model Context Protocol (MCP) server implementation for remote memory bank mana |

### Other (168 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | ⭐ 89.9k | 65 | A collection of MCP servers. |
| [servers](https://github.com/modelcontextprotocol/servers) | ⭐ 87.8k | 71 | Model Context Protocol Servers |
| [activepieces](https://github.com/activepieces/activepieces) | ⭐ 23.0k | 74 | AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • A |
| [Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | ⭐ 15.2k | 89 | MCP server to provide Figma layout information to AI coding agents like Cursor |
| [aisuite](https://github.com/andrewyng/aisuite) | ⭐ 14.9k | 83 | Simple, unified interface to multiple Generative AI providers  |
| [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | ⭐ 14.4k | 64 | MCP for xiaohongshu.com |
| [inspector](https://github.com/modelcontextprotocol/inspector) | ⭐ 10.2k | 73 | Visual testing tool for MCP servers |
| [ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) | ⭐ 9.7k | 88 | AI-powered reverse engineering assistant that bridges IDA Pro with language mode |
| [Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH) | ⭐ 7.4k | 55 | MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients |
| [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | ⭐ 6.3k | 89 | MCP Server for Computer Use in Windows |
| [stitch-skills](https://github.com/google-labs-code/stitch-skills) | ⭐ 6.2k | 70 | A library of Agent Skills designed to work with the Stitch MCP server. Each skil |
| [XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP) | ⭐ 6.0k | 74 | A Model Context Protocol (MCP) server and CLI that provides tools for agent use  |
| [mobile-mcp](https://github.com/mobile-next/mobile-mcp) | ⭐ 5.3k | 86 | Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android,  |
| [magic-mcp](https://github.com/21st-dev/magic-mcp) | ⭐ 5.3k | 30 | It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for wo |
| [mcporter](https://github.com/openclaw/mcporter) | ⭐ 4.7k | 90 | Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them |
| *...and 153 more* | | | |

### Productivity (18 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | ⭐ 5.5k | 86 | MCP server for Atlassian tools (Confluence, Jira) |
| [notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | ⭐ 5.1k | 90 | Programmatic access to Google NotebookLM — via command-line interface (CLI), Mod |
| [NotFair](https://github.com/nowork-studio/NotFair) | ⭐ 3.0k | 68 | Open-source Claude Code skills for SEO, GEO, Google Ads, Meta Ads |
| [google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | ⭐ 2.8k | 88 | Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search |
| [vexa](https://github.com/Vexa-ai/vexa) | ⭐ 2.2k | 0 | Open-source meeting transcription API for Google Meet, Microsoft Teams & Zoom. A |
| [slack-mcp-server](https://github.com/korotovsky/slack-mcp-server) | ⭐ 1.7k | 0 | The most powerful MCP Slack Server with no permission requirements, Apps support |
| [phantom](https://github.com/ghostwright/phantom) | ⭐ 1.4k | 0 | An AI co-worker with its own computer. Self-evolving, persistent memory, MCP ser |
| [keeper.sh](https://github.com/ridafkih/keeper.sh) | ⭐ 1.2k | 0 | Calendar sync tool & universal calendar MCP server. Aggregate, sync and control  |
| [mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) | ⭐ 927 | 0 | This MCP server integrates with your Google Drive and Google Sheets, to enable c |
| [colab-mcp](https://github.com/googlecolab/colab-mcp) | ⭐ 699 | 0 | An MCP server for interacting with Google Colab |
| [Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server) | ⭐ 369 | 0 | A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Goo |
| [nanobanana-mcp-server](https://github.com/zhongweili/nanobanana-mcp-server) | ⭐ 368 | 0 | AI image generation MCP server powered by Google Gemini, with smart model select |
| [mcp-google-map](https://github.com/cablate/mcp-google-map) | ⭐ 360 | 0 | A powerful Model Context Protocol (MCP) server providing comprehensive Google Ma |
| [mcp-email-server](https://github.com/ai-zerolab/mcp-email-server) | ⭐ 267 | 0 | IMAP and SMTP via MCP Server |
| [mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc) | ⭐ 228 | 0 | A Model Context Protocol (MCP) server providing access to Google Search Console |
| *...and 3 more* | | | |

### Security (4 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [obsidian-local-rest-api](https://github.com/coddingtonbear/obsidian-local-rest-api) | ⭐ 2.5k | 73 | A secure REST API and Model Context Protocol (MCP) server for your vault. |
| [mcpvault](https://github.com/bitbonsai/mcpvault) | ⭐ 1.5k | 0 | A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access |
| [Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server) | ⭐ 1.2k | 0 | A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop wi |
| [streamable-mcp-server-template](https://github.com/iceener/streamable-mcp-server-template) | ⭐ 133 | 0 | Production-ready MCP server template with Streamable HTTP transport. Supports No |

### Web (47 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [playwright-mcp](https://github.com/microsoft/playwright-mcp) | ⭐ 34.4k | 90 | Playwright MCP server |
| [mcp-chrome](https://github.com/hangwin/mcp-chrome) | ⭐ 12.0k | 53 | Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) serve |
| [mcp](https://github.com/BrowserMCP/mcp) | ⭐ 6.7k | 32 | Browser MCP is a Model Context Provider (MCP) server that allows AI applications |
| [DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | ⭐ 6.2k | 85 | This is MCP server for Claude that gives it terminal control, file system search |
| [bb-browser](https://github.com/epiral/bb-browser) | ⭐ 5.9k | 66 | Your browser is the API. CLI + MCP server for AI agents to control Chrome with y |
| [mcp-playwright](https://github.com/executeautomation/mcp-playwright) | ⭐ 5.6k | 48 | Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in |
| [exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) | ⭐ 4.6k | 79 | Exa MCP for web search and web crawling! |
| [mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | ⭐ 3.4k | 79 | Allow LLMs to control a browser with Browserbase and Stagehand |
| [anything-analyzer](https://github.com/Mouseww/anything-analyzer) | ⭐ 3.0k | 76 | 全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE   |  All- |
| [brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | ⭐ 2.5k | 88 | A powerful Model Context Protocol (MCP) server that provides an all-in-one solut |
| [DevDocs](https://github.com/cyberagiinc/DevDocs) | ⭐ 2.1k | 0 | Completely free, private, UI based Tech Documentation MCP server. Designed for c |
| [js-reverse-mcp](https://github.com/zhizhuodemao/js-reverse-mcp) | ⭐ 2.0k | 0 | AI Agent-first JS 逆向 MCP Server：有头 Chrome 调试、断点、网络/WebSocket 分析、Patchright 反检测，可 |
| [open-webSearch](https://github.com/Aas-ee/open-webSearch) | ⭐ 1.5k | 0 | Multi-engine MCP server, CLI, and local daemon for agent web search and content  |
| [apify-mcp-server](https://github.com/apify/apify-mcp-server) | ⭐ 1.4k | 0 | The Apify MCP server enables your AI agents to extract data from social media, s |
| [deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp) | ⭐ 1.4k | 0 | 📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other |
| *...and 32 more* | | | |

---

## 🔍 Quality Breakdown — Top 10

| Server | README | License | Tests | CI | Releases | Stars | Recency | Issues | **Total** |
|--------|:------:|:-------:|:-----:|:--:|:--------:|:-----:|:-------:|:------:|:---------:|
| **semiotic** | ✅ | ✅ | ✅ | ✅ | ✅ | 2.7k | today | 461/461 | **90** |
| **mcporter** | ✅ | ✅ | ✅ | ✅ | ✅ | 4.7k | yesterday | 102/102 | **90** |
| **ha-mcp** | ✅ | ✅ | ✅ | ✅ | ✅ | 3.7k | today | 509/516 | **90** |
| **playwright-mcp** | ✅ | ✅ | ✅ | ✅ | ✅ | 34.4k | 2d ago | 862/862 | **90** |
| **context-mode** | ✅ | ✅ | ✅ | ✅ | ✅ | 18.3k | today | 395/405 | **90** |
| **notebooklm-mcp-cli** | ✅ | ✅ | ✅ | ✅ | ✅ | 5.1k | 2d ago | 122/122 | **90** |
| **Figma-Context-MCP** | ✅ | ✅ | ✅ | ✅ | ✅ | 15.2k | 3d ago | 170/176 | **89** |
| **Windows-MCP** | ✅ | ✅ | ✅ | ✅ | ✅ | 6.3k | 2d ago | 110/114 | **89** |
| **fast-agent** | ✅ | ✅ | ✅ | ✅ | ✅ | 3.8k | today | 233/248 | **89** |
| **fastmcp** | ✅ | ✅ | ✅ | ✅ | ✅ | 25.8k | today | 1427/1662 | **89** |

---

## 💡 Key Insights

- **Most popular**: [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) with 89.9k stars
- **Highest quality**: [semiotic](https://github.com/nteract/semiotic) with a score of 90/100
- **Largest category**: `other` with 168 servers
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

*Powered by GitHub Actions · Scanned daily · Last run: 2026-06-28 10:08 UTC*

*Built to solve the MCP ecosystem's [discovery gap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) — because the protocol's own roadmap says discoverability is a top priority.*