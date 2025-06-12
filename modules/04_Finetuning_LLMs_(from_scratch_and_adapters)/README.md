# 🔧 Module 04: Fine-Tuning LLMs (From Scratch and Adapters)

This module teaches you how to train your own model using the dataset you built in Module 03.
You’ll explore parameter-efficient fine-tuning (PEFT) methods, learn how Unsloth optimizes the process, and run your first end-to-end training loop.

---

## 🎯 Objectives

By the end of this module, you will:

* Understand the difference between full fine-tuning, LoRA, and QLoRA
* Use the Unsloth framework to accelerate LLM training
* Train a model on your `.jsonl` data
* Save and reload model checkpoints
* Begin testing accuracy and hallucination rate

---

## ✅ Skills Gained

* Loading and training a model with Unsloth
* Understanding PEFT: LoRA and QLoRA
* Monitoring training loss and model checkpoints
* Evaluating model responses against known outputs

---

## 🗂️ Activities

### 1. Theory: Finetuning vs LoRA vs QLoRA

Read this guide: [https://sebastianraschka.com/blog/2023/llm-finetuning.html](https://sebastianraschka.com/blog/2023/llm-finetuning.html)
Understand:

* When to choose full vs adapter-based fine-tuning
* How LoRA "freezes" base model weights and trains small injection matrices
* Why QLoRA enables 4-bit training with low resource usage

### 2. Launch `train_model.ipynb`

Use the notebook created in the `labs/unsloth_finetune/` folder.
Walk through:

* Loading your JSONL dataset
* Initializing Unsloth’s model wrapper
* Setting batch size and epoch count
* Training and saving your model

### 3. Run a Training Script (Optional)

Use `train_tiny_model.py` to automate CLI-based fine-tuning.

```bash
python train_tiny_model.py
```

### 4. Save + Reload Your Checkpoint

```python
model.save_pretrained("./checkpoints/my_model")
model = model.from_pretrained("./checkpoints/my_model")
```

### 5. Preview Evaluation Notebook

See `evaluate_model.ipynb` and run sample completions against your dataset.

---

## 🧪 Lab: Train Your First Model

**Goal:** Fine-tune Zephyr-1.3B or TinyLlama on your 50-example dataset.

Track:

* Training time
* Loss curve
* Number of steps
* Output examples for 3–5 test prompts

Bonus:

* Add `wandb` integration to log training in real time.
* Try a custom LoRA rank (e.g. 16 vs 32) and compare performance.

---

## 🔗 Linked Modules

* [Module 03: Building Datasets](../03_Building_Datasets_for_LLM_Training/README.md)
* [Module 05: Minimizing Hallucinations](../05_Minimizing_Hallucinations_in_Code_Generation/README.md)

---

## ✅ Completion Checklist

* [ ] I understand the difference between LoRA and QLoRA
* [ ] I’ve run a notebook or script to train a model
* [ ] I saved and reloaded a model checkpoint
* [ ] I previewed my model’s outputs
* [ ] I’m ready to evaluate hallucination or accuracy
