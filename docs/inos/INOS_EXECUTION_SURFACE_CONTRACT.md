# INOS Execution Surface Contract

## Object class

A coding environment is an **execution surface / runtime surface**. It is not an institution, operator identity, authority source, router, validator, custodian, or canon store.

The governing separation is:

```text
Institution
  -> Assignment
  -> System Operator / Technical Actor
  -> Runtime / Execution Surface
  -> Workload Identity
  -> Run
  -> Artifact + Evidence + Receipt
```

## Allowed posture

The surface may, when a mission packet permits it:

- inspect repository state;
- read source and contracts;
- plan implementation;
- edit bounded files;
- create candidate code and documentation;
- run tests, linters, typecheckers, builds, and static analysis;
- create diffs and evidence;
- propose follow-up work.

## Prohibited inference

Technical capability does not imply governance authority.

The surface must never infer any of the following merely because it can technically perform the action:

- institutional authority;
- operator assignment;
- AIM routing authority;
- exact-context authorization;
- canon status;
- BUILD PASS;
- ARK custody or seal;
- deployment approval;
- release approval;
- permission to alter credentials, protected branches, production data, or destructive state.

## Required mission context

Before consequential implementation, resolve or explicitly mark unresolved:

```yaml
mission_id:
session_id:
run_id:
institution_ref:
system_operator_ref:
runtime_ref:
workload_identity_ref:
route_ref:
authority_decision_ref:
source_refs: []
source_hashes: []
scope:
allowed_paths: []
allowed_tools: []
forbidden_actions: []
acceptance_tests: []
return_receipt_required: true
```

A missing route or authority decision must not be silently converted into permission.

## Evidence return

Every completed run should return:

- changed files;
- git diff summary;
- test/build commands actually run;
- exact command results and exit status;
- unresolved failures;
- artifact paths/hashes when applicable;
- network/MCP usage if material;
- deviations from mission scope;
- next gate required.

## LOCKED_v0.1 naming

`LOCKED_v0.1` is the package/release label used by the current build-kit family. The label itself does not prove a substantive LDR acceptance or authority decision.
