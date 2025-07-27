---
description: Perform comprehensive code review
---

## Context

- Target: $ARGUMENTS
- Status: !`git status`
- Diff: !`git diff`

## Your task

- If specific target is provided, review those files/changes
- If no target specified, focus on uncommitted changes (staged and unstaged modifications)
- Use the `reviewer` agent to perform the comprehensive review
