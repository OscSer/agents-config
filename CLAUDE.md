# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains personal configuration for Claude Code, including custom agents, slash commands, and settings that enhance development workflows.

## Available Resources

### Custom Agents

- `implementer` - Implements complex features following SOLID principles and clean code practices
- `reviewer` - Performs comprehensive code reviews focusing on quality, security, and maintainability
- `debugger` - Diagnoses and fixes errors using systematic root cause analysis
- `planner` - Creates detailed implementation plans and system architecture

### Custom Commands

- `/implement` - Executes implementation plans using the implementer and reviewer agents
- `/commit` - Creates standardized commit messages following conventional commit format
- `/plan` - Generates detailed implementation plans in markdown format

### Quick Workflows

- Use `/plan [request]` to create implementation plans
- Use `/implement [plan]` to execute plans with automatic code review
- Use `/commit` to create standardized commit messages

---

# Agent Development Guidelines

## Structure Requirements

All agents must follow this structure:

1. **YAML Frontmatter** - Contains metadata
2. **Role Definition** - Clear description of the agent's purpose
3. **Principles/Guidelines** - Core development principles
4. **Quality Standards** - Specific quality criteria

## Naming Conventions

- Use descriptive English names
- Single word when possible (implementer, reviewer, debugger)
- Focus on action/role rather than technology
- Avoid abbreviations or acronyms

---

# Command Development Guidelines

## Structure Requirements

All commands must follow this structure:

1. **YAML Frontmatter** - Contains description
2. **Context Section** - Input variables and environment
3. **Task Section** - Clear instructions for execution
4. **Format Specifications** - Output format requirements

## Naming Conventions

- Use action verbs (implement, commit, plan)
- Keep names concise and memorable
- Avoid redundant prefixes or suffixes
- Ensure uniqueness across all commands

## Integration Patterns

- Use `$ARGUMENTS` for user input
- Delegate complex logic to specialized agents
- Include commands with `!` prefix for context
- Specify output formats and file structures

## Templates

### Agent Template

```markdown
---
name: agent_name
description: Brief description of what this agent does and when to use it.
---

You are a [role description] specializing in [specific expertise area].

When invoked:

1. [First step]
2. [Second step]
3. [Third step]
4. [Additional steps as needed]

[Role-specific section]:

- [Principle 1]
- [Principle 2]
- [Principle 3]

Quality standards:

- [Standard 1]
- [Standard 2]
- [Standard 3]

[Final guidance or motto]
```

### Command Template

````markdown
---
description: Brief description of command functionality
---

## Context

- Input: $ARGUMENTS
- [Additional context variables]
- [Commands if needed]: !`command`

## Your task

- [Main task description]
- [Important constraints or requirements]
- [Agent delegation if applicable]
- [Output format specifications]

```
[Expected output format]
```
````

## Extension Processes

### Adding New Agents

1. **Design Phase**

   - Define clear, focused role
   - Identify unique value proposition
   - Map integration with existing agents
   - Define quality standards

2. **Implementation**

   - Create agent file in `agents/` directory
   - Follow agent template structure
   - Use consistent naming conventions
   - Include comprehensive process definition

3. **Integration**

   - Update CLAUDE.md and README.md if needed
   - Create corresponding commands if needed

4. **Validation**
   - Verify no role overlap with existing agents
   - Test agent delegation from commands
   - Ensure quality standards are met
   - Review and refine based on usage

### Adding New Commands

1. **Design Phase**

   - Define command purpose and scope
   - Map to existing agents for delegation
   - Specify input/output formats
   - Plan integration workflows

2. **Implementation**

   - Create command file in `commands/` directory
   - Follow command template structure
   - Use descriptive naming
   - Include proper agent delegation
