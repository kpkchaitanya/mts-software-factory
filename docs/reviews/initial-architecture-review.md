---
document_id: REV-ARCH-001
status: draft-for-human-review
version: 0.1
date: 2026-11-01
decision_authority: none
---

# Initial Architecture Rationalization — One-Page Review

> **Draft, not approved.** This is an L1 review lens. The [architecture analysis](architecture-rationalization.md) and [migration inventory](migration-assessment.md) carry deeper reasoning. Do not migrate code or scaffold the proposed folders from this review.

## Decision requested

Approve, amend or reject **the proposed factory/product boundary, ontology, traceability contracts, first slice and evaluation plan**. Folder layout and migration classifications remain proposals until an explicit decision/ADR.

## Executive findings

1. The [governing strategy](../../strategy/ai-sdlc-software-factory-strategy.md) is broader than the existing MTS Testing System. Preserve the four systems—product, production, engineering, learning—as factory concerns, not educational-specific behavior.
2. [mts-crossmodel](https://github.com/kpkchaitanya/mts-crossmodel) contains substantive Math and shared worksheet assets, schemas, gate controls, tests, manifests and publishing logic. **Presence and old PASS notes are not current test execution evidence.**
3. Educational history captures specific requirements and ELA release lessons, but a dated successful PDF delivery is not proof of a general automated ELA pipeline.
4. Biggest cross-source gap: machine-verifiable **intent → requirement → criterion → artifact/build → verification → release → runtime outcome → requirement delta** coverage. Run manifests are a promising partial substrate, not yet a complete requirement ledger.
5. A narrow Math worksheet-spec-to-verification slice is a lower-risk first implementation than wholesale migration. An ELA counterpart would test genuine cross-domain reuse after it is independently verified.

## Three-source synthesis

| Concern | Strategy authority | Legacy implementation evidence | Historical domain evidence | Initial assessment |
|---|---|---|---|---|
| Factory scope | Generic four-system factory, M0–M8 | Worksheet-centric MTS Testing System | Subject × capability × output | Separate factory kernel from first educational product |
| Requirements | Stable IDs, AC/QAS, ledger | Brief subject requirements and Math feature specs | Rich ELA/Math style and QA deltas | Formalize atomic requirements and acceptance tests |
| Architecture | 3D, C1–C4, ADRs | Worksheet C1/C2 diagrams and Math ADRs | Proposed taxonomy/quality needs | Re-map C1/C2 and avoid reusing outdated M-stage numbering |
| Verification | Independent evidence across every stage | Math tests, gates, manifests, schemas | Specific released ELA PDF lessons | Re-run baseline, capture current pass/fail and new negative cases |
| Learning | OBS/LRN/DELTA back to truth | Some run history and legacy status docs | Repeated formatting, key and publishing defects | Make each defect an owned regression and delta |
| Automation | Earned per phase, human authority | Slash commands and harness adapters | Manual reviews/publishing episodes | Keep A-level per phase; no autonomy claims from scripts |

## Proposed principles for approval

- **Factory vs product:** factory owns reusable lifecycle, contracts, trace/evidence, gates and adapters; products own domain ontology, curricula, scoring and format policies.
- **Requirements hierarchy:** outcome → product capability → requirement → acceptance criterion/quality scenario → slice and evidence; every node stable-ID/versioned.
- **Educational ontology:** keep **subject**, **learning capability** and **artifact/output kind** separately modeled, with many-to-many mappings rather than a rigid three-column identity.
- **Status discipline:** distinct proposed, implemented, verified, released, observed, accepted and superseded; evidence required for promotion.

## Recommended first vertical slice

**SLICE-PROPOSED-001 — Traceable Math worksheet verification:** ingest one existing Math Worksheet Spec revision, independently verify its answer-key correctness and schema conformance, emit criterion-linked evidence and a human-readable requirement coverage brief. No live Drive publication or changing generation logic in the first slice. Exact fixture, requirements, baseline and acceptance thresholds to be selected during M1/M2 approval.

## Human gate

- **Status:** Awaiting review (no approval inferred).
- **Key unresolved decisions:** canonical ID registry shape; terminology of educational capabilities; authoritative location of product documents; exact first slice and release environment; evidence retention/privacy policy.
- **Next step if approved:** record ADRs, implement only the approved vertical slice with baseline regressions; retain legacy repository unchanged until explicitly authorized cutover.
