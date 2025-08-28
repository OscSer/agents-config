# Project Instructions

Personal configuration for AI agents.

## Structure

- `claude/` - Claude Code configuration
- `gemini/` - Gemini CLI configuration
- `opencode/` - OpenCode configuration
- `rules/` - Shared agent rules
- `install.py` - Automated installation with symbolic links

## Development

- When making any changes, you must check whether install.py needs to be updated
- NEVER use context7, ALWAYS consult the appropriate documentation for each agent:

**Claude Code docs**

- [Settings](https://docs.anthropic.com/en/docs/claude-code/settings)
- [Commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [MCP](https://docs.anthropic.com/en/docs/claude-code/mcp)
- [Rules](https://docs.anthropic.com/en/docs/claude-code/memory)

**Gemini docs**

- [Settings & MCP & Rules](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/configuration.md)
- [Commands](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/commands.md#custom-commands)

**Opencode docs**

- [Settings](https://opencode.ai/docs/config/)
- [Commands](https://opencode.ai/docs/commands/#markdown)
- [MCP](https://opencode.ai/docs/mcp-servers/)
- [Rules](https://opencode.ai/docs/rules/)
