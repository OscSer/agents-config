# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains personal configuration for Claude Code, including custom agents, slash commands, and settings that enhance development workflows.

## Architecture

### Configuration Structure

- `agents/` - Custom specialized agents for different development tasks
- `commands/` - Custom slash commands for automated workflows
- `settings/` - Configuration files including main Claude Code settings

### Custom Agents

- `implementer` - Implements complex features following SOLID principles and clean code practices
- `reviewer` - Performs comprehensive code reviews focusing on quality, security, and maintainability
- `debugger` - Diagnoses and fixes errors using systematic root cause analysis
- `planner` - Creates detailed implementation plans and system architecture

### Custom Commands

- `/implement` - Executes implementation plans using the implementer and reviewer agents
- `/commit` - Creates standardized commit messages following conventional commit format
- `/plan` - Generates detailed implementation plans in markdown format

### Workflow Commands

- Use `/plan [request]` to create implementation plans
- Use `/implement [plan]` to execute plans with automatic code review
- Use `/commit` to create standardized commit messages

## Development Guidelines

### Agent Development Patterns

#### Agent Structure
All agents follow a consistent structure:

1. **YAML Frontmatter** - Contains metadata
2. **Role Definition** - Clear description of the agent's purpose
3. **Process Section** - Step-by-step execution flow
4. **Principles/Guidelines** - Core development principles
5. **Quality Standards** - Specific quality criteria

#### Agent Naming Conventions
- Use descriptive English names
- Single word when possible (implementer, reviewer, debugger)
- Focus on action/role rather than technology
- Avoid abbreviations or acronyms

#### Agent Quality Checklist
- [ ] Clear, focused role definition
- [ ] Step-by-step process outlined
- [ ] Quality standards defined
- [ ] Consistent formatting and structure
- [ ] No overlapping responsibilities with existing agents

### Command Development Patterns

#### Command Structure
All commands follow this structure:

1. **YAML Frontmatter** - Contains description
2. **Context Section** - Input variables and environment
3. **Task Section** - Clear instructions for execution
4. **Format Specifications** - Output format requirements

#### Command Naming Conventions
- Use action verbs (implement, commit, plan)
- Keep names concise and memorable
- Avoid redundant prefixes or suffixes
- Ensure uniqueness across all commands

#### Command Integration Patterns
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

[Process section]:
- [Process step 1]
- [Process step 2]
- [Process step 3]

Quality standards:
- [Standard 1]
- [Standard 2]
- [Standard 3]

[Final guidance or motto]
```

### Command Template

```markdown
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

[Additional format specifications if needed]:

```text
[Expected output format]
```

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
   - Update CLAUDE.md agent list
   - Create corresponding commands if needed
   - Test with real scenarios
   - Document usage examples

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

3. **Configuration**
   - Test command execution
   - Verify agent delegation works correctly
   - Document usage patterns
   - Update workflow documentation

4. **Validation**
   - Test with various input scenarios
   - Verify output format consistency
   - Ensure proper error handling
   - Update CLAUDE.md command list

