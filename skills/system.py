from datetime import datetime
from tools.decorators import tool
import subprocess


class SystemSkills:

    @tool(
    name="open_notepad",
    description="Open Microsoft Notepad."
    )
    def open_notepad(self):

        subprocess.Popen("notepad.exe")

        return "Opening Notepad."

    def get_time(self):

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}."

    def get_date(self):

        current_date = datetime.now().strftime("%A, %d %B %Y")

        return f"Today is {current_date}."