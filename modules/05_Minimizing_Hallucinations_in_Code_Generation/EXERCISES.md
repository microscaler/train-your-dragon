# 🧪 Module 05 – Practice Exercises: Minimizing Hallucinations

These exercises help you learn how to identify and reduce hallucinations in code-focused LLMs.

---

## ✅ Exercise 1: Review Known Hallucination Patterns

* Open `data/hallucination_cases.jsonl`
* Categorize each example:

  * API misuse
  * Nonexistent method/class
  * Fabricated syntax
* Add 2 of your own based on experience

🎯 Goal: Build awareness of common hallucination modes

---

## ✅ Exercise 2: Prompt Rewriting

* Take 3 vague prompts like:

  * “Write a script to upload a file”
  * “Make this better”
  * “Use a queue”
* Rewrite them with grounding:

  * Add language (e.g., Python)
  * Limit scope (e.g., use asyncio)
  * Mention expected libraries

🎯 Goal: Practice prompt design to steer generation

---

## ✅ Exercise 3: Evaluate a Real Model Response

* Run your model with one of the hallucination test prompts
* Manually inspect whether the output is:

  * Valid and executable
  * Based on a real API/method
* Label and log your result as ✅, ⚠️, or ❌

🎯 Goal: Gain hands-on exposure to real model behavior

---

## ✅ Exercise 4: Add Hallucination Detection to Eval Loop

* In `evaluate_model.ipynb`, add a `"hallucinated"` field to each result
* Use manual judgment, or keyword heuristics to flag incorrect tokens
* Optional: generate a bar chart of accuracy categories

🎯 Goal: Make hallucination measurable and actionable

---

## ✅ Exercise 5: Create a Hallucination Test Suite

* Define 5 prompts where the correct answer is known
* Save them as `hallucination_eval.jsonl`
* Use `hallucination_check.py` to evaluate your model

🎯 Goal: Create a reusable testbed for API-version hallucination
