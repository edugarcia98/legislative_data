"""
Data manipulation functions
"""

from csv import DictReader
from typing import Generator


def _load_data_from_csv(file_path: str) -> Generator[dict, None, None]:
    """
    Loads data from CSV

    Args:
        file_path (str): File path
    Returns:
        Generator
    """
    with open(file_path, newline="") as csv_file:
        reader = DictReader(csv_file)

        for row in reader:
            yield row


def bills_data() -> Generator[dict, None, None]:
    """
    Loads data from bills.csv

    Returns:
        Generator
    """
    return _load_data_from_csv("legislative_data/data/bills.csv")


def legislators_data() -> Generator[dict, None, None]:
    """
    Loads data from legislators.csv

    Returns:
        Generator
    """
    return _load_data_from_csv("legislative_data/data/legislators.csv")


def vote_results_data() -> Generator[dict, None, None]:
    """
    Loads data from vote_results.csv

    Returns:
        Generator
    """
    return _load_data_from_csv("legislative_data/data/vote_results.csv")


def votes_data() -> Generator[dict, None, None]:
    """
    Loads data from votes.csv

    Returns:
        Generator
    """
    return _load_data_from_csv("legislative_data/data/votes.csv")
