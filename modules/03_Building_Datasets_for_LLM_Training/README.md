# 📦 Module 03: Building Datasets for LLM Training

This module teaches you how to curate, structure, and format datasets to fine-tune your LLMs effectively.

---

## 🎯 Objectives

By the end of this module, you will:

* Understand what makes a good prompt-response pair
* Learn the difference between instruction tuning and raw pretraining data
* Create `.jsonl` datasets compatible with Unsloth and HuggingFace
* Design synthetic and semi-supervised examples using ChatGPT
* Prepare the foundation for all future fine-tuning labs

---

## ✅ Skills Gained

* Writing high-quality instruction-completion examples
* Validating and visualizing `.jsonl` datasets
* Using ChatGPT to generate and expand synthetic datasets
* Aligning dataset format with LLM compatibility standards

---

## 🗂️ Activities

### 1. Review Prompt Design Guidelines

Read: [Stanford Alpaca formatting](https://github.com/tatsu-lab/stanford_alpaca#data-release)
Understand:

* What’s in an `instruction`, `input`, and `output`
* Why you don’t need all three in every example

### 2. Analyze Existing JSONL

Inspect sample files in `data/coroutine_training_data.jsonl`
Check for:

* Consistency in field names (`instruction`, `output`)
* Clean formatting (no escaped newlines)

### 3. Generate Your Own Examples

Use ChatGPT to:

* Convert user stories or issues into instruction-output pairs
* Create coding tasks with realistic output

Example prompt:

```markdown
Write a JSONL-formatted training example where:
- Instruction: “Convert this thread-based Python server to use coroutines”
- Output: A coroutine-based implementation with `asyncio`
```

### 4. Validate Your Dataset

Write a Python script to:

* Open a `.jsonl` file
* Count examples, check field consistency
* Print a random sample

---

## 🧪 Lab: Build 50 Synthetic Coding Examples

**Goal:** Populate `data/custom_training.jsonl` with 50 high-quality instruction-output pairs that:

* Emphasize coroutine-based reasoning
* Span Python, Rust, TypeScript if desired
* Include some intentionally flawed examples for robustness

Use ChatGPT, static code, or real-world patterns. Bonus: Tag with metadata (e.g. `"lang": "rust"`).

---

## 🔗 Linked Modules

* [Module 02: Architecture](../02_LLM_Architecture_&_Training_Foundations/README.md)
* [Module 04: Fine-Tuning](../04_Finetuning_LLMs_%28from_scratch_and_adapters%29/README.md)

---

## ✅ Completion Checklist

* [ ] I understand how prompt+completion examples work
* [ ] I reviewed the JSONL format
* [ ] I generated new examples with ChatGPT
* [ ] I validated my dataset structure
* [ ] I have a `.jsonl` file with at least 50 usable samples
