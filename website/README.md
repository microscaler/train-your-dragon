## modules/00_orientation/

It includes:

- Course context and structure
- Self-assessment and journaling activities
- Optional team onboarding
- ChatGPT-based milestone planning
- Completion checklist to track learner progress

---

## Module 01 Environment Setup in the canvas.

It includes:

- OS-specific install guidance
- conda and pip setup
- LLM inference test via HuggingFace
- Notebook launch tips
- A CLI lab script assignment (test_inference.py)
- Completion checklist
--- 

## Module 02 Data Preparation

It now includes:

- Both LLM theory and transformer fundamentals
- Simplified explanations, analogies, and instructor notes
- HuggingFace exploration and lab preview
- Forward-looking transitions to Module 03

---

## Module 03 Model Training

It includes:

- Prompt/response design principles
- Use of .jsonl with Unsloth or HuggingFace
- Instructions for generating synthetic examples using ChatGPT
- Validation guidance
- A lab to build 50 focused training samples
- Clear format guidelines (instruction/output)
- Prompt and output design do’s and don’ts
- JSONL structure + validation tips
- Sources of good training data
- Preview of the 50-example lab
- Transition into Module 04: Fine-Tuning

--- 

## Module 04 Fine-Tuning LLMs (from scratch and adapters)

It includes:

- Clear comparison between full fine-tuning, LoRA, and QLoRA
- Instructions for running both notebooks and CLI scripts
- A milestone lab to train your first usable model
- Reloading and evaluating model behavior

---

## Module 05 Minimizing Hallucinations in Code Generation

It includes:

- Clear explanation of hallucination in LLMs (especially for code)
- Activity flow from detection → prompt redesign → model scoring
- Lab to track and visualise hallucination rates
- Checklist to assess learner confidence and output quality

---

## Module 06 Continual Training & Iterative Improvement of LLMs

It includes:

- Definition and motivation for continual learning
- Activities to derive delta data from hallucination logs
- Workflow for correcting, retraining, and re-evaluating
- A lab for tracking feedback loops in practice

---

## Module 07 Evaluation & Alighnment of LLMs

It includes:

- Goal-focused evaluation workflows (accuracy, hallucination, pass@k)
- Activities for test case creation, model comparison, and tracking
- A lab to measure and visualize evaluation results across versions

--- 

## Module 08 Retrieval & Augmented Generation (RAG)

It includes:

- A full explanation of the RAG architecture
- Activities for corpus preparation, embedding, indexing, and prompt assembly
- A lab for building a search-backed code assistant
- CLI and UI extension options

---

## Module 09 Deployment & Productionizing LLMs

It includes:

- Team role definitions
- Contribution workflows
- Prompt jams and model evals
- A lab for publishing a team model with documentation

## Module 10 Data Governance, Licensing & Ethical IA Considerations

It includes:

- Legal risk awareness (MIT, GPL, proprietary)
- Dataset policy writing
- Redaction and filtering best practices
- Provenance and audit metadata strategy

## Module 11 Tokenizer Training & Optimization

It includes:

- Objectives for tokenizer architecture and efficiency
- Token count comparisons across vocab strategies
- Custom tokenizer training and usage
- Completion criteria for real-world impact

## Module 14 Adversarial Testing & Robustness

It includes:

- Planner–executor patterns
- Tool calling via functions
- Multi-agent turn-taking logic
- Labs for chaining and replay

## Module 15 Adversarial Testing & Robustness

It includes:

- Pass@k and edit-distance metrics
- HumanEval-style benchmarks
- Leaderboard tracking
- CI-based regression tests