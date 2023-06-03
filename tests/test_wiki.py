import os

from github import Github

g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))


def test_no_wiki() -> None:
    """Simple Test to check if all repos have no wikis"""
    for repo in g.get_user().get_repos(affiliation="owner"):
        assert not repo.has_wiki, f"Repo {repo.name} has a wiki"
