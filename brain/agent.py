import json

from brain.llm import LLM
from tools.manager import ToolManager
from tools.adapter import OpenAIToolAdapter


class Agent:

    def __init__(self):

        self.llm = LLM()
        self.tool_manager = ToolManager()
        self.adapter = OpenAIToolAdapter()

    def chat(self, messages):

        response = self.llm.chat(
            messages,
            tools=self.adapter.export()
        )

        message = response.choices[0].message

        # Normal response
        if not message.tool_calls:
            return message.content

        # First requested tool
        tool_call = message.tool_calls[0]

        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print(f"\nTool Requested: {tool_name}")
        print(f"Arguments: {arguments}")

        result = self.tool_manager.execute(
            tool_name,
            **arguments
        )

        return result