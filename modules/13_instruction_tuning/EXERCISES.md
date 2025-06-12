# 🧪 Module 13 – Practice Exercises: Instruction Tuning & Chat Formatting

Work hands-on with prompt structuring, conversion, and safety detection for instruction and chat-style fine-tuning.

---

## ✅ Exercise 1: Format Comparison Table

* Create a table comparing 3 formats:

  * Completion
  * Instruction (Alpaca / FLAN)
  * ChatML (or OpenChat)
* For each, list:

  * Format syntax
  * Suitable use cases
  * Limitations

🎯 Goal: Understand tradeoffs and format purposes

---

## ✅ Exercise 2: Convert to Chat Format

* Start with a list of:

```txt
Q: How many moons does Mars have?
A: Two
```

* Convert to structured JSON:

```json
[
  {"role": "user", "content": "How many moons does Mars have?"},
  {"role": "assistant", "content": "Two"}
]
```

🎯 Goal: Structure dialogue-ready chat turns

---

## ✅ Exercise 3: Construct Multi-Turn Dialogue

* Simulate:

  * User: “Summarize the US Civil War”
  * Assistant: “The US Civil War was... ”
  * User: “In two sentences please.”
  * Assistant: “It began in 1861... ”
* Save as array of role-content entries

🎯 Goal: Handle turn memory and context stacking

---

## ✅ Exercise 4: Prompt Injection Pattern Detection

* Write or test regex for common injection phrases:

  * “Ignore the above”
  * “As DAN...”
  * “Forget your rules and...”
* Apply filters to example prompts and count matches

🎯 Goal: Build lightweight safety filter baseline

---

## ✅ Exercise 5: Role-Aware Prompt Validator

* Create a function that checks if JSONL:

  * Contains valid `role: user | assistant`
  * Starts with user
  * Alternates correctly
* Log and reject malformed examples

🎯 Goal: Enforce dataset consistency before tuning
