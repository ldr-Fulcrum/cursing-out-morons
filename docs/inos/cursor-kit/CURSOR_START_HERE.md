# Cursor Start Here

## Placement in INOS

```text
LDR / governed source / build kits
        ↓
Institution + mission assignment
        ↓
AIM route + exact-context authority
        ↓
System operator
        ↓
Cursor workspace / Agent
        ↓
implementation + tests + diffs
        ↓
receipt/evidence
        ↓
BUILD / ARK / other gates as applicable
```

Cursor is a runtime/execution surface, not a lane.

## Current Cursor mechanics used by this kit

- Repository rules live in `.cursor/rules/*.mdc`.
- `.mdc` project rules use frontmatter such as `description`, `globs`, and `alwaysApply`.
- `AGENTS.md` is supported as repository guidance.
- Project MCP configuration lives in `.cursor/mcp.json`; global MCP configuration can live in `~/.cursor/mcp.json`.
- Do not commit raw credentials into MCP configuration. Use environment interpolation or approved OAuth/credential mechanisms.

## Global vs repository layer

**Global rules** should contain only durable INOS execution boundaries.

**Repository rules** should contain architecture, commands, code style, source-of-truth, test expectations, and write boundaries for that repository.

Repository assumptions must not silently bleed into another repository.

## Consequential actions

For protected-branch writes, deployment, production data changes, credential changes, destructive operations, canon/registry updates, or external publication, require an explicit mission packet and applicable approval/authority evidence.
