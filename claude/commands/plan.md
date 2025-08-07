---
description: "Create an implementation plan for a given request"
---

## Context

- Request: $ARGUMENTS

## Your task

- Create a file in the `/plan` directory
- The file name should include the day, month and a title of maximum 3 words `plan/31-07-refactor-auth.md`
- Reference specific files, functions, and variables (but not lines) in tasks when necessary `relative_file_path:function|variable`
- At the end you should inform the user `plan created: [relative file path]`
- Expected file structure:

```markdown
# [plan title]

## Objective

[objective description]

## Phases

- [] First phase

  - First task
  - Second task
  - ...

- [] Second phase

  - First task
  - Second task
  - ...

- [] ...

- [] Validation tasks

  - Check typecheck
  - Check linter
  - Check tests
  - ...
```
