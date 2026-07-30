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