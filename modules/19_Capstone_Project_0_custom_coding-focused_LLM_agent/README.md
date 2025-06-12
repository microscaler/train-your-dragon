# Capstone Project 0: Custom Coding-Focused LLM Agent

## 🧠 Goal
Train and deploy a low-hallucination LLM that can assist in code generation for Rust, Python, and TypeScript — with a coroutine-first mindset.

## 📦 Dataset
- Custom curated `.jsonl` with coroutine-centric prompts
- Synthetic and real codebases (internal or open source)

## 🛠 Tasks
- Fine-tune on prompt-output pairs using Unsloth
- Add synthetic eval prompts to track hallucination
- Connect to JetBrains or VS Code as a completions plugin

## ✅ Evaluation Criteria
- Correct usage of coroutines over threads
- Syntax-valid output
- Improvement over baseline GPT-3.5 behavior
