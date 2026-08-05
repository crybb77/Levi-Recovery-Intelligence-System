import json
from pathlib import Path


PROFILE_PATH = Path("data/client_profile.json")


def get_client_profile():
    """
    Loads and returns the client's profile information.
    """

    with open(PROFILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def get_preferred_name():
    """
    Returns the client's preferred name.
    """

    profile = get_client_profile()
    return profile["preferred_name"]


def get_program_name():
    """
    Returns the rehabilitation program name.
    """

    profile = get_client_profile()
    return profile["program_name"]