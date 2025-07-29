---
description: "Create an implementation plan for a given request"
---

## Context

- Request: $ARGUMENTS

## Your task

- Create a file in the `/plan` directory
- The file name should include the day, month and a title of maximum 3 words, example: `plan/31-07-refactor-auth.md`
- Use the `software-architect` agent to get a detailed analysis
- At the end you should inform the user `plan created: [relative file path]`
- Expected file structure:

```markdown
# [plan title]

## Objective

[objective description]

## Phases

- [] 1. First phase

- First task
- Second task
- ...

- [] 2. Second phase

- First task
- Second task
- ...
```
