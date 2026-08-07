from tools.registry import registry


class ToolManager:
    """
    Executes registered tools.
    """

    def get_tool(self, name):

        tool = registry.get(name)

        if tool is None:
            raise ValueError(f"Unknown tool: {name}")

        return tool

    def execute(self, name, **kwargs):

        tool = self.get_tool(name)

        return tool["function"](**kwargs)

    def available_tools(self):

        return registry.all()