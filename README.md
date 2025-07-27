# Claude Code - Personal Configuration

This repository contains my personal configuration for Claude Code.

## Installation

To copy this configuration to your system:

```bash
# Clone this repository
git clone https://github.com/OscSer/claude-code-config.git

# Navigate to the folder
cd claude-code-config

# Copy custom agents
cp -r agents/ ~/.claude/agents/

# Copy custom commands
cp -r commands/ ~/.claude/commands/

# Copy main configuration
cp settings/settings.json ~/.claude/settings.json
```

## Workflow

```mermaid
flowchart TD
    A[Usuario solicita funcionalidad] --> B{¿Es complejo?}
    
    B -->|Sí| C[/plan - Crear plan de implementación]
    B -->|No| G[Implementación directa]
    
    C --> D[planner agent]
    D --> E[plan/DD-MM_titulo.md]
    
    E --> F[/implement - Ejecutar plan]
    F --> H[implementer agent]
    
    H --> I[Implementación paso a paso]
    I --> J[reviewer agent]
    J --> K{¿Revisión OK?}
    
    K -->|No| L[Correcciones]
    L --> I
    
    K -->|Sí| M[/commit - Crear commit]
    G --> M
    
    M --> N[Commit estandarizado]
    
    O[/code-review] --> P[reviewer agent]
    P --> Q[Reporte de revisión]
    
    R[debugger agent] --> S[Análisis y solución de errores]
    
    style C fill:#e1f5fe
    style F fill:#e8f5e8
    style M fill:#fff3e0
    style O fill:#fce4ec
    style D fill:#f3e5f5
    style H fill:#f3e5f5
    style J fill:#f3e5f5
    style R fill:#f3e5f5
```

## Structure

- `agents/` - Custom specialized agents
- `commands/` - Custom slash commands
- `settings/` - Configuration files
  - `settings.json` - Main Claude Code configuration
