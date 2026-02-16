import pytest

import github_api


def test_list_repositories_requires_non_empty_user():
    with pytest.raises(ValueError):
        github_api.list_repositories("")


def test_list_repositories_rejects_whitespace_user():
    with pytest.raises(ValueError):
        github_api.list_repositories("   ")


def test_get_repos_with_commit_counts_requires_non_empty_user():
    with pytest.raises(ValueError):
        github_api.get_repos_with_commit_counts("")


def test_format_repo_commit_report():
    report = github_api.format_repo_commit_report(
        "john567", [("Triangle567", 10), ("Square567", 27)]
    )

    assert report == [
        "User: john567 Repo: Triangle567 - Number of commits: 10",
        "User: john567 Repo: Square567 - Number of commits: 27",
    ]


def test_main_without_arguments_returns_usage_code(capsys):
    exit_code = github_api.main([])
    captured = capsys.readouterr()

    assert exit_code == 2
    assert "Usage: python github_api.py <github_user_id>" in captured.out
