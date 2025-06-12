# 🧮 Module 12: Tokenizer Engineering & Vocabulary Optimization

This module teaches you how tokenization affects model performance, vocabulary coverage, and training efficiency. You’ll experiment with tokenizer design, vocabulary stats, and optimizing token splits for coding or multilingual workloads.

---

## 🎯 Objectives

By the end of this module, you will:

* Understand how LLM tokenizers work and why they matter
* Train a custom tokenizer for your use case (code, domain-specific)
* Analyze token count efficiency and fragmentation
* Swap tokenizers in an existing model pipeline

---

## ✅ Skills Gained

* BPE, Unigram, and SentencePiece knowledge
* Vocabulary coverage evaluation
* Tokenizer training and export
* Tokenization-aware dataset curation

---

## 🗂️ Activities

### 1. Analyze Tokenization Efficiency

* Take 5–10 sample `.py`, `.md`, or `.jsonl` files
* Tokenize using:

  * GPT tokenizer (tiktoken)
  * SentencePiece
  * Your model’s current tokenizer
* Measure:

  * Total tokens
  * Average tokens per line
  * Fragmentation (how many splits per common word)

### 2. Train a Custom Tokenizer

* Use HuggingFace `tokenizers` or `sentencepiece`
* Input: curated domain files (e.g. `data/internal_curated/`)
* Output: tokenizer model + vocab
* Save in `tokenizers/your_vocab/`

### 3. Evaluate Vocabulary Coverage

* Choose 100 test prompts or completions
* Count:

  * Tokens in base tokenizer
  * Tokens in new tokenizer
* Visualize: bar chart of token counts

### 4. Swap Tokenizer in Model Pipeline

* Load a pre-trained model with a new tokenizer
* Fine-tune a small dataset with the custom vocab
* Log any decoding errors or perf diffs

---

## 🧪 Lab: Tokenizer Battle

1. Choose 5 `.py` and 5 `.md` files
2. Tokenize with 3 methods (e.g. GPT, HF, custom)
3. Compare average tokens per 100 lines
4. Chart results and declare best performance for your domain

Bonus:

* Use multilingual corpus and test language-specific performance

---

## 🔗 Linked Modules

* [Module 03: Dataset Construction](../03_Building_Datasets_for_LLM_Training/README.md)
* [Module 12: Scalable Training Infrastructure](../14_Scalable_Training_Infrastructure/README.md)

---

## ✅ Completion Checklist

* [ ] I trained a tokenizer from source data
* [ ] I compared token count efficiency between vocab strategies
* [ ] I saved a tokenizer model and used it in a model pipeline
* [ ] I can visualize and explain fragmentation, padding, and token quality
