---
description: "Commit staged changes"
---

## Context

- Recent commits: !`git log --oneline -10`
- Current staged changes: !`git diff --staged`

## Your task

- Create a single git commit
- NEVER run `git add` without explicit authorization. If there are no changes in the staging area, ask the user to provide explicit confirmation.
- If the project has defined commit instructions, follow them
- The commit description should be concise and clear
- The commit must follow conventional commit format `<type>[scope]: <description>`
- After creating the commit, inform the user: `Commit created: [complete commit message]`

## Constraints

- Only commit staged changes
- Follow conventional commit format strictly
- Keep commit messages clear and descriptive
