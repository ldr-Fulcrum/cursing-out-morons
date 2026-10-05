# INOS Cursor Environment Build Kit

Purpose: stand up Cursor as a governed **execution surface** for Infinite Network / TEAM AI repositories.

This kit has two layers:

1. **Global operator layer** — copy-safe user rules for Cursor Settings.
2. **Repository layer** — version-controlled `.cursor/rules/`, `AGENTS.md`, MCP template, mission intake, return contract, and bootstrap helpers.

Cursor may inspect, implement, test, refactor, and propose. Cursor is never ARC, AIM, BUILD, ARK, WAR, TWIN, or an authority source merely because it has technical access.

## Quick start

1. Read `CURSOR_START_HERE.md`.
2. Copy `global/CURSOR_GLOBAL_USER_RULES.md` into Cursor User Rules.
3. Copy the contents of `repo-template/` into a target repository.
4. Review `.cursor/mcp.json.template`; create `.cursor/mcp.json` only with approved servers and environment-variable based credentials.
5. Fill `INOS_TASK_INTAKE.template.yaml` for consequential work.
6. Start Agent with `CURSOR_KICKOFF_PROMPT.md`.
7. Return evidence using `INOS_TASK_RETURN.template.md`.

## Status

Candidate build kit. It defines runtime discipline and configuration scaffolding. It does not grant authority, register a runtime, connect an MCP server, or prove BUILD acceptance.
