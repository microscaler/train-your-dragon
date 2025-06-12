# 🧪 Fine-Tuning with Unsloth: Lab Overview

Welcome to the `unsloth_finetune` lab! This directory contains beginner-friendly tools and notebooks for training and evaluating your first small LLM using [Unsloth](https://github.com/unslothai/unsloth).

---

## 🧠 Purpose

This lab helps you:

* Understand the basics of instruction fine-tuning
* Work with small code-centric datasets (e.g. coroutine examples)
* Use 4-bit models like Zephyr 1.3B or TinyLlama on your laptop
* Evaluate outputs for correctness and hallucination

---

## 📁 Directory Contents

| File                   | Description                                                              |
| ---------------------- | ------------------------------------------------------------------------ |
| `train_model.ipynb`    | Step-by-step notebook for loading, formatting data, and training a model |
| `evaluate_model.ipynb` | Interactive evaluation notebook for reviewing outputs from your model    |
| `train_tiny_model.py`  | Script version of the training pipeline for automation                   |
| `run_eval.py`          | Script to evaluate pass\@k or hallucination rate on sample prompts       |
| `eval_prompts.jsonl`   | Test prompts to measure model quality post-finetune                      |

---

## ✅ How to Run

### Step 1: Install your environment

```bash
pip install -r ../../requirements.txt
```

Or if you prefer conda:

```bash
conda create -n train-your-dragon python=3.10
conda activate train-your-dragon
pip install -r ../../requirements.txt
```

### Step 2: Train your first model

Run the notebook:

```bash
jupyter notebook train_model.ipynb
```

Or execute the script:

```bash
python train_tiny_model.py
```

### Step 3: Evaluate your model

```bash
python run_eval.py
```

Or open `evaluate_model.ipynb` in VS Code or Jupyter.

---

## 🧪 Customize This Lab

* Edit `coroutine_training_data.jsonl` to try different instruction styles
* Replace the base model in `train_tiny_model.py` with another Unsloth-compatible checkpoint
* Use `wandb` for live monitoring (optional)

---

## 🔗 Related Modules

* 📘 Module 3: Building Datasets
* 🛠 Module 4: Fine-Tuning LLMs
* 🧪 Module 7: Evaluation & Alignment

Let’s train your dragon — one prompt at a time. 🐉
