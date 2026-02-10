# Task Proposals from Codebase Review

## 1) Typo fix task
**Task:** Clean up Markdown formatting typo in `README.md` around the `main.py` section.

- The README currently contains malformed emphasis markers like ``***main.py`` and trailing `***`, which render incorrectly.
- Update the line to use proper inline-code formatting and plain text.

**Why this matters:** Improves readability and professionalism of project documentation.

---

## 2) Bug fix task
**Task:** Fix falsy-value handling in prediction output logic in `main.py`.

- In the CLI section, the code uses `if prediction:` after calling `predict_future(...)`.
- If the model predicts `0.0`, the CLI incorrectly prints "Not enough data to predict." even though a valid prediction exists.
- Change the condition to `if prediction is not None:`.

**Why this matters:** Prevents incorrect user-facing results for valid zero-value predictions.

---

## 3) Code comment/documentation discrepancy task
**Task:** Align README architecture description with the actual implementation.

- The README states that `main.py` *connects* `stat.py` and `ml.py`.
- In reality, `main.py` defines its own stats/ML functions and does not import those modules.
- Update README to reflect the current design, or refactor code so `main.py` actually imports and uses `stat.py` / `ml.py`.

**Why this matters:** Keeps docs trustworthy and reduces onboarding confusion.

---

## 4) Test improvement task
**Task:** Add a regression test for zero-valued predictions and `None` handling in `predict_future`.

- Add tests that verify:
  - `predict_future` returns `None` when fewer than 2 expenses are provided.
  - CLI decision logic treats `0.0` as a valid prediction (after bug fix).
- Include fixtures with deterministic dates/amounts so the model behavior is stable.

**Why this matters:** Prevents recurrence of the truthiness bug and improves confidence in ML output handling.
