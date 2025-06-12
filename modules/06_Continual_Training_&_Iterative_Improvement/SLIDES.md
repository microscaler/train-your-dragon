# 🎓 Slide Deck: Module 06 – Continual Training & Iterative Improvement

---

## Slide 1: Welcome to Module 06

**Title:** Improving Your Model Over Time

> Note: This module connects evaluation to training—learners will iterate for the first time.

---

## Slide 2: What Is Continual Learning?

* Training an existing model on new, relevant examples
* Keeps the model current without full retraining
* Used to:

  * Fix mistakes (hallucination corrections)
  * Teach new behavior (API version updates)
  * Improve weak areas (e.g. coroutines, doc generation)

---

## Slide 3: The Feedback Loop

* Input → Model → Output → Error → Correction → Retrain
* Data from:

  * Human review
  * Eval logs
  * User complaints

> Note: Highlight that small patches can drive large impact.

---

## Slide 4: Delta Training

* Delta = new or corrected examples only
* Merge or append to base dataset
* Retrain on:

  * Just the delta
  * Or base + delta (light epoch)

---

## Slide 5: Example Correction Cycle

1. Run hallucination eval
2. Extract all ❌ errors
3. Fix them manually or with GPT
4. Add to `delta.jsonl`
5. Fine-tune for 1–2 epochs
6. Rerun eval

---

## Slide 6: Common Use Cases

* Domain-specific improvements
* Version-aware completions
* Fixing tool-using errors (e.g. broken shell commands)

---

## Slide 7: Lab Preview – Fix & Retrain

**Goal:** Improve your model using just 10 curated error fixes

* Build `hallucination_corrections.jsonl`
* Append or isolate as delta
* Fine-tune again
* Compare outputs (before/after)

---

## Slide 8: Pitfalls to Avoid

* Forgetting: fine-tuning too much on narrow data
* Drift: model becomes biased toward recent patches
* Overfitting: memorizing corrections without generalizing

---

## Slide 9: Best Practices

* Use versioned checkpoints (`v1.0`, `v1.1`, etc.)
* Keep correction logs with sources
* Re-evaluate regularly using test harnesses

---

## Slide 10: Coming Up Next…

**Module 07: Evaluation & Alignment**

* How to design formal test suites
* Track model accuracy, preference, and consistency

> Note: Transition from manual to formalized, reproducible scoring.
