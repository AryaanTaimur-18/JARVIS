from tools.decorators import tool
from datetime import datetime
import mss
from pathlib import Path


@tool(

    name="take_screenshot",

    description="Capture the user's screen and save it as an image."

)

def take_screenshot():



    screenshots_dir = Path("data") / "screenshots"

    screenshots_dir.mkdir(parents=True, exist_ok=True)



    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")



    file_path = screenshots_dir / f"screenshot_{timestamp}.png"



    try:

        with mss.mss() as sct:

            sct.shot(output=str(file_path))



        return f"Screenshot saved successfully at '{file_path}'."



    except Exception as e:

        return f"Failed to take screenshot: {e}"