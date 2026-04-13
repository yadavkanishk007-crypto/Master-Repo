"""
generate_structure.py
Auto-generates a structured repository directory with README files
for all repositories (public + private) of the authenticated GitHub user.
"""

import os
import shutil
import sys
import logging
from dataclasses import dataclass, field
from typing import Optional
import requests

# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────

USERNAME = "yadavkanishk007-crypto"  # ← Change this
TOKEN = os.environ.get("GITHUB_TOKEN", "")
PROTECTED_DIRS = {".github", ".git", "__pycache__", ".venv"}
API_BASE = "https://api.github.com"
PER_PAGE = 100

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


# ──────────────────────────────────────────────
# Data Model
# ──────────────────────────────────────────────

@dataclass
class Repo:
    name: str
    description: str
    url: str
    stars: int
    language: Optional[str]
    is_fork: bool
    is_private: bool
    topics: list = field(default_factory=list)
    license_name: Optional[str] = None
    open_issues: int = 0

    @staticmethod
    def from_api(data: dict) -> "Repo":
        return Repo(
            name=data["name"],
            description=data.get("description") or "No description provided.",
            url=data["html_url"],
            stars=data.get("stargazers_count", 0),
            language=data.get("language"),
            is_fork=data.get("fork", False),
            is_private=data.get("private", False),
            topics=data.get("topics", []),
            license_name=(data.get("license") or {}).get("name"),
            open_issues=data.get("open_issues_count", 0),
        )


# ──────────────────────────────────────────────
# GitHub API Client
# ──────────────────────────────────────────────

class GitHubClient:
    def __init__(self, username: str, token: str):
        self.username = username
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        })

    def fetch_repos(self) -> list:
        repos, page = [], 1

        if TOKEN:
            log.info("Authenticated — fetching all repos (public + private) for: %s", self.username)
        else:
            log.warning("No token found — fetching public repos only for: %s", self.username)

        while True:
            # /user/repos fetches all repos for the authenticated user (public + private)
            # falls back to /users/{username}/repos for unauthenticated requests
            if TOKEN:
                url = f"{API_BASE}/user/repos"
                params = {
                    "per_page": PER_PAGE,
                    "page": page,
                    "sort": "updated",
                    "affiliation": "owner",
                    "visibility": "all",
                }
            else:
                url = f"{API_BASE}/users/{self.username}/repos"
                params = {
                    "per_page": PER_PAGE,
                    "page": page,
                    "sort": "updated",
                }

            response = self.session.get(url, params=params, timeout=15)
            response.raise_for_status()
            batch = response.json()

            if not batch:
                break

            repos.extend(Repo.from_api(r) for r in batch)
            log.info("  Page %d → %d repos fetched", page, len(repos))
            page += 1

        log.info("Total: %d repositories", len(repos))
        return repos


# ──────────────────────────────────────────────
# File System Operations
# ──────────────────────────────────────────────

class StructureBuilder:

    @staticmethod
    def clean_stale_folders(active_repos: list) -> None:
        active_names = {r.name for r in active_repos}
        for entry in os.scandir("."):
            if (
                entry.is_dir()
                and entry.name not in active_names
                and entry.name not in PROTECTED_DIRS
            ):
                log.info("Removing stale folder: %s", entry.name)
                shutil.rmtree(entry.path)

    @staticmethod
    def write_repo_readme(repo: Repo) -> None:
        os.makedirs(repo.name, exist_ok=True)
        path = os.path.join(repo.name, "README.md")

        # Badges
        badges = ""
        if repo.is_private:
            badges += "![Private](https://img.shields.io/badge/visibility-private-red) "
        else:
            badges += "![Public](https://img.shields.io/badge/visibility-public-brightgreen) "
        if repo.language:
            lang_encoded = repo.language.replace(" ", "%20")
            badges += f"![Language](https://img.shields.io/badge/language-{lang_encoded}-blue) "
        badges += f"![Stars](https://img.shields.io/badge/stars-{repo.stars}-yellow) "
        if repo.license_name:
            license_encoded = repo.license_name.replace(" ", "%20").replace("-", "--")
            badges += f"![License](https://img.shields.io/badge/license-{license_encoded}-green)"

        topics_md = (
            " ".join(f"`{t}`" for t in repo.topics)
            if repo.topics else "_No topics_"
        )

        visibility = "🔒 Private" if repo.is_private else "🌐 Public"

        content = f"""\
# {repo.name}

{badges}

> {repo.description}

## 📊 Stats

| Field        | Value |
|--------------|-------|
| 👁 Visibility | {visibility} |
| ⭐ Stars      | {repo.stars} |
| 🛠 Language  | {repo.language or "N/A"} |
| 🐛 Issues    | {repo.open_issues} |
| 📜 License   | {repo.license_name or "N/A"} |

## 🏷 Topics

{topics_md}

## 🔗 Links

- [View on GitHub]({repo.url})

---
_Auto-generated by [generate\\_structure.py](../generate_structure.py)_
"""
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        log.info("  Written: %s", path)

    @staticmethod
    def write_main_readme(repos: list) -> None:
        original_repos = sorted(
            [r for r in repos if not r.is_fork],
            key=lambda r: r.stars,
            reverse=True,
        )
        forked_repos = [r for r in repos if r.is_fork]

        public_count = sum(1 for r in repos if not r.is_private)
        private_count = sum(1 for r in repos if r.is_private)

        def repo_block(repo: Repo) -> str:
            lang_str = f" · 🛠 {repo.language}" if repo.language else ""
            lock_str = " 🔒" if repo.is_private else ""
            return (
                f"### 📁 [{repo.name}](./{repo.name}){lock_str}\n\n"
                f"> {repo.description}\n\n"
                f"⭐ {repo.stars}{lang_str} · [GitHub →]({repo.url})\n\n---\n"
            )

        content = "# 🚀 My GitHub Projects\n\n"
        content += (
            f"> Auto-generated · "
            f"**{len(original_repos)}** original · "
            f"**{len(forked_repos)}** forked · "
            f"**{public_count}** public · "
            f"**{private_count}** private\n\n"
        )
        content += "## 📌 Original Repositories\n\n"
        content += "\n".join(repo_block(r) for r in original_repos)

        if forked_repos:
            content += "\n## 🍴 Forked Repositories\n\n"
            content += "\n".join(repo_block(r) for r in forked_repos)

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(content)
        log.info("Main README.md written (%d repos total)", len(repos))


# ──────────────────────────────────────────────
# Entry Point
# ──────────────────────────────────────────────

def main() -> None:
    try:
        client = GitHubClient(USERNAME, TOKEN)
        repos = client.fetch_repos()

        if not repos:
            log.warning("No repositories found. Exiting.")
            sys.exit(0)

        builder = StructureBuilder()
        builder.clean_stale_folders(repos)

        for repo in repos:
            builder.write_repo_readme(repo)

        builder.write_main_readme(repos)
        log.info("✅ Done.")

    except requests.HTTPError as e:
        log.error("GitHub API error: %s", e.response.text)
        sys.exit(1)
    except requests.RequestException as e:
        log.error("Network error: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
