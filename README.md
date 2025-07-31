# AI Agents Configuration

This repository contains my personal configuration for AI agents.

## Installation

### Clone Repository

```bash
# Clone this repository
git clone https://github.com/OscSer/agents-config.git

# Navigate to the folder
cd agents-config
```

### Quick Installation

```bash
# Run the installation script
./install.sh
```

> ⚠️ **Important**: The installation script creates symbolic links to this repository. This means:
>
> - Any existing `~/.claude/agents/`, `~/.claude/commands/`, `~/.claude/settings.json` and `~/.config/opencode/agents/` will be **replaced**
> - If you want to preserve your existing configuration, you can copy the files manually instead of running the script

### Manual Installation

```bash
# Copy Claude Code agents
cp -r claude/agents/* ~/.claude/agents/

# Copy Claude Code commands
cp -r claude/commands/* ~/.claude/commands/

# Copy Claude Code configuration
cp claude/settings/settings.json ~/.claude/settings.json

# Copy OpenCode agents
cp -r opencode/agents/* ~/.config/opencode/agents/
```

## Structure

```
├── claude/
│   ├── agents/               # Claude Code specialized agents
│   ├── commands/             # Claude Code slash commands
│   ├── settings/             # Claude Code configuration files
│   └── templates/            # Claude Code templates
└── opencode/
    ├── agents/               # OpenCode specialized agents
    └── templates/            # OpenCode templates
```

## Available Agents

- **software-architect** - Designs software architecture and creates comprehensive system blueprints
- **senior-developer** - Implements complex features and diagnoses technical issues with comprehensive expertise

## Available Commands

- **/plan** - Creates implementation plans using the software-architect agent
- **/implement** - Executes implementation using the senior-developer agent
- **/commit** - Creates conventional commits with proper formatting

## Workflow

```mermaid
flowchart TD
    %% Top level command
    Plan["/plan<br/>🤖 software-architect"]

    %% Development workflow
    Plan --> PlanFile["📄 plan/DD-MM_title.md"]
    PlanFile --> Review["👤 User reviews plan"]
    Review --> Implement["/implement<br/>🤖 senior-developer"]
    Implement --> CodeReview["👤 User reviews code"]
    CodeReview --> Commit["/commit<br/>📝 conventional commits"]

    %% Command styles with rounded corners and shadows
    style Plan fill:#e3f2fd,stroke:#1976d2,stroke-width:3px,color:#1976d2,font-weight:bold
    style Implement fill:#e8f5e8,stroke:#388e3c,stroke-width:3px,color:#2e7d32,font-weight:bold
    style Commit fill:#f3e5f5,stroke:#7b1fa2,stroke-width:3px,color:#6a1b9a,font-weight:bold

    %% File style
    style PlanFile fill:#f5f5f5,stroke:#757575,stroke-width:2px,color:#424242,font-style:italic

    %% User action style
    style Review fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#e65100,font-style:italic
    style CodeReview fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#e65100,font-style:italic

    %% Link styles
    linkStyle 0 stroke:#1976d2,stroke-width:3px
    linkStyle 1 stroke:#757575,stroke-width:2px
    linkStyle 2 stroke:#388e3c,stroke-width:3px
    linkStyle 3 stroke:#f57f17,stroke-width:2px
    linkStyle 4 stroke:#7b1fa2,stroke-width:3px
```
