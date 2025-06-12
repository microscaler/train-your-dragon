# 🧠 Module 02 – Slide Deck: LLM Architecture & Training Foundations

---

## Slide 1: What Is an LLM?

* A large language model (LLM) predicts the next token in a sequence
* Trained on vast corpora of text/code
* Capable of understanding, generating, and reasoning with text

> Note: Emphasize that LLMs don’t "know" facts — they model distributions over tokens.

---

## Slide 2: Welcome to Module 02

**Title:** Understanding How LLMs Work

> Note: Today we’ll demystify the structure of modern LLMs like LLaMA, Mistral, and DeepSeek. This gives you a mental map of what you’re building and tuning in the rest of the course.

---

## Slide 3: Why Learn Architecture?

* Informed tuning = better decisions
* Helps debug model behavior
* Know your model’s limits

> Note: You can’t effectively prompt, fine-tune, or evaluate what you don’t structurally understand.

---

## Slide 4: What Is a Transformer?

* A neural network architecture built from attention layers
* Introduced in "Attention Is All You Need" (2017)
* Core components:

  * Multi-head self-attention
  * Feed-forward layers
  * Layer norm and residuals

> Note: Use the classic transformer diagram and annotate it live.

---

## Slide 5: Transformer Overview

* Encoder-decoder vs decoder-only
* Multi-head self-attention
* Positional encodings
* Residual connections and layer norm

> Note: Most LLMs today are decoder-only (GPT style) — we’ll focus there.

---

## Slide 6: Tokenization

* LLMs work on tokens, not characters or words
* BPE, SentencePiece, and WordPiece are popular tokenizers
* Examples:

  * "Hello world" → `['Hello', 'Ġworld']`

> Note: Live demo with a tokenizer encourages intuition.

---

## Slide 7: Tokenization in Action

* Sentence → Tokens → IDs → Model
* Token limit (e.g. 2048 or 4096) constrains how much the model can “see”

> Note: Use `AutoTokenizer` to test this with real models.

---

## Slide 8: Attention Explained Simply

* Self-attention = learn what parts of the sequence to focus on
* Query, key, value: think “search, match, return”
* Matrix multiplication yields a weighted average of inputs

> Note: Reinforce with analogy (e.g. reading while highlighting what matters).

---

## Slide 9: Key Terminology

| Term        | What it Means                        |
| ----------- | ------------------------------------ |
| Token       | Sub-word unit fed into the model     |
| Embedding   | Vector representation of a token     |
| Hidden size | Dimensionality of transformer layers |
| Head        | Independent attention mechanism      |
| Logits      | Raw prediction scores per token      |

---

## Slide 10: Decoder vs Encoder Models

| Model Type      | Examples            | Purpose                    |
| --------------- | ------------------- | -------------------------- |
| Decoder-only    | GPT, LLaMA, Mistral | Generation (causal)        |
| Encoder-only    | BERT                | Classification, embeddings |
| Encoder-decoder | T5, BART            | Translation, summarization |

> Note: Clarify that most chat assistants use decoder-only models.

---

## Slide 11: Training Types

* **Pretraining**: learn from unlabeled data (next-token prediction)
* **Fine-tuning**: specialize on task-specific data
* **Instruction tuning**: align with natural language commands
* **RLHF**: preference alignment with human feedback

> Note: Draw this as a funnel — from broad to narrow

---

## Slide 12: Model Sizes & Parameters

* 1B vs 7B vs 13B vs 70B models
* Tradeoffs: quality ↔ latency ↔ memory ↔ cost
* Fine-tuning feasible up to 13B on consumer GPUs (w/ quantization)

> Note: We’ll focus on 1.3B to 7B class models in this course.

---

## Slide 13: Code LLM Families

* CodeLlama, DeepSeek Coder, StarCoder, WizardCoder
* Finetuned for:

  * Indentation-aware syntax
  * Function completion
  * Chain-of-thought

> Note: These models were trained with dataset structure in mind — you’ll need to match it for best performance.

---

## Slide 14: HuggingFace Tour (Live)

* Browse [https://huggingface.co/models](https://huggingface.co/models)
* Filters: `language: python`, `library: transformers`, `task: text-generation`
* Download configs and check VRAM usage

> Note: This tour prepares students for the Model Dive lab.

---

## Slide 15: Lab Preview – Model Dive

### 🧪 Hands-On Activity: Inspecting Model Anatomy

**Objective:** Use `AutoConfig` from HuggingFace Transformers to explore and compare LLM model architectures.

```python
from transformers import AutoConfig

model_id_1 = "unsloth/zephyr-1.3b-bnb-4bit"
model_id_2 = "tiiuae/falcon-rw-1b"

config1 = AutoConfig.from_pretrained(model_id_1)
config2 = AutoConfig.from_pretrained(model_id_2)

print(f"Model 1: {model_id_1}")
print("Layers:", config1.num_hidden_layers)
print("Hidden size:", config1.hidden_size)
print("Heads:", config1.num_attention_heads)
print("Max positions:", config1.max_position_embeddings)
print("Vocab size:", config1.vocab_size)

print("
---
")
print(f"Model 2: {model_id_2}")
print("Layers:", config2.num_hidden_layers)
print("Hidden size:", config2.hidden_size)
print("Heads:", config2.num_attention_heads)
print("Max positions:", config2.max_position_embeddings)
print("Vocab size:", config2.vocab_size)
```

> Note: Ask students to compare output and reflect:
>
> * Which model is more parameter-heavy?
> * Which model would likely require more VRAM?
> * Are both models quantized?

Encourage logging the results in a file called `model_dive.md`.
**Goal:** Use `AutoConfig` to inspect two models

* Num layers
* Hidden size
* Num heads
* Max positions
* Vocab size

---

## Slide 16: Coming Up Next…

**Module 03: Building Your Dataset**

* What makes a good prompt?
* What structure do LLMs expect?
* How to build `.jsonl` files for training

> Note: This is where we’ll shift from theory into dataset engineering and real prompts.
