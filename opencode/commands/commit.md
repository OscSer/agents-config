---
description: "Commit staged changes"
---

## Context

- Recent commits: !`git log --oneline -10`
- Current staged changes: !`git diff --staged`

## Your task

- Create a single git commit with staged changes
- NEVER run `git add` without explicit authorization. If there are no changes in the staging area, ask the user to provide explicit confirmation
- If the project has defined commit instructions, follow them
- The commit must be in english
- The commit description should be concise and clear
- The commit must follow conventional commit format `<type>[scope]: <description>`
- After creating the commit, inform the user: `Commit created: [complete commit message]`
