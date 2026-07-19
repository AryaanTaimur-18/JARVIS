import subprocess
from datetime import datetime

from tools.decorators import tool


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
