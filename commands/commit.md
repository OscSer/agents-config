---
description: Commit staged changes
---

## Context

- Recent commits: !`git log --oneline -10`
- Current staged changes: !`git diff --staged`

## Your task

- Based on the above changes, create a single git commit.
- NEVER run `git add` without explicit user authorization. Only work with files that are already staged.
- If the project has defined commit instructions, follow them.
- The commit description should be concise and clear.
- The commit must follow conventional commit format:

```text
<type>[scope]: <description>

[body]
```
