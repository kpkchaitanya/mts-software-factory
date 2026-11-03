"""Deterministic preflight for four-option multiple-choice assessments.

Semantic distractor quality is NOT automatically established by this module.
An independent reviewer must inspect actual passage evidence and record approval.
Run: python -m mts_factory.assessment.mcq_quality path/to/bank.json
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

TRAP_FAMILIES = {
    "too-broad": "scope", "too-narrow": "scope", "scope-shift": "scope",
    "too-generic": "precision", "too-specific": "precision",
    "plausible-unsupported": "precision", "partially-correct": "precision",
    "over-modified": "transformation", "under-modified": "transformation",
    "cause-effect-reversal": "transformation", "tone-shift": "transformation",
    "nearby-text": "transformation",
}
LETTERS = "ABCD"


def validate_bank(bank: dict, *, minimum: int = 8, maximum: int = 10,
                  max_per_letter: int = 4, max_run: int = 2,
                  require_independent_review: bool = True) -> list[str]:
    """Return actionable release-blocking failures (empty list means structural pass).

    Check one passage/section at a time, not an aggregate across multiple passages.
    Thresholds are defaults for MTS RC 8-10-item sections; other assessment products
    must provide explicitly governed thresholds rather than inheriting them blindly.
    """
    errors: list[str] = []
    questions = bank.get("questions")
    if not isinstance(questions, list):
        return ["questions must be a list"]
    if not minimum <= len(questions) <= maximum:
        errors.append(f"expected {minimum}-{maximum} questions; found {len(questions)}")

    letters: list[str] = []
    question_ids: list[str] = []
    observed_families: set[str] = set()

    for index, question in enumerate(questions, 1):
        if not isinstance(question, dict):
            errors.append(f"question {index}: object required")
            continue
        qid = question.get("id")
        if not isinstance(qid, str) or not qid.strip():
            errors.append(f"question {index}: stable id required")
            qid = f"position-{index}"
        question_ids.append(qid)
        choices = question.get("choices")
        if not isinstance(choices, list) or len(choices) != 4:
            errors.append(f"{qid}: exactly 4 choice objects required")
            continue
        if any(not isinstance(c, dict) for c in choices):
            errors.append(f"{qid}: all choices must be objects")
            continue
        ids = [c.get("id") for c in choices]
        if ids != list(LETTERS):
            errors.append(f"{qid}: printed choice IDs must be A, B, C, D in order")
        if any(not isinstance(c.get("text"), str) or not c["text"].strip() for c in choices):
            errors.append(f"{qid}: every choice needs nonempty text")
        correct = question.get("correct_choice_id")
        if correct not in LETTERS:
            errors.append(f"{qid}: correct_choice_id must be A/B/C/D")
        else:
            letters.append(correct)
        families: set[str] = set()
        for choice in choices:
            if choice.get("id") == correct:
                continue
            cid = choice.get("id", "?")
            trap = choice.get("trap_type")
            if trap not in TRAP_FAMILIES:
                errors.append(f"{qid}/{cid}: recognized distractor trap_type required")
            else:
                family = TRAP_FAMILIES[trap]
                families.add(family)
                observed_families.add(family)
            for field in ("misconception", "elimination_evidence"):
                if not isinstance(choice.get(field), str) or not choice[field].strip():
                    errors.append(f"{qid}/{cid}: {field} required")
        if len(families) < 2:
            errors.append(f"{qid}: distractors must span at least 2 reasoning families")

        if require_independent_review:
            review = question.get("review")
            if not isinstance(review, dict):
                errors.append(f"{qid}: independent semantic review required")
                continue
            author, reviewer = question.get("author_id"), review.get("reviewer_id")
            if not author or not reviewer or author == reviewer:
                errors.append(f"{qid}: reviewer_id must differ from author_id")
            if review.get("status") != "approved":
                errors.append(f"{qid}: independent reviewer approval missing")
            for field in ("unique_answer_checked", "passage_blind_checked",
                          "distractor_quality_checked"):
                if review.get(field) is not True:
                    errors.append(f"{qid}: review.{field} must be true")
            if not isinstance(review.get("correct_answer_evidence"), str) or not review["correct_answer_evidence"].strip():
                errors.append(f"{qid}: review.correct_answer_evidence required")
    if len(set(question_ids)) != len(question_ids):
        errors.append("duplicate question IDs")
    frequencies = Counter(letters)
    if letters:
        missing = [letter for letter in LETTERS if frequencies[letter] == 0]
        if missing:
            errors.append(f"correct answer positions missing: {', '.join(missing)}")
        for letter in LETTERS:
            if frequencies[letter] > max_per_letter:
                errors.append(f"answer position {letter} appears {frequencies[letter]} times (max {max_per_letter})")
        run = 1
        for index in range(1, len(letters)):
            run = run + 1 if letters[index] == letters[index - 1] else 1
            if run == max_run + 1:
                errors.append(f"answer sequence contains >{max_run} consecutive {letters[index]} choices")
        if len(letters) >= 8 and len(set(letters[:4])) == 4 and all(
            letter == letters[i % 4] for i, letter in enumerate(letters)
        ):
            errors.append("predictable repeating four-choice cycle")
    if len(questions) >= minimum and len(observed_families) < 3:
        errors.append("passage needs scope, precision AND transformation distractor families")

    if "answer_key" in bank:
        answer_key = bank["answer_key"]
        if not isinstance(answer_key, list):
            errors.append("answer_key must be a list")
        else:
            expected = [(q.get("id"), q.get("correct_choice_id"))
                        for q in questions if isinstance(q, dict)]
            actual = [(a.get("question_id"), a.get("correct_choice_id"))
                      for a in answer_key if isinstance(a, dict)]
            if actual != expected:
                errors.append("answer_key must match exact selected question IDs, order and correct answers")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bank", type=Path, help="JSON file containing one passage's questions")
    parser.add_argument("--min-questions", type=int, default=8)
    parser.add_argument("--max-questions", type=int, default=10)
    parser.add_argument("--max-per-letter", type=int, default=4)
    parser.add_argument("--max-run", type=int, default=2)
    arguments = parser.parse_args()
    bank = json.loads(arguments.bank.read_text(encoding="utf-8"))
    errors = validate_bank(bank, minimum=arguments.min_questions,
                           maximum=arguments.max_questions,
                           max_per_letter=arguments.max_per_letter,
                           max_run=arguments.max_run)
    for error in errors:
        print("FAIL:", error)
    if errors:
        print(f"Assessment quality gate BLOCKED: {len(errors)} finding(s)")
        return 1
    print("Assessment structural gate PASS — independent semantic approval recorded; not independently proven by this tool")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
