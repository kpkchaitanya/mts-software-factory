# AI-SDLC Software Factory Strategy

**Purpose:** Convert a promising POC into a repeatable, governable capability for producing and evolving production software.

**Operating principle:** **Humans own intent, judgment and authority. AI accelerates elaboration and execution. Deterministic systems provide evidence.**

---

## 1. The Software Factory Model

A software factory is not a large code generator. It is a reusable production system that repeatedly transforms governed human intent into observable, supportable software.

```text
Human intent
    ↓
Living product and domain truth
    ↓
Structured requirements and measurable quality
    ↓
Product/process model
    ↓
3D architecture + cross-cutting constraints
    ↓
Modular vertical slices
    ↓
Evidence from tests, evaluations and runtime
    ↓
Governed learning returned to product truth
```

The factory has four inseparable parts:

| Part | Purpose | Durable assets |
|---|---|---|
| **Product system** | Preserve what and why | `PRODUCT.md`, domain ontology, requirements, scenarios, acceptance criteria |
| **Production system** | Define how work moves | lifecycle, phase contracts, workflows, commands, reusable templates |
| **Engineering system** | Build repeatable product slices | architecture, modules, APIs, code, configuration, tests, CI/CD |
| **Learning system** | Improve from evidence | telemetry, evaluations, incidents, decisions, constraint backlog, updated specs |

The product is the output. The factory is the reusable system that keeps producing and improving products.

---

## 2. Non-Negotiable Factory Constitution

1. **Intent before implementation.** Every material change traces to an approved human intent, outcome or constraint.
2. **One fact, one authoritative home.** Other artifacts reference it instead of copying it.
3. **Living specifications are production assets.** Product, requirements, architecture and tests evolve together.
4. **No unresolved critical ambiguity crosses a gate.** Record an assumption only when its risk and owner are explicit.
5. **Architecture is analyzed in 3D.** Functionality, applications/interfaces/technology and entities/data are resolved together.
6. **Non-functional qualities and responsibility govern all three dimensions.** They are overlays, not afterthoughts.
7. **Build modular, bounded, end-to-end vertical slices.** Each slice must be demonstrable and independently verifiable.
8. **Externalize variability.** Stable product behavior belongs in product artifacts; legitimate variation belongs in configuration or extension mechanisms.
9. **Evidence beats confidence.** Generated code is incomplete until executed, tested and observed.
10. **Automation is earned.** A phase moves from manual to assisted to semi-automated to highly automated only after its contract and controls are dependable.
11. **Humans retain authority.** Business intent, risk acceptance, architecture exceptions and production release boundaries remain explicitly owned.
12. **Every defect improves the factory.** Fix the instance, then strengthen the relevant spec, template, test, rule, tool or feedback loop.

---

## 3. M0–M8 Adoptable Production Lifecycle

Each level is a **logical capability and quality gate**, not necessarily a separate team or waterfall phase. Small changes may traverse the model quickly; complex concepts use Iterative Constraint Resolution to zoom in, resolve and rejoin the flow.

| Level | Factory capability | Required inputs | Repeatable activities | Authoritative outputs | Exit evidence / gate |
|---|---|---|---|---|---|
| **M0 — POC / Vibe Coding** | Explore cheaply | problem hypothesis, time box | prototype, compare approaches, test feasibility | disposable prototype, findings, risks, go/stop decision | learning captured; production code is not assumed |
| **M1 — Intent & Domain Ontology** | Preserve meaning | sponsor intent, users, domain sources | define outcomes, boundaries, vocabulary, functional areas, entities and relationships | `PRODUCT.md`, intent map, ontology/glossary, scope and anti-scope | human owner confirms what, why, who and boundaries |
| **M2 — Requirements & Quality** | Make intent verifiable | M1 truth | scenarios, constraints, acceptance criteria, NFRs, examples and edge cases | requirements, quality-attribute scenarios, acceptance/evaluation plan | ambiguity assessed; success is measurable |
| **M3 — Structured Product & Process** | Make work operable | M1–M2 | map functional areas to phases; define manual/AI-assisted/semi/fully automated mode; separate product core from customization | phase map, process model, business rules/config model, product-extension model | process and variation points are explicit |
| **M4 — 3D Architecture & Trade-offs** | Make coherent choices | M1–M3 plus enterprise constraints | analyze functionality, anatomy and flow together; resolve boundaries, alternatives, ownership and trade-offs | C1/C2 views, high-level ERD, interface map, NFR tactics, responsibility map, ADRs | architecture satisfies scenarios; decisions and owners recorded |
| **M5 — Detailed Design** | Make slices implementable | approved M4 boundaries | define C3/C4 components, APIs, contracts, state, workflows, algorithms, migrations and test seams | slice design packet, contracts, detailed ERD, pseudocode, test design | slice is bounded, contract-complete and independently testable |
| **M6 — Iterative Modular Vertical-Slice Build & Integration** | Produce working increments | approved slice packet | code plus configuration; contract-first integration; migrations; documentation; incremental PRs | executable slice, tests, build artifacts, provenance | build, policy, contract and integration gates pass |
| **M7 — Continuous Verification** | Produce trustworthy evidence | executable slice | unit/integration/contract/E2E/security/performance tests; AI evals; exploratory/manual verification; regression | evidence bundle, trace report, exceptions, release recommendation | acceptance and quality thresholds pass; residual risk accepted |
| **M8 — Observe, Learn & Adapt** | Close the learning loop | deployed behavior and user feedback | collect telemetry, compare outcomes, analyze failures and drift, prioritize next constraint | runtime evidence, learning log, updated backlog/specs/ontology, next constraint | learning is incorporated into authoritative sources |

### The minimum trace chain

```text
Intent → Requirement → Architecture decision → Slice → Code/config
      → Test/evaluation → Build → Deployment → Runtime evidence → Learning
```

No factory artifact is complete if its upstream intent or downstream evidence cannot be found.

### 3A. Intent-to-Outcome Observability

The factory requires more than runtime logs. It must make the **state of every approved requirement observable from intent through production outcome**.

There are four complementary observability planes:

| Plane | Primary question | Required evidence |
|---|---|---|
| **Intent observability** | Are we implementing the complete and current requirement? | intent ID, requirement ID/version, acceptance criteria, scope, owner, requirement-delta history |
| **Engineering observability** | Where and how is it being implemented? | architecture/design decisions, task/slice IDs, code/config changes, commits, builds and responsible station runs |
| **Verification observability** | What proves that it works completely? | requirement-derived tests/evals, coverage result, negative/edge cases, quality scenarios, approved exceptions |
| **Runtime observability** | Does the released behavior produce the intended outcome? | deployment/version, traces, logs, metrics, user/business outcome, incidents and feedback |

Operational telemetry alone can help diagnose a defect while still leaving half a requirement unimplemented. Therefore, the factory must maintain both:

1. **Execution telemetry:** what the system and agent stations did.
2. **Semantic traceability:** why each action exists and which requirement, scenario and outcome it satisfies.

#### Requirement trace graph

Every governed change participates in this graph:

```text
Intent / Outcome
  → Requirement + Acceptance Criteria + Quality Scenarios
    → Process Phase + 3D Architecture Decision
      → Modular Slice + Detailed Design + Contract
        → Code / Configuration / Data Migration
          → Test / Evaluation / Review Evidence
            → Build / Release / Deployment
              → Runtime Signal / User Outcome / Feedback
                → Learning → Requirement Delta → Updated Intent or Requirement
```

Each node has a stable ID and version. Each relationship is explicit—for example `implements`, `constrains`, `verified_by`, `released_as`, `observed_by`, `supersedes` or `produced_delta`.

#### Requirement Coverage Ledger

Maintain a machine-readable ledger generated from authoritative artifacts and rendered as a human-reviewable table.

| Field | Meaning |
|---|---|
| Requirement ID and version | Stable identity of the governed requirement |
| Intent/outcome link | Why the requirement exists |
| Owner and approver | Human authority and decision responsibility |
| Acceptance criteria | Observable functional completion conditions |
| Quality scenarios | Non-functional completion conditions |
| Architecture/design links | Where the requirement is allocated and resolved |
| Slice and implementation links | Code, configuration, data and migration realization |
| Verification links | Tests, evaluations, reviews and exceptions |
| Release/runtime links | Build, deployment, telemetry and outcome evidence |
| Status | `Unelaborated`, `Ready`, `In progress`, `Implemented`, `Verified`, `Released`, `Observed`, `Accepted`, `Superseded` |
| Coverage gaps | Missing behavior, scenario, evidence, environment or responsibility |
| Requirement-delta links | Learning that changed the requirement and downstream impact |

The ledger must distinguish:

- **implemented** — code/config/data exists;
- **verified** — all mapped acceptance and quality evidence passes;
- **released** — the verified implementation is deployed;
- **observed** — runtime signals confirm the expected behavior;
- **accepted** — the accountable human confirms the intended outcome is satisfied.

No requirement is considered complete merely because a ticket is closed or code is merged.

#### Completeness and consistency gates

Before release, the factory automatically and/or humanly checks:

- every in-scope requirement maps to at least one slice;
- every acceptance criterion and relevant quality scenario maps to evidence;
- every implementation element maps back to an approved requirement or enabling decision;
- every applicable interface/data contract has producer and consumer verification;
- every exception has an owner, rationale, risk, expiry/review date and compensating control;
- no superseded requirement is being implemented accidentally;
- requirement, design, code and test versions are mutually consistent;
- deployment and telemetry identify the exact requirement-bearing build.

#### Station run log and trace context

Every station execution emits a structured, append-only run record:

```yaml
run_id: RUN-...
correlation_id: FLOW-...
station: M0..M8
actor: human | agent | workflow
actor_version: model-or-tool-version
input_artifact_ids: []
input_versions: []
requirement_ids: []
decisions_and_assumptions: []
actions_and_tool_calls: []
output_artifact_ids: []
evidence_ids: []
status: proposed | running | blocked | passed | failed | approved
approver: human-owner
timestamps: {}
cost_and_usage: {}
errors_and_exceptions: []
next_station_or_delta_route: ...
```

Logs must be searchable by requirement, slice, artifact, build, deployment, station, agent, human owner and time. Sensitive reasoning is not required; record inputs, decisions, actions, evidence and outcomes needed for reconstruction and audit.

#### Minimum observability views

The factory should expose five review views from the same trace data:

1. **Requirement completeness:** what is missing before the requirement is truly complete?
2. **Forward trace:** where did this intent become architecture, implementation, evidence and runtime behavior?
3. **Backward trace:** why does this code, configuration, test or deployment exist?
4. **Delta impact:** which artifacts, tests, owners and releases are affected by a new requirement delta?
5. **Flow health:** where is work blocked, repeatedly failing or accumulating exceptions?

### 3B. Human-Reviewable Artifact System by Agent Station

Every M-station owns an authoritative artifact contract. Agents may draft and maintain the artifacts; accountable humans review the one-page view and approve the gate.

#### Progressive drill-down model

| Level | Intended reader and purpose | Content rule |
|---|---|---|
| **L0 — Factory Map** | executive/team orientation | one visual showing M0–M8, learning loop, owners and current flow status |
| **L1 — One-Page Station Brief** | human gate review | purpose, inputs, key decisions, deltas, risks, outputs, evidence, trace coverage and approval |
| **L2 — Governed Specification** | product/architecture/engineering review | complete structured artifact for the station, linked rather than duplicated |
| **L3 — Executable Assets** | agents, developers and CI/CD | schemas, contracts, code, configuration, tests, workflows, dashboards |
| **L4 — Evidence and History** | audit, learning and reconstruction | immutable run logs, versions, decisions, approvals, results, runtime evidence and deltas |

The L1 brief is not another source of truth. It is a generated or carefully maintained **review lens** containing concise decisions and links to authoritative L2–L4 artifacts.

#### Universal one-page station brief template

Each station maintains `M<n>-<station>-BRIEF.md` using this contract:

```markdown
# M<n> — <Station Name> | Review Brief

## 1. Purpose and Current Decision
Outcome sought, decision required, status and accountable owner.

## 2. Inputs and Trace Scope
Linked intent/requirement/delta IDs, artifact versions and assumptions.

## 3. What Changed
Concise delta from the previously approved baseline.

## 4. Key Content / Decisions
The 3–7 items a human must understand; alternatives and trade-offs where relevant.

## 5. Coverage and Gaps
Requirements covered, missing mappings, unresolved constraints and exceptions.

## 6. Evidence
Tests, evaluations, analyses, prototypes, runtime signals or review results.

## 7. Outputs and Downstream Impact
Authoritative artifact links, affected stations, contracts, owners and releases.

## 8. Risks, Responsibility and Escalations
Risks, controls, responsible parties, approval boundaries and stop conditions.

## 9. Human Gate
Approve | Approve with conditions | Return for revision | Stop
Approver, date, conditions and next review.
```

#### Canonical artifact and atomic-entity model per station

Each station has one primary Markdown artifact that explains the coherent whole. Precise traceability uses smaller atomic entities with stable IDs. The primary artifact links to those IDs; it does not replace them or duplicate their complete content.

| Station | Primary artifact | Atomic trace entities | Canonical ID namespaces | Suggested atomic storage | Human gate focuses on |
|---|---|---|---|---|---|
| **M0 — Explore / POC** | `exploration.md` | hypothesis, experiment, finding | `HYP-001`, `EXP-001`, `FND-001` | `docs/exploration/experiments/EXP-001.md` | what was tested and learned; go, pivot or stop; whether any POC asset may enter production |
| **M1 — Intent & Domain** | `PRODUCT.md` and `ontology.md` | intent, outcome, domain term, domain entity | `INT-001`, `OUT-001`, `TERM-001`, `ENT-001` | `docs/product/intents/INT-001.md`; `docs/domain/entities/ENT-001.md` | purpose, users, outcomes, vocabulary, boundaries and shared meaning |
| **M2 — Requirements & Quality** | `requirements.md` | requirement, acceptance criterion, quality scenario, constraint | `REQ-001`, `AC-001.1`, `QAS-001`, `CST-001` | `docs/requirements/REQ-001.md`; criteria may remain addressable sections within it | completeness, clarity, measurability, quality and scope |
| **M3 — Product & Process** | `process.md` | functional area, phase, business rule, variation point | `FA-001`, `PHASE-001`, `RULE-001`, `VAR-001` | `docs/process/phases/PHASE-001.md`; `docs/process/rules/RULE-001.md` | flow, automation mode, handoffs, product core and legitimate variation |
| **M4 — 3D Architecture** | `architecture.md` | architecture decision, component, interface, responsibility; reuses domain entities and quality scenarios | `ADR-001`, `CMP-001`, `IFC-001`, `RESP-001`; reuse `ENT-*`, `QAS-*` | `docs/architecture/adr/ADR-001.md`; architecture catalog entries under `components/`, `interfaces/`, `responsibilities/` | 3D coherence, alternatives, boundaries, quality tactics, ownership and trade-offs |
| **M5 — Detailed Design** | `design.md` | vertical slice, design component, API/event contract, state, algorithm | `SLICE-001`, `DC-001`, `API-001`, `EVT-001`, `STATE-001`, `ALG-001` | `docs/design/slices/SLICE-001.md`; executable contracts under `contracts/` | whether the slice is bounded, implementable, contract-complete and independently testable |
| **M6 — Modular Build** | `implementation.md` | implementation unit, configuration item, migration, build | `IMP-001`, `CFG-001`, `MIG-001`, `BUILD-001` | `docs/implementation/IMP-001.md`; configuration and migrations beside executable assets | whether the approved design is realized in the identified build with provenance |
| **M7 — Verification & Evidence** | `verification.md` | test, evaluation, evidence result, approved exception | `TEST-001`, `EVAL-001`, `EVD-001`, `EXC-001` | `tests/`; `evals/`; `evidence/EVD-001.json`; `docs/exceptions/EXC-001.md` | whether every in-scope criterion and quality scenario has sufficient evidence |
| **M8 — Observe, Learn & Feedback** | `learning.md` | observation, runtime signal, feedback item, learning, requirement delta | `OBS-001`, `SIG-001`, `FDB-001`, `LRN-001`, `DELTA-001` | `docs/learning/LRN-001.md`; `deltas/DELTA-001.md`; telemetry in the observability platform | whether runtime evidence changes intent, requirements, architecture, design or implementation |

`TERM-*` is reserved for domain vocabulary and `CST-*` for requirements constraints. This prevents the earlier ambiguity of using `CON-*` for two different concepts.

#### Aggregate artifact versus atomic entity

```text
architecture.md                         # coherent human-readable architecture
├── CMP-001  Order Service              # atomic component
├── IFC-001  Order Submission API       # atomic interface
├── ENT-001  Order                      # reused domain entity
├── RESP-001 Order ownership            # atomic responsibility
├── QAS-003  Availability scenario      # reused quality scenario
├── ADR-001  Event-driven submission    # atomic decision file
└── ADR-002  Order data ownership       # atomic decision file
```

Use a separate file when an entity has its own lifecycle, owner, approval, alternatives or history—especially `REQ-*`, `ADR-*`, `SLICE-*`, `EXC-*` and `DELTA-*`. Lightweight catalog entities may remain addressable records inside the primary artifact or a structured catalog, provided their IDs remain stable and linkable.

#### Canonical cross-station trace example

```text
INT-001
  → OUT-002
    → REQ-012 / AC-012.1 / QAS-003
      → PHASE-003 / RULE-008
        → ADR-001 / CMP-001 / IFC-002 / ENT-001
          → SLICE-004 / API-002
            → IMP-021 / CFG-004 / BUILD-019
              → TEST-041 / EVAL-006 / EVD-052
                → OBS-014 / SIG-009
                  → LRN-003 / DELTA-006
```

This chain is navigable in both directions. A requirement shows its realization and evidence; a code, configuration, test or runtime signal shows the intent and decision that justify its existence.

#### Artifact navigation contract

Every primary artifact and independently stored atomic entity begins with a small metadata block:

```yaml
artifact_id: ARCHITECTURE | REQ-012 | ADR-001 | SLICE-004 | EVD-052 | ...
artifact_type: intent | requirement | architecture | design | implementation | evidence | learning
station: M0..M8
status: draft | review | approved | superseded
version: ...
owner: ...
approvers: []
source_ids: []
requirement_ids: []
atomic_entity_ids: []
delta_ids: []
supersedes: []
downstream_ids: []
last_verified_against: []
```

Every station summary provides direct links to its primary artifact, atomic entities, executable assets and evidence/history. Every deeper artifact links back to its governing intent, requirement and station artifact. This creates a navigable system rather than a folder of disconnected documents.

#### Template governance

- Store canonical templates under `templates/stations/M0` through `M8`.
- Version templates separately from product artifacts.
- Generate a project artifact from a pinned template version.
- Preserve user-authored and approved content when templates evolve.
- Review templates using representative products before promotion to the golden path.
- Treat template changes as factory changes: test them, record provenance and measure downstream effects.
- Keep the one-page briefs concise; move detail into linked drill-downs rather than shrinking fonts or duplicating content.

---

## 4. M4: The 3D Architecture Kernel

The five architecture concerns are organized as **three primary dimensions plus two governing overlays**.

| Model role | Architecture concern | Body analogy | Questions answered |
|---|---|---|---|
| **Dimension 1** | Functional | **Physiology** | What capabilities and processes must occur? In what hierarchy and phases? |
| **Dimension 2** | Applications, interfaces and technology | **Anatomy** | Which body parts realize the behavior? How are they bounded and connected? What technology is justified? |
| **Dimension 3** | Informational: entities and data | **Circulation / flow** | What flows between parts? What are its meaning, lifecycle, relationships and ownership? |
| **Governing overlay** | Non-functional | **Health and fitness** | How secure, reliable, scalable, usable, observable and maintainable must every intersection be? |
| **Governing overlay** | Responsibility | **Control and accountability** | Which human, team, AI agent or software component decides, performs, approves and operates? |

Example: `Circulate blood` is the physiology; `heart, arteries and veins` are anatomy; `blood` is the information being transported. Health constraints apply throughout, while control and accountability determine who or what regulates, monitors and intervenes.

### 3D resolution rule

For every meaningful capability, create a small matrix:

| Functional phase | Application/interface/technology | Entities and data | Quality scenarios | Responsibility |
|---|---|---|---|---|
| What must happen? | Where and through which contracts? | What enters, changes and exits? | How well and under what failure modes? | Who owns, approves, operates and responds? |

If any column is materially unknown, the concept remains an architectural constraint and must not be hidden inside implementation.

---

## 5. Iterative Constraint Resolution

The factory advances by resolving the most limiting uncertainty—not by creating every document in full detail up front.

```text
Detect → Prioritize → Bound → Analyze in 3D → Resolve
      → Integrate → Verify → Record learning → Next constraint
```

For each constraint:

1. State the observable limitation or unanswered decision.
2. Identify the outcome it blocks and the risk of deferral.
3. Bound the smallest useful investigation or vertical slice.
4. Analyze physiology, anatomy and information flow together.
5. Apply non-functional scenarios and responsibility ownership.
6. Compare alternatives and record the decision in an ADR.
7. Build or simulate enough to obtain evidence.
8. Update the authoritative artifacts and constraint backlog.

Use spikes only for learning. A spike becomes product work only after its learning is translated into governed design and production-quality acceptance criteria.

---

## 6. The Repeatable Unit: A Modular Vertical Slice

The preferred work package is a thin, end-to-end slice that crosses only the layers necessary to deliver one observable outcome.

Every slice must contain:

| Slice element | Minimum content |
|---|---|
| Intent | user/business outcome and source |
| Scope | included behavior, exclusions and assumptions |
| 3D design | functional phase, components/interfaces/technology, entities/data |
| Overlays | relevant NFR scenarios and responsibility/approval boundaries |
| Contracts | API, event, file, UI or workflow contracts and compatibility rules |
| Variation | product behavior vs configuration vs approved extension |
| Evidence | acceptance examples, tests, evaluations and observable runtime signals |
| Release | migration, rollout, rollback and operational ownership |

Prefer a sequence of complete slices over horizontal layers such as “build all APIs, then all UIs.” A slice should be small enough for focused review and large enough to produce end-to-end evidence.

---

## 7. Factory Asset Architecture

Use four artifact classes to keep context deterministic and economical.

| Artifact class | Purpose | Typical formats | Rule |
|---|---|---|---|
| **Knowledge** | Facts, concepts and context | `.md`, ontology, examples, curated references | explanatory; provenance-preserved |
| **Configuration** | Approved variability | `.yaml`, `.json`, policy tables, feature flags | schema-validated; no hidden code |
| **Command** | Thin human/agent entry point | `.md`, CLI command | declares inputs, output and invoked workflow |
| **Workflow** | Orchestrated production procedure | `.yaml`, `.md`, pipeline definition | restartable, observable and gate-aware |
| **Skill** | Reusable reasoning or specialized task method | instruction package + references/templates | bounded purpose; versioned and testable |
| **Code** | Deterministic execution | source, scripts, services | used where repeatability matters more than interpretation |
| **Tests & evaluations** | Executable evidence | test code, fixtures, eval datasets, rubrics | derived from intent and failure history |
| **Templates & output** | Reusable skeletons and deliverables | repo templates, docs, manifests | parameterized; product/customization separated |

Principle: **reason with knowledge, vary with configuration, enter through commands, orchestrate with workflows, reuse expertise through skills, and execute deterministically with code.**

---

## 8. Reference Repository Blueprint

```text
/
├── PRODUCT.md                     # audience, problem, purpose, boundaries, outcomes
├── AGENTS.md                      # concise agent operating contract and pointers
├── README.md                      # human entry point and local quick start
├── docs/
│   ├── intent/                    # intent map, ontology, glossary
│   ├── requirements/              # scenarios, constraints, acceptance criteria
│   ├── process/                   # phases and automation modes
│   ├── architecture/
│   │   ├── c1-context.md
│   │   ├── c2-containers.md
│   │   ├── data-model.md
│   │   ├── interfaces.md
│   │   ├── quality-scenarios.md
│   │   ├── responsibilities.md
│   │   └── adr/
│   ├── design/                    # slice design packets
│   ├── operations/                # SLOs, runbooks, recovery
│   └── learning/                  # decisions, incidents, constraints, retrospectives
├── specs/                         # living feature/slice specifications
├── contracts/                     # OpenAPI, AsyncAPI, schemas, conformance cases
├── config/                        # externalized product/project configuration
├── extensions/                    # bounded customization mechanisms
├── src/                           # product code
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── contract/
│   ├── e2e/
│   ├── security-performance/
│   └── evals/                     # AI behavior datasets, rubrics and thresholds
├── workflows/                     # agent and delivery workflows
├── skills/                        # reusable task expertise
├── templates/                     # golden-path skeletons
├── scripts/                       # deterministic developer/factory operations
├── observability/                 # dashboards, alerts, telemetry contracts
├── infra/                         # infrastructure as code
└── .github/
    ├── workflows/                 # reusable CI/CD and provenance workflows
    ├── CODEOWNERS
    ├── pull_request_template.md
    └── agent instructions         # tool-specific thin adapters, if needed
```

### Context architecture

Keep root instructions short. Use them as a map to authoritative, scoped files. Load context progressively by task rather than injecting the whole repository. Generated summaries never silently replace authoritative sources.

---

## 9. Quality and Verification System

Verification has three complementary layers:

| Layer | Best for | Examples |
|---|---|---|
| **Deterministic gates** | objective correctness and policy | compile, lint, schema, unit, contract, dependency, security, license, migration checks |
| **Model-based evaluations** | semantic or judgment-bearing quality | requirement coverage, design coherence, answer quality, unsafe behavior, style rubric |
| **Human verification** | intent, trade-offs and accountable risk | product acceptance, architecture decision, UX judgment, production authorization |

Required behavior:

- Run the existing baseline tests before changing code.
- Add or update tests with the behavior change.
- Execute the real product path; do not accept unexecuted generated code.
- Convert manually discovered failures into permanent regression evidence.
- Use independent review for high-risk changes; the producer should not be the only evaluator.
- Keep retries bounded. Repeated failure becomes a constraint requiring human analysis, not an infinite agent loop.
- Produce an evidence bundle for every releasable slice.

### Evidence bundle

```text
spec/version + commit + build provenance + test/eval results
+ security/compliance checks + deployment record + runtime signals
+ approved exceptions + accountable owners
```

---

## 10. Product Core, Configuration and Customization

Use this decision order whenever variability appears:

1. **Product core:** Is it invariant behavior that should work for every adopter?
2. **Configuration:** Is it an anticipated variation expressible as validated data or policy?
3. **Extension:** Is it legitimate bounded behavior behind a stable interface?
4. **Fork/custom code:** Is isolation unavoidable and its lifecycle explicitly funded?

Business rules should be externalized only when their semantics, validation, ownership, versioning and test coverage are clear. Moving arbitrary logic into YAML does not make it maintainable.

Every configuration field needs:

- schema, type and allowed range;
- default and backward-compatibility behavior;
- owning role;
- security classification;
- validation and test cases;
- effective-date/version semantics when business behavior changes over time.

---

## 11. Controlled Automation Ladder

Automation is selected **per functional phase**, not once for the entire product.

| Level | Operating mode | Human role | Promotion evidence |
|---|---|---|---|
| **A0 Manual** | humans perform the phase | perform and document | process and decision points understood |
| **A1 Assisted** | AI recommends or drafts | direct and verify each output | repeated usefulness and safe boundaries |
| **A2 Semi-automated** | workflow performs routine sequence | approve checkpoints and exceptions | stable contracts, metrics and rollback |
| **A3 Conditional autonomy** | workflow completes normal cases | handle escalations | exception detection and SLOs proven |
| **A4 High automation** | autonomous for most cases | govern policy and rare risks | sustained reliability and auditability |
| **A5 Full automation** | closed-loop operation within a bounded domain | retain authority over policy and shutdown | only where consequence, reversibility and evidence justify it |

The same product can contain A0 discovery, A1 architecture, A3 test execution and A4 deployment verification. Mixed automation is a design strength.

---

## 12. Factory Roles and Responsibility

Roles may be people, teams or explicitly bounded agents, but accountability remains human.

| Role | Accountable for |
|---|---|
| Product intent owner | purpose, users, outcomes, scope and priority |
| Domain steward | ontology, rules, examples and semantic consistency |
| Architecture owner | 3D coherence, NFR tactics, boundaries and ADRs |
| Factory/platform owner | templates, workflows, skills, golden paths and developer experience |
| Slice owner | end-to-end delivery and evidence for a bounded outcome |
| Quality/security owner | independent gates, evaluation policy and exceptions |
| Operations owner | SLOs, telemetry, deployment, recovery and learning |
| AI agent | bounded elaboration/execution with declared permissions, inputs and outputs |

For every workflow action define: **propose, execute, verify, approve, operate and escalate**. Never use “AI owns it” as a responsibility assignment.

---

## 13. Adoption Strategy: POC to Software Factory

Do not attempt to automate the full lifecycle first. Establish a dependable path for one product and one representative slice, then generalize what survives evidence.

### Stage 0 — Inventory the POC

- Freeze a reproducible POC baseline.
- Capture what was learned, what is disposable and what may be reusable.
- Identify unverified assumptions, hidden dependencies, security gaps and missing tests.
- Select one valuable, bounded production outcome.

**Exit:** explicit go/stop/pivot decision and named product owner.

### Stage 1 — Establish product truth

- Create `PRODUCT.md`, ontology/glossary and scope boundaries.
- Convert prompt history and tribal knowledge into authoritative artifacts.
- Define measurable requirements, examples and quality scenarios.
- Create trace IDs or stable links between intent, requirements and evidence.

**Exit:** humans can reconstruct why the selected slice should exist.

### Stage 2 — Resolve architecture in 3D

- Map phases/capabilities, C1/C2 components and high-level entity flow.
- Apply non-functional scenarios and responsibility boundaries.
- Record alternatives and ADRs.
- Decide product core, configuration and extension points.

**Exit:** the slice has coherent boundaries, contracts and owners.

### Stage 3 — Build the first production slice

- Create the detailed slice packet.
- Implement in small, reviewable changes.
- Add deterministic tests, semantic evals where relevant and manual exploration.
- Add CI, secrets handling, dependency controls, observability, rollout and rollback.

**Exit:** a user-visible outcome runs in a production-like environment with an evidence bundle.

### Stage 4 — Extract the golden path

- Identify the assets that were truly reusable.
- Convert them into versioned templates, workflows, schemas, skills and reusable CI.
- Parameterize approved variation; do not clone product-specific assumptions.
- Scaffold a second slice or product from the golden path.

**Exit:** a second use case is faster without sacrificing evidence or traceability.

### Stage 5 — Operate and scale the factory

- Publish a self-service product/slice creation path with reviewed inputs.
- Maintain a catalog of templates, components, APIs and owners.
- Measure flow, quality, adoption, cost and runtime outcomes.
- Use learning and incident data to improve the factory assets centrally.

**Exit:** teams can repeatedly create conforming software, and factory improvements compound across products.

---

## 14. First 90-Day Implementation Plan

| Period | Focus | Deliverables |
|---|---|---|
| **Days 1–15** | POC assessment and constitution | baseline, product owner, `PRODUCT.md`, ontology, risk/constraint backlog, initial metrics |
| **Days 16–30** | Requirements and 3D architecture | quality scenarios, phase model, C1/C2, entity flow, responsibility map, first ADRs |
| **Days 31–50** | First modular production slice | slice packet, contracts, code/config separation, baseline test/eval suite |
| **Days 51–65** | Delivery and evidence | reusable CI, security gates, provenance, deployment/rollback, telemetry and runbook |
| **Days 66–75** | Runtime learning | controlled release, user feedback, SLO evidence, constraint review, updated specs |
| **Days 76–90** | Factory extraction | golden-path template, reusable workflows/skills, second-slice trial, adoption guide |

Start with one team and one representative product. A factory is proven by the second successful use, not by the sophistication of its first framework.

---

## 15. Measures That Prevent “More Code” from Masquerading as Progress

### Product outcomes

- user outcome achieved;
- time to validated learning;
- adoption, task success and outcome quality;
- escaped requirement defects.

### Flow

- intent-to-evidence lead time;
- slice size and cycle time;
- wait time at gates;
- rework caused by ambiguity or architecture drift.

### Quality and operations

- acceptance/contract pass rate;
- escaped defects and change failure rate;
- reliability/SLO attainment and recovery time;
- security, privacy and compliance findings;
- trace completeness.

### Factory effectiveness

- percentage of work using a golden path;
- reuse rate of templates, components, workflows and tests;
- time to scaffold and validate a second product/slice;
- factory-origin defects versus product-origin defects;
- cost per accepted slice and human review time;
- automation level by phase, with exception and rollback rates.

Do not use generated lines of code, prompts executed or agent hours as success measures.

---

## 16. Pioneer and Implementation Practices Incorporated

| Source | Practice adopted into this model |
|---|---|
| [Andrej Karpathy — Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) | Define desired behavior through examples/evaluation criteria; treat data and feedback as programmable assets; optimize where behavior can be repeatedly evaluated. |
| [Addy Osmani — How to write a good spec for AI agents](https://addyo.substack.com/p/how-to-write-a-good-spec-for-ai-agents) | Use concise evolving specs, small tasks, read-only planning, explicit boundaries, self-checks and domain expertise instead of giant prompts. |
| [OpenAI — Harness engineering](https://openai.com/index/harness-engineering/) | Humans steer; agents execute inside a legible repository with enforceable architecture, tools, feedback loops, self-review and continuous entropy reduction. |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | Make specifications living executable assets; use constitution → specify → plan → tasks → implement → converge; package reusable processes without agent lock-in. |
| [Simon Willison — Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/) | Run tests first, execute generated software, perform exploratory/manual verification and convert discovered failures into regression tests. |
| [Backstage Software Templates](https://backstage.io/docs/features/software-templates/) | Offer reviewed, parameterized golden paths that scaffold components and register their ownership instead of copying repositories manually. |
| [GitHub reusable workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows) and [artifact attestations](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations) | Centralize delivery policy, reduce workflow duplication and preserve verifiable build provenance. |
| [Microsoft Agentic SDLC Starter](https://github.com/microsoft/agentic-sdlc-starter) | Assess ambiguity, resolve it, generate structured specifications, build from governed inputs and validate output against guardrails. |

These sources are design inputs, not a mandate to copy any one framework. The factory remains model-, agent-, IDE-, language- and cloud-portable.

---

## 17. Definition of a Working Software Factory

The model is working when:

- a new team can begin from a reviewed golden path rather than a blank repository;
- a human can trace any production behavior back to intent and forward to evidence;
- agents can find authoritative context without large prompt dumps;
- modular slices can be built, verified, released and rolled back independently;
- product core and customization do not contaminate each other;
- quality, security and operational requirements are enforced by reusable gates;
- production learning updates specifications, evaluations and factory assets;
- the second and third products become faster while retaining or improving quality;
- humans spend more time on intent, trade-offs and learning, and less on repetitive translation.

That is the transition from **AI-assisted project delivery** to an **adoptable AI Software Factory**.
