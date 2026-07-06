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