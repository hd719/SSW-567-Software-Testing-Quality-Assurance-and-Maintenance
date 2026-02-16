from __future__ import annotations

import sys
from typing import Any

import requests

BASE_URL = "https://api.github.com"


def _get_json(url: str, *, timeout: int = 10) -> Any:
    """Return parsed JSON from a URL."""
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()


def list_repositories(user_id: str) -> list[str]:
    """Return repository names for a GitHub user."""
    if not user_id or not user_id.strip():
        raise ValueError("user_id must be a non-empty string")

    repos_url = f"{BASE_URL}/users/{user_id}/repos"
    repos_payload = _get_json(repos_url)

    if not isinstance(repos_payload, list):
        raise ValueError("Unexpected response for repositories endpoint")

    return [repo["name"] for repo in repos_payload if isinstance(repo, dict) and "name" in repo]


def count_repository_commits(user_id: str, repo_name: str) -> int:
    """Return commit count for one repository."""
    commits_url = f"{BASE_URL}/repos/{user_id}/{repo_name}/commits"
    commits_payload = _get_json(commits_url)

    if not isinstance(commits_payload, list):
        raise ValueError("Unexpected response for commits endpoint")

    return len(commits_payload)


def get_repos_with_commit_counts(user_id: str) -> list[tuple[str, int]]:
    """Return list of (repo_name, commit_count) for a user."""
    repo_names = list_repositories(user_id)
    return [(repo_name, count_repository_commits(user_id, repo_name)) for repo_name in repo_names]


def format_repo_commit_report(user_id: str, repo_stats: list[tuple[str, int]]) -> list[str]:
    """Return display lines in assignment format."""
    return [
        f"User: {user_id} Repo: {repo_name} - Number of commits: {commit_count}"
        for repo_name, commit_count in repo_stats
    ]


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint."""
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1:
        print("Usage: python github_api.py <github_user_id>")
        return 2

    user_id = args[0]
    repo_stats = get_repos_with_commit_counts(user_id)
    for line in format_repo_commit_report(user_id, repo_stats):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
