# 🧪 Module 14 – Practice Exercises: Tool Use & Multi-Agent Systems

Explore how to build robust LLM-based systems that call tools, delegate tasks, and verify results.

---

## ✅ Exercise 1: Define a Function-Calling Task

* Write a task for an assistant agent to solve:

  * e.g. "Get current weather for Tokyo and suggest clothes"
* Define 2–3 tool APIs:

  * `weather(city) -> {temp, rain}`
  * `suggest_clothes(temp, rain)`
* Write one-shot prompt to describe how agent should plan

🎯 Goal: Design a basic tool-calling setup

---

## ✅ Exercise 2: Simulate Agent Turn Sequence

* Create a list of dicts like:

```python
history = [
  {"role": "planner", "message": "Need weather → clothes"},
  {"role": "executor", "tool": "weather(Tokyo)", "output": "22C, rain"},
  {"role": "presenter", "message": "Bring umbrella, wear light jacket"}
]
```

* Replay and extend to 5–7 turns

🎯 Goal: Practice chaining reasoning with memory

---

## ✅ Exercise 3: Add Verification Layer

* Write a `validate_output()` step between executor and presenter
* Validate against:

  * expected keys or units
  * absurd values
* Return pass/fail and escalate if fail

🎯 Goal: Insert guardrails into tool-use loop

---

## ✅ Exercise 4: Extend to Multi-Agent Roleplay

* Assign planner, researcher, presenter to classmates or personas
* Task: "Find 3 affordable laptops for coding in 2025"
* Researcher finds specs, presenter composes message, planner checks constraints

🎯 Goal: Experience multi-agent collaboration + logging

---

## ✅ Exercise 5: Tool Replay Debugging

* Store a simulated `turn_log = [dict(role, tool, input, output)]`
* Write a replay function to re-run only failed turns with mock or live data
* Log success/failure delta

🎯 Goal: Enable diagnostic and partial rollback flows
