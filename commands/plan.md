---
description: Create an implementation plan for a given request
---

## Context

- Request: $ARGUMENTS

## Your task

- Create a file in the `/plan` directory, the file name should include the day, month and a title of maximum 3 words, example: `plan/31-07_refactor-auth.md`
- Analyze the user's request and use the `planner` agent to create a detailed implementation plan
- If any task is complex, divide it into multiple sub-tasks
- At the end you should inform the user `plan created: [relative file path]`
- The plan should be in markdown format and include this structure:

```markdown
# [plan title]

## Objective

[objective description]

## Scope

[scope description]

## Tasks

- [] First task

  - First step
  - Second step

- [] Second task

  - First step
  - Second step
  - Third step

- [rest of tasks...]
```
