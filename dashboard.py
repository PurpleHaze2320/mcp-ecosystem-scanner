"""
Dashboard Generator for MCP Ecosystem Scanner
Generates a rich README.md registry with quality scores, categories, and trends.
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path

import yaml

DATA_DIR = Path(__file__).parent / "data"
CONFIG_PATH = Path(__file__).parent / "config.yaml"
README_PATH = Path(__file__).parent / "README.md"


def load_latest() -> dict:
    with open(DATA_DIR / "latest.json") as f:
        return json.load(f)


def load_history() -> dict:
    path = DATA_DIR / "history.json"
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def format_number(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}k"
    return str(n)


def quality_badge(score: float) -> str:
    if score >= 70:
        return "🟢 Excellent"
    elif score >= 50:
        return "🔵 Good"
    elif score >= 30:
        return "🟡 Fair"
    elif score >= 10:
        return "🟠 Needs Work"
    return "🔴 Minimal"


def quality_bar(score: float) -> str:
    filled = round(score / 10)
    return "█" * filled + "░" * (10 - filled)


def days_ago(iso_date: str) -> str:
    if not iso_date:
        return "N/A"
    try:
        dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
        days = (datetime.now(timezone.utc) - dt).days
        if days == 0:
            return "today"
        if days == 1:
            return "yesterday"
        if days < 30:
            return f"{days}d ago"
        if days < 365:
            return f"{days // 30}mo ago"
        return f"{days // 365}y ago"
    except Exception:
        return "N/A"


def transport_badges(transport: list) -> str:
    badges = []
    for t in transport:
        if t == "stdio":
            badges.append("`stdio`")
        elif t == "sse":
            badges.append("`SSE`")
        elif t == "streamable-http":
            badges.append("`HTTP`")
    return " ".join(badges) if badges else "—"


def generate_readme(data: dict, history: dict, config: dict) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Prepare sorted server list
    servers = []
    for name, info in data.items():
        if "analysis" in info and not info["analysis"].get("error"):
            servers.append(info)

    servers.sort(key=lambda x: x.get("analysis", {}).get("quality_score", 0), reverse=True)
    total = len(servers)

    # Category counts
    categories = {}
    for s in servers:
        cat = s.get("category", "other")
        categories.setdefault(cat, []).append(s)

    # Language breakdown
    languages = {}
    for s in servers:
        lang = s.get("language", "Unknown") or "Unknown"
        languages[lang] = languages.get(lang, 0) + 1

    # Transport breakdown
    transports = {"stdio": 0, "sse": 0, "streamable-http": 0, "unknown": 0}
    for s in servers:
        found = s.get("validation", {}).get("metadata", {}).get("transport", [])
        if found:
            for t in found:
                transports[t] = transports.get(t, 0) + 1
        else:
            transports["unknown"] += 1

    # New servers (created in last 30 days)
    new_servers = [s for s in servers if s.get("created_at") and
                   (datetime.now(timezone.utc) - datetime.fromisoformat(s["created_at"].replace("Z", "+00:00"))).days < 30]

    lines = [
        "# 🔬 MCP Ecosystem Scanner",
        "",
        "> The most comprehensive automated registry of [Model Context Protocol](https://modelcontextprotocol.io/) servers.",
        "> Discovers, validates, and quality-scores every MCP server on GitHub — daily.",
        "",
        f"> **{total}** servers catalogued | **{len(categories)}** categories | Last scan: **{now}**",
        "",
        "## Why This Exists",
        "",
        "MCP is the open standard that lets AI agents (Claude, GPT, Gemini, etc.) connect to external tools and data.",
        "The ecosystem is exploding — but discovery is fragmented. The official registry is young, awesome-lists are",
        "manually curated, and there's no automated way to know which servers are well-maintained vs. abandoned.",
        "",
        "This scanner crawls GitHub daily, validates each repo as a genuine MCP server, and scores its quality",
        "based on documentation, tests, CI, maintenance activity, and community adoption.",
        "",
        "---",
        "",
    ]

    # ─── Stats Overview ───
    total_stars = sum(s.get("stars", 0) for s in servers)
    avg_quality = sum(s.get("analysis", {}).get("quality_score", 0) for s in servers) / max(total, 1)

    lines += [
        "## 📊 Ecosystem Overview",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Total MCP Servers | **{total}** |",
        f"| Combined GitHub Stars | **{format_number(total_stars)}** |",
        f"| Average Quality Score | **{avg_quality:.1f}/100** |",
        f"| New This Month | **{len(new_servers)}** |",
        f"| Categories | **{len(categories)}** |",
        "",
    ]

    # Language breakdown
    lang_parts = [f"**{lang}**: {count}" for lang, count in sorted(languages.items(), key=lambda x: -x[1])[:6]]
    lines += [
        "**Languages:** " + " · ".join(lang_parts),
        "",
        "**Transports:** " + " · ".join(f"`{t}`: {c}" for t, c in transports.items() if c > 0),
        "",
        "---",
        "",
    ]

    # ─── New & Trending ───
    if new_servers:
        new_servers.sort(key=lambda x: x.get("stars", 0), reverse=True)
        lines += [
            "## 🆕 New This Month",
            "",
            "| Server | Stars | Language | Category | Quality |",
            "|--------|-------|----------|----------|---------|",
        ]
        for s in new_servers[:15]:
            name = s["full_name"]
            desc = (s.get("description") or "")[:60]
            quality = s.get("analysis", {}).get("quality_score", 0)
            lines.append(
                f"| [{s['name']}](https://github.com/{name}) | ⭐ {format_number(s.get('stars', 0))} | {s.get('language', '?')} | `{s.get('category', 'other')}` | {quality_bar(quality)} {quality:.0f} |"
            )
        lines += ["", "---", ""]

    # ─── Top Servers by Quality ───
    lines += [
        "## 🏆 Top Servers by Quality Score",
        "",
        "| Rank | Server | Quality | Stars | Description | Category | Transport |",
        "|------|--------|---------|-------|-------------|----------|-----------|",
    ]

    for i, s in enumerate(servers[:30], 1):
        name = s["full_name"]
        desc = (s.get("description") or "—")[:70]
        quality = s.get("analysis", {}).get("quality_score", 0)
        transport = transport_badges(s.get("validation", {}).get("metadata", {}).get("transport", []))
        lines.append(
            f"| {i} | [{s['name']}](https://github.com/{name}) | {quality_bar(quality)} **{quality:.0f}** | {format_number(s.get('stars', 0))} | {desc} | `{s.get('category', 'other')}` | {transport} |"
        )

    lines += ["", "---", ""]

    # ─── By Category ───
    lines += ["## 📂 Servers by Category", ""]

    for cat in sorted(categories.keys()):
        cat_servers = sorted(categories[cat], key=lambda x: x.get("stars", 0), reverse=True)
        count = len(cat_servers)

        lines += [
            f"### {cat.replace('-', ' ').title()} ({count} servers)",
            "",
            "| Server | Stars | Quality | Description |",
            "|--------|-------|---------|-------------|",
        ]

        for s in cat_servers[:15]:
            name = s["full_name"]
            desc = (s.get("description") or "—")[:80]
            quality = s.get("analysis", {}).get("quality_score", 0)
            lines.append(
                f"| [{s['name']}](https://github.com/{name}) | ⭐ {format_number(s.get('stars', 0))} | {quality:.0f} | {desc} |"
            )

        if count > 15:
            lines.append(f"| *...and {count - 15} more* | | | |")
        lines += [""]

    lines += ["---", ""]

    # ─── Quality Breakdown for Top 10 ───
    lines += [
        "## 🔍 Quality Breakdown — Top 10",
        "",
        "| Server | README | License | Tests | CI | Releases | Stars | Recency | Issues | **Total** |",
        "|--------|:------:|:-------:|:-----:|:--:|:--------:|:-----:|:-------:|:------:|:---------:|",
    ]

    for s in servers[:10]:
        a = s.get("analysis", {})
        check = lambda b: "✅" if b else "❌"
        lines.append(
            f"| **{s['name']}** | {check(a.get('has_readme'))} | {check(a.get('has_license'))} | {check(a.get('has_tests'))} | {check(a.get('has_ci'))} | {check(a.get('has_releases'))} | {format_number(s.get('stars', 0))} | {days_ago(s.get('pushed_at'))} | {a.get('closed_issues', 0)}/{a.get('open_issues', 0) + a.get('closed_issues', 0)} | **{a.get('quality_score', 0):.0f}** |"
        )

    lines += ["", "---", ""]

    # ─── Key Insights ───
    lines += ["## 💡 Key Insights", ""]

    most_starred = max(servers, key=lambda x: x.get("stars", 0)) if servers else None
    if most_starred:
        lines.append(f"- **Most popular**: [{most_starred['name']}](https://github.com/{most_starred['full_name']}) with {format_number(most_starred['stars'])} stars")

    highest_quality = servers[0] if servers else None
    if highest_quality:
        lines.append(f"- **Highest quality**: [{highest_quality['name']}](https://github.com/{highest_quality['full_name']}) with a score of {highest_quality['analysis']['quality_score']:.0f}/100")

    biggest_cat = max(categories.items(), key=lambda x: len(x[1])) if categories else None
    if biggest_cat:
        lines.append(f"- **Largest category**: `{biggest_cat[0]}` with {len(biggest_cat[1])} servers")

    if new_servers:
        lines.append(f"- **New this month**: {len(new_servers)} servers — the ecosystem is growing fast")

    archived = [s for s in servers if s.get("archived")]
    if archived:
        lines.append(f"- **Archived/abandoned**: {len(archived)} servers are no longer maintained")

    lines += ["", "---", ""]

    # ─── How to Use ───
    lines += [
        "## 🚀 Running the Scanner",
        "",
        "```bash",
        "git clone https://github.com/YOUR_USERNAME/mcp-ecosystem-scanner.git",
        "cd mcp-ecosystem-scanner",
        "pip install -r requirements.txt",
        "",
        "# Set GitHub token (recommended for higher API limits)",
        "export GITHUB_TOKEN=ghp_your_token_here",
        "",
        "# Run the scanner",
        "python scanner.py",
        "",
        "# Generate the dashboard",
        "python dashboard.py",
        "```",
        "",
        "## ⚙️ How Quality Scoring Works",
        "",
        "Each server gets a score from 0–100 based on:",
        "",
        "| Signal | Points | What It Checks |",
        "|--------|--------|----------------|",
        "| Has README | 10 | Documentation exists |",
        "| Has License | 5 | Open source license present |",
        "| Has Tests | 15 | Test directory found |",
        "| Has CI/CD | 10 | GitHub Actions or similar configured |",
        "| Has Releases | 10 | At least one tagged release |",
        "| GitHub Stars | 15 | Community adoption (log scale) |",
        "| Recent Activity | 15 | Days since last commit |",
        "| Issue Health | 10 | Ratio of closed to total issues |",
        "",
        "## 📋 Adding a Server Manually",
        "",
        "Add repos to `config.yaml` under `discovery.seed_repos`:",
        "",
        "```yaml",
        "seed_repos:",
        "  - owner/my-mcp-server",
        "```",
        "",
        "---",
        "",
        f"*Powered by GitHub Actions · Scanned daily · Last run: {now}*",
        "",
        "*Built to solve the MCP ecosystem's [discovery gap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) — because the protocol's own roadmap says discoverability is a top priority.*",
    ]

    return "\n".join(lines)


def main():
    config = load_config()
    data = load_latest()
    history = load_history()

    readme = generate_readme(data, history, config)
    with open(README_PATH, "w") as f:
        f.write(readme)

    print(f"✅ Dashboard written to {README_PATH}")
    print(f"   {len(data)} servers in registry")


if __name__ == "__main__":
    main()
