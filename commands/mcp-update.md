---
description: Update MCP permissions
---

## Your task
- Analyze the `mcpServers` property in `/home/oscar/.claude.json`, don't read the entire file because it's very long
- Update the `permissions.allow` in `/home/oscar/.claude/settings.json`
- You must add all available resources from the `mcpServers`
- You must remove resources that are no longer available (never remove `mcp__ide__getDiagnostics`)
