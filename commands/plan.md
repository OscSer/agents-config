---
description: "Create an implementation plan for a given request"
---

## Context

- Request: $ARGUMENTS

## Your task

- Create a file in the `/plan` directory, the file name should include the day, month and a title of maximum 3 words, example: `plan/31-07-refactor-auth.md`
- Use the `software-architect` agent to get a detailed analysis
- At the end you should inform the user `plan created: [relative file path]`
- The file must have the following structure:

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
    - ...

  - [] Second task

    - First step
    - Second step
    - Third step
    - ...

  - [Rest of tasks...]
  ```

## Constraints

- Break down complex tasks into manageable sub-tasks
- Consider dependencies between tasks
