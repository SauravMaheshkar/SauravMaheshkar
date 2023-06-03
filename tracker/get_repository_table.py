"""Get a markdown table of all repositories that have a specific topic"""
import gc
import os
from typing import List

import pandas as pd
from github import Github

from .topics import ALL_TOPICS

g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))


def create_repo_list(tracker_topic: str) -> str:
    """
    Create a markdown table of all repositories that have a specific topic.

    Args:
        tracker_topic (str): The topic to search for.

    Returns:
        str: A markdown table of all repositories that have a specific topic.
    """

    # Assert that the topic is valid.
    assert tracker_topic in ALL_TOPICS, f"{tracker_topic} is not a valid topic."

    repos: List[str] = []

    # Get all repositories that have the topic.
    for repo in g.get_user().get_repos(affiliation="owner"):
        if tracker_topic in repo.get_topics():
            repos.append(repo.name)

    # Create a dataframe from the list of repositories.
    repo_dataframe = pd.DataFrame(repos, columns=["Repository Name"])
    # Add a link to the repository.
    repo_dataframe["Repository Name"] = repo_dataframe["Repository Name"].apply(
        lambda x: f"[{x}](https://github.com/SauravMaheshkar/{x})"
    )
    # Set the index to the repository name.
    repo_dataframe = repo_dataframe.set_index(keys="Repository Name")

    # Garbage Collection
    _ = gc.collect()

    # Return the corresponding markdown table.
    return repo_dataframe.to_markdown()