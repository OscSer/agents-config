#!/usr/bin/env python3

import sys
import json
import shutil
from pathlib import Path
from typing import Optional


class InstallError(Exception):
    """Base exception for installation errors"""

    pass


class SymlinkError(InstallError):
    """Exception raised when symlink operations fail"""

    pass


class ConfigError(InstallError):
    """Exception raised when configuration operations fail"""

    pass


class ConfigInstaller:
    """Handles installation of Claude Code and OpenCode configurations"""

    def __init__(self, repo_dir: Optional[Path] = None):
        self.repo_dir = repo_dir or Path(__file__).parent.absolute()
        self.claude_dir = Path.home() / ".claude"
        self.opencode_dir = Path.home() / ".config" / "opencode"

    def validate_source(self, path: str) -> bool:
        """Validate that source path exists in repository"""
        full_path = self.repo_dir / path
        if not full_path.exists():
            print(f"Warning: {path} not found in repository, skipping...")
            return False
        return True

    def create_symlink(self, source: Path, target: Path) -> bool:
        """Create symlink with fallback to copy"""
        if not source.exists():
            raise SymlinkError(f"Source {source} does not exist")

        try:
            if target.exists() or target.is_symlink():
                if target.is_dir() and not target.is_symlink():
                    shutil.rmtree(target)
                else:
                    target.unlink()

            target.symlink_to(source)
            return True

        except OSError as e:
            print(f"Warning: Symbolic link failed ({e}), falling back to copy...")
            try:
                if source.is_dir():
                    shutil.copytree(source, target)
                else:
                    shutil.copy2(source, target)
                return True
            except Exception as copy_error:
                raise SymlinkError(
                    f"Failed to create symlink or copy {source} to {target}: {copy_error}"
                )

    def update_claude_mcp_config(self) -> bool:
        """Update Claude MCP configuration"""
        mcp_source = self.repo_dir / "claude" / ".mcp.json"
        claude_config = Path.home() / ".claude.json"

        if not mcp_source.exists():
            print("Warning: claude/.mcp.json not found, skipping MCP configuration...")
            return False

        print("Updating Claude MCP configuration...")

        try:
            with open(mcp_source, "r") as f:
                mcp_data = json.load(f)

            if "mcpServers" not in mcp_data:
                raise ConfigError("mcpServers not found in claude/.mcp.json")

            claude_data = {}
            if claude_config.exists():
                with open(claude_config, "r") as f:
                    claude_data = json.load(f)

            claude_data["mcpServers"] = mcp_data["mcpServers"]

            with open(claude_config, "w") as f:
                json.dump(claude_data, f, indent=2)

            print("✓ MCP configuration updated successfully")
            return True

        except (json.JSONDecodeError, OSError) as e:
            raise ConfigError(f"Failed to update MCP configuration: {e}")

    def install_claude_code(self) -> bool:
        """Install Claude Code configuration"""
        print("Installing Claude Code configuration...")

        try:
            self.claude_dir.mkdir(parents=True, exist_ok=True)
            success = True

            # Install commands
            if (
                self.validate_source("claude/commands")
                and (self.repo_dir / "claude" / "commands").is_dir()
            ):
                print("Installing Claude Code custom commands...")
                if self.create_symlink(
                    self.repo_dir / "claude" / "commands", self.claude_dir / "commands"
                ):
                    print("✓ Claude Code commands installed")

            # Install settings
            if (
                self.validate_source("claude/settings.json")
                and (self.repo_dir / "claude" / "settings.json").is_file()
            ):
                print("Installing Claude Code configuration...")
                shutil.copy2(
                    self.repo_dir / "claude" / "settings.json",
                    self.claude_dir / "settings.json",
                )
                print("✓ Claude Code configuration installed")

            # Install shared AGENTS.md
            if (
                self.validate_source("common/AGENTS.md")
                and (self.repo_dir / "common" / "AGENTS.md").is_file()
            ):
                print("Installing shared AGENTS.md for Claude Code...")
                if self.create_symlink(
                    self.repo_dir / "common" / "AGENTS.md",
                    self.claude_dir / "AGENTS.md",
                ):
                    print("✓ Claude Code shared AGENTS.md installed")

            # Update MCP configuration
            if (
                self.validate_source("claude/.mcp.json")
                and (self.repo_dir / "claude" / ".mcp.json").is_file()
            ):
                self.update_claude_mcp_config()

            return success

        except (SymlinkError, ConfigError, OSError) as e:
            print(f"Error installing Claude Code: {e}")
            return False

    def install_opencode(self) -> bool:
        """Install OpenCode configuration"""
        print("Installing OpenCode configuration...")

        try:
            self.opencode_dir.mkdir(parents=True, exist_ok=True)
            success = True

            # Install commands
            if (
                self.validate_source("opencode/commands")
                and (self.repo_dir / "opencode" / "commands").is_dir()
            ):
                print("Installing OpenCode custom commands...")
                if self.create_symlink(
                    self.repo_dir / "opencode" / "commands",
                    self.opencode_dir / "command",
                ):
                    print("✓ OpenCode commands installed")

            # Install configuration
            if (
                self.validate_source("opencode/settings/config.json")
                and (self.repo_dir / "opencode" / "settings" / "config.json").is_file()
            ):
                print("Installing OpenCode configuration...")
                shutil.copy2(
                    self.repo_dir / "opencode" / "settings" / "config.json",
                    self.opencode_dir / "config.json",
                )
                print("✓ OpenCode configuration installed")

            # Install shared AGENTS.md
            if (
                self.validate_source("common/AGENTS.md")
                and (self.repo_dir / "common" / "AGENTS.md").is_file()
            ):
                print("Installing shared AGENTS.md for OpenCode...")
                if self.create_symlink(
                    self.repo_dir / "common" / "AGENTS.md",
                    self.opencode_dir / "AGENTS.md",
                ):
                    print("✓ OpenCode shared AGENTS.md installed")

            return success

        except (SymlinkError, OSError) as e:
            print(f"Error installing OpenCode: {e}")
            return False

    def install_all(self) -> bool:
        """Install both Claude Code and OpenCode configurations"""
        print("Claude Code & OpenCode Configuration Installation")
        print("=================================================")

        claude_success = self.install_claude_code()
        opencode_success = self.install_opencode()

        if claude_success and opencode_success:
            print("")
            print("✅ Installation complete!")
            print("Claude Code configuration is available in ~/.claude/")
            print("OpenCode configuration is available in ~/.config/opencode/")
            return True
        else:
            print("")
            print(
                "⚠️ Installation completed with some errors. Check the output above for details."
            )
            return False


def main():
    """Main installation function"""
    try:
        installer = ConfigInstaller()
        success = installer.install_all()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\nInstallation interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error during installation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
