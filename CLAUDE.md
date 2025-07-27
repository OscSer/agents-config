# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains personal configuration for Claude Code, including custom agents, slash commands, and settings that enhance development workflows.

## Templates

Development templates are available in the `/templates` directory:

- **Agent Template**: `templates/agent-template.md` - Template for creating new agents
- **Command Template**: `templates/command-template.md` - Template for creating new commands

Use these templates as starting points when creating new agents or commands to ensure consistency with project standards.

## Extension Processes

### Adding New Agents

1. **Design Phase**

   - Define clear, focused role
   - Identify unique value proposition
   - Map integration with existing agents
   - Define quality standards

2. **Implementation**

   - Create agent file in `agents/` directory
   - Use `templates/agent-template.md` as starting point
   - Use consistent naming conventions
   - Include comprehensive process definition

3. **Validation**
   - Verify no role overlap with existing agents
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
   - Use `templates/command-template.md` as starting point
   - Use descriptive naming
   - Include proper agent delegation

3. **Validation**

   - Validate agent delegation
   - Document usage patterns
   - Update workflow documentation

## Documentation

- Update CLAUDE.md and README.md if needed
