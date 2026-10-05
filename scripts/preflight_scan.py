#!/usr/bin/env python3
"""Repo preflight: checks INOS Cursor execution-surface invariants. Exit 1 on any FAIL."""
import hashlib, json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
results = []
def check(name, ok, detail=""):
    results.append((name, ok, detail))

# 1. rules present, with frontmatter
rules = sorted((root / ".cursor/rules").glob("*.mdc"))
check("9 rules 00-08 present", [r.name[:2] for r in rules] == [f"{i:02d}" for i in range(9)], str(len(rules)))
for r in rules:
    t = r.read_text()
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    check(f"{r.name} frontmatter", bool(m) and "description:" in m.group(1) and "alwaysApply:" in m.group(1))

# 2. required files
for f in ["AGENTS.md", "CURSOR_KICKOFF_PROMPT.md", "INOS_TASK_INTAKE.template.yaml",
          "INOS_TASK_RETURN.template.md", "docs/inos/INOS_EXECUTION_SURFACE_CONTRACT.md", ".gitignore", ".cursorignore"]:
    check(f"exists {f}", (root / f).is_file())

# 3. kit manifest hashes
mf = root / "docs/inos/cursor-kit/MANIFEST.json"
if mf.is_file():
    bad = []
    for e in json.loads(mf.read_text())["files"]:
        cands = [root / "docs/inos/cursor-kit" / e["path"], root / e["path"].removeprefix("repo-template/")]
        p = next((c for c in cands if c.is_file()), None)
        if p is None or hashlib.sha256(p.read_bytes()).hexdigest() != e["sha256"]:
            bad.append(e["path"])
    check("kit files match manifest (drift list = modified/missing)", not bad, ", ".join(bad))

# 4. no raw secrets / live mcp.json with literal token
pat = re.compile(r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|Bearer\s+[A-Za-z0-9._-]{20,})")
hits = []
for p in root.rglob("*"):
    if p.is_file() and ".git" not in p.parts and p.stat().st_size < 1_000_000:
        try:
            if pat.search(p.read_text()): hits.append(str(p.relative_to(root)))
        except UnicodeDecodeError: pass
check("no raw secrets", not hits, ", ".join(hits))
live = root / ".cursor/mcp.json"
if live.is_file():
    check("mcp.json uses env interpolation only", "${env:" in live.read_text() and not pat.search(live.read_text()))

# 5. gitignore protects secrets
gi = (root / ".gitignore").read_text() if (root / ".gitignore").is_file() else ""
check(".gitignore covers .env", ".env" in gi)

w = max(len(n) for n, _, _ in results)
for n, ok, d in results:
    print(f"{'PASS' if ok else 'FAIL'}  {n:<{w}}  {d if not ok else ''}")
fails = sum(not ok for _, ok, _ in results)
print(f"\n{len(results)-fails}/{len(results)} passed")
sys.exit(1 if fails else 0)
