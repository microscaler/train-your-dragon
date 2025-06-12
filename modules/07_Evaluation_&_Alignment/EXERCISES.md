# 🧪 Module 07 – Practice Exercises: Evaluation & Alignment

These exercises help you create structured test cases and benchmark model quality over time.

---

## ✅ Exercise 1: Create an Evaluation Test Set

* Open a new file `data/eval_cases.jsonl`
* Add 5–10 prompts where you know the correct output
* Include one each of:

  * API usage
  * Language edge case
  * Error handling pattern

🎯 Goal: Build a reliable test harness

---

## ✅ Exercise 2: Score a Single Checkpoint

* Run `evaluate_model.ipynb` using your latest model
* Score outputs as ✅, ⚠️, ❌
* Log result counts in a small summary table

🎯 Goal: Quantify your model’s strengths and gaps

---

## ✅ Exercise 3: Compare Two Models

* Run the same prompts on `model_v1.0` and `model_v1.1`
* Score both side-by-side in a spreadsheet or table
* Identify where one is stronger or worse

🎯 Goal: Detect regressions before shipping updates

---

## ✅ Exercise 4: Visualize Accuracy Trends

* Convert scores into numeric values (e.g. ✅ = 1, ❌ = 0)
* Track over 2–3 model versions
* Plot a line chart to show progress

🎯 Goal: Make improvement (or drift) visible

---

## ✅ Exercise 5: Save Eval History

* Create `logs/eval_log.json`
* Append one record per eval run:

  ```json
  {
    "checkpoint": "model_v1.1",
    "accuracy": 0.82,
    "hallucination_rate": 0.14,
    "eval_date": "2024-06-01"
  }
  ```

🎯 Goal: Maintain reproducible evaluation lineage
