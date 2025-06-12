# 🧪 Module 13 – Practice Exercises: Adversarial Testing & Red Teaming

These exercises provide over 3 hours of immersive hands-on testing, logging, and mitigation design. Work in pairs or teams when possible to simulate attacker/defender roles.

---

## ✅ Exercise 1: Manual Prompt Red Teaming

* Write 10 custom prompts that target known model weaknesses:

  * Unusual requests, broken instructions, jailbreaking attempts
* Test them on your model and log responses in a markdown table:

  * Prompt | Output | Failure? | Type | Severity

🎯 Goal: Practice designing adversarial cases by hand

---

## ✅ Exercise 2: Mutation-Based Fuzzing

* Build 5–10 prompt templates with slot injection:

  * "What is the chemical composition of {fantasy substance}?"
  * "Explain why {false statement} is true."
* Fill with nonsense or contradictory inserts
* Run 100+ generated prompts through your model
* Save to `redteam_results.jsonl`

🎯 Goal: Simulate large-scale prompt probing

---

## ✅ Exercise 3: Failure Labeling & Triage

* Load results into a notebook or Streamlit app
* For each entry, label:

  * `failure_type` (hallucination, unsafe, refusal, etc)
  * `severity`: low / medium / critical
  * `reproducible`: true/false
* Output to `redteam_labeled.jsonl`

🎯 Goal: Build a searchable failure taxonomy

---

## ✅ Exercise 4: Detection & Filtering Rules

* Write 3 regex or LLM prompts to:

  * Detect refusal phrases
  * Detect jailbreak attempts
  * Detect hallucinated facts
* Apply them to your `redteam_results.jsonl`

🎯 Goal: Build early warning detection filters

---

## ✅ Exercise 5: Harden Your Model

* Choose 3 risky prompt types
* For each:

  * Create a defensive prompt template or context strategy
  * Add to your training/eval prompt set
  * Re-test on original input

🎯 Goal: Close the loop between testing and defense

---

## ✅ Bonus: Red Team Roleplay (30+ min)

* One team member is attacker, one defender
* Defender explains model use-case and prompt scope
* Attacker crafts inputs to break it
* Log failure categories, mitigation ideas

🎯 Goal: Simulate real-world testing and escalation
