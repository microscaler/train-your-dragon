# 📊 Module 17: Evaluation Benchmarks & Leaderboards

This module explores how to objectively evaluate LLM outputs, compare model versions, and create reproducible evaluation pipelines.

---

## 🎯 Objectives

By the end of this module, you will:

* Evaluate models using pass\@k, exact match, edit distance, and AST-based methods
* Build benchmarks using HumanEval-style test suites
* Create a leaderboard that tracks model versions and performance
* Automate scoring in CI pipelines

---

## ✅ Skills Gained

* Metric selection and evaluation harness design
* Test suite creation for code and natural language
* Leaderboard design and regression tracking
* CI-integrated model scoring

---

## 🗂️ Activities

### 1. Choose an Evaluation Strategy

| Metric         | Best For                 |
| -------------- | ------------------------ |
| Pass\@k        | Code generation          |
| Exact match    | Text, QA, doc generation |
| Edit distance  | Step-by-step reasoning   |
| AST comparison | Programming correctness  |

---

### 2. Create a Custom HumanEval Set

* Write 5–10 function stubs with:

  * `def ...(): ...` prompt
  * Hidden test assertions
* Evaluate `exec(model_output)` vs tests
* Score pass/fail for each sample

---

### 3. Build a Leaderboard Tracker

* Track columns:

  * Model name/version
  * Score
  * Eval date
  * Dataset/test set used
* Save to `data/leaderboard.csv` and sort by column

---

### 4. Automate Evaluation in CI

* Add a test runner:

  * Loads model checkpoint
  * Runs benchmark set
  * Dumps metrics to file
* Mark CI job as failed on regression

---

## 🧪 Lab: Model Score Tracker

1. Create 3 fake outputs for one prompt
2. Apply edit distance, exact match, and AST parse check
3. Save results to `results.jsonl`
4. Append summary to leaderboard file

Bonus:

* Generate graphs over time from leaderboard log

---

## 🔗 Linked Modules

* [Module 06: Continual Training](../06_Continual_Training_&_Iterative_Improvement/README.md)
* [Module 12: Scalable Training](../12_Scalable_Training_Infrastructure/README.md)
* [Module 18: LLMOps](../18_LLMOps_&_Model_Lifecycle_Management/README.md)

---

## ✅ Completion Checklist

* [ ] I defined evaluation metrics for my use case
* [ ] I created a custom benchmark test set
* [ ] I scored multiple model outputs consistently
* [ ] I built or updated a leaderboard file
* [ ] I integrated scoring into an automated workflow
