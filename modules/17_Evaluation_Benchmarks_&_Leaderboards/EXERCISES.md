# 🧪 Module 15 – Practice Exercises: Evaluation Benchmarks & Leaderboards

Hands-on exercises to help you design, run, and track meaningful model evaluations.

---

## ✅ Exercise 1: Build a Custom Eval Prompt

* Write 3–5 function stubs:

  * `def double(x):` or `def format_date(str):`
* For each:

  * Create 2+ hidden test cases
  * Save as `.py` test file or inline asserts

🎯 Goal: Scaffold your own HumanEval-like set

---

## ✅ Exercise 2: Score Sample Completions

* Generate 3 different outputs for one prompt
* Evaluate using:

  * Exact match
  * Edit distance (Levenshtein)
  * AST compilation check
* Record score: pass/fail or percentage match

🎯 Goal: Practice multi-metric evaluation

---

## ✅ Exercise 3: Log Evaluation Results

* Store completion logs in `results.jsonl`:

```json
{"prompt": "def add(x, y):", "completion": "return x + y", "score": 1.0, "method": "exact"}
```

* Include timestamp and model version
* Save summary stats to `leaderboard.csv`

🎯 Goal: Make scores persistent and traceable

---

## ✅ Exercise 4: CI Eval Simulation

* Write a script that:

  * Loads test prompts
  * Loads candidate completions
  * Scores completions
  * Fails job if below threshold

🎯 Goal: Prepare for weekly model evaluation in CI

---

## ✅ Exercise 5: Visualize Score Trends

* Create a leaderboard with 3+ model checkpoints
* Plot score over time
* Compare across:

  * Prompt sets
  * Metrics
  * Config changes

🎯 Goal: Spot regressions and improvements at a glance
