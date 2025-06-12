# 🧪 Module 12 – Practice Exercises: Tokenizer Engineering

These exercises will help you build, evaluate, and apply a custom tokenizer.

---

## ✅ Exercise 1: Token Count Comparison

* Choose 3 domain files (`.py`, `.md`, `.jsonl`)
* Tokenize each file using:

  * OpenAI `tiktoken` (GPT)
  * `AutoTokenizer` from HuggingFace
  * SentencePiece (if installed)
* Record total tokens and avg tokens per 100 lines

🎯 Goal: Visualize tokenizer fragmentation and verbosity

---

## ✅ Exercise 2: Train Your Own Tokenizer

* Use `tokenizers` or `sentencepiece`
* Input: `data/internal_curated/*.txt`
* Set vocab size: 8,000 or 16,000
* Output model files to `tokenizers/custom-vocab/`

🎯 Goal: Generate a tokenizer tailored to your corpus

---

## ✅ Exercise 3: Vocab Coverage Test

* Choose 50–100 lines of target completions
* Tokenize with base tokenizer and your new one
* Count:

  * `UNK` tokens
  * Fragmented strings
* Compare token counts side by side

🎯 Goal: Evaluate real usage improvement

---

## ✅ Exercise 4: Swap Tokenizer in Model Pipeline

* Load model from `unsloth` or HF `AutoModel`
* Load your custom tokenizer via path
* Fine-tune on 100 example dataset
* Log decoding differences and any errors

🎯 Goal: End-to-end tokenizer integration

---

## ✅ Exercise 5: Chart Your Results

* Build a CSV log of:

  * File name
  * Tokenizer name
  * Total tokens
* Visualize in a bar chart or stacked graph

🎯 Goal: Show domain-specific token efficiency clearly
