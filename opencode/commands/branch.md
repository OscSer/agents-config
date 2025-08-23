---
description: "Move current changes to a new branch"
---

## Context

- Current branch: !`git branch --show-current`
- Current changes: !`git status --porcelain`
- (optional) Description: $ARGUMENTS

## Your task

- Move all current changes to a new branch with intelligent naming
- Analyze modified files from git status and description provided to generate descriptive branch name
- Follow this exact sequence:
  1. Verify there are changes to move (exit if none)
  2. Execute: `git stash push -u -m "Moving to branch: [generated-name]"`
  3. Execute: `git checkout main`
  4. Execute: `git pull` to update main with latest changes
  5. Execute: `git checkout -b [generated-branch-name]`
  6. Execute: `git stash pop`
  7. Confirm success and inform user of new branch name
- Branch names must be valid: lowercase, hyphens instead of spaces, no special characters
