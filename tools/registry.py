class ToolRegistry:
    """
    Stores every tool available to JARVIS.
    """

    def __init__(self):
        self._tools = {}

    def register(
        self,
        name,
        description,
        function,
        parameters=None
    ):

        self._tools[name] = {
            "name": name,
            "description": description,
            "function": function,
            "parameters": parameters or {}
        }

    def get(self, name):
        return self._tools.get(name)

    def all(self):
        return self._tools


registry = ToolRegistry()