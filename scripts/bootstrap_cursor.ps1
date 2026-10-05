param(
  [string]$Target = "."
)

$ErrorActionPreference = "Stop"

Write-Host "INOS Cursor bootstrap preflight"
if (-not (Test-Path $Target)) { throw "Target does not exist: $Target" }

$gitDir = Join-Path $Target ".git"
if (-not (Test-Path $gitDir)) {
  Write-Warning "Target is not a Git repository root. Review placement before continuing."
}

$rulesDir = Join-Path $Target ".cursor\rules"
New-Item -ItemType Directory -Force -Path $rulesDir | Out-Null

Write-Host "Created/verified: $rulesDir"
Write-Host "This script intentionally does not copy or overwrite governance files automatically."
Write-Host "Copy the repo-template contents after reviewing existing AGENTS.md, .cursor/rules, and MCP configuration."
