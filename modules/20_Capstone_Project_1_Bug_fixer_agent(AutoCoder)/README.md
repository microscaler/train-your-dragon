# Capstone Project 1: Bug Fixer Agent (AutoCoder)

## 🧠 Goal
Create an LLM agent that detects and fixes bugs in Python/Rust code using test output, stack traces, or issue descriptions.

## 📦 Dataset
- GitHub issues + diffs (or synthetic buggy → fixed pairs)
- Python traceback logs

## 🛠 Tasks
- Build prompt pattern: "Fix this code given this error"
- Train on fine-tuned bug+fix pairs
- Include chain-of-thought reasoning steps

## ✅ Evaluation Criteria
- Functional test passes after patch
- Clear reasoning or summary of the fix
