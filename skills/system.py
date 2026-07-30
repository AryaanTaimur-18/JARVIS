import subprocess
from datetime import datetime

from tools.decorators import tool

import os

from utils.paths import (
    get_desktop,
    get_documents,
    get_downloads,
    get_pictures,
)


@tool(
    name="open_notepad",
    description="Open Microsoft Notepad."
)
def open_notepad():

    subprocess.Popen("notepad.exe")

    return "Opening Notepad."


@tool(
    name="get_time",
    description="Returns the current system time."
)
def get_time():

    return datetime.now().strftime("%I:%M %p")


@tool(
    name="get_date",
    description="Returns today's date."
)
def get_date():

    return datetime.now().strftime("%A, %d %B %Y")


import subprocess

from tools.decorators import tool

APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "chrome": "chrome.exe",
}


@tool(
    name="open_application",
    description="Open a desktop application by name."
)
def open_application(application_name):

    application_name = application_name.lower()

    exe = APPLICATIONS.get(application_name)

    if exe is None:
        return f"Sorry, I don't know how to open '{application_name}'."

    try:
        subprocess.Popen(exe)
        return f"Opening {application_name.title()}."

    except Exception as e:
        return f"Failed to open {application_name}: {e}"
    
import webbrowser

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "linkedin": "https://www.linkedin.com",
    "chatgpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com",
}


@tool(
    name="open_website",
    description="Open a website by name."
)
def open_website(website_name):

    website_name = website_name.lower()

    if website_name.startswith(("http://", "https://")):
        url = website_name
    else:
        url = WEBSITES.get(website_name)

    if url is None:
        return f"Sorry, I don't know how to open '{website_name}'."

    try:
        webbrowser.open(url)
        return f"Opening {website_name.title()}."

    except Exception as e:
        return f"Failed to open {website_name}: {e}"
    
from pathlib import Path

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
    
    
