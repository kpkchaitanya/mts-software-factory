---
document_id: REV-ARCH-002
status: draft-for-human-review
version: 0.1
date: 2026-11-01
---

# Architecture & Source Rationalization — Detailed Draft

Primary sources: [governing strategy](../../strategy/ai-sdlc-software-factory-strategy.md), [legacy codebase](https://github.com/kpkchaitanya/mts-crossmodel), [historical handoff](../../strategy/source-history/mts-educational-factory-conversation.md). [One-page review](initial-architecture-review.md). Assertions about runtime behavior are **not** independently re-executed here.

## 1. Three-source overlap, gaps and contradictions

| Theme | Agreement | Gap / tension | Proposed reconciliation |
|---|---|---|---|
| Model-neutral | Strategy and legacy both favor thin adapters | Legacy has separate `.agents/`, `.claude/`, `.github/prompts/`, `commands/` | Single governed workflow; adapters are entry points only, inspect parity rather than copy wholesale |
| Lifecycle | Intent, approvals, tests, learning shared | Older Math architecture calls C1/C2 an **M3** architecture; governing strategy assigns architecture to **M4** | Strategy M0–M8 governs new lifecycle; preserve old document's historic terminology with provenance |
| Scope | Shared services plus subject expertise | Legacy `src/mts` intertwines worksheet product and platform concepts | Separate domain-independent factory kernel from educational application plugin |
| Rules | Both require canonical specs and independent verification | Config precedence in legacy and strategy's authority hierarchy may conflict; paths/Drive IDs baked into configuration | Explicit precedence/ownership ADR; keep deployment destinations as product configuration |
| Output | Worksheet and key derive from one spec | History adds ELA-specific PQYA/poetry and print-density constraints not formalized in code | Subject-specific evaluator, validated layout profiles and joint consistency regression |
| Evidence | Old run manifests, gates and tests exist | No demonstrated complete requirement coverage ledger or semantic trace graph | Extend artifact ID graph incrementally with source and evidence links |
| Release | Human publish gate is emphasized | Repo scripts and run snapshots do not prove latest end-to-end authorization, provenance or rollback | Release contract: approvals, verified build, recipient/location, post-publish verification |
| Educational history | Rich observations with real defect categories | Handoff is curated fallback, not complete source or approved specs | Promote through reviewed REQ/AC/TEST/DELTA, preserving link to observation |

## 2. Product/factory boundary and requirements hierarchy

**Factory (domain-neutral):** intent intake, artifact registry and versioning, M-station orchestration, human review, quality gates, trace graph and coverage ledger, audit/evidence, run telemetry, feedback and delta management, model/IDE adapters, reusable CI.

**Product domain (MTS education):** curriculum and standards, grade/course, subject knowledge, lesson/practice/diagnostic semantics, assessment questions and keys, YPQA/PQYA-style analysis (naming requires decision), difficulty/spiral policy, layout, delivery audience and source licensing.

**Reusable production adapter vs product policy:** a Google Docs renderer or Drive publisher can be a replaceable adapter; fonts, two-column print targets, passage length and week/grade naming are product-controlled config/specs. The factory should not know Grade 6 or a Google folder ID.

Proposed hierarchy:

```text
Factory Charter / Product PRODUCT.md
  └─ INT-* intent → OUT-* measurable outcome
       └─ FA-* capability → REQ-* requirement (versioned)
            ├─ AC-* acceptance criterion
            ├─ QAS-* quality scenario / CST-* constraint
            └─ PHASE-* process + ADR-* architecture + SLICE-* design
                 └─ IMP-* / BUILD-* → TEST-* / EVD-* → release → OBS-* → LRN-* → DELTA-*
```

Requirements are independently addressable and testable. `PRODUCT.md` establishes enduring product why/who/boundary; `requirements.md` and atomic REQ files specify objectively verifiable behavior. A requirement's `accepted` state is not equivalent to `implemented`, `verified` or `released`.

## 3. Ontology proposal, deliberately not flattened

- **Subject:** Math, ELA; Physics/Science as candidate future members.
- **Topic / concept:** Algebra, fractions, reading comprehension, vocabulary, waves; dependent on subject/versioned curriculum.
- **Learning capability:** curriculum planning, lesson design, instruction, guided practice, independent practice, diagnostic assessment, mock testing, performance analysis, remediation, reference/study.
- **Educational artifact type:** lesson plan, worksheet, answer key, annotated passage, diagnostic test, mock test, rubric, cheatsheet, study guide, feedback report.
- **Delivery instance:** learner group, grade/course, instructional week, source revision, artifact format, print layout profile, destination and approvals.
- **Assessment unit:** passage / question / item / answer / explanation / scoring criterion; subject-specific subtypes and provenance.
- **Evidence:** curriculum source citation, coverage, calculation proof, rubric result, review and release receipt.

A capability may produce several artifact types, and the same artifact type can support several capabilities. Avoid identifying a worksheet solely by `subject × capability × artifact`; include versioned context and a stable artifact ID. Distinguish a diagnostic *capability* from the diagnostic *test artifact*.

## 4. M0–M8 station and artifact architecture

Use the [strategy's canonical station table](../../strategy/ai-sdlc-software-factory-strategy.md#3b-human-reviewable-artifact-system-by-agent-station) without copying its complete rules here.

| Station | Review whole | Atomic record / gate |
|---|---|---|
| M0 | `exploration.md` | HYP/EXP/FND; go/pivot/stop |
| M1 | `PRODUCT.md`, `ontology.md` | INT/OUT/TERM/ENT; owner approves scope |
| M2 | `requirements.md` | REQ/AC/QAS/CST; measurable completeness |
| M3 | `process.md` | FA/PHASE/RULE/VAR; variation and automation modes |
| M4 | `architecture.md` | ADR/CMP/IFC/RESP; 3D and ownership trade-offs |
| M5 | `design.md` | SLICE/DC/API/EVT/STATE/ALG; implementable contract |
| M6 | `implementation.md` | IMP/CFG/MIG/BUILD; provenance |
| M7 | `verification.md` | TEST/EVAL/EVD/EXC; independent evidence and coverage |
| M8 | `learning.md` | OBS/SIG/FDB/LRN/DELTA; accepted delta routed upstream |

Generate a one-page review brief per station from these atomic authoritative records. Every execution has correlation ID, actor/version, input and output IDs, assumptions, approvals, events and evidence. Require forward/backward links and explicit `supersedes` on deltas. Do not pretend that one Markdown file per possible entity is automatically necessary.

## 5. C1–C4 and three dimensions

**C1:** context with educators/learners, product owner, reviewers, external curriculum licensors, document/publishing systems, AI harnesses and MTS product; factory control plane separate from product surface.

**C2:** proposed logical containers: factory governance/trace service; workflow and human gates; evidence/verification service; educational domain services; artifact/render adapter; delivery/observability adapter. These are *logical partitions*, not mandates for deployable microservices.

**C3:** for chosen first slice inspect spec loader, Math verifier, schema validator, run repository and evidence writer as components; all interface boundaries must be contract-tested.

**C4:** only when a complex module needs code-level decomposition. Avoid large speculative class models.

Three independent architectural dimensions: (1) functionality and process (physiology), (2) applications/interfaces/technology (anatomy), (3) information/entities and flow (circulation). Every decision also specifies quality scenarios and human/agent responsibility overlays. For example, independent verification (function) invokes a verifier contract (application) over a versioned Worksheet Spec, answer and EVD record (information), under correctness, reproducibility and human approval constraints.

## 6. Proposed permanent folder structure — NOT APPROVED

```text
/
  README.md  AGENTS.md  PRODUCT.md
  strategy/                          # governing method, original provenance, migration plan
  docs/
    product/  domain/  requirements/  process/
    architecture/{adr,components,interfaces}/  design/
    implementation/  verification/  learning/  reviews/
  specs/                             # versioned product/slice specs
  contracts/                         # schemas, API/event/file contracts
  config/                            # validated variation, no duplicated rules
  src/factory/                       # genuinely generic kernel, after proof
  products/mts-education/            # domain modules and product policies
  tests/  evals/  evidence/           # executable checks + generated proof (retention policy needed)
  workflows/  skills/  templates/  scripts/
  observability/  infra/  .github/   # only when implementation warrants
```

This is a **logical target**, not permission to create empty directories. Choice between `src/factory` and a separately versioned platform, and whether product code nests under `products/`, requires ADR and slice evidence.

## 7. Proposed ADR queue (all unapproved)

| Candidate | Decision question |
|---|---|
| ADR-001 | Factory kernel vs educational product boundary and packaging |
| ADR-002 | Atomic ID registry, versioning, trace-graph persistence and generated ledger |
| ADR-003 | Source precedence, configuration vs requirements and conflict handling |
| ADR-004 | Subject/capability/artifact ontology and extension cardinalities |
| ADR-005 | Verification/evidence schema, independence and release states |
| ADR-006 | Human gates, station automation ladder and exceptions |
| ADR-007 | Output adapters, template rendering, provenance and publication idempotency |
| ADR-008 | Migration/cutover, regression baselines and legacy retention |

## 8. Risks and unresolved constraints

- **Evidence quality:** repository file presence and historical PASS assertions are not latest test results.
- **Educational correctness:** Math calculations and ELA textual support require independent, domain-specific oracles, plus visual QA and layout checks.
- **Security/privacy:** student data, content licenses, credentials, Drive destination identifiers, telemetry retention and agent run log redaction need owners.
- **Premature generalization:** a factory kernel designed only from worksheets may be product-specific in disguise.
- **Provider portability:** different AI harnesses may support different tools, yet should execute same authoritative contracts.
- **Source drift:** stale Run Manifest references, copy-pasted adapter rules and dated curriculum sources can diverge.
- **Human authority:** exceptions and gate bypasses need bounded evidence and cannot silently waive mandatory correctness checks.
- **Naming ambiguity:** historical 'YPQA' and 'PQYA' forms and overlapping capability/product nouns require domain-owner resolution.

## 9. First independently verifiable slice — proposed acceptance packet

`SLICE-PROPOSED-001`: one frozen, existing Math Worksheet Spec revision → schema check → independent arithmetic/answer and item integrity checks → criterion-scoped evidence JSON → human L1 coverage view. Proposed acceptance:

1. Same immutable input yields stable validation/evidence semantics.
2. Every included requirement/criterion receives passed/failed/blocked/not-covered result with evidence reference.
3. Deliberately corrupted answer or malformed spec is rejected (negative fixtures).
4. A correction creates a new version and captures old/new provenance, not silent overwrite.
5. No publish occurs; human gate recognizes **verified**, not **released**.
6. Baseline existing tests are run before code changes; results and platform versions retained.

This is a planning hypothesis, **not** verified current functionality or authorization to implement.
