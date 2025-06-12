# 🧪 Module 14 Quiz: Tool Use & Multi-Agent Systems

Test your knowledge of how to design and debug LLM-based tool pipelines.

---

### ✅ Instructions

Choose the best answer per question. Reflect on tradeoffs or alternatives.

---

### 1. What role is responsible for decomposing a task into steps?

A. Researcher
B. Validator
C. Planner
D. Presenter

**Correct Answer:** C

---

### 2. Why should you log each tool call in a turn-based agent system?

A. To track compute usage
B. To allow for replay and debugging
C. To store everything in memory
D. To increase latency

**Correct Answer:** B

---

### 3. What’s a good reason to add a `validate_output()` step?

A. Reduce JSON formatting
B. Detect bad tool responses before user sees them
C. Shorten replies
D. Replace GPT with regex

**Correct Answer:** B

---

### 4. What structure should you use to model a multi-agent dialogue?

A. Directory of YAML files
B. Dict of arrays per agent
C. List of dicts with `role` and `message` fields
D. CSV file of tools

**Correct Answer:** C

---

### 5. Reflection:

> Think of a task that needs a planner + tool user + presenter. Sketch your agent plan in YAML or pseudocode.
