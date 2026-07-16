# Development Log

## 2026-07-15

### Milestone: Agent Workflow

Today I completed the OpenAI-style tool execution loop.

The agent now:
- Sends available tools to the LLM.
- Executes one or more tool calls.
- Builds a temporary conversation.
- Performs a second LLM pass.
- Returns natural-language responses.

Lessons learned:
- Assistant tool-call messages must precede tool responses.
- Each tool response requires its own `tool_call_id`.
- Keeping conversation memory separate from internal agent messages simplifies the architecture.

## 2026-07-16

### Milestone: Agent Workflow

- Implemented OpenAI-compatible tool calling.
- Added support for multiple tool executions.
- Added second LLM pass for natural responses.
- Separated agent orchestration from tool execution.