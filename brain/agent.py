import json

from brain.llm import LLM
from tools.manager import ToolManager
from tools.adapter import OpenAIToolAdapter

from events.event_bus import event_bus


class Agent:

    def __init__(self):

        self.llm = LLM()
        self.tool_manager = ToolManager()
        self.adapter = OpenAIToolAdapter()

    def chat(self, messages):

        # Notify GUI that thinking has started
        event_bus.thinking_started.emit()

        response = self.llm.chat(
            messages,
            tools=self.adapter.export()
        )

        message = response.choices[0].message

        # If no tools are needed, we're done thinking
        if not message.tool_calls:

            event_bus.thinking_finished.emit()

            return message.content

        # Conversation for second LLM call
        agent_messages = messages.copy()

        agent_messages.append(
            {
                "role": "assistant",
                "content": message.content,
                "tool_calls": message.tool_calls,
            }
        )

        # Execute requested tools
        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(f"\nTool Requested: {tool_name}")
            print(f"Arguments: {arguments}")

            # Notify tool started
            event_bus.tool_started.emit(
                tool_name,
                arguments
            )

            try:

                tool = self.tool_manager.get_tool(tool_name)

                result = self.tool_manager.execute(
                    tool_name,
                    **arguments
                )

                # Notify tool succeeded
                event_bus.tool_succeeded.emit(
                    tool_name,
                    arguments,
                    str(result)
                )

                if tool.get("direct_response", False):
                
                    event_bus.thinking_finished.emit()

                    return str(result)

            except Exception as e:

                # Notify tool failed
                event_bus.tool_failed.emit(
                    tool_name,
                    arguments,
                    str(e)
                )

                # Stop thinking before re-raising
                event_bus.thinking_finished.emit()

                raise

            # Send tool result back to the LLM
            agent_messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result),
                }
            )

        # Second LLM call
        final_response = self.llm.chat(agent_messages)

        # Notify GUI that thinking has finished
        event_bus.thinking_finished.emit()

        return final_response.choices[0].message.content