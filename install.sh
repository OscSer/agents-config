#!/bin/bash

set -e

echo "Claude Code Configuration Installation"
echo "======================================"

if [ ! -d "$HOME/.claude" ]; then
    echo "Creating .claude directory..."
    mkdir -p "$HOME/.claude"
fi

if [ -d "agents" ]; then
    echo "Installing custom agents..."
    mkdir -p "$HOME/.claude/agents"
    cp -r agents/* "$HOME/.claude/agents/"
    echo "✓ Agents installed"
fi

if [ -d "commands" ]; then
    echo "Installing custom commands..."
    mkdir -p "$HOME/.claude/commands"
    cp -r commands/* "$HOME/.claude/commands/"
    echo "✓ Commands installed"
fi

if [ -f "settings/settings.json" ]; then
    echo "Installing configuration..."
    cp settings/settings.json "$HOME/.claude/settings.json"
    echo "✓ Configuration installed"
fi

echo ""
echo "✅ Installation complete!"
echo "Your Claude Code configuration has been installed successfully."