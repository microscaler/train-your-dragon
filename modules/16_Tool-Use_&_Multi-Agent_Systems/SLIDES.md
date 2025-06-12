# 🎓 Slide Deck: Module 14 – Tool Use & Multi-Agent Systems

---

## Slide 1: Welcome to Module 14

**Title:** Tool-Using Agents and Multi-Agent Coordination

> Note: You’re no longer just prompting — you’re orchestrating agents.

---

## Slide 2: Why LLMs Need Tools

* Language models don’t have access to:

  * APIs
  * Search results
  * State or memory
* Tool usage = extend model reach with verifiable actions

---

## Slide 3: Function Calling – Concept

* User → Agent → `function_name(args)`
* Agent calls real tool, uses output in reply
* LLM predicts when and what to call based on system context

---

## Slide 4: Planner → Executor Model

* Planner: breaks request into tool steps
* Executor: runs function or calls API
* Optional: Reasoner to verify or refine

---

## Slide 5: Example Tool Pipeline

**Task:** “Summarize today’s error logs and email to DevOps”

1. `load_logs()`  → raw errors
2. `summarize(errors)`  → bullet points
3. `email(summary)`  → delivery to team

---

## Slide 6: Function Call Format (HF / OpenAI)

```json
{
  "function": "weather",
  "parameters": {
    "city": "Tokyo"
  }
}
```

* Can be JSON schema or code stub
* Parsed by orchestrator or plugin runtime

---

## Slide 7: Multi-Agent Roles

* Planner: turns goals into actions
* Researcher: finds or queries facts
* Validator: checks assumptions or citations
* Presenter: writes final output for user

---

## Slide 8: Simulating Turn Logic

* Track `history = [ {role, message, tool_call?} ]`
* Agents reason per turn based on last output
* Log all decisions for traceability

---

## Slide 9: Fallbacks and Replays

* If a tool fails:

  * Agent retries
  * Calls backup
  * Prompts user for new input
* Save turn logs → support audit and debugging

---

## Slide 10: Lab – Simulate Agent with Tools

* Define 3 mock tools: `search()`, `calc()`, `log()`
* Build agent that receives task, plans tool usage, verifies, presents
* Log all tool calls, messages, and assumptions

---

## Slide 11: Coming Up Next…

**Module 15: Evaluation Benchmarks & Leaderboards**

* How to track model quality across checkpoints and teams
