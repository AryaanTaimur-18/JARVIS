# Changelog

## v0.4.0 - Native AI Tool Calling

### Added

- Introduced the Agent layer to manage interactions between the LLM and tools.
- Implemented native OpenAI-compatible tool calling using LM Studio.
- Added dynamic tool discovery through the tool registry.
- Connected the OpenAI Tool Adapter to the LLM.
- Implemented ToolManager for automatic tool execution.
- Successfully executed AI-selected tools such as:
  - open_notepad
  - get_time
- Verified that the local Qwen model can request multiple tools in a single response.

### Next

- Execute multiple tool calls.
- Send tool results back to the LLM.
- Produce natural responses after tool execution.

## Milestone: Agent Core Completed

Today I completed the core architecture of JARVIS.

The agent now follows the OpenAI function-calling workflow:
1. Sends the conversation and available tools to the LLM.
2. Receives one or more tool calls.
3. Executes each requested tool.
4. Builds a temporary conversation containing the assistant's tool requests and tool outputs.
5. Sends the updated conversation back to the LLM.
6. Returns a natural-language response to the user.

This separates responsibilities cleanly:
- The LLM decides *what* to do.
- The ToolManager performs the actions.
- The Agent coordinates the interaction.
- ConversationMemory remains free of internal tool messages.