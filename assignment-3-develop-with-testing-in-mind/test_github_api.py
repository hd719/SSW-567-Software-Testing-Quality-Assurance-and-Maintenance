from unittest.mock import Mock, patch

import pytest

import github_api


def _response(payload, status_code=200):
    response = Mock()
    response.json.return_value = payload
    response.raise_for_status = Mock()
    if status_code >= 400:
        response.raise_for_status.side_effect = github_api.requests.HTTPError(
            f"HTTP {status_code}"
        )
    return response


@patch("github_api.requests.get")
def test_list_repositories_returns_names(mock_get):
    mock_get.return_value = _response(
        [{"name": "Triangle567"}, {"name": "Square567"}, {"id": 1234}]
    )

    assert github_api.list_repositories("john567") == ["Triangle567", "Square567"]


def test_list_repositories_requires_non_empty_user():
    with pytest.raises(ValueError):
        github_api.list_repositories("")


@patch("github_api.requests.get")
def test_count_repository_commits_returns_length(mock_get):
    mock_get.return_value = _response([{"sha": "1"}, {"sha": "2"}, {"sha": "3"}])

    assert github_api.count_repository_commits("john567", "Triangle567") == 3


@patch("github_api.requests.get")
def test_get_repos_with_commit_counts(mock_get):
    mock_get.side_effect = [
        _response([{"name": "Triangle567"}, {"name": "Square567"}]),
        _response([{"sha": "1"}, {"sha": "2"}]),
        _response([{"sha": "1"}]),
    ]

    assert github_api.get_repos_with_commit_counts("john567") == [
        ("Triangle567", 2),
        ("Square567", 1),
    ]


@patch("github_api.requests.get")
def test_request_failure_raises_requests_error(mock_get):
    mock_get.side_effect = github_api.requests.RequestException("boom")

    with pytest.raises(github_api.requests.RequestException):
        github_api.list_repositories("john567")


def test_format_repo_commit_report():
    report = github_api.format_repo_commit_report(
        "john567", [("Triangle567", 10), ("Square567", 27)]
    )

    assert report == [
        "User: john567 Repo: Triangle567 - Number of commits: 10",
        "User: john567 Repo: Square567 - Number of commits: 27",
    ]
