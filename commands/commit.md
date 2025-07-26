---
description: Create a commit message following project standards
---

## Context
- Recent commits: !`git log --oneline -10`
- Current staged changes: !`git diff --staged`

## Your task
- Based on the above changes, create a single git commit.
- If the project has defined commit instructions, follow them.
- The commit description should be concise and clear.
- The commit must follow this format:

```text
<type>[scope]: <description>

[body]
```
