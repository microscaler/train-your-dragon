# 🎓 Slide Deck: Module 08 – Retrieval-Augmented Generation (RAG)

---

## Slide 1: Welcome to Module 08

**Title:** Teaching Your LLM to Look Things Up

> Note: This module shifts from generation to grounded augmentation. Learners build a smarter assistant that relies on real facts.

---

## Slide 2: What Is RAG?

* **Retrieval-Augmented Generation** combines:

  * Vector search (retriever)
  * Prompt assembly (context injection)
  * LLM generation
* Solves: hallucination, outdated knowledge, domain-specific accuracy

---

## Slide 3: Why Use RAG?

* Use external docs without fine-tuning
* Avoid hallucinating function names, versions, config keys
* Build assistants that are:

  * Searchable
  * Cite-able
  * Lightweight to update

---

## Slide 4: RAG Architecture (Simple)

1. User asks question
2. Query is embedded (vectorized)
3. Search corpus for similar chunks
4. Assembled into prompt
5. Model responds

> Note: Show a flowchart or diagram if possible.

---

## Slide 5: Chunking and Embedding

* Split documents into small token windows (\~300–500 tokens)
* Use embedding models (e.g. `sentence-transformers`, `text-embedding-ada-002`)
* Store chunks in:

  * FAISS (simple, local)
  * ChromaDB (open source)
  * Weaviate (cloud-scale)

---

## Slide 6: Prompt Assembly

* Prompt = `\n\n<chunk_1>\n<chunk_2>\n...\n<user_query>`
* Inject as part of `system` or preamble
* Keep total tokens < model context limit

---

## Slide 7: RAG Query Loop

* Embed user query
* Search index for top-k relevant chunks
* Combine with query
* Send to model
* Return answer and citations

---

## Slide 8: Lab – Local RAG Assistant

Task:

* Load `.md`, `.py`, or `.rs` files
* Embed and index
* Accept user input and return grounded completions

Bonus:

* Stream with `gradio` or `streamlit`
* Return chunk source metadata

---

## Slide 9: RAG in Practice

| Use Case       | Corpus         | Model Role                  |
| -------------- | -------------- | --------------------------- |
| Doc assistant  | Markdown docs  | Answer questions w/ context |
| Code assistant | Project source | Find usages, explain APIs   |
| QA chatbot     | Knowledge base | Explain policy, flow, etc.  |

---

## Slide 10: Coming Up Next…

**Module 09: Teaching & Scaling LLMs in Teams**

* Train teammates to use, improve, and contribute to your AI stack
