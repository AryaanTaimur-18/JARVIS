class ToolRegistry:
    """
    Stores every tool available to JARVIS.
    """

    def __init__(self):
        self._tools = {}

    def register(self, tool):

        self._tools[tool["name"]] = tool

    def get(self, name):

        return self._tools.get(name)

    def all(self):

        return self._tools


registry = ToolRegistry()