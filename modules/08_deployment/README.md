# 🔍 Module 08: Retrieval-Augmented Generation (RAG)

In this module, you’ll teach your LLM to fetch information from external sources instead of hallucinating it. You’ll build a mini RAG system that grounds responses in real documents.

---

## 🎯 Objectives

By the end of this module, you will:

* Understand the architecture and benefits of RAG
* Create an embedding-powered document retriever
* Connect retrieval results to prompt generation
* Run a full RAG-enhanced question-answering pipeline

---

## ✅ Skills Gained

* Chunking and embedding documents
* Using FAISS or Chroma for similarity search
* Augmenting prompts with retrieval context
* Building simple search-backed assistants

---

## 🗂️ Activities

### 1. What Is RAG?

* RAG = Retrieval-Augmented Generation
* Combines search engine + LLM to answer queries
* Reduces hallucination and improves factual accuracy

### 2. Prepare Your Document Corpus

* Collect Markdown, API docs, or `.py`/`.rs` files
* Chunk into \~300–500 token segments
* Save chunks to `data/corpus/`

### 3. Embed and Index

* Use `sentence-transformers` or OpenAI embedding models
* Build a FAISS or Chroma vector index
* Save as `data/corpus_index.faiss` or `chroma/`

### 4. Retrieval + Prompt Assembly

* For each user query:

  * Embed the query
  * Retrieve top-k similar chunks
  * Assemble full prompt with `retrieved_docs + user_query`

### 5. Run the RAG Loop

* Send augmented prompt to your fine-tuned model
* Optionally return citations from documents

---

## 🧪 Lab: Build a Local RAG Assistant

1. Prepare a folder of `.md` and `.py` docs
2. Chunk and embed them
3. Create a retriever that returns top 3 matches
4. Use them to answer queries like:

   * “How does the `coroutine` decorator work?”
   * “Show me where `go!` is used in the Rust examples.”

Bonus:

* Stream responses with `streamlit` or `gradio`
* Add a CLI tool (`rag_query.py`)

---

## 🔗 Linked Modules

* [Module 05: Hallucinations](../05_hallucination_control/README.md)
* [Module 07: Evaluation](../07_Evaluation_&_Alignment/README.md)
* [Module 09: Teaching & Scaling](../10_Teaching_&_Scaling_LLMDevelopment_in_Your_Org/README.md)

---

## ✅ Completion Checklist

* [ ] I understand what RAG is and how it works
* [ ] I built a document retriever and index
* [ ] I assembled prompts with real retrieved context
* [ ] I ran RAG-augmented completions successfully
* [ ] I’m ready to expand RAG into IDE or chatbot tooling
