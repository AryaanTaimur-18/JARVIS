from tools.registry import registry


class ToolManager:
    """
    Executes registered tools.
    """

    def execute(self, name, **kwargs):

        tool = registry.get(name)

        if tool is None:
            raise ValueError(f"Unknown tool: {name}")

        return tool["function"](**kwargs)

    def available_tools(self):
        return registry.all()