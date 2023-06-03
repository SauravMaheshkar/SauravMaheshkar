import os

from github import Github

g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))


def test_git_health() -> None:
    """Simple Test to check if all repos follow some healthy git rules"""
    for repo in g.get_user().get_repos(affiliation="owner"):
        # Skip archived repos
        if repo.archived:
            continue
        assert (
            repo.delete_branch_on_merge is True
        ), f"{repo.name} does not have delete_branch_on_merge enabled"
