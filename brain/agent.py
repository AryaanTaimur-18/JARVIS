import json

from brain.llm import LLM
from tools.manager import ToolManager
from tools.adapter import OpenAIToolAdapter


class Agent:

    def __init__(self):

        self.llm = LLM()
        self.tool_manager = ToolManager()
        self.adapter = OpenAIToolAdapter()

        # Callbacks (connected by AssistantWorker)
        self.on_thinking_started = None
        self.on_thinking_finished = None

        self.on_tool_started = None
        self.on_tool_finished = None
        self.on_tool_failed = None

    def chat(self, messages):

        # Notify GUI that thinking has started
        if self.on_thinking_started:
            self.on_thinking_started()

        response = self.llm.chat(
            messages,
            tools=self.adapter.export()
        )

        message = response.choices[0].message

        # If no tools are needed, we're done thinking
        if not message.tool_calls:

            if self.on_thinking_finished:
                self.on_thinking_finished()

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
            if self.on_tool_started:
                self.on_tool_started(
                    tool_name,
                    arguments
                )

            try:

                result = self.tool_manager.execute(
                    tool_name,
                    **arguments
                )

                # Notify tool succeeded
                if self.on_tool_finished:
                    self.on_tool_finished(
                        tool_name,
                        arguments,
                        str(result)
                    )

            except Exception as e:

                # Notify tool failed
                if self.on_tool_failed:
                    self.on_tool_failed(
                        tool_name,
                        arguments,
                        str(e)
                    )

                # Stop thinking before re-raising
                if self.on_thinking_finished:
                    self.on_thinking_finished()

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
        if self.on_thinking_finished:
            self.on_thinking_finished()

        return final_response.choices[0].message.content