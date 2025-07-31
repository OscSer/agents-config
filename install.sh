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

echo "Claude Code Configuration Installation"
echo "======================================"

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
    create_symlink "$REPO_DIR/claude/settings/settings.json" "$HOME/.claude/settings.json"
    echo "✓ Configuration installed"
fi

echo ""
echo "✅ Installation complete!"
echo "Your Claude Code configuration has been installed successfully."
