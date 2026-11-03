"""Positive and deliberate negative fixtures for 016 / 017."""
import copy
import unittest

from mts_factory.assessment.mcq_quality import validate_bank


TRAPS = [
    ("too-broad", "extends source claim beyond its scope"),
    ("too-specific", "adds a detail source does not establish"),
    ("over-modified", "changes the original causal or rhetorical meaning"),
]


def fixture(answers="CABDCBADAC"):
    questions = []
    for i, correct in enumerate(answers, 1):
        choices = []
        wrong = iter(TRAPS)
        for label in "ABCD":
            if label == correct:
                choices.append({"id": label, "text": "supported answer"})
            else:
                trap, misconception = next(wrong)
                choices.append({
                    "id": label, "text": f"plausible alternative {label}",
                    "trap_type": trap,
                    "misconception": misconception,
                    "elimination_evidence": "Source paragraph/stanza evidence rules this out",
                })
        questions.append({
            "id": f"Q{i:02d}", "author_id": "author-a",
            "correct_choice_id": correct,
            "choices": choices,
            "review": {
                "reviewer_id": "reviewer-b",
                "status": "approved",
                "unique_answer_checked": True,
                "passage_blind_checked": True,
                "distractor_quality_checked": True,
                "correct_answer_evidence": "Quoted source evidence for this question",
            },
        })
    return {
        "passage_id": "POEM-01",
        "questions": questions,
        "answer_key": [
            {"question_id": q["id"], "correct_choice_id": q["correct_choice_id"]}
            for q in questions
        ],
    }


class TestMcqQuality(unittest.TestCase):
    def test_balanced_with_reviewer_and_matching_key_passes(self):
        self.assertEqual(validate_bank(fixture()), [])

    def test_psalm_like_nine_A_rejected(self):
        errors = validate_bank(fixture("AABAAAAAAA"))
        self.assertTrue(any("appears 9 times" in e for e in errors), errors)

    def test_triple_run_rejected(self):
        errors = validate_bank(fixture("AAABCDABCD"))
        self.assertTrue(any("consecutive" in e for e in errors), errors)

    def test_four_letter_cycle_rejected(self):
        errors = validate_bank(fixture("ABCDABCDAB"))
        self.assertTrue(any("cycle" in e for e in errors), errors)

    def test_missing_distractor_misconception_rejected(self):
        bank = fixture()
        bank["questions"][0]["choices"][1]["misconception"] = ""
        self.assertTrue(any("misconception required" in e for e in validate_bank(bank)))

    def test_repeated_trap_family_rejected(self):
        bank = fixture()
        for c in bank["questions"][0]["choices"]:
            if c["id"] != bank["questions"][0]["correct_choice_id"]:
                c["trap_type"] = "too-broad"
        self.assertTrue(any("at least 2" in e for e in validate_bank(bank)))

    def test_semantic_review_missing_rejected(self):
        bank = fixture()
        del bank["questions"][1]["review"]
        self.assertTrue(any("semantic review required" in e for e in validate_bank(bank)))

    def test_review_by_author_rejected(self):
        bank = fixture()
        bank["questions"][0]["review"]["reviewer_id"] = "author-a"
        self.assertTrue(any("must differ" in e for e in validate_bank(bank)))

    def test_review_flags_must_be_true(self):
        bank = fixture()
        bank["questions"][0]["review"]["unique_answer_checked"] = False
        self.assertTrue(any("unique_answer_checked" in e for e in validate_bank(bank)))

    def test_stale_answer_key_rejected_after_reordering(self):
        bank = fixture()
        bank["questions"][0]["correct_choice_id"] = "B"
        self.assertTrue(any("answer_key must match" in e for e in validate_bank(bank)))

    def test_missing_letter_rejected_per_passage(self):
        errors = validate_bank(fixture("AABBAABBAA"))
        self.assertTrue(any("positions missing" in e for e in errors))

    def test_choice_count_rejected(self):
        bank = fixture()
        bank["questions"][0]["choices"].pop()
        self.assertTrue(any("exactly 4" in e for e in validate_bank(bank)))

    def test_duplicate_question_id_rejected(self):
        bank = fixture()
        bank["questions"][1]["id"] = bank["questions"][0]["id"]
        self.assertTrue(any("duplicate question IDs" in e for e in validate_bank(bank)))


if __name__ == "__main__":
    unittest.main()
