# 🎓 Slide Deck: Module 17 – Evaluation Benchmarks & Leaderboards

---

## Slide 1: Welcome to Module 15

**Title:** Measuring What Matters: LLM Evaluation

> Note: If you can't track it, you can't trust it.

---

## Slide 2: Why Model Evaluation Matters

* Evaluation lets us:

  * Compare checkpoints
  * Validate fixes
  * Catch regressions
  * Report improvements

---

## Slide 3: Common Evaluation Metrics

| Metric        | Use Case                    |
| ------------- | --------------------------- |
| Exact Match   | Question answering, doc gen |
| Pass\@k       | Code generation             |
| Edit Distance | Reasoning accuracy          |
| AST Match     | Code correctness            |

---

## Slide 4: What Is HumanEval?

* A benchmark of coding prompts
* Each has:

  * Function stub
  * Hidden test cases
* Model must generate valid function body

---

## Slide 5: Build Your Own Test Harness

* Create prompt: `def add(x, y):`
* Provide:

  * Test case: `assert add(2, 3) == 5`
* Execute safely:

  * `exec()` sandbox
  * Timeout protection

---

## Slide 6: Leaderboard Design

| Model    | Score | Date       | Notes      |
| -------- | ----- | ---------- | ---------- |
| llama-7b | 84.2  | 2025-06-01 | no dropout |
| deepseek | 88.0  | 2025-06-03 | retrained  |

* Log as CSV, JSONL, or SQL
* Track eval dataset + method

---

## Slide 7: CI Integration Tips

* Add job to CI:

  * Run test suite with model
  * Write metrics to `results.json`
  * Fail if metrics < threshold
* Schedule weekly checkpoint tests

---

## Slide 8: Visualization Ideas

* Line chart of score over time
* Bar chart of models per test set
* Histogram of pass/fail count

---

## Slide 9: Lab – Evaluation & Log Tracker

* Evaluate 3 completions
* Score with:

  * Exact match
  * Edit distance
  * AST compile check
* Log summary to `leaderboard.csv`

---

## Slide 10: Coming Up Next…

**Module 16: LLMOps & Model Lifecycle**

* Versioning
* Promotion
* Audit and rollback
