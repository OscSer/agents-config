# Claude Code - Personal Configuration

This repository contains my personal configuration for Claude Code.

## Installation

To copy this configuration to your system:

```bash
# Clone this repository
git clone https://github.com/OscSer/claude-code-config.git

# Navigate to the folder
cd claude-code-config

# Copy custom agents
cp -r agents/ ~/.claude/agents/

# Copy custom commands
cp -r commands/ ~/.claude/commands/

# Copy main configuration
cp settings.json ~/.claude/settings.json
```

## Structure

- `agents/` - Custom specialized agents
- `commands/` - Custom slash commands
- `settings.json` - Main Claude Code configuration
