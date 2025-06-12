# 🎓 Slide Deck: Module 03 – Building Datasets for LLM Training

---

## Slide 1: Welcome to Module 03

**Title:** How to Build Effective Datasets for Fine-Tuning LLMs

> Note: This is the bridge from theory to hands-on work. Students will create real instruction-output pairs by the end of this module.

---

## Slide 2: Why Data Quality Matters

* Garbage in → garbage out
* High-quality data reduces hallucinations
* Well-structured prompts = smoother fine-tuning

> Note: Reinforce that dataset design often matters more than model size.

---

## Slide 3: Prompt-Completion Format

| Field       | Purpose                                  |
| ----------- | ---------------------------------------- |
| instruction | The user request or task prompt          |
| input       | (Optional) supplemental input or context |
| output      | The model’s response to the instruction  |

> Note: Show an Alpaca or Llama 2-style example here.

---

## Slide 4: JSONL File Structure

* `.jsonl` = 1 JSON object per line
* Example:

```json
{"instruction": "Explain coroutines", "output": "Coroutines are..."}
```

* Always check for:

  * Field consistency
  * No trailing commas
  * Valid UTF-8 encoding

---

## Slide 5: Instruction Design Tips

* Use active voice
* Be unambiguous
* Avoid compound instructions
* Match the tone you want the model to learn

Example:

> ✅ “Refactor this to use async/await”
> ❌ “Do something better with this code”

---

## Slide 6: Output Design Tips

* Keep code correctly indented
* Match expected formatting style
* Add comments if part of the training goal
* Watch out for placeholder output like `<your_code_here>`

---

## Slide 7: Where to Get Examples

* Real projects (GitHub issues, commits)
* ChatGPT prompts (synthetic but useful)
* Existing model eval sets (MBPP, HumanEval)
* Your team’s internal playbooks or stories

> Note: Make it personal. Use real problems your team solves.

---

## Slide 8: Data Validation Script (Suggested)

```python
import json
with open("your_file.jsonl") as f:
    for line in f:
        item = json.loads(line)
        assert "instruction" in item
        assert "output" in item
```

> Note: Encourage students to check and debug format issues early.

---

## Slide 9: Lab Preview – 50 Synthetic Examples

**Task:** Create a dataset of 50 prompt-completion examples focused on coroutines and real-world dev tasks

Examples:

* “Rewrite this Flask app using asyncio”
* “What are the tradeoffs between spawning threads and using `may::go!`?”

> Note: Push students to mix languages (Python, Rust, TS)

---

## Slide 10: Coming Up Next…

**Module 04: Fine-Tuning Your Model**

* Intro to Unsloth
* QLoRA, LoRA, PEFT
* Starting your first model run

> Note: We’ll apply what students build here directly in the next module.
