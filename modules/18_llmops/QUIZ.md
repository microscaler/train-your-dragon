# 🧪 Module 16 Quiz: LLMOps & Lifecycle

Evaluate your knowledge of model versioning, regression checks, and audit processes.

---

### ✅ Instructions

Choose the best answer per question. Reflect on how you’d use this in your project.

---

### 1. What should a model version directory include?

A. Only the checkpoint file
B. A checkpoint, metadata, and evaluation results
C. Python scripts only
D. Token counts only

**Correct Answer:** B

---

### 2. Why store `eval.json` with your model?

A. To save GPU logs
B. To compare performance with past versions
C. To count tokens only
D. To store prompt length

**Correct Answer:** B

---

### 3. What is a safe practice for promoting a model to production?

A. Merge every new checkpoint immediately
B. Require evaluation and score comparison before promotion
C. Pick the one with largest file size
D. Only use float16 models

**Correct Answer:** B

---

### 4. What should a prompt registry track?

A. Prompt author and change rationale
B. GPU used to generate it
C. HTML formatting
D. Token position

**Correct Answer:** A

---

### 5. Reflection:

> Describe a real-world scenario where model rollback is important. How would your logs and files help you recover?
