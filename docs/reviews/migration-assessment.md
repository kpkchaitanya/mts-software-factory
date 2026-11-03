---
document_id: REV-MIG-001
status: draft-for-human-review
version: 0.1
date: 2026-11-01
source_repository: kpkchaitanya/mts-crossmodel
source_ref: master
verification_scope: repository-inspection-only
---

# Legacy Asset Migration Assessment — Draft

[One-page review](initial-architecture-review.md) · [Architecture reasoning](architecture-rationalization.md)

**Classification is proposed, not authorized.** No runnable code or configurations have been moved. Current repository tree inspected, but no fresh tests or production credentials used. Earlier migration reports are historical assertions, not current pass evidence.

| Legacy asset / representative path | Proposed disposition | Rationale / preservation rule | Preconditions / regression gate |
|---|---|---|---|
| `constitution.md`, `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md` | **Refactor** | Extract unique governance into one canonical authority; keep thin provider adapters | Diff rules and test instruction precedence, no dropped human gates |
| `ontology.md`, `program.md` | **Refactor** | Worksheet ontology and program direction are narrower than factory/domain split | M1 vocabulary, owners and cross-links approved |
| `docs/subjects/math/requirements.md`; `specs/generate_math_worksheets/` | **Refactor** | Valuable Math semantics, detailed older feature plans and existing ADRs | Map every retained rule to REQ/AC; resolve legacy M3/M4 numbering |
| `docs/subjects/ela/requirements.md`, `data/config/subjects/ela.yaml` | **Refactor** | ELA configuration and starter rules exist; implementation depth is unequal | Formalize RC, poetry, typography, question/evidence requirements and negative fixtures |
| `src/mts/subjects/math/{p0_runtime,question_plan,validation,verification,weekly_workflow}.py` | **Adopt selectively / Refactor** | Candidate tested Math logic, not a proven domain-neutral factory kernel | Re-run current baseline + boundary and mutation tests; preserve behavior before refactor |
| `src/mts/infrastructure/{configuration,file_system,google_docs,printing}/` | **Refactor** | Likely reusable adapters; Google-specific dependencies must not define core | Contract tests, idempotence, mocks and environment-independent tests |
| `src/mts/workflow_management/`, `src/mts/worksheets/` | **Refactor** | Gate, manifest and spec repository patterns can underpin traceability | Reproduce existing gates; extend to requirement IDs and evidence |
| `src/mts/publishing/`, `scripts/{publish_weekly_artifacts,render_weekly_specs_to_drive,deliver_weekly_worksheets}.py` | **Adopt selectively / Refactor** | Practical publishing path with real-world value and failure modes | Dry-run, provenance, no duplicate publish, correct destinations, human gate |
| `schemas/{worksheet-spec,run-manifest,definitions/*}.json` | **Adopt / Extend** | Strong starting contracts for canonical spec, run, approval and verification | Schema validation, backward compatibility, new trace fields |
| `data/master/subjects/math/` | **Adopt with provenance review** | Curriculum, course catalog, progressive backbone and compatibility data | Freshness, licensing, consistency and sample question tests |
| `data/config/project/base.yaml`; `data/config/worksheet_types/` | **Refactor** | Clear policy separation but hard-coded education context and folder identifiers | Configuration hierarchy ADR, schema checks, stage/production separation |
| `tests/shared/`, `tests/subjects/math/`, `tests/integration/` | **Adopt and expand** | Existing executable regression seeds; no current pass result from this review | Run baseline pinned environment, retain fixtures, add defect regressions |
| `commands/`, `.agents/skills/`, `.claude/commands/`, `.github/prompts/` | **Replace duplicated wrappers with thin generated adapters** | Risk of multiple divergent copies of same workflow policy | Semantic parity and smoke tests across harnesses |
| `data/transactions/legacy_runs/`, `archive/` | **Archive / preserve read-only** | Historical release evidence and provenance, potentially oversized and sensitive | Inventory retention, privacy, checksums and legal/license requirements; no destructive deletion |
| `outputs/`, `outputs-copilot/` placeholders and old migration plans | **Archive or supersede** | Output location concepts and dated plans are not permanent architecture | Reconcile with current external Drive release evidence and approved destination contract |
| `docs/knowledge/ai-native-sdlc-personal.md` | **Archive/reference** | Older lifecycle terminology may contradict current M0–M8 governing strategy | Preserve provenance; authoritative method stays in strategy |

## Verification and migration invariants

1. Freeze source commit, dependency/tool versions and reproducible test command before any asset migration.
2. Capture baseline results (pass, fail, skipped) and separate them from old reported PASS counts.
3. Preserve independently verified behavior with parity fixtures before changing boundaries.
4. For every migrated path record source SHA, target, requirement IDs, owner, disposition, tests, verification result and rollback.
5. No deletion or legacy cutover until new output proves equivalence or intentionally approved delta.
6. No claim that ELA is automated until subject-specific implementation, visual QA, provenance and release tests pass end to end.
7. An observed failure requires OBS → LRN/DELTA → approved requirement change → TEST regression.

## Priority gaps for first slice

- Requirement coverage ledger is not demonstrated as a generated authoritative view.
- Trace IDs are partial across Math specs/manifests and not end-to-end through runtime outcome.
- Release state and observed/accepted outcome are not represented as distinct verified stages everywhere.
- ELA needs durable subject evaluator and proof beyond dated PDF exemplars.
- Documentation and adapter rules risk drift.
- Runtime security, privacy and retention conditions need explicit owner and gate.

## Proposed migration sequence (requires later approval)

1. Baseline one existing Math fixture and test suite read-only.
2. Normalize a narrow Worksheet Spec/verification/evidence contract without replacing generation or publishing.
3. Prove a first end-to-end traceable verification slice with negative fixtures.
4. Add an ELA counterpart to test whether the generalized contract really holds.
5. Only then consolidate shared components, workflow adapters and release infrastructure.

The current decision is **review**, not migration authorization.
