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

        if not message.tool_calls:
            return message.content

        results = {}

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(f"\nTool Requested: {tool_name}")
            print(f"Arguments: {arguments}")

            result = self.tool_manager.execute(
                tool_name,
                **arguments
            )

            results[tool_name] = result

            agent_messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            }
        )
            
        agent_messages = messages.copy()
        
        agent_messages.append(
        {
        "role": "assistant",
        "content": message.content,
        "tool_calls": message.tool_calls
        }
    )