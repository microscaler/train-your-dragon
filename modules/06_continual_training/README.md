# 🔁 Module 06: Continual Training & Iterative Improvement

In this module, you’ll learn how to improve your model over time using feedback loops, delta training, and error-driven dataset expansion.

---

## 🎯 Objectives

By the end of this module, you will:

* Understand what continual learning is and why it matters
* Learn techniques for safely updating an LLM without catastrophic forgetting
* Expand your dataset based on model output errors or coverage gaps
* Train incrementally and evaluate whether performance improves

---

## ✅ Skills Gained

* Building and updating datasets iteratively
* Fine-tuning incrementally on delta datasets
* Capturing feedback signals from human reviews or eval failures
* Running experiments to track regressions vs improvements

---

## 🗂️ Activities

### 1. What Is Continual Training?

* Keeping a model up-to-date by teaching it new concepts without starting over
* Useful for:

  * Company-specific knowledge
  * Fixing hallucination patterns
  * Adapting to new APIs or coding patterns

### 2. Identify Delta Examples

Use logs from `hallucination_eval.ipynb`:

* Extract all `hallucinated: true` cases
* Use ChatGPT or manual editing to generate corrected outputs
* Append to a new file: `data/hallucination_corrections.jsonl`

### 3. Train on Corrections

* Merge your delta file with the original training set
* Fine-tune for 1–2 more epochs on the new combined dataset
* Log loss and accuracy changes

### 4. Evaluate and Compare

* Rerun `hallucination_eval.ipynb`
* Track: Hallucination rate, pass\@k, API misuse reduction

Optional:

* Use model versioning folders (e.g. `v1.0`, `v1.1`) to compare outputs side by side

---

## 🧪 Lab: Build a Feedback Loop

1. Annotate 10 hallucinated responses
2. Correct the answers and tag source error
3. Fine-tune again using only those 10 fixes
4. Compare before/after outputs

Bonus:

* Store all eval diffs in `logs/model_evolution.json`
* Share one interesting before/after case with a teammate

---

## 🔗 Linked Modules

* [Module 05: Hallucinations](../05_hallucination_control/README.md)
* [Module 07: Evaluation](../07_Evaluation_&_Alignment/README.md)
* [Module 16: LLMOps](../18_LLMOps_&_Model_Lifecycle_Management/README.md)

---

## ✅ Completion Checklist

* [ ] I understand what continual learning is
* [ ] I generated a delta dataset
* [ ] I trained on only the delta set
* [ ] I evaluated changes in performance
* [ ] I can explain the value of feedback-driven model improvement
