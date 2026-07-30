from pathlib import Path
from tools.decorators import tool
import os

from utils.paths import (
    get_desktop,
    get_documents,
    get_downloads,
    get_pictures,
)

@tool(
    name="create_folder",
    description="Create a folder on the desktop."
)
def create_folder(folder_name):
    
    from utils.paths import get_desktop

    desktop = get_desktop()

    folder_path = desktop / folder_name

    print(Path.home())
    print(desktop)
    print(folder_path)

    if folder_path.exists():
        return f"The folder '{folder_name}' already exists."

    try:
        folder_path.mkdir(parents=True)
        print("Exists after mkdir:", folder_path.exists())
        return f"Created folder '{folder_name}' successfully."

    except Exception as e:
        return f"Failed to create folder '{folder_name}': {e}"


@tool(
    name="open_folder",
    description="Open a folder by name from common locations such as Desktop, Documents, Downloads, or Pictures."
)
def open_folder(folder_name):

    folder_name = folder_name.strip()

    locations = [
        get_desktop(),
        get_documents(),
        get_downloads(),
        get_pictures(),
    ]

    special_folders = {
    "desktop": get_desktop(),
    "documents": get_documents(),
    "downloads": get_downloads(),
    "pictures": get_pictures(),
    }

    special = special_folders.get(folder_name.lower())

    if special:
        os.startfile(special)
        return f"Opening {folder_name.title()}."

    for location in locations:

        candidate = location / folder_name

        if candidate.exists() and candidate.is_dir():

            os.startfile(candidate)

            return f"Opening folder '{folder_name}'."

    return f"Couldn't find a folder named '{folder_name}'."
