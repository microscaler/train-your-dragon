# 🎓 Slide Deck: Module 07 – Evaluation & Alignment

---

## Slide 1: Welcome to Module 07

**Title:** Evaluating Your Model Beyond Just Loss

> Note: Most LLMs are deployed without rigorous evaluation. This module teaches repeatable, testable methods.

---

## Slide 2: Why Evaluate?

* You can’t improve what you can’t measure
* Avoid regressions during fine-tuning
* Track hallucination, accuracy, preference, and alignment

---

## Slide 3: Types of Evaluation

| Metric        | What It Measures             | Useful When              |
| ------------- | ---------------------------- | ------------------------ |
| Accuracy      | Exact/correct match          | Known outputs available  |
| pass\@k       | Diversity of correct guesses | Sampling is used         |
| Hallucination | Rate of confident wrongs     | Open-ended generations   |
| Preference    | Human-like ranking           | Multiple outputs present |

---

## Slide 4: Creating a Test Set

* 10–50 prompts
* Include:

  * Known API calls
  * Language features
  * Formatting patterns
* Store in `data/eval_cases.jsonl`

> Note: Start small. Grow over time.

---

## Slide 5: Running an Evaluation

* Use notebook: `evaluate_model.ipynb` or `hallucination_eval.ipynb`
* Score:

  * ✅ Exact match
  * ⚠️ Partial match
  * ❌ Incorrect or hallucinated
* Log per example + summary rate

---

## Slide 6: Tracking Model Versions

* Use model folders: `checkpoints/model_v1.0`, `model_v1.1`
* Run same test prompts across models
* Record:

  * Which improved
  * Which regressed
  * Notes on deltas

---

## Slide 7: Log Your Results

Create `logs/eval_log.json` with:

* Model name
* Date
* Accuracy %, hallucination rate
* Notes or config diffs

> Note: Treat eval like unit tests for LLMs

---

## Slide 8: Visualizing Evaluation

* Use bar or line charts to show progress
* Chart: Accuracy %, hallucination %, per model
* Tools:

  * Matplotlib
  * WandB
  * CSV → Google Sheets

---

## Slide 9: Lab Preview – Compare v1.0 to v1.1

Task:

* Run same prompts on both checkpoints
* Log which model performs better
* Count ✅, ⚠️, ❌ responses

> Note: A model isn’t better unless it passes more tests

---

## Slide 10: Coming Up Next…

**Module 08: Retrieval-Augmented Generation (RAG)**

* Teach your model how to fetch facts instead of hallucinating them
* Build a search-backed chat assistant
