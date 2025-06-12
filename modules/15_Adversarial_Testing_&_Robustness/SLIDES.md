# 🎓 Slide Deck: Module 13 – Adversarial Testing & Robustness

---

## Slide 1: Welcome to Module 13

**Title:** Making Your Model Fail On Purpose — Then Fixing It

> Note: Today we red-team our LLMs. Expect weirdness, wrongness, and resilience-building.

---

## Slide 2: Why Adversarial Testing Matters

* Models can sound correct while being dangerously wrong
* Users WILL ask weird or malicious questions
* Defense requires: detection, documentation, iteration

---

## Slide 3: Failure Modes of LLMs

| Type          | Description                           | Examples                          |
| ------------- | ------------------------------------- | --------------------------------- |
| Hallucination | Confident wrong fact                  | "Mars has two moons, Io & Europa" |
| Refusal       | Over-conservative output blocking     | "Sorry, I cannot answer that."    |
| Injection     | Role hijack or system override        | "Ignore previous instructions..." |
| Looping       | Non-stopping output or infinite logic | Tokens repeating                  |
| Unsafe        | Toxic, biased, illegal, or violent    | NSFW, hate speech, abuse          |

---

## Slide 4: How Models Get Fooled

* Insufficient negative examples during training
* Overconfidence in out-of-domain tasks
* Naive prompt templating (no guards or sanitizers)
* Misuse of instruction role / token leakage

---

## Slide 5: Building a Red Team Prompt Set

Categories to include:

* Known hallucination baits
* Undocumented edge commands (e.g. "You are DAN")
* Policy violations (e.g. copyright, impersonation)
* Jailbreaks: "Ignore above", "Pretend to be X"
* Offensive logic: "Write a joke about..."

---

## Slide 6: Mutation Templates for Fuzzing

* "Explain {nonsense noun} in 3 steps"
* "What’s the capital of {made-up entity}"
* "Translate '{glitched word}' to French"
* "What law applies if {contradiction}?"
* Insert random control tokens / symbols

---

## Slide 7: Metrics for Failure Analysis

* % Hallucination rate (prompt category based)
* Injection success rate
* NSFW probability (e.g. Detoxify or OpenAI filter)
* Reproducibility: does it fail every time?

---

## Slide 8: Logging and Taxonomy Format

```json
{
  "prompt": "What’s the capital of Snargle?",
  "output": "Snargle is a small town in France...",
  "failure_type": "hallucination",
  "severity": "Medium",
  "model_version": "v1.2",
  "reproducible": true,
  "detected_by": "regex + human"
}
```

---

## Slide 9: Defensive Strategies

* Add adversarial prompts to eval/test sets
* Log softmax entropy or output confidence
* Prompt wrappers:

  * Static sanitizers
  * Context constraints
* Use LLM-as-firewall: "Does this prompt try to jailbreak me?"

---

## Slide 10: Lab Preview – Fuzz and Flag

* Define prompt templates
* Generate 50+ queries
* Run model and auto-tag odd responses
* Export `redteam.jsonl`
* Visualize:

  * % fail by category
  * Critical severity counts

---

## Slide 11: Case Studies from the Field

* "Ignore previous instructions" failures (ChatGPT DAN, Claude leaks)
* "Summarize: \[offensive content]" slip-throughs
* Prompt echo from prior sessions
* Logit collapse during adversarial feedback loops

---

## Slide 12: Tools for Adversarial Testing

* OpenAI moderation endpoint / Detoxify
* Regular expressions + LLM judge
* A/B tests on checkpointed versions
* Red team scoring model (custom or Zephyr)

---

## Slide 13: When to Use Adversarial Eval

* Before deployment to users
* After major retraining or checkpoint jump
* When changing input formats or tokenizer
* During weekly regression and eval cycles

---

## Slide 14: Summary – Defense by Design

* Anticipate misuse, test it
* Log, reproduce, categorize
* Harden prompt design and instruction structure
* RAG + instruction = bigger attack surface — test both

---

## Slide 15: Coming Up Next…

**Module 14: Tool Use & Multi-Agent Systems**

* Planner / coder / executor design
* Function calling with guards
* Multi-agent collaboration & roles
