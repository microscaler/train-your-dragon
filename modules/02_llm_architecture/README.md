# 🧠 Module 02: LLM Architecture & Training Foundations

This module provides the theoretical foundation for understanding how LLMs work under the hood. You'll learn about the transformer architecture, attention mechanisms, tokenization, and how pretraining and fine-tuning interact.

---

## 🎯 Objectives

By the end of this module, you will:

* Understand the anatomy of a transformer-based language model
* Know how pretraining, fine-tuning, and instruction tuning differ
* Grasp the significance of tokenization and attention
* Develop mental models for how LLMs generate sequences

---

## ✅ Skills Gained

* Describe transformer architecture components
* Differentiate pretraining vs fine-tuning
* Visualize token flow through attention layers
* Read model cards and training specs with confidence

---

## 🗂️ Activities

### 1. Watch or read foundational explainer:

* [Jay Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
* [Explained: Attention Is All You Need (Paper Summary)](https://www.youtube.com/watch?v=iDulhoQ2pro)

### 2. Slide walkthrough (see `SLIDES.md`)

* Key terms: hidden state, query-key-value, multi-head attention
* Diagram of attention stack and positional encoding

### 3. Tokenizer demo (optional CLI or notebook)

```bash
from transformers import AutoTokenizer
model_id = "tiiuae/falcon-rw-1b"
tok = AutoTokenizer.from_pretrained(model_id)
tok("The future of Rust is coroutine-based")
```

### 4. Compare LLM types

* Decoder-only (GPT, LLaMA, Mistral)
* Encoder-decoder (T5, BART)
* Chat vs instruct-tuned vs base models

---

## 🧪 Lab: Architecture Quiz + Visual Walkthrough

* Complete the `quiz.md` in this folder
* Open and annotate the provided `transformer_stack_diagram.png`
* Answer: What does the attention mask do? How is positional information encoded?

---

## 🔗 Linked Modules

* [Module 03: Dataset Building](../03_datasets/README.md)
* [Module 12: Tokenizer Optimization](../12_Tokenizer_Engineering_&_Vocabulary_Optimization/README.md)

---

## ✅ Completion Checklist

* [ ] I understand the flow of tokens through a transformer
* [ ] I can explain attention, layers, and logits
* [ ] I know the difference between GPT, T5, LLaMA, and Mistral
* [ ] I completed the lab quiz and diagram review
