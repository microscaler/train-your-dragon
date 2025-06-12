# 📊 Module 07: Evaluation & Alignment

This module teaches you how to design evaluation workflows that measure your model’s accuracy, usefulness, and alignment with your goals.

---

## 🎯 Objectives

By the end of this module, you will:

* Understand how to evaluate LLM performance beyond loss
* Define evaluation cases and test sets
* Measure accuracy, pass\@k, and hallucination rates
* Track model regressions and improvements across versions

---

## ✅ Skills Gained

* Creating prompt-based test sets
* Using `pass@k` and manual correctness scoring
* Visualizing model accuracy over time
* Comparing model outputs across checkpoints

---

## 🗂️ Activities

### 1. Define Evaluation Cases

* Create a small set of prompts with known-good outputs
* Store in `data/eval_cases.jsonl`
* Include a variety of topics: coroutines, API usage, CLI tools, doc generation

### 2. Run Structured Evaluations

* Use `evaluate_model.ipynb` or `hallucination_eval.ipynb`
* Measure:

  * Exact match
  * Substring match
  * `pass@k` rate (if sampling)

### 3. Compare Versions

* Load two model checkpoints (e.g. `v1.0` and `v1.1`)
* Run evals with same prompts
* Log differences using a comparison tool or table

### 4. Record Trends

* Create or update a `logs/eval_log.json` file
* Track: checkpoint name, eval date, accuracy, hallucination rate, notes

---

## 🧪 Lab: Accuracy & Alignment Tracker

1. Define 10 core eval prompts with known outputs
2. Run on latest model checkpoint
3. Score:

* ✅ Exact match
* ⚠️ Partial / related
* ❌ Incorrect or hallucinated

4. Log in a CSV or JSON format
5. Repeat after each retraining cycle

Bonus:

* Visualize pass/fail chart with matplotlib
* Add `wandb` tracking for long-term trends

---

## 🔗 Linked Modules

* [Module 05: Hallucination](../05_Minimizing_Hallucinations_in_Code_Generation/README.md)
* [Module 06: Continual Training](../06_Continual_Training_&_Iterative_Improvement/README.md)
* [Module 16: LLMOps](../18_LLMOps_&_Model_Lifecycle_Management/README.md)

---

## ✅ Completion Checklist

* [ ] I created a reusable set of test prompts
* [ ] I measured outputs with accuracy and alignment metrics
* [ ] I tracked evaluation results over time
* [ ] I compared two model checkpoints on the same evals
* [ ] I feel confident in making model-vs-model comparisons
