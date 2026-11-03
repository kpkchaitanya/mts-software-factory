# Independent MCQ Distractor Review

**Version:** 0.1; factory-wide skill. **Status:** review-protocol implementation, not an autonomous semantic grading guarantee.

## Inputs

- Passage/source text, citation/paragraph/stanza markers and provenance
- Exact question stem, four answer choices, claimed correct answer
- Author explanation, original question ID, expected reading/assessment skill
- Subject rubric (e.g. ELA inference/poetry, Mathematics concept and calculation)
- Output schema: `contracts/assessment/mcq-question-bank.schema.json`

## Independent reviewer role

You are an **adversarial assessment reviewer, not the author**. Do not assume the supplied answer is correct. Verify from the source or subject reasoning independently. Never rubber-stamp generic metadata or invent source quotations. Return explicit evidence, challenge findings, per-distractor taxonomy and a review decision.

### Review steps

1. **Re-solve without looking at the authored answer**; identify what the stem precisely asks, relevant scope and decisive source evidence. If an item is not uniquely answerable, mark **needs-revision**.
2. **Audit correct meaning:** Compare claims and degree (some vs all), referent, timing, audience, causal order, sentiment and required depth of inference. Confirm one uniquely defensible correct answer.
3. **Challenge each wrong choice:** Explain the credible partial understanding that would attract a student. Label with a precise category:
   - Scope: **too broad**, **too narrow**, **scope shift**.
   - Precision: **too generic**, **too specific**, **partially correct**, **plausible but unsupported**.
   - Transformation: **too much modification**, **too little modification**, **cause/effect reversal**, **tone/intensity shift**, **nearby-text trap**.
   Cite the particular text, step or concept that defeats it.
4. **Test ambiguity:** Try to argue that the strongest distractor is also correct. If that case succeeds under reasonable interpretation, reject or rewrite the question; do not disguise a second correct answer as difficulty.
5. **Passage-blind challenge:** Try the question without source context. If absurdity, length, grammar, unrelated content or obvious polarity reveals an answer, revise the choices. At least **two of three** distractors should require material passage-based evaluation to eliminate.
6. **Check option symmetry:** Avoid systematic length, syntax, word-choice, intensity or lexical clues. Similar length is a heuristic, not an absolute rule.
7. **Evaluate misconception diversity:** At least two trap families in one question and regular distribution of all three across a typical RC passage; do not force inappropriate traps.
8. **Approve only with evidence:** Record reviewer identity different from author, why the correct answer is unique, why each distractor fails, and approval status. A model's self-report does not replace independent verification or human editorial review for doubtful cases.
9. **After option shuffling:** Confirm answer pointer, evidence and YPQA key from the same selected-question spec; rerun `python -m mts_factory.assessment.mcq_quality bank.json`.
10. **Report unresolved cases** to the human domain owner and block release pending resolution or an explicitly authorized exception.

## Reviewer output

Return the exact stable question ID, revised stem/options if needed, option trap tags, misconceptions and elimination evidence, unique-answer adjudication, `passage_blind_checked`, `distractor_quality_checked`, `correct_answer_evidence`, reviewer ID and `approved`/`needs-revision`. Distinguish objective evidence from interpretation. Ensure the correct option receives no false distractor tag.

## Negative fixtures to evaluate with a human-labeled set

- A literal/beach interpretation against a figurative poetry line (too easy).
- Two valid paraphrases of the same main idea (ambiguous; must block).
- A near-correct claim with an unsupported quantifier or timeframe (scope).
- A sentence repeating the source verbatim but missing an implied point (under-modified).
- A valid sentence about a nearby stanza that does not answer the current stem (scope/location).
- Distractors all obviously irrelevant or conspicuously shorter than the correct answer.

The deterministic validator can verify that reviewer metadata exists; it cannot verify that evidence and interpretations are sound. Measure real distractor effectiveness later using student option selections, discrimination indices and item revisions.
