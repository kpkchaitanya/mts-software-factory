# Assessment MCQ Quality — Proposed shared contract

Status: **implemented as an initial review slice; not yet integrated with all publishing workflows**. Requirement deltas **ELA-ANS-DIST-016** and **ELA-DISTRACTOR-017** originated in the Grade 6 `A Psalm of Life` review. Applies to 4-option MCQs across subjects when suitably configured; passage-specific defaults belong to RC only.

## Intent

Students should be assessed on comprehension and reasoning, not rewarded for guessing a dominant letter or rejecting obviously irrelevant options. Correct answers must be determined by evidence **before** answer positions are shuffled. Position randomization cannot change correctness or invent plausible support.

## 016 — Answer-position / pattern gate (deterministic)

- For a reading-comprehension section with 8–10 four-choice questions: each of A–D must appear at least once; no choice appears more than four times; no more than two identical letters consecutively; reject a repeated 4-letter A/B/C/D permutation cycle.
- Measure **per passage/section**, not just across a worksheet; poetry and fiction cannot hide each other's bias.
- Report counts and violations. Do not use a fixed pattern repeatedly. Preserve question IDs and recheck the key **after** choice reordering.
- These are initial policy thresholds, not mathematical guarantees of randomness; other assessment sizes and formats need explicit policy profiles.

## 017 — Distractor plausibility / reasoning gate (independent semantic review)

For each wrong choice require: (a) a tagged plausible misunderstanding; (b) why a partially prepared student may select it; (c) a specific evidence-based elimination explanation. Across a passage, regularly rotate the three reasoning families:

| Family | Trap variants | Reader's required distinction |
|---|---|---|
| **Scope** | too broad, too narrow, scope shift | exact claim, audience, timeframe, focus |
| **Precision** | too generic, too specific, partially correct, plausible but unsupported | precision and evidence limit |
| **Transformation** | too much modification, too little modification, causal reversal, tone shift, nearby-text trap | preservation of meaning, logic and inference |

At least two families should appear among three distractors for each question, and all three across a typical 8–10-question passage. **Variety is a design goal, not license to force a bad trap.** If a source cannot sustain this mix, obtain a documented exception or rewrite the question bank.

Independent reviewer must:
1. Prove **exactly one** option is defensible for the precise stem using passage evidence.
2. Try to make a credible case for each alternative; revise a second defensible answer (ambiguity).
3. Perform a **passage-blind** elimination challenge. Revise obvious absurdities, mismatched grammar, suspicious option length and simplistic keyword giveaways.
4. Confirm at least **two of three distractors require passage-dependent reasoning** to eliminate.
5. Check that the author is not the sole reviewer; record actual reviewer identity, rationale and approval. Never self-generate a fake independent pass.
6. Confirm the teacher key explains the misconception and decisive elimination evidence **for each** distractor.

The Python gate tests metadata, family coverage and recorded review approval. It **cannot** judge whether semantic claims or human review are true. This requires a different reviewer (human or independently prompted model) with access to the source, followed by human judgment for ambiguous cases. Real student item-analysis is the future outcome signal.

## QA sequencing / release policy

`Author correct answer + evidence → author misconception-based distractors → independently challenge ambiguity and evidence → reorder answers with balance checks → regenerate same-spec teacher key → reverify answer mapping → layout/visual QA → publish`.

A failed deterministic check blocks. A missing, failed or unverified semantic review blocks. Store review provenance and defect linkage in the run evidence. Published artifacts are not altered silently.

## Regression requirements

Include negative fixtures for dominant A, repeated-letter runs, predictable four-position cycles, missing misconception/evidence, repetitive trap families, missing independent review, multiple-answer ambiguity flagged by reviewer, and a stale key after reordering. The tests in `tests/test_mcq_quality.py` exercise structural failure cases. *Actual* ambiguous alternatives require separate human/model evaluation fixtures and adjudicated labels.

## Integration gap

The current `mts-software-factory` repository is still being bootstrapped; this module is **not yet invoked** by the historical Drive-based ELA generator or by every Math/ELA command in `mts-crossmodel`. Next change must wire the canonical selected-question manifest and renderer/publisher to call this validator and record reviewer evidence before allowing publication. The November 2 PDFs have **not** been regenerated or republished by this change.
