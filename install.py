#!/usr/bin/env python3

import sys
import json
import shutil
from pathlib import Path
from typing import Optional, TypedDict


class InstallError(Exception):
    """Base exception for installation errors"""

    pass


class SymlinkError(InstallError):
    """Exception raised when symlink operations fail"""

    pass


class ConfigError(InstallError):
    """Exception raised when configuration operations fail"""

    pass


class AgentConfig(TypedDict):
    label: str
    settings_source: str
    settings_target: str
    commands_target: str
    rules_source: str
    rules_target: str
    has_mcp: bool


class ConfigInstaller:
    """Handles installation of Claude Code, OpenCode, and Gemini CLI configurations"""

    AGENTS_CONFIG: dict[str, AgentConfig] = {
        "claude": {
            "label": "Claude Code",
            "settings_source": "settings.json",
            "settings_target": "settings.json",
            "commands_target": "commands",
            "rules_source": "common/AGENTS.md",
            "rules_target": "CLAUDE.md",
            "has_mcp": True,
        },
        "gemini": {
            "label": "Gemini CLI",
            "settings_source": "settings.json",
            "settings_target": "settings.json",
            "commands_target": "commands",
            "rules_source": "common/AGENTS.md",
            "rules_target": "GEMINI.md",
            "has_mcp": False,
        },
        "opencode": {
            "label": "OpenCode",
            "settings_source": "settings/opencode.json",
            "settings_target": "opencode.json",
            "commands_target": "command",
            "rules_source": "common/AGENTS.md",
            "rules_target": "AGENTS.md",
            "has_mcp": False,
        },
    }

    def __init__(self, repo_dir: Optional[Path] = None):
        self.repo_dir = repo_dir or Path(__file__).parent.absolute()
        self.claude_dir = Path.home() / ".claude"
        self.opencode_dir = Path.home() / ".config" / "opencode"
        self.gemini_dir = Path.home() / ".gemini"

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

    def install_agent(self, agent_name: str) -> bool:
        config = self.AGENTS_CONFIG[agent_name]
        agent_label = config["label"]

        if agent_name == "claude":
            target_dir = self.claude_dir
        elif agent_name == "gemini":
            target_dir = self.gemini_dir
        elif agent_name == "opencode":
            target_dir = self.opencode_dir
        else:
            raise InstallError(f"Unknown agent: {agent_name}")

        print(f"Installing {agent_label} configuration...")

        try:
            target_dir.mkdir(parents=True, exist_ok=True)

            # Install commands
            commands_source = self.repo_dir / agent_name / "commands"
            if self.validate_source(f"{agent_name}/commands") and commands_source.is_dir():
                print(f"Installing custom commands for {agent_label}...")
                if self.create_symlink(commands_source, target_dir / config["commands_target"]):
                    print(f"✓ {agent_label} commands installed")

            # Install settings
            settings_source_path = self.repo_dir / agent_name / config["settings_source"]
            if self.validate_source(f"{agent_name}/{config['settings_source']}") and settings_source_path.is_file():
                print(f"Installing {agent_label} configuration...")
                shutil.copy2(
                    settings_source_path,
                    target_dir / config["settings_target"],
                )
                print(f"✓ {agent_label} configuration installed")

            # Install rules
            rules_source_path = self.repo_dir / config["rules_source"]
            if self.validate_source(config["rules_source"]) and rules_source_path.is_file():
                doc_name = config["rules_target"]
                print(f"Installing shared {doc_name} for {agent_label}...")
                if self.create_symlink(
                    rules_source_path,
                    target_dir / doc_name,
                ):
                    print(f"✓ {agent_label} shared {doc_name} installed")

            # Update MCP configuration if needed
            if agent_name == "claude" and config["has_mcp"]:
                if (
                    self.validate_source("claude/.mcp.json")
                    and (self.repo_dir / "claude" / ".mcp.json").is_file()
                ):
                    self.update_claude_mcp_config()

            return True

        except (SymlinkError, ConfigError, OSError) as e:
            print(f"Error installing {agent_label}: {e}")
            return False

    def install_all(self) -> bool:
        """Install all agent configurations"""
        print("Claude Code, OpenCode & Gemini CLI Configuration Installation")
        print("===============================================================")

        success_flags: list[bool] = []
        for agent_name in self.AGENTS_CONFIG:
            success = self.install_agent(agent_name)
            success_flags.append(success)

        if all(success_flags):
            print("")
            print("✅ Installation complete!")
            print("Claude Code configuration is available in ~/.claude/")
            print("OpenCode configuration is available in ~/.config/opencode/")
            print("Gemini CLI configuration is available in ~/.gemini/")
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
