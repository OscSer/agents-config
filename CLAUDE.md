# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains personal configuration for Claude Code, including custom agents, slash commands, and settings that enhance development workflows.

## Architecture

### Configuration Structure

- `agents/` - Custom specialized agents for different development tasks
- `commands/` - Custom slash commands for automated workflows
- `settings.json` - Main Claude Code configuration with permissions

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
