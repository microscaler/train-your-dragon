# 🧪 Module 03 Quiz: Building Datasets for LLMs

Test your understanding of prompt design, formatting, and dataset validation.

---

### ✅ Instructions

* Choose the best answer for each multiple-choice question
* Reflect on open-ended questions in your learner journal

---

### 1. Which of the following is a valid `.jsonl` entry for instruction tuning?

```json
A. {"prompt": "Write a function", "output": "def foo(): pass"}
B. {"instruction": "Explain decorators", "output": "A decorator is..."}
C. {"input": "Classify this text", "label": "positive"}
D. {"command": "Generate Python code", "result": "print()"}
```

**Correct Answer:** B

---

### 2. Why is it important to validate a `.jsonl` file before training?

A. To reduce token cost
B. To verify field presence and avoid training crashes
C. To convert to YAML
D. To download new models

**Correct Answer:** B

---

### 3. Which field is optional in the Alpaca-style format?

A. instruction
B. output
C. input
D. completion

**Correct Answer:** C

---

### 4. What’s a good practice when designing outputs?

A. Use `<INSERT CODE>` placeholders
B. Vary field names to avoid repetition
C. Ensure code is syntactically valid and readable
D. Save outputs in a `.docx` file

**Correct Answer:** C

---

### 5. Open Reflection:

> Think of a time when you encountered unclear documentation or a vague bug report. Rewrite it now as a clear `instruction + output` pair.

Write your answer in your journal or share with a teammate.
