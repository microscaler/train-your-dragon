# 🧪 Module 08 – Practice Exercises: Retrieval-Augmented Generation (RAG)

These exercises help you build, test, and expand a functional local RAG system.

---

## ✅ Exercise 1: Prepare Your Corpus

* Create a folder `data/corpus/`
* Add 5–10 `.md` or `.py` files
* Make sure the content contains:

  * Function definitions
  * Explanatory text
  * Config files or structured comments

🎯 Goal: Assemble real content to retrieve from

---

## ✅ Exercise 2: Chunk and Embed

* Use `sentence-transformers` to embed 300–500 token chunks
* Save into a FAISS or Chroma index (`corpus_index.faiss` or `chroma/`)
* Test: embed a query and print top 3 matches

🎯 Goal: Build a retriever that works

---

## ✅ Exercise 3: Build Prompt Assembler

* Write a function:

```python
prompt = assemble_prompt(top_chunks, user_query)
```

* Combine 2–3 top results with the user’s input

🎯 Goal: Feed high-context prompts into your model

---

## ✅ Exercise 4: Run the Full RAG Loop

* Accept a question from stdin or hardcoded
* Retrieve relevant docs
* Generate an answer using your model
* Print the full response + context sources

🎯 Goal: End-to-end grounding + generation

---

## ✅ Exercise 5: Evaluate Effectiveness

* Ask 2–3 factual or code-based questions that your base model often hallucinates
* Rerun with and without RAG
* Compare hallucination rate manually

🎯 Goal: Demonstrate the value of retrieval for real-world tasks
