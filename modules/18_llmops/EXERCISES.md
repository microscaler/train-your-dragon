# 🧪 Module 16 – Practice Exercises: LLMOps & Lifecycle Management

Solidify your model versioning, audit tracking, and reproducibility workflows.

---

## ✅ Exercise 1: Version a Model Output Directory

* Create a folder `models/model_v1.0/`
* Add:

  * `checkpoint.bin` (mock or real)
  * `eval.json` with dummy metrics
  * `README.md` or `model_card.json`

🎯 Goal: Start artifact tracking and structure

---

## ✅ Exercise 2: Git-Backed Prompt Registry

* Add `prompts/` directory under version control
* Each prompt = file with:

  * Author name
  * Reason for test case
  * Use case tag
* Commit 3–5 prompts with metadata

🎯 Goal: Enable changelog and review of test sets

---

## ✅ Exercise 3: Run and Compare Eval Sets

* Use your eval harness to score `model_v1.0`
* Save output as `eval.json`
* Clone dir → `model_v1.1/` and make 1 change
* Re-run and compare `eval.json` to check delta

🎯 Goal: Detect regressions and differences

---

## ✅ Exercise 4: Automate Score Check in CI

* Add script `check_eval_threshold.py`
* Load `eval.json`
* Compare against stored `best_score.json`
* Fail job if accuracy drops >1%

🎯 Goal: Enforce promotion gating

---

## ✅ Exercise 5: Reproducibility Test

* Restore same tokenizer, prompt set, and config
* Run identical model (or dummy code)
* Ensure results match or explain delta
* Log in `repro_report.md`

🎯 Goal: Build habits of audit and re-run discipline
