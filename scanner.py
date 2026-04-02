"""
MCP Ecosystem Scanner
Discovers, analyzes, and scores MCP (Model Context Protocol) servers across GitHub.
"""

import json
import os
import re
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests
import yaml

DATA_DIR = Path(__file__).parent / "data"
CONFIG_PATH = Path(__file__).parent / "config.yaml"

GITHUB_API = "https://api.github.com"


def get_headers():
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def gh_get(url: str, params: dict = None) -> dict | list | None:
    """GitHub API request with rate limit handling."""
    if not url.startswith("http"):
        url = f"{GITHUB_API}{url}"

    resp = requests.get(url, headers=get_headers(), params=params, timeout=30)

    if resp.status_code == 403 and "rate limit" in resp.text.lower():
        reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait = max(reset - int(time.time()), 1)
        print(f"  ⏳ Rate limited. Waiting {min(wait, 120)}s...")
        time.sleep(min(wait, 120))
        return gh_get(url, params)

    if resp.status_code in (404, 422):
        return None

    resp.raise_for_status()
    return resp.json()


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


# ─── Discovery ────────────────────────────────────────────────────────────────


def search_github_repos(query: str, max_results: int = 100) -> list[dict]:
    """Search GitHub for repos matching a query."""
    repos = []
    page = 1
    per_page = min(max_results, 100)

    while len(repos) < max_results:
        data = gh_get("/search/repositories", {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": per_page,
            "page": page,
        })
        if not data or not data.get("items"):
            break

        for item in data["items"]:
            repos.append({
                "full_name": item["full_name"],
                "name": item["name"],
                "description": item.get("description", ""),
                "stars": item.get("stargazers_count", 0),
                "forks": item.get("forks_count", 0),
                "language": item.get("language", ""),
                "created_at": item.get("created_at", ""),
                "updated_at": item.get("updated_at", ""),
                "pushed_at": item.get("pushed_at", ""),
                "topics": item.get("topics", []),
                "license": (item.get("license") or {}).get("spdx_id", ""),
                "archived": item.get("archived", False),
                "html_url": item.get("html_url", ""),
                "default_branch": item.get("default_branch", "main"),
            })

        if len(data["items"]) < per_page:
            break
        page += 1
        time.sleep(1)  # Respect search rate limits

    return repos


def discover_servers(config: dict) -> dict[str, dict]:
    """Discover MCP servers from multiple sources."""
    discovery = config["discovery"]
    all_repos = {}

    # Search GitHub
    for query in discovery["github_queries"]:
        print(f"🔍 Searching: {query}")
        repos = search_github_repos(query, discovery.get("max_per_query", 100))
        for r in repos:
            if r["stars"] >= discovery.get("min_stars", 3):
                all_repos[r["full_name"]] = r
        time.sleep(2)

    # Add seed repos
    for repo_name in discovery.get("seed_repos", []):
        if repo_name not in all_repos:
            print(f"🌱 Fetching seed repo: {repo_name}")
            data = gh_get(f"/repos/{repo_name}")
            if data:
                all_repos[repo_name] = {
                    "full_name": data["full_name"],
                    "name": data["name"],
                    "description": data.get("description", ""),
                    "stars": data.get("stargazers_count", 0),
                    "forks": data.get("forks_count", 0),
                    "language": data.get("language", ""),
                    "created_at": data.get("created_at", ""),
                    "updated_at": data.get("updated_at", ""),
                    "pushed_at": data.get("pushed_at", ""),
                    "topics": data.get("topics", []),
                    "license": (data.get("license") or {}).get("spdx_id", ""),
                    "archived": data.get("archived", False),
                    "html_url": data.get("html_url", ""),
                    "default_branch": data.get("default_branch", "main"),
                }

    print(f"\n📦 Discovered {len(all_repos)} candidate repos")
    return all_repos


# ─── Validation ───────────────────────────────────────────────────────────────


def check_file_exists(repo: str, path: str) -> bool:
    """Check if a file exists in a repo."""
    result = gh_get(f"/repos/{repo}/contents/{path}")
    return result is not None


def get_file_content(repo: str, path: str) -> str | None:
    """Get decoded content of a file."""
    import base64
    result = gh_get(f"/repos/{repo}/contents/{path}")
    if result and result.get("content"):
        try:
            return base64.b64decode(result["content"]).decode("utf-8", errors="replace")
        except Exception:
            return None
    return None


def validate_mcp_server(repo_data: dict, config: dict) -> dict:
    """Validate whether a repo is actually an MCP server and extract metadata."""
    repo = repo_data["full_name"]
    detection = config["detection"]
    signals = []
    metadata = {"tools": [], "transport": [], "sdk": "unknown"}

    # Check repo name/description signals
    name_desc = f"{repo_data['name']} {repo_data.get('description', '')}".lower()
    if "mcp" in name_desc and "server" in name_desc:
        signals.append("name_match")
    if "model context protocol" in name_desc:
        signals.append("description_match")

    # Check topics
    topics = repo_data.get("topics", [])
    mcp_topics = [t for t in topics if "mcp" in t.lower()]
    if mcp_topics:
        signals.append("topic_match")

    # Check README for MCP keywords
    readme_content = get_file_content(repo, "README.md") or get_file_content(repo, "readme.md") or ""
    readme_lower = readme_content.lower()
    for keyword in detection.get("readme_keywords", []):
        if keyword.lower() in readme_lower:
            signals.append("readme_keyword")
            break

    # Detect transport type from README
    if "stdio" in readme_lower:
        metadata["transport"].append("stdio")
    if "sse" in readme_lower or "server-sent" in readme_lower:
        metadata["transport"].append("sse")
    if "streamable http" in readme_lower or "streamablehttp" in readme_lower:
        metadata["transport"].append("streamable-http")

    # Detect SDK / language
    lang = repo_data.get("language", "").lower()

    if lang in ("python", ""):
        # Check pyproject.toml or requirements.txt for MCP packages
        pyproject = get_file_content(repo, "pyproject.toml") or ""
        requirements = get_file_content(repo, "requirements.txt") or ""
        setup_py = get_file_content(repo, "setup.py") or ""
        combined = f"{pyproject} {requirements} {setup_py}".lower()

        for pkg in detection.get("python_packages", []):
            if pkg.lower() in combined:
                signals.append(f"python_dep:{pkg}")
                metadata["sdk"] = "python"
                break

    if lang in ("typescript", "javascript", ""):
        # Check package.json for MCP packages
        pkg_json = get_file_content(repo, "package.json") or ""
        pkg_lower = pkg_json.lower()

        for pkg in detection.get("npm_packages", []):
            if pkg.lower() in pkg_lower:
                signals.append(f"npm_dep:{pkg}")
                metadata["sdk"] = "typescript"
                break

    # Extract tools from README (look for tool lists)
    tool_pattern = re.findall(r'`(\w+)`\s*[-–—:]\s*(.{10,80})', readme_content)
    if tool_pattern:
        metadata["tools"] = [{"name": t[0], "description": t[1].strip()} for t in tool_pattern[:20]]

    is_mcp = len(signals) >= 2 or "name_match" in signals

    return {
        "is_mcp": is_mcp,
        "confidence": min(1.0, len(signals) * 0.25),
        "signals": signals,
        "metadata": metadata,
    }


# ─── Analysis ─────────────────────────────────────────────────────────────────


def analyze_repo(repo_data: dict, config: dict) -> dict:
    """Deep analysis of a confirmed MCP server repo."""
    repo = repo_data["full_name"]
    scoring = config["scoring"]

    checks = {
        "has_readme": False,
        "has_license": bool(repo_data.get("license")),
        "has_tests": False,
        "has_ci": False,
        "has_releases": False,
        "stars": repo_data.get("stars", 0),
        "recent_commits": 0,
        "open_issues": 0,
        "closed_issues": 0,
        "contributors": 0,
        "last_commit_days_ago": 999,
    }

    # Check README
    checks["has_readme"] = check_file_exists(repo, "README.md") or check_file_exists(repo, "readme.md")

    # Check for tests
    for test_path in ["tests", "test", "__tests__", "spec", "src/tests"]:
        if check_file_exists(repo, test_path):
            checks["has_tests"] = True
            break

    # Check for CI
    for ci_path in [".github/workflows", ".circleci", ".travis.yml", "Jenkinsfile"]:
        if check_file_exists(repo, ci_path):
            checks["has_ci"] = True
            break

    # Check releases
    releases = gh_get(f"/repos/{repo}/releases", {"per_page": 1})
    if releases and len(releases) > 0:
        checks["has_releases"] = True

    # Commit activity
    commits = gh_get(f"/repos/{repo}/commits", {"per_page": 1, "since": (datetime.now(timezone.utc) - timedelta(days=30)).isoformat()})
    if commits:
        # Use Link header to get count
        checks["recent_commits"] = len(commits)

    # Last commit
    if repo_data.get("pushed_at"):
        pushed = datetime.fromisoformat(repo_data["pushed_at"].replace("Z", "+00:00"))
        checks["last_commit_days_ago"] = (datetime.now(timezone.utc) - pushed).days

    # Issues
    open_issues = gh_get("/search/issues", {"q": f"repo:{repo} is:issue is:open", "per_page": 1})
    closed_issues = gh_get("/search/issues", {"q": f"repo:{repo} is:issue is:closed", "per_page": 1})
    checks["open_issues"] = open_issues.get("total_count", 0) if open_issues else 0
    checks["closed_issues"] = closed_issues.get("total_count", 0) if closed_issues else 0

    # Compute quality score (0-100)
    score = 0
    if checks["has_readme"]:
        score += scoring.get("has_readme_weight", 10)
    if checks["has_license"]:
        score += scoring.get("has_license_weight", 5)
    if checks["has_tests"]:
        score += scoring.get("has_tests_weight", 15)
    if checks["has_ci"]:
        score += scoring.get("has_ci_weight", 10)
    if checks["has_releases"]:
        score += scoring.get("release_exists_weight", 10)

    # Stars score (log scale, max 15)
    import math
    star_score = min(scoring.get("stars_weight", 15), math.log2(max(checks["stars"], 1)) * 2)
    score += star_score

    # Recency score
    recency = max(0, scoring.get("recent_commits_weight", 15) - checks["last_commit_days_ago"] * 0.1)
    score += recency

    # Issue responsiveness
    total_issues = checks["open_issues"] + checks["closed_issues"]
    if total_issues > 0:
        close_ratio = checks["closed_issues"] / total_issues
        score += close_ratio * scoring.get("issue_responsiveness_weight", 10)

    checks["quality_score"] = round(min(100, score), 1)

    return checks


def auto_categorize(repo_data: dict, config: dict) -> str:
    """Auto-categorize a server based on name, description, and topics."""
    text = f"{repo_data['name']} {repo_data.get('description', '')} {' '.join(repo_data.get('topics', []))}".lower()
    categories = config.get("categories", {})

    best_cat = "other"
    best_count = 0

    for cat, keywords in categories.items():
        if cat == "other":
            continue
        count = sum(1 for kw in keywords if kw in text)
        if count > best_count:
            best_count = count
            best_cat = cat

    return best_cat


# ─── Main Pipeline ────────────────────────────────────────────────────────────


def load_history() -> dict:
    path = DATA_DIR / "history.json"
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}


def save_history(history: dict):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_DIR / "history.json", "w") as f:
        json.dump(history, f, indent=2, default=str)


def run_scan(config: dict) -> dict:
    """Full scan pipeline: discover → validate → analyze → score."""
    now = datetime.now(timezone.utc).isoformat()
    history = load_history()

    # Step 1: Discover
    print("=" * 60)
    print("🔍 PHASE 1: Discovery")
    print("=" * 60)
    candidates = discover_servers(config)

    # Step 2: Validate
    print("\n" + "=" * 60)
    print("✅ PHASE 2: Validation")
    print("=" * 60)
    confirmed = {}
    total = len(candidates)

    for i, (name, repo_data) in enumerate(candidates.items(), 1):
        print(f"[{i}/{total}] Validating {name}...", end=" ")
        validation = validate_mcp_server(repo_data, config)

        if validation["is_mcp"]:
            print(f"✅ MCP server (confidence: {validation['confidence']:.0%})")
            confirmed[name] = {**repo_data, "validation": validation}
        else:
            print("❌ Not an MCP server")

        time.sleep(0.3)

    print(f"\n📋 Confirmed {len(confirmed)}/{total} repos as MCP servers")

    # Step 3: Analyze top servers (limit deep analysis to save API calls)
    print("\n" + "=" * 60)
    print("🔬 PHASE 3: Deep Analysis")
    print("=" * 60)

    # Sort by stars, analyze top 100
    sorted_servers = sorted(confirmed.values(), key=lambda x: x.get("stars", 0), reverse=True)
    analyze_limit = min(len(sorted_servers), 100)

    results = {}
    for i, server in enumerate(sorted_servers[:analyze_limit], 1):
        name = server["full_name"]
        print(f"[{i}/{analyze_limit}] Analyzing {name}...")

        try:
            analysis = analyze_repo(server, config)
            category = auto_categorize(server, config)

            results[name] = {
                **server,
                "analysis": analysis,
                "category": category,
                "scanned_at": now,
            }

            print(f"  ⭐ {server['stars']} | Quality: {analysis['quality_score']} | Category: {category}")

        except Exception as e:
            print(f"  ❌ Error: {e}")
            results[name] = {**server, "analysis": {"error": str(e)}, "category": "other", "scanned_at": now}

        time.sleep(0.5)

    # Include remaining confirmed servers without deep analysis
    for server in sorted_servers[analyze_limit:]:
        name = server["full_name"]
        category = auto_categorize(server, config)
        results[name] = {
            **server,
            "analysis": {"quality_score": 0, "shallow": True},
            "category": category,
            "scanned_at": now,
        }

    # Update history
    for name, server in results.items():
        if name not in history:
            history[name] = []
        history[name].append({
            "timestamp": now,
            "stars": server.get("stars", 0),
            "quality_score": server.get("analysis", {}).get("quality_score", 0),
        })
        # Keep 90 days
        cutoff = (datetime.now(timezone.utc) - timedelta(days=90)).isoformat()
        history[name] = [h for h in history[name] if h["timestamp"] >= cutoff]

    save_history(history)

    # Save results
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_DIR / "latest.json", "w") as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\n🎉 Scan complete! {len(results)} MCP servers catalogued.")
    return results


def main():
    config = load_config()
    results = run_scan(config)
    return results


if __name__ == "__main__":
    main()
