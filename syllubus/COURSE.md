# 🧠 **Course Title**: *LLM Training & Fine-Tuning for Practical AI Agents*

## 🎯 Target Outcome

By the end of this course, you (and your team) will be able to:

* Understand the architecture and training dynamics of LLMs
* Build and fine-tune coding-focused LLMs that reduce hallucinations
* Evaluate, align, and deploy LLMs in production
* Use ChatGPT and local tooling in tandem for continual improvement
* Train and scale AI capabilities within an engineering organization

---

## 🧩 MODULE 00: Orientation

* ✅ Introduction to LLM Training & Use Cases
* ✅ How to use this course: co-training with ChatGPT
* ✅ Setting up your AI dev environment (local + cloud options)
* ✅ Self-assessment: skills baseline and goal-setting

---
## 💻 MODULE 01: Environment Setup & Tooling
- 1.1 Required software: Python, pip/conda, VSCode or JetBrains, Git
- 1.2 Installing Unsloth, HuggingFace Transformers, Datasets, and Accelerate
- 1.3 GPU vs CPU setup (macOS, Windows, Linux)
- 1.4 Recommended specs: 16GB RAM minimum, 8GB+ VRAM GPU preferred (e.g. RTX 3060+, M1/M2 Pro, or Google Colab/T4)
- 1.5 Local vs hosted training environments (LM Studio, Ollama, Colab, RunPod)
- 1.6 Setting up vector stores and LLM services (Chroma, FAISS, LM Studio)
- 1.7 Lab: Set up your local training and inference environment with a test LLM

### 🧰 Platform-Specific Setup Notes
- **macOS (Apple Silicon)**: Use Homebrew, Python 3.10+, Metal backend supported by PyTorch. M1/M2 optimized wheels available for `transformers`, `torch`, `accelerate`, and `unsloth`. LM Studio/Ollama run natively.
- **Linux (Ubuntu/Debian/Fedora)**: Use `apt` or `dnf`, Python 3.10+, pip v23+, virtualenv or conda. Most GPU support (CUDA, ROCm) applies here. Compatible with `llama.cpp`, `Unsloth`, and GPU-aware runtimes.
- **Windows 11 (WSL2 Recommended)**: Use WSL2 with Ubuntu, or Anaconda if staying native. Windows-native Python may need extra config for `torch`. GPU access via WSL2 (NVIDIA drivers + CUDA Toolkit). Use VSCode Remote + WSL.

> 📌 All labs going forward will include Mac, Linux, and Windows setup guidance.
---

## 📘 MODULE 02: LLM Architecture & Training Foundations

* 2.1 History of language models (transformers, pretraining, autoregression)
* 2.2 Anatomy of a transformer-based LLM
* 2.3 Pretraining vs finetuning vs instruction tuning
* 2.4 Tokenization & vocabulary strategies (BPE, SentencePiece, tiktoken)
* 2.5 Attention mechanisms, layers, and memory constraints

---

## 🧑‍💻 MODULE 03: Building Datasets for LLM Training

* 3.1 Dataset types: raw code, dialog, instruct, synthetic
* 3.2 Cleaning & deduplication: code and natural language
* 3.3 Building synthetic coding datasets (Alpaca, ChatML, CoT)
* 3.4 Using ChatGPT to bootstrap safe/correct coding prompts
* 3.5 Lab: create a 500-example `.jsonl` dataset for coroutine-focused Rust and Python code

---

## 🛠 MODULE 04: Finetuning LLMs (from scratch and adapters)

* 4.1 Choosing a model: llama.cpp, Mistral, DeepSeek, Zephyr, CodeLlama, WizardCoder
* 4.2 Quantization: 4-bit, 8-bit, QLoRA, GPTQ
* 4.3 LoRA, QLoRA, PEFT and adapter-based tuning
* 4.4 Training pipelines: Unsloth, HuggingFace, Axolotl, SFTTrainer
* 4.5 Evaluation strategies: BLEU, pass\@k, HumanEval, hallucination metrics
* 4.6 Lab: Finetune CodeLlama-13B on a local coding dataset

---

## 🧠 MODULE 05: Minimizing Hallucinations in Code Generation

* 5.1 Root causes of hallucination in LLMs (pretraining + decoding)
* 5.2 Prompt design and architectural mitigation
* 5.3 Reinforcement Learning from Human Feedback (RLHF) and preference tuning
* 5.4 Chain-of-thought prompting for structured reasoning
* 5.5 Integrating static analysis & code correctness in training feedback
* 5.6 Lab: Benchmark hallucinations across prompt styles and model checkpoints

---

## 🧰 MODULE 06: Continual Training & Iterative Improvement

* 6.1 Retaining vs forgetting: how LLMs update knowledge
* 6.2 Online learning, delta adapters, and periodic refresh
* 6.3 Using ChatGPT to synthetically expand and correct your dataset
* 6.4 Evaluating regressions during continual learning
* 6.5 Lab: Add 50 new synthetic examples based on team feedback and retrain

---

## 🧪 MODULE 07: Evaluation & Alignment

* 7.1 Creating eval sets (coding problems, bugfix, doc-gen, CLI tools)
* 7.2 Prompt injection & safety audits for coding agents
* 7.3 Alignment testing (expected vs actual responses)
* 7.4 Human-in-the-loop feedback loops
* 7.5 Lab: Build a test harness to measure model improvements week-to-week

---

## 🚀 MODULE 08: LLM Deployment for Developer Teams

* 8.1 Choosing serving methods: Ollama, LM Studio, vLLM, TextGenUI, BentoML
* 8.2 JetBrains, VSCode, and CLI tool integrations
* 8.3 Multi-modal assistants (code + terminal + documentation lookup)
* 8.4 GitOps-based evaluation pipelines (autograders, commits, fail/pass)
* 8.5 Building agent wrappers with guardrails (Guardrails.ai, LangChain, etc.)

## 📚 MODULE 09: Retrieval-Augmented Generation (RAG) for Developer Workflows

* 9.1 What is RAG? Architecture and principles
* 9.2 When to use RAG vs. fine-tuning (or both)
* 9.3 Designing a RAG system for low-hallucination code agents
* 9.4 Indexing your private codebase using Chroma, FAISS, or Weaviate
* 9.5 Creating a prompt-assembly pipeline that includes retrieved content
* 9.6 **Lab**: Build a RAG demo using your own Rust/Python code corpus
* 9.7 **Integrate RAG retrieval into Unsloth-finetuned LLM for autocomplete**
* 9.8 **Hook into JetBrains or VS Code to power contextual code suggestions**
* 9.9 Lab: Deploy your trained model into a JetBrains plugin

---

## 🧑‍🏫 MODULE 10: Teaching & Scaling LLM Development in Your Org

* 10.1 Internal knowledge base of patterns and hallucination fixes
* 10.2 Teaching developers how to prompt and supervise code LLMs
* 10.3 Continuous integration with model checkpoints
* 10.4 Growing an AI Engineering culture

---
## 📘 MODULE 11: Data Governance, Licensing & Ethical AI Use
- 11.1 Dataset licensing: MIT, GPL, Apache and risk profiles
- 11.2 PII redaction and GDPR compliance
- 11.3 Dataset filtering for exploit/malware prevention
- 11.4 Safe code generation practices (e.g. avoiding unsafe Rust)
- 11.5 Responsible synthetic data generation

## 🧮 MODULE 12: Tokenizer Engineering & Vocabulary Optimization
- 12.1 Tokenization methods: BPE, Unigram, SentencePiece
- 12.2 Evaluating tokenization performance for code
- 12.3 Training a custom tokenizer for mixed natural language and code
- 12.4 Vocabulary compression and fragmentation
- 12.5 Lab: Train and benchmark your own tokenizer on your coding dataset

## 💬 MODULE 13: Instruction Tuning & Chat Formatting
- 13.1 Instruction formats: ChatML, Alpaca, OpenChat, Zephyr
- 13.2 Consistent format handling and role structure
- 13.3 Prompt injection and safety strategy
- 13.4 Prompt design: CoT, ReAct, multi-step
- 13.5 Lab: Convert your corpus into a ChatML-safe multi-turn dialogue dataset

## 🧱 MODULE 14: Scalable Training Infrastructure
- 14.1 Deepspeed, FSDP, HuggingFace Accelerate
- 14.2 Mixed precision, gradient checkpointing
- 14.3 Distributed dataset processing
- 14.4 Checkpoint recovery and reproducibility
- 14.5 Lab: Launch a multi-GPU or multi-node Unsloth training job

## 🔍 MODULE 15: Adversarial Testing & Robustness
- 15.1 Prompt fuzzing and mutation testing
- 15.2 Adversarial coding queries and jailbreak defense
- 15.3 Model introspection and probing (e.g. logit lens)
- 15.4 Safety audits for CLI, unsafe or malicious code
- 15.5 Lab: Design adversarial prompts and test for hallucination triggers

## 🤖 MODULE 16: Tool-Use & Multi-Agent Systems
- 16.1 Planner-agent-executor architectures
- 16.2 Function calling with validation and repair
- 16.3 Shell/REPL integration for verified results
- 16.4 Multi-agent orchestration: AutoGen, CrewAI, LangGraph
- 16.5 Lab: Build a multi-role AI assistant (planner + coder + fixer)

## 📊 MODULE 17: Evaluation Benchmarks & Leaderboards
- 17.1 pass@k, exact match, AST match, edit distance
- 17.2 Building a HumanEval or MBPP clone
- 17.3 Internal leaderboards and regression tracking
- 17.4 CI/weekly reports and graphs
- 17.5 Lab: Create a team-accessible model comparison dashboard

## 🔁 MODULE 18: LLMOps & Model Lifecycle Management
- 18.1 Dataset and model versioning
- 18.2 CI/CD for model updates and evaluation
- 18.3 Dev/staging/prod checkpoints
- 18.4 Audit logs and lineage tracking
- 18.5 Lab: Set up GitOps + model evaluation automation in your project

---

## 🔁 Capstone Project

* Train, deploy, and validate a custom coding-focused LLM agent using Unsloth
* Must demonstrate:

  * Correct coroutine bias
  * Low hallucination on unseen problems
  * Integration with an IDE or dev workflow
  * Team documentation & reproducible training process

Capstone projects should:

* Reinforce the full course pipeline
* Be grounded in realistic data and deployment
* Demonstrate measurable improvement via LLMs (RAG, fine-tuning, prompting)

---

## 🧠 Evaluation Criteria for Capstone Worthy Projects

| Feature                        | Must Have | Nice to Have |
| ------------------------------ | --------- | ------------ |
| Access to public/free data     | ✅         |              |
| Real user intent / usage model | ✅         |              |
| Allows fine-tuning + RAG       | ✅         |              |
| Works with embeddings/search   | ✅         |              |
| Supports structured eval       | ✅         |              |
| Plugin/agent integration       | ✅         |              |

---

## ✅ Ideas (Rated)

| Idea                                      | Comment                                                                                                                      | Score (0–10) |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------ |
| 🛒 **Purchase-based recommender**         | Can be synthetic or built from public Kaggle ecommerce logs. Enables clustering + RAG on product features. Very practical.   | **8/10**     |
| 🎬 **Movie recommender (IMDb)**           | IMDb+TMDB APIs and embedding metadata = strong RAG combo. Can pair with user prompt tuning (“what should I watch tonight?”). | **9/10**     |
| 🎵 **Music recommender**                  | Tricky due to fewer open datasets + subjective preferences. Better as part of a multi-modal agent.                           | **6/10**     |
| 📈 **Stock picker (RAG + Google Stocks)** | Perfect RAG candidate. Can demonstrate day-to-day updates + hallucination resistance. Needs clear eval boundaries.           | **9/10**     |

---

## 🆕 Additional Capstone Ideas (High Value)

### 1. **Bug Fixer Agent (AutoCoder)**

* Dataset: GitHub issues + fix diffs, or Python/Rust error logs
* Task: Given a broken snippet, fix it + explain why
* Teaches: Prompt alignment, chain-of-thought, few-shot fine-tune

➡️ *High demand for enterprise code QA bots*

---

### 2. **LLM-Powered Search Engine for a Codebase**

* Dataset: Your own open-source repo + docs
* Task: Query in natural language (e.g. “how is this API validated?”)
* Teaches: Chunking, vector search, doc summarization

➡️ *Use your own projects as grounding material*

---

### 3. **Contract Summarizer / Policy Parser**

* Dataset: EU or U.S. public contracts, regulations (PDF to Markdown)
* Task: RAG + summarizer to answer questions like “who’s liable?”
* Teaches: RAG robustness, PDF ingestion, hallucination traps

➡️ *Great for enterprise and compliance contexts*

---

### 4. **Self-Tuning Prompt Explorer**

* Dataset: Prompt-variant pairs with ranked model responses
* Task: Build an agent that mutates prompts, observes LLMs, and ranks best variants
* Teaches: Prompt engineering at scale + eval tracking

➡️ *Can run on top of Unsloth with your own checkpoints*

---

### 5. **Dataset Validator / Profiler**

* Dataset: Any public dataset (CSV, JSON, API, logs)
* Task: LLM parses, validates, and builds a schema or documentation page
* Teaches: Tool use, data typing, deterministic LLM integration

➡️ *Bridge between data science and ML pipelines*

---

Here is the fully formatted capstone project entry you can insert into your syllabus or capstone list:


### 🧩 Capstone Project 6: OpenAPI Spec Builder from User Stories

**🧠 Goal:**  
Build an LLM-powered assistant that takes natural language prompts or user stories and generates or completes an OpenAPI 3.x YAML specification.

**📦 Dataset:**  
- Public GitHub OpenAPI specs (via search or curated repositories)
- OpenAPI examples from [APIs.guru](https://apis.guru) or [SwaggerHub](https://swagger.io/tools/swaggerhub/)
- Synthetic user story → endpoint mappings created by you or ChatGPT

**🛠 Task Overview:**
- Parse input stories like:  
  > “Allow users to upload profile pictures with a PUT to /users/{id}/photo”
- Search the existing OpenAPI YAML for similar paths or operations
- Suggest or append missing endpoint definitions
- Autogenerate:
  - `paths`, `parameters`, `requestBody`, `responses`
  - Example payloads
  - Schemas where needed
- Assist user interactively to refine the API spec

**🧪 What This Teaches:**
- Advanced prompt structuring and chain-of-thought reasoning
- YAML manipulation and grounding in structured documents
- Finetuning on semi-structured code+markup formats
- Use of RAG to reference canonical specs

**🧰 Extensions:**
- Connect with Swagger Editor or VS Code OpenAPI plugins
- Run as a CLI tool or GitHub Action to assist API teams
- Export OpenAPI → Postman Collection → SDK via codegen

**✅ Evaluation Criteria:**
- Correctness of endpoint definitions
- Alignment to RESTful conventions
- Hallucination avoidance in schemas and methods
- Developer usability (clear error messages, interactive flow)

This project bridges LLMs with practical developer tooling for real-world impact.


### 🧩 Capstone Project 7: Interactive User Story Expander

**🧠 Goal:**  
Create an LLM-powered tool that transforms terse user story summaries into fully enriched user stories with acceptance criteria, edge case prompts, and clarifying follow-up questions.

**📦 Dataset:**  
- Public product backlogs (e.g. open-source GitHub issue templates)
- Internal company user stories (anonymized)
- Synthetic user stories generated via ChatGPT
- Existing datasets of Agile epics and acceptance test templates

**🛠 Task Overview:**
- Accept inputs like:
  > “As a user, I want to link my GCP project or org via a simple setup flow.”
- Use the LLM to:
  - Expand the input into a detailed narrative with business context
  - Add a list of **acceptance criteria** (Gherkin or bullet format)
  - Prompt the user for additional clarification (e.g. “Should this support both project and org-level IAM?”)
  - Suggest edge cases, constraints, and success/failure modes

**✨ Features:**
- Inline editing and iteration loop with the user
- Export to Markdown, CSV, or Jira format
- Option to convert structured output into OpenAPI seeds or test case templates

**🧪 What This Teaches:**
- Prompt templating and chaining
- Chain-of-thought reasoning applied to requirements gathering
- RAG (optional) for referencing existing domain stories or docs
- Human-in-the-loop clarification and enrichment workflows

**✅ Evaluation Criteria:**
- Completeness of output (story + criteria + prompts)
- Relevance and value of follow-up questions
- Lack of contradiction or hallucination
- Developer-readiness of output (can it go to engineering directly?)

This project bridges product thinking and generative AI, improving collaboration between stakeholders and technical teams.


---

## 🧩 Proposal

Let’s create a **Capstone Library** where each project includes:

* Summary + user story
* Data source (public URL or script)
* Model strategy (RAG, finetune, prompt-only)
* Evaluation method (pass/fail, ranking, leaderboard)
* Optional integrations (JetBrains, CLI, VSCode, browser)

Would you like me to scaffold the first 3 capstone entries in a folder like `capstones/` with `README.md` + instructions?


---

With your syllabus now fully structured and covering everything from fundamentals to deployment and LLMOps, we can proceed using this course in two effective ways:

---

See [Execution plan](./EXECUTION_PLAN.md) for a detailed phase-based execution strategy.