# 🧪 Module 06 – Practice Exercises: Continual Training

These exercises will help you apply continual learning patterns to iteratively improve your fine-tuned LLM.

---

## ✅ Exercise 1: Extract Hallucination Failures

* Open `logs/hallucination_eval_results.json`
* Copy 3–5 `hallucinated: true` examples
* Paste into a new file: `data/hallucination_corrections.jsonl`

🎯 Goal: Build your delta dataset

---

## ✅ Exercise 2: Generate Correct Outputs

* For each failure, use ChatGPT to generate a fixed response
* Keep the original prompt as `instruction`
* Store output as the `expected` response

🎯 Goal: Curate high-quality training fixes

---

## ✅ Exercise 3: Retrain with the Delta

* Use `train_model.ipynb`
* Replace dataset path with `hallucination_corrections.jsonl`
* Run 1–2 epochs only
* Save as `checkpoints/model_v1.1`

🎯 Goal: See whether small patch training works

---

## ✅ Exercise 4: Compare Model Outputs

* Load both `model_v1.0` and `model_v1.1`
* Run same test prompts
* Log differences in accuracy, hallucination rate

🎯 Goal: Gain insight into model improvement patterns

---

## ✅ Exercise 5: Maintain Version Log

* Create a new file: `logs/version_changelog.json`
* Add a record of each model, date, training data summary
* Bonus: Log eval stats (e.g. hallucination rate, top failure types)

🎯 Goal: Establish a reproducible improvement pipeline
