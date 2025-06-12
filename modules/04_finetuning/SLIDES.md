# 🎓 Slide Deck: Module 04 – Fine-Tuning LLMs

---

## Slide 1: Welcome to Module 04

**Title:** Fine-Tuning Your LLM Using Unsloth

> Note: This is the module where learners move from theory into model training. Build confidence through step-by-step clarity.

---

## Slide 2: What Is Fine-Tuning?

* Teaching a model new behaviors or domain knowledge
* Uses labelled prompt-response examples
* Often builds on top of a pretrained base model

> Note: Show a diagram: base model + adapter layers → task-specific head

---

## Slide 3: Full Finetuning vs Adapter-Based

| Strategy      | Resource Need   | Pros                           | Cons                    |
| ------------- | --------------- | ------------------------------ | ----------------------- |
| Full Finetune | High (GPU, RAM) | Maximum control, full rewrites | Expensive, slow         |
| LoRA          | Low             | Fast, memory efficient         | Trains adapters only    |
| QLoRA         | Very Low        | 4-bit quantized, laptop-ready  | Slightly lower accuracy |

> Note: Use this to recommend the best option per use case.

---

## Slide 4: Unsloth to the Rescue

* Wraps HuggingFace APIs for fast PEFT-based fine-tuning
* Works on Zephyr, TinyLlama, DeepSeek, and more
* Compatible with CPU, Apple Silicon, and CUDA

> Note: Explain why it’s ideal for this course: fast, local, flexible.

---

## Slide 5: Anatomy of a Training Script

```python
model, tokenizer = FastLanguageModel.from_pretrained(...)
dataset = load_dataset(...)
args = TrainingArguments(...)
model.train_model(dataset, args)
```

> Note: Explain each part. Show it live if possible.

---

## Slide 6: Checkpointing Best Practices

* Save checkpoints every epoch or N steps
* Use `save_pretrained()` to persist your work
* Reload checkpoints with `from_pretrained()`

> Note: Encourage storing outputs in `checkpoints/my_model/`

---

## Slide 7: Optional: wandb Tracking

* Monitor training loss in real time
* Track parameter settings
* Compare LoRA vs QLoRA runs visually

> Note: Recommended for teams or multiple training experiments

---

## Slide 8: Lab – Train a Model

**Goal:** Train Zephyr or TinyLlama on your custom dataset

Steps:

1. Run `train_model.ipynb` or `train_tiny_model.py`
2. Monitor loss and output
3. Save checkpoint
4. Preview outputs in `evaluate_model.ipynb`

---

## Slide 9: Troubleshooting Tips

* Check for RAM/VRAM limits
* Use small batch size (2–4)
* Ensure your `.jsonl` has no formatting errors
* Use `print()` statements to debug dataset

---

## Slide 10: Coming Up Next…

**Module 05: Minimizing Hallucinations in Code Generation**

* What causes hallucination?
* Prompt vs model tuning
* Evaluation strategies and safety

> Note: Use this transition to position quality as the next challenge.
