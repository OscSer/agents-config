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

echo "Claude Code & OpenCode Configuration Installation"
echo "================================================="

if [ ! -d "$HOME/.claude" ]; then
    echo "Creating .claude directory..."
    mkdir -p "$HOME/.claude"
fi

if validate_source "claude/agents" && [ -d "claude/agents" ]; then
    echo "Installing custom agents..."
    create_symlink "$REPO_DIR/claude/agents" "$HOME/.claude/agents"
    echo "✓ Agents installed"
fi

if validate_source "claude/commands" && [ -d "claude/commands" ]; then
    echo "Installing custom commands..."
    create_symlink "$REPO_DIR/claude/commands" "$HOME/.claude/commands"
    echo "✓ Commands installed"
fi

if validate_source "claude/settings/settings.json" && [ -f "claude/settings/settings.json" ]; then
    echo "Installing configuration..."
    cp "$REPO_DIR/claude/settings/settings.json" "$HOME/.claude/settings.json"
    echo "✓ Configuration installed"
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

echo ""
echo "✅ Installation complete!"
echo "Your Claude Code and OpenCode configurations have been installed successfully."
echo "Claude Code agents and commands are available in ~/.claude/"
echo "OpenCode agents are available in ~/.config/opencode/"
