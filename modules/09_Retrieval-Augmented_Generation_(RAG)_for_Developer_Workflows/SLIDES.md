# 🎓 Slide Deck: Module 09 – Teaching & Scaling LLM Development in Your Org

---

## Slide 1: Welcome to Module 09

**Title:** Building an Internal LLM Practice

> Note: This module shows how to take what you’ve learned and spread it across your team.

---

## Slide 2: Why It Matters

* LLMs aren’t just a tool — they’re a team capability
* You need:

  * Shared process
  * Shared models
  * Shared responsibility

---

## Slide 3: Common Roles in a Team LLM Stack

| Role                 | Description                              |
| -------------------- | ---------------------------------------- |
| AI Product Owner     | Defines use cases and success criteria   |
| Prompt/Eval Engineer | Crafts prompts and tests model output    |
| Data Curator         | Reviews and expands training data        |
| Training Engineer    | Fine-tunes models and tracks performance |

---

## Slide 4: Contribution Workflow

* Central `data/`, `prompts/`, and `logs/` folders
* Contributors:

  * Add prompts
  * Review hallucinations
  * Propose new evals
* Tools:

  * Notebooks (`hallucination_eval.ipynb`)
  * Pull requests / GitHub Issues

---

## Slide 5: Prompt Jams (Team Lab Sessions)

* 60–90 minute session
* Each team member brings 3–5 real tasks
* Compare outputs:

  * Base model
  * Fine-tuned model
  * RAG version (optional)

> Note: This builds engagement and visibility

---

## Slide 6: Model Review and Change Log

* Each model version should have:

  * Date, author, goal
  * Metrics (accuracy, hallucination rate)
  * Known gaps or risks
* Store in `/models/team_checkpoints/model_vX/README.md`

---

## Slide 7: Peer Testing and Feedback

* Ask a peer to:

  * Run 3 test prompts
  * Record clarity, correctness, hallucination
  * Suggest 1 new prompt or fix

> Note: Great prep for handoff, docs, and audit

---

## Slide 8: Lab – Publish and Share a Model

* Use shared `models/team_checkpoints/`
* Add README + changelog
* Share link with one peer
* Ask for testing and feedback

---

## Slide 9: What This Enables

* Prompt and eval reuse
* CI-style evaluation for models
* Growth from individual → team → org capability

---

## Slide 10: Coming Up Next…

**Module 10: Data Governance, Licensing & Ethical AI Use**

* Avoid license traps
* Audit your training sources
* Design ethical prompts and outputs
