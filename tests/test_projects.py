import os

from github import Github

g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))


def test_no_projects() -> None:
    """Simple Test to check if all repos have no projects"""
    for repo in g.get_user().get_repos(affiliation="owner"):
        assert not repo.has_projects, f"Repo {repo.name} has a project"
