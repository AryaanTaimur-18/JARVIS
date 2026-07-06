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