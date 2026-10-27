# 🔬 MCP Ecosystem Scanner

[![Daily Scan](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner/actions/workflows/scan.yml/badge.svg)](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner/actions/workflows/scan.yml)
[![MCP Servers](https://img.shields.io/badge/MCP_servers-423-blue)](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/mcp-ecosystem-scanner?style=social)](https://github.com/PurpleHaze2320/mcp-ecosystem-scanner/stargazers)

> The most comprehensive automated registry of [Model Context Protocol](https://modelcontextprotocol.io/) servers.
> Discovers, validates, and quality-scores every MCP server on GitHub — daily.

> **423** servers catalogued | **10** categories | Last scan: **2026-10-27 13:10 UTC**

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
| Total MCP Servers | **423** |
| Combined GitHub Stars | **1.3M** |
| Average Quality Score | **17.9/100** |
| New This Month | **2** |
| Categories | **10** |

**Languages:** **TypeScript**: 210 · **Python**: 168 · **Go**: 11 · **JavaScript**: 10 · **Unknown**: 8 · **C#**: 3

**Transports:** `stdio`: 243 · `sse`: 334 · `streamable-http`: 129 · `unknown`: 52

---

## 🆕 New This Month

| Server | Stars | Language | Category | Quality |
|--------|-------|----------|----------|---------|
| [coop-anything](https://github.com/cranebeaker/coop-anything) | ⭐ 1.5k | Python | `other` | ░░░░░░░░░░ 0 |
| [invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp) | ⭐ 885 | Python | `web` | ░░░░░░░░░░ 0 |

---

## 🏆 Top Servers by Quality Score

| Rank | Server | Quality | Stars | Description | Category | Transport |
|------|--------|---------|-------|-------------|----------|-----------|
| 1 | [Douyin_TikTok_Download_API](https://github.com/Evil0ctal/Douyin_TikTok_Download_API) | █████████░ **90** | 20.9k | 🚀 自托管的抖音、TikTok、B 站数据采集与无水印视频下载 API，支持 AI agent 通过 MCP 调用与离线语音转文字，Dock | `data` | `SSE` |
| 2 | [excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) | █████████░ **90** | 4.3k | Excel MCP server: let AI (Claude, Cursor, Codex) create and edit Excel | `ai-ml` | `stdio` `SSE` `HTTP` |
| 3 | [kordoc](https://github.com/chrisryugj/kordoc) | █████████░ **90** | 2.8k | 모두 파싱해버리겠다 — HWP·HWPX·PDF·Office 문서를 Markdown으로. 양식 자동 채우기와 신구대조를 갖춘 C | `ai-ml` | — |
| 4 | [gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli) | █████████░ **90** | 6.4k | Programmatic access to Gemini Notebook - via command-line interface (C | `other` | `SSE` |
| 5 | [korean-law-mcp](https://github.com/chrisryugj/korean-law-mcp) | █████████░ **90** | 2.8k | 법제처 국가법령정보를 LLM에서 바로 조회하는 MCP 서버. 법령·판례·조례 검색과 인용 검증 | MCP server for  | `ai-ml` | — |
| 6 | [AiSOC](https://github.com/beenuar/AiSOC) | █████████░ **90** | 4.3k | Open-source AI Security Operations Center: alert fusion, LLM-agent tri | `dev-tools` | `SSE` |
| 7 | [playwright-mcp](https://github.com/microsoft/playwright-mcp) | █████████░ **90** | 38.7k | Playwright MCP server | `web` | `stdio` `SSE` |
| 8 | [Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | █████████░ **90** | 16.1k | MCP server to provide Figma layout information to AI coding agents lik | `other` | `stdio` |
| 9 | [ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | █████████░ **90** | 3.1k | Local video editor for coding agents: 42 FFmpeg tools with a machine-r | `other` | `stdio` `SSE` |
| 10 | [supergateway](https://github.com/supercorp-ai/supergateway) | █████████░ **90** | 2.9k | Run MCP stdio servers over HTTP streamable, SSE and SSE over stdio. AI | `other` | `stdio` `SSE` `HTTP` |
| 11 | [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) | █████████░ **89** | 5.2k | Your Personal Librarian Agent. Ask anything on your computer, organize | `ai-ml` | `stdio` `SSE` |
| 12 | [agent-device](https://github.com/callstack/agent-device) | █████████░ **89** | 5.2k | Mobile app automation and verification for AI coding agents. CLI, MCP  | `other` | `stdio` `SSE` |
| 13 | [davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) | █████████░ **89** | 3.8k | MCP server integration for DaVinci Resolve Studio | `dev-tools` | `stdio` `SSE` |
| 14 | [fast-agent](https://github.com/evalstate/fast-agent) | █████████░ **89** | 4.0k | Code, Build and Evaluate agents - excellent Model and Skills/MCP/ACP/A | `other` | `stdio` `SSE` `HTTP` |
| 15 | [KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server) | █████████░ **89** | 3.0k | KiCAD MCP is a Model Context Protocol (MCP) implementation that enable | `dev-tools` | `stdio` `SSE` |
| 16 | [next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | █████████░ **89** | 36.4k | Draw and edit draw.io diagrams by chatting with an AI. Web app, deskto | `ai-ml` | `SSE` |
| 17 | [worldmonitor](https://github.com/koala73/worldmonitor) | █████████░ **89** | 89.6k | Real-time global intelligence dashboard. AI-powered news aggregation,  | `other` | `HTTP` |
| 18 | [critical](https://github.com/addyosmani/critical) | █████████░ **89** | 10.3k | Extract & Inline Critical-path CSS in HTML pages | `other` | `stdio` `SSE` |
| 19 | [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | █████████░ **89** | 10.5k | MCP Server for Computer Use in Windows | `other` | `stdio` `SSE` `HTTP` |
| 20 | [registry](https://github.com/modelcontextprotocol/registry) | █████████░ **89** | 7.4k | A community driven registry service for Model Context Protocol (MCP) s | `files` | `SSE` |
| 21 | [tabularis](https://github.com/TabularisDB/tabularis) | █████████░ **88** | 5.3k | Open-source desktop SQL workspace with 3 built-in database drivers and | `data` | `stdio` `SSE` |
| 22 | [agent-scan](https://github.com/snyk/agent-scan) | █████████░ **88** | 3.2k | Security scanner for AI agents, MCP servers and agent skills. | `other` | `stdio` `SSE` |
| 23 | [fastmcp](https://github.com/PrefectHQ/fastmcp) | █████████░ **88** | 28.2k | 🚀 The fast, Pythonic way to build MCP servers and clients. | `ai-ml` | `SSE` |
| 24 | [gpt-researcher](https://github.com/assafelovic/gpt-researcher) | █████████░ **88** | 30.3k | An autonomous agent that conducts deep research on any data using any  | `ai-ml` | `SSE` |
| 25 | [csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | █████████░ **88** | 4.6k | The official C# SDK for Model Context Protocol servers and clients. Ma | `dev-tools` | `SSE` |
| 26 | [python-sdk](https://github.com/modelcontextprotocol/python-sdk) | █████████░ **88** | 24.7k | The official Python SDK for Model Context Protocol servers and clients | `dev-tools` | `stdio` `SSE` `HTTP` |
| 27 | [EvoScientist](https://github.com/EvoScientist/EvoScientist) | █████████░ **88** | 4.9k | 🔬 Harness Vibe Research with Self-evolving AI Scientists | `dev-tools` | `stdio` `SSE` |
| 28 | [mcp-context-forge](https://github.com/IBM/mcp-context-forge) | █████████░ **88** | 4.7k | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, | `dev-tools` | `stdio` `SSE` `HTTP` |
| 29 | [arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | █████████░ **88** | 3.2k | A local MCP server for agent literature work. Original-LaTeX section r | `ai-ml` | `stdio` `SSE` `HTTP` |
| 30 | [mobile-mcp](https://github.com/mobile-next/mobile-mcp) | █████████░ **88** | 10.0k | Model Context Protocol Server for Mobile Automation and Scraping (iOS, | `other` | `stdio` `SSE` `HTTP` |

---

## 📂 Servers by Category

### Ai Ml (72 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | ⭐ 36.4k | 89 | Draw and edit draw.io diagrams by chatting with an AI. Web app, desktop app, and |
| [gpt-researcher](https://github.com/assafelovic/gpt-researcher) | ⭐ 30.3k | 88 | An autonomous agent that conducts deep research on any data using any LLM provid |
| [fastmcp](https://github.com/PrefectHQ/fastmcp) | ⭐ 28.2k | 88 | 🚀 The fast, Pythonic way to build MCP servers and clients. |
| [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | ⭐ 17.2k | 69 | Agent framework and applications built upon Qwen>=3.0, featuring Function Callin |
| [pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server) | ⭐ 11.8k | 72 | The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter  |
| [mcp-use](https://github.com/mcp-use/mcp-use) | ⭐ 10.8k | 74 | The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Serve |
| [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | ⭐ 8.6k | 71 | Build effective agents using Model Context Protocol and simple workflow patterns |
| [awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | ⭐ 6.3k | 57 | Tutorials, Guides and Agent Skills Directories |
| [awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) | ⭐ 5.8k | 25 | Awesome MCP Servers - A curated list of Model Context Protocol servers |
| [5ire](https://github.com/nanbingxyz/5ire) | ⭐ 5.4k | 88 | 5ire is a cross-platform desktop AI assistant, MCP client. It compatible with ma |
| [mcp-ui](https://github.com/MCP-UI-Org/mcp-ui) | ⭐ 5.2k | 64 | UI over MCP. Create next-gen UI experiences with the protocol and SDK! |
| [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) | ⭐ 5.2k | 89 | Your Personal Librarian Agent. Ask anything on your computer, organize files, re |
| [claude-code-guide](https://github.com/zebbern/claude-code-guide) | ⭐ 4.7k | 62 | Claude Code Guide - Setup, Commands, workflows, agents, skills & tips-n-tricks f |
| [mcp-server-chart](https://github.com/antvis/mcp-server-chart) | ⭐ 4.4k | 84 | 🤖 A visualization mcp & skills contains 25+ visual charts using @antvis. Using f |
| [optillm](https://github.com/algorithmicsuperintelligence/optillm) | ⭐ 4.3k | 87 | Optimizing inference proxy for LLMs |
| *...and 57 more* | | | |

### Cloud (6 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [skills](https://github.com/microsoft/skills) | ⭐ 3.1k | 75 | Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents |
| [azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) | ⭐ 2.1k | 0 | The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to  |
| [mcp](https://github.com/cloudflare/mcp) | ⭐ 1.0k | 0 | MCP server for the Cloudflare API |
| [mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) | ⭐ 397 | 0 | An MCP server for Azure DevOps |
| [sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers) | ⭐ 245 | 0 | Sample implementations of AI Agents and MCP Servers running on AWS Serverless co |
| [Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server) | ⭐ 236 | 0 | Creates a simple MCP tool server with "streaming" HTTP. |

### Data (28 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [Douyin_TikTok_Download_API](https://github.com/Evil0ctal/Douyin_TikTok_Download_API) | ⭐ 20.9k | 90 | 🚀 自托管的抖音、TikTok、B 站数据采集与无水印视频下载 API，支持 AI agent 通过 MCP 调用与离线语音转文字，Docker 一键部署。|  |
| [tabularis](https://github.com/TabularisDB/tabularis) | ⭐ 5.3k | 88 | Open-source desktop SQL workspace with 3 built-in database drivers and 24 shippe |
| [dbhub](https://github.com/bytebase/dbhub) | ⭐ 3.7k | 75 | Token conscious database MCP server for Postgres, MySQL, SQL Server, Oracle, Mar |
| [FlyEnv](https://github.com/xpf0000/FlyEnv) | ⭐ 3.3k | 74 | Native local development environment for Windows, macOS & Linux. A modern altern |
| [carbon](https://github.com/crbnos/carbon) | ⭐ 2.8k | 62 | Open-source manufacturing ERP, MES and QMS. Quoting, MRP, inventory, shop floor, |
| [mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) | ⭐ 2.2k | 0 | A Model Context Protocol server that provides read-only access to MySQL database |
| [pg-aiguide](https://github.com/timescale/pg-aiguide) | ⭐ 1.9k | 0 | MCP server and Claude plugin for Postgres skills and documentation. Helps AI cod |
| [mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) | ⭐ 1.4k | 0 | A Model Context Protocol (MCP) server that enables secure interaction with MySQL |
| [mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) | ⭐ 1.1k | 0 | A Model Context Protocol server to connect to MongoDB databases and MongoDB Atla |
| [mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry) | ⭐ 1.0k | 0 | Enterprise-ready MCP Gateway & Registry that centralizes AI development tools wi |
| [mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) | ⭐ 989 | 0 | Neo4j Labs Model Context Protocol servers |
| [supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server) | ⭐ 834 | 0 | Query MCP enables end-to-end management of Supabase via chat interface: read & w |
| [mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) | ⭐ 656 | 0 | MCP server for interacting with Neon Management API and databases |
| [mcp-redis](https://github.com/redis/mcp-redis) | ⭐ 641 | 0 | The official Redis MCP Server is a natural language interface designed for agent |
| [mcp-for-security](https://github.com/cyproxio/mcp-for-security) | ⭐ 628 | 0 | MCP for Security: A collection of Model Context Protocol servers for popular sec |
| *...and 13 more* | | | |

### Dev Tools (81 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [TrendRadar](https://github.com/sansan0/TrendRadar) | ⭐ 63.2k | 79 | ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS,  |
| [python-sdk](https://github.com/modelcontextprotocol/python-sdk) | ⭐ 24.7k | 88 | The official Python SDK for Model Context Protocol servers and clients |
| [typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | ⭐ 13.7k | 87 | The official TypeScript SDK for Model Context Protocol servers and clients |
| [modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | ⭐ 9.5k | 74 | Specification and documentation for the Model Context Protocol |
| [dashboard-icons](https://github.com/homarr-labs/dashboard-icons) | ⭐ 8.9k | 65 | 3,400+ curated icons and logos for dashboards and AI agents. SVG, PNG and WEBP o |
| [git-mcp](https://github.com/idosal/git-mcp) | ⭐ 8.5k | 58 | Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP ser |
| [go-sdk](https://github.com/modelcontextprotocol/go-sdk) | ⭐ 5.3k | 74 | The official Go SDK for Model Context Protocol servers and clients. Maintained i |
| [EvoScientist](https://github.com/EvoScientist/EvoScientist) | ⭐ 4.9k | 88 | 🔬 Harness Vibe Research with Self-evolving AI Scientists |
| [mcp-context-forge](https://github.com/IBM/mcp-context-forge) | ⭐ 4.7k | 88 | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/g |
| [notion-mcp-server](https://github.com/makenotion/notion-mcp-server) | ⭐ 4.7k | 64 | Official Notion MCP Server |
| [csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | ⭐ 4.6k | 88 | The official C# SDK for Model Context Protocol servers and clients. Maintained i |
| [mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | ⭐ 4.4k | 72 | Product specific Cloudflare MCP servers |
| [AiSOC](https://github.com/beenuar/AiSOC) | ⭐ 4.3k | 90 | Open-source AI Security Operations Center: alert fusion, LLM-agent triage, MITRE |
| [rust-sdk](https://github.com/modelcontextprotocol/rust-sdk) | ⭐ 4.1k | 74 | The official Rust SDK for the Model Context Protocol |
| [mcp](https://github.com/microsoft/mcp) | ⭐ 3.8k | 73 | Catalog of official Microsoft MCP (Model Context Protocol) server implementation |
| *...and 66 more* | | | |

### Files (10 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [context-mode](https://github.com/mksglu/context-mode) | ⭐ 32.5k | 80 | Context window optimization for AI coding agents. Sandboxes tool output (98% red |
| [webiny-js](https://github.com/webiny/webiny-js) | ⭐ 8.0k | 73 | Open-source, self-hosted CMS platform on AWS serverless (Lambda, DynamoDB, S3).  |
| [registry](https://github.com/modelcontextprotocol/registry) | ⭐ 7.4k | 89 | A community driven registry service for Model Context Protocol (MCP) servers. |
| [spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp) | ⭐ 4.3k | 53 | A Model Context Protocol (MCP) server that provides structured spec-driven devel |
| [redamon](https://github.com/samugit83/redamon) | ⭐ 3.2k | 77 | Open-source, self-hosted AI penetration testing framework: maps your attack surf |
| [mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) | ⭐ 693 | 0 | Go server implementing Model Context Protocol (MCP) for filesystem operations. |
| [mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development) | ⭐ 439 | 0 | Spec-Driven Development MCP Server, not just Vibe Coding |
| [mcp-server](https://github.com/mapbox/mcp-server) | ⭐ 363 | 0 | Mapbox Model Context Protocol (MCP) server |
| [OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server) | ⭐ 210 | 0 | Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and  |
| [mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe) | ⭐ 171 | 0 | 小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an  |

### Finance (2 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate) | ⭐ 1.0k | 0 | A remote Cloudflare MCP server boilerplate with user authentication and Stripe f |
| [memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp) | ⭐ 920 | 0 | A Model Context Protocol (MCP) server implementation for remote memory bank mana |

### Other (162 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [servers](https://github.com/modelcontextprotocol/servers) | ⭐ 91.6k | 74 | Model Context Protocol Servers |
| [worldmonitor](https://github.com/koala73/worldmonitor) | ⭐ 89.6k | 89 | Real-time global intelligence dashboard. AI-powered news aggregation, geopolitic |
| [activepieces](https://github.com/activepieces/activepieces) | ⭐ 25.2k | 74 | AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • A |
| [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | ⭐ 16.6k | 74 | MCP for xiaohongshu.com |
| [aisuite](https://github.com/andrewyng/aisuite) | ⭐ 16.4k | 79 | Simple, unified interface to multiple Generative AI providers  |
| [Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | ⭐ 16.1k | 90 | MCP server to provide Figma layout information to AI coding agents like Cursor |
| [ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) | ⭐ 13.2k | 86 | AI-powered reverse engineering assistant that bridges IDA Pro with language mode |
| [inspector](https://github.com/modelcontextprotocol/inspector) | ⭐ 11.2k | 75 | Visual testing tool for MCP servers |
| [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | ⭐ 10.5k | 89 | MCP Server for Computer Use in Windows |
| [critical](https://github.com/addyosmani/critical) | ⭐ 10.3k | 89 | Extract & Inline Critical-path CSS in HTML pages |
| [mobile-mcp](https://github.com/mobile-next/mobile-mcp) | ⭐ 10.0k | 88 | Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android,  |
| [stitch-skills](https://github.com/google-labs-code/stitch-skills) | ⭐ 8.6k | 64 | A library of Agent Skills designed to work with the Stitch MCP server. Each skil |
| [Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH) | ⭐ 7.8k | 53 | MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients |
| [tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | ⭐ 7.0k | 74 | AI-assisted TradingView chart analysis — connect Claude Code to your TradingView |
| [MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP) | ⭐ 6.5k | 74 | A Model Context Protocol (MCP) server and CLI that provides tools for agent use  |
| *...and 147 more* | | | |

### Productivity (11 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | ⭐ 6.1k | 83 | MCP server for Atlassian tools (Confluence, Jira) |
| [slack-mcp-server](https://github.com/korotovsky/slack-mcp-server) | ⭐ 1.9k | 0 | The most powerful MCP Slack Server with no permission requirements, Apps support |
| [phantom](https://github.com/ghostwright/phantom) | ⭐ 1.5k | 0 | An AI co-worker with its own computer. Self-evolving, persistent memory, MCP ser |
| [keeper.sh](https://github.com/ridafkih/keeper.sh) | ⭐ 1.4k | 0 | Calendar sync tool & universal calendar MCP server. Aggregate, sync and control  |
| [Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server) | ⭐ 425 | 0 | A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Goo |
| [nanobanana-mcp-server](https://github.com/zhongweili/nanobanana-mcp-server) | ⭐ 402 | 0 | AI image generation MCP server powered by Google Gemini, with smart model select |
| [mcp-email-server](https://github.com/Wh1isper/mcp-email-server) | ⭐ 369 | 0 | Full-featured, multi-account MCP email server for Windows, macOS, and Linux—read |
| [mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc) | ⭐ 280 | 0 | A Model Context Protocol (MCP) server providing access to Google Search Console |
| [google-tag-manager-mcp-server](https://github.com/stape-io/google-tag-manager-mcp-server) | ⭐ 238 | 0 | MCP server for Google Tag Manager |
| [mcp-server-apple-events](https://github.com/FradSer/mcp-server-apple-events) | ⭐ 229 | 0 | MCP server providing native macOS integration with Apple Reminders and Calendar  |
| [mcp-server-asana](https://github.com/roychri/mcp-server-asana) | ⭐ 149 | 0 | — |

### Security (3 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [obsidian-local-rest-api](https://github.com/coddingtonbear/obsidian-local-rest-api) | ⭐ 3.1k | 74 | A secure REST API and Model Context Protocol (MCP) server for your vault. |
| [mcpvault](https://github.com/bitbonsai/mcpvault) | ⭐ 1.7k | 0 | A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access |
| [Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server) | ⭐ 1.2k | 0 | A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop wi |

### Web (48 servers)

| Server | Stars | Quality | Description |
|--------|-------|---------|-------------|
| [playwright-mcp](https://github.com/microsoft/playwright-mcp) | ⭐ 38.7k | 90 | Playwright MCP server |
| [apify-mcp-server](https://github.com/apify/apify-mcp-server) | ⭐ 13.4k | 87 | The Apify MCP server enables your AI agents to extract data from social media, s |
| [mcp-chrome](https://github.com/hangwin/mcp-chrome) | ⭐ 12.5k | 53 | Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) serve |
| [firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) | ⭐ 7.7k | 82 | Official Firecrawl MCP server, the context API for AI agents: search, scrape, an |
| [mcp](https://github.com/BrowserMCP/mcp) | ⭐ 7.2k | 65 | Browser MCP is a Model Context Provider (MCP) server that allows AI applications |
| [bb-browser](https://github.com/epiral/bb-browser) | ⭐ 6.3k | 54 | Your browser is the API. CLI + MCP server for AI agents to control Chrome with y |
| [mcp-playwright](https://github.com/executeautomation/mcp-playwright) | ⭐ 5.7k | 47 | Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in |
| [exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) | ⭐ 5.2k | 78 | Exa MCP for web search and web crawling! |
| [anything-analyzer](https://github.com/Mouseww/anything-analyzer) | ⭐ 3.8k | 82 | 全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE   |  All- |
| [mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | ⭐ 3.4k | 74 | Allow LLMs to control a browser with Browserbase and Stagehand |
| [js-reverse-mcp](https://github.com/zhizhuodemao/js-reverse-mcp) | ⭐ 3.0k | 83 | AI Agent-first JS 逆向 MCP Server：有头 Chrome 调试、断点、网络/WebSocket 分析、Patchright 反检测，可 |
| [brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | ⭐ 2.7k | 0 | A powerful Model Context Protocol (MCP) server that provides an all-in-one solut |
| [tavily-mcp](https://github.com/tavily-ai/tavily-mcp) | ⭐ 2.5k | 0 | Production ready MCP server with real-time search, extract, map & crawl. |
| [12306-mcp](https://github.com/Joooook/12306-mcp) | ⭐ 2.4k | 0 | This is a 12306 ticket search server based on the Model Context Protocol (MCP). |
| [DevDocs](https://github.com/cyberagiinc/DevDocs) | ⭐ 2.1k | 0 | Completely free, private, UI based Tech Documentation MCP server. Designed for c |
| *...and 33 more* | | | |

---

## 🔍 Quality Breakdown — Top 10

| Server | README | License | Tests | CI | Releases | Stars | Recency | Issues | **Total** |
|--------|:------:|:-------:|:-----:|:--:|:--------:|:-----:|:-------:|:------:|:---------:|
| **Douyin_TikTok_Download_API** | ✅ | ✅ | ✅ | ✅ | ✅ | 20.9k | today | 644/645 | **90** |
| **excel-mcp-server** | ✅ | ✅ | ✅ | ✅ | ✅ | 4.3k | today | 89/89 | **90** |
| **kordoc** | ✅ | ✅ | ✅ | ✅ | ✅ | 2.8k | today | 92/92 | **90** |
| **gemini-notebook-mcp-cli** | ✅ | ✅ | ✅ | ✅ | ✅ | 6.4k | yesterday | 175/175 | **90** |
| **korean-law-mcp** | ✅ | ✅ | ✅ | ✅ | ✅ | 2.8k | yesterday | 121/121 | **90** |
| **AiSOC** | ✅ | ✅ | ✅ | ✅ | ✅ | 4.3k | today | 92/95 | **90** |
| **playwright-mcp** | ✅ | ✅ | ✅ | ✅ | ✅ | 38.7k | 4d ago | 915/917 | **90** |
| **Figma-Context-MCP** | ✅ | ✅ | ✅ | ✅ | ✅ | 16.1k | today | 171/179 | **90** |
| **ffmpeg-skill** | ✅ | ✅ | ✅ | ✅ | ✅ | 3.1k | today | 52/54 | **90** |
| **supergateway** | ✅ | ✅ | ✅ | ✅ | ✅ | 2.9k | today | 95/99 | **90** |

---

## 💡 Key Insights

- **Most popular**: [servers](https://github.com/modelcontextprotocol/servers) with 91.6k stars
- **Highest quality**: [Douyin_TikTok_Download_API](https://github.com/Evil0ctal/Douyin_TikTok_Download_API) with a score of 90/100
- **Largest category**: `other` with 162 servers
- **New this month**: 2 servers — the ecosystem is growing fast
- **Archived/abandoned**: 16 servers are no longer maintained

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

*Powered by GitHub Actions · Scanned daily · Last run: 2026-10-27 13:10 UTC*

*Built to solve the MCP ecosystem's [discovery gap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) — because the protocol's own roadmap says discoverability is a top priority.*