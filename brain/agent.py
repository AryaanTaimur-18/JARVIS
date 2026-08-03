import json

from brain.llm import LLM
from tools.manager import ToolManager
from tools.adapter import OpenAIToolAdapter
from events.event_bus import event_bus

from events.constants import Events

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

        # Temporary conversation for the second LLM call
        agent_messages = messages.copy()

        # Preserve the assistant's tool requests
        agent_messages.append(
            {
                "role": "assistant",
                "content": message.content,
                "tool_calls": message.tool_calls
            }
        )

        results = {}

        # Execute every requested tool
        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(f"\nTool Requested: {tool_name}")
            print(f"Arguments: {arguments}")


            event_bus.emit(
                Events.TOOL_STARTED,
                tool_name=tool_name,
                arguments=arguments
            )

            try:

                result = self.tool_manager.execute(
                    tool_name,
                    **arguments
                )

                event_bus.emit(
                    Events.TOOL_SUCCEEDED,
                    tool_name=tool_name,
                    arguments=arguments,
                    result=result
                )

            except Exception as e:

                event_bus.emit(
                    Events.TOOL_FAILED,
                    tool_name=tool_name,
                    arguments=arguments,
                    error=str(e)
                )

                raise

            results[tool_name] = result

            # Add one tool message for THIS tool
            agent_messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )

        # Second LLM call
        final_response = self.llm.chat(agent_messages)

        return final_response.choices[0].message.content
        