# Agents Instructions

Personal configuration for AI agents (Claude Code and OpenCode) with custom agents, commands, and settings.

## Project Structure

- `claude/` - Claude Code configuration (agents, commands, settings, templates)
- `opencode/` - OpenCode configuration (agents, settings, templates)
- `common/` - Shared instructions (AGENTS.md)
- `install.py` - Automated installation with symbolic links

## Workflow

1. **Plan**: `/plan` → Creates plan using software-architect agent
2. **Implement**: `/implement` → Executes with senior-developer agent
3. **Commit**: `/commit` → Creates conventional commits

## MCP Tools Available

- **serena**: Semantic code analysis and editing
- **context7**: Up-to-date library documentation
- **sequential-thinking**: Decision-making assistance

## Templates Usage

- `claude/templates/agent-template.md` - For new Claude Code agents
- `claude/templates/command-template.md` - For new Claude Code commands
- `opencode/templates/agent-template.md` - For new OpenCode agents
