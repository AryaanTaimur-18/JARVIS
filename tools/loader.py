from pathlib import Path
import importlib


class ToolLoader:
    """
    Automatically imports every skill module.
    """

    def __init__(self, skills_folder="skills"):
        self.skills_folder = Path(skills_folder)

    def load(self):

        for file in self.skills_folder.glob("*.py"):

            if file.stem == "__init__":
                continue

            module_name = f"{self.skills_folder.name}.{file.stem}"

            importlib.import_module(module_name)

            print(f"✓ Loaded {module_name}")