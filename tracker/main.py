"""Generates the README.md file"""
from .get_repository_table import create_repo_list
from .topics import ALL_TOPICS


def create_topic_dropdown(tracker_topic: str) -> str:
    """
    Creates a markdown dropdown for a given topic

    Args:
        tracker_topic (str): The topic to create the dropdown for

    Returns:
        str: The markdown dropdown
    """
    markdown_table = create_repo_list(tracker_topic)

    return f"""
<details>
<summary>{tracker_topic}</summary>
<br>

{markdown_table}

</details>
<br>
<br>
"""


def get_text() -> str:
    """
    Creates the markdown text for the README

    Returns:
        str: markdown text containing all the dropdowns
    """
    text = ""
    for topic in ALL_TOPICS:
        text += create_topic_dropdown(topic)
    return text


if __name__ == "__main__":
    with open("tracker/README.md", "w", encoding="utf-8") as f:
        f.write(get_text())