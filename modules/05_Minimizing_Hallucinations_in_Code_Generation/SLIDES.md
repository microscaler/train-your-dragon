# 🎓 Slide Deck: Module 05 – Minimizing Hallucinations in Code Generation

---

## Slide 1: Welcome to Module 05

**Title:** How to Reduce Hallucination in Code-Generating LLMs

> Note: Hallucination is a top reason models fail in production—this module helps learners detect and prevent it.

---

## Slide 2: What Is Hallucination?

* When an LLM generates false or unverifiable output
* In code, this can mean:

  * Calling APIs that don’t exist
  * Inventing syntax
  * Fabricating doc references

> Note: Hallucinations are high-confidence errors—students must learn to spot them.

---

## Slide 3: Why It Happens

* LLMs are **probability machines**, not databases
* Trained to **complete**, not **fact-check**
* Long-tail code examples may be rare or unseen

> Note: You can’t “delete” hallucination, but you can reduce and steer it.

---

## Slide 4: Code-Specific Hallucinations

Examples:

* `client.connect()` (API doesn't exist)
* `print await()` (bad syntax)
* `# coroutine_tag` (fabricated attribute)

> Note: Use examples from real model outputs or student projects.

---

## Slide 5: Prompt Design Matters

* Add constraints: “Only use standard library”
* Use system prompts to set scope
* Try Chain-of-Thought: “First explain, then code”

> Note: Prompting is your first line of defense.

---

## Slide 6: Evaluation by Human or Heuristic

| Method        | Pros                 | Cons                    |
| ------------- | -------------------- | ----------------------- |
| Human review  | Highest accuracy     | Time-consuming          |
| Regex checker | Fast for simple bugs | Not semantically rich   |
| AST diff      | Structure-aware      | May miss logical errors |

> Note: Choose depending on your budget and audience.

---

## Slide 7: Visualizing Hallucination

* Use bar charts to compare:

  * ✅ Accurate
  * ⚠️ Partial / questionable
  * ❌ Hallucinated
* Repeat tests across model versions

> Note: Encourage students to treat this like a regression dashboard.

---

## Slide 8: Lab – Track Hallucination Rate

Task:

1. Run your model on 10 prompt cases
2. Categorize each result
3. Count and plot results

Bonus:

* Add `pass@k` support
* Log changes across checkpoints

example:

```json
{ "hallucinated": True, "reason": "Incorrect API call to nonexistent function" }
```
and
```json
{
  "instruction": "Use `aiofiles` to open a file in Python",
  "output": "...",
  "hallucinated": true,
  "reason": "The method `aiofiles.open_sync()` does not exist"
}

```
---

## Slide 9: What Doesn’t Work

* Asking the model “are you sure?”
* Blind trust in output format
* Ignoring low-confidence answers

> Note: Teach students to verify outputs and write tests if possible.

---

## Slide 10: Coming Up Next…

**Module 06: Continual Training & Iterative Improvement**

* How to teach your model new lessons over time
* Use feedback to improve accuracy and alignment

> Note: This transition introduces the “feedback loop” idea—model improvement isn’t a one-shot process.


4596 6101 2372 3171
02/29
955