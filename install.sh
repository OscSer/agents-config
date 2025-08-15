#!/bin/bash

set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

create_symlink() {
    local source="$1"
    local target="$2"

    if [ ! -e "$source" ]; then
        echo "Warning: Source $source does not exist, skipping..."
        return 1
    fi

    if [ -e "$target" ] || [ -L "$target" ]; then
        rm -rf "$target"
    fi

    if ln -sf "$source" "$target" 2>/dev/null; then
        return 0
    else
        echo "Warning: Symbolic link failed, falling back to copy..."
        if [ -d "$source" ]; then
            cp -r "$source" "$target"
        else
            cp "$source" "$target"
        fi
        return 0
    fi
}

validate_source() {
    local path="$1"
    if [ ! -e "$REPO_DIR/$path" ]; then
        echo "Warning: $path not found in repository, skipping..."
        return 1
    fi
    return 0
}

update_claude_mcp_config() {
    local mcp_source="$REPO_DIR/claude/.mcp.json"
    local claude_config="$HOME/.claude.json"
    
    if [ ! -f "$mcp_source" ]; then
        echo "Warning: claude/.mcp.json not found, skipping MCP configuration..."
        return 1
    fi
    
    echo "Updating Claude MCP configuration..."
    
    python3 -c "
import json
import os
import sys

mcp_source = '$mcp_source'
claude_config = '$claude_config'

try:
    with open(mcp_source, 'r') as f:
        mcp_data = json.load(f)
    
    if 'mcpServers' not in mcp_data:
        print('Error: mcpServers not found in claude/.mcp.json')
        sys.exit(1)
    
    if os.path.exists(claude_config):
        with open(claude_config, 'r') as f:
            claude_data = json.load(f)
    else:
        claude_data = {}
    
    claude_data['mcpServers'] = mcp_data['mcpServers']
    
    with open(claude_config, 'w') as f:
        json.dump(claude_data, f, indent=2)
    
    print('✓ MCP configuration updated successfully')
    
except Exception as e:
    print(f'Error updating MCP configuration: {e}')
    sys.exit(1)
"
    
    return $?
}

echo "Claude Code & OpenCode Configuration Installation"
echo "================================================="

if [ ! -d "$HOME/.claude" ]; then
    echo "Creating Claude Code directory..."
    mkdir -p "$HOME/.claude"
fi

if validate_source "claude/agents" && [ -d "claude/agents" ]; then
    echo "Installing Claude Code custom agents..."
    create_symlink "$REPO_DIR/claude/agents" "$HOME/.claude/agents"
    echo "✓ Claude Code agents installed"
fi

if validate_source "claude/commands" && [ -d "claude/commands" ]; then
    echo "Installing Claude Code custom commands..."
    create_symlink "$REPO_DIR/claude/commands" "$HOME/.claude/commands"
    echo "✓ Claude Code commands installed"
fi

if validate_source "claude/settings/settings.json" && [ -f "claude/settings/settings.json" ]; then
    echo "Installing Claude Code configuration..."
    cp "$REPO_DIR/claude/settings/settings.json" "$HOME/.claude/settings.json"
    echo "✓ Claude Code configuration installed"
fi

if validate_source "common/AGENTS.md" && [ -f "common/AGENTS.md" ]; then
    echo "Installing shared AGENTS.md for Claude Code..."
    create_symlink "$REPO_DIR/common/AGENTS.md" "$HOME/.claude/AGENTS.md"
    echo "✓ Claude Code shared AGENTS.md installed"
fi

if validate_source "claude/.mcp.json" && [ -f "claude/.mcp.json" ]; then
    update_claude_mcp_config
fi

if [ ! -d "$HOME/.config/opencode" ]; then
    echo "Creating OpenCode directory..."
    mkdir -p "$HOME/.config/opencode"
fi

if validate_source "opencode/agents" && [ -d "opencode/agents" ]; then
    echo "Installing OpenCode agents..."
    create_symlink "$REPO_DIR/opencode/agents" "$HOME/.config/opencode/agent"
    echo "✓ OpenCode agents installed"
fi

if validate_source "opencode/settings/config.json" && [ -f "opencode/settings/config.json" ]; then
    echo "Installing OpenCode configuration..."
    cp "$REPO_DIR/opencode/settings/config.json" "$HOME/.config/opencode/config.json"
    echo "✓ OpenCode configuration installed"
fi

if validate_source "common/AGENTS.md" && [ -f "common/AGENTS.md" ]; then
    echo "Installing shared AGENTS.md for OpenCode..."
    create_symlink "$REPO_DIR/common/AGENTS.md" "$HOME/.config/opencode/AGENTS.md"
    echo "✓ OpenCode shared AGENTS.md installed"
fi

echo ""
echo "✅ Installation complete!"
echo "Your Claude Code and OpenCode configurations have been installed successfully."
echo "Claude Code agents and commands are available in ~/.claude/"
echo "OpenCode configuration is available in ~/.config/opencode/"
