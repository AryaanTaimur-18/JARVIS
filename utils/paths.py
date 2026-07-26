from pathlib import Path
import os


def get_desktop():
    """
    Returns the user's Desktop folder.
    Supports both normal Windows profiles and OneDrive Desktop redirection.
    """

    onedrive_desktop = Path.home() / "OneDrive" / "Desktop"

    if onedrive_desktop.exists():
        return onedrive_desktop

    return Path.home() / "Desktop"

def get_documents():
    return Path.home() / "Documents"

def get_downloads():
    return Path.home() / "Downloads"

def get_pictures():
    return Path.home() / "Pictures"

