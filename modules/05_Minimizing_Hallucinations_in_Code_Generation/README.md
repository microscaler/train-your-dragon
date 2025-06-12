# 🧠 Module 05: Minimizing Hallucinations in Code Generation

In this module, you'll learn what causes LLM hallucinations—especially in code—and how to design training, prompts, and evaluation strategies to reduce them.

---

## 🎯 Objectives

By the end of this module, you will:

* Understand the causes of hallucinations in LLMs
* Learn how to reduce hallucination through better data, prompts, and evaluation
* Design and run hallucination-resistance tests
* Improve confidence in your model’s answers

---

## ✅ Skills Gained

* Identifying hallucination patterns in code responses
* Designing prompts that encourage grounded responses
* Testing LLM output against known ground truth
* Logging hallucination rates and quality over time

---

## 🗂️ Activities

### 1. Read: What Is Hallucination?

* A hallucination is when the model confidently generates false or unverifiable information
* In code, this may include:

  * Calling nonexistent functions
  * Using APIs incorrectly
  * Fabricating syntax

### 2. Review Examples of Hallucination

Explore samples in `data/hallucination_cases.jsonl` (or generate your own):

* Run your model on known test prompts
* Record whether it generates misleading or invalid responses

### 3. Design Prompts to Minimize Hallucination

Strategies:

* Explicit instructions: “Use only standard library”
* Chain-of-thought: “First explain, then code”
* Retrieval-augmented prompts (covered in Module 7.5)

### 4. Test With `evaluate_model.ipynb`

Add metadata to results:

```python
{ "hallucinated": True, "reason": "Incorrect API call to nonexistent function" }
```

---

## 🧪 Lab: Hallucination Tracker

1. Choose 10 prompts with known correct answers
2. Generate completions using your model
3. Score each as: ✅ correct, ⚠️ partially correct, ❌ hallucinated
4. Create a simple bar chart with counts per category

Bonus:

* Log `pass@k` if using multiple completions
* Track regression/improvement over model versions

---

## 🔗 Linked Modules

* [Module 04: Fine-Tuning](../04_Finetuning_LLMs_%28from_scratch_and_adapters%29/README.md)
* [Module 07: Evaluation & Alignment](../07_Evaluation_&_Alignment/README.md)
* [Module 09: Retrieval-Augmented Generation (RAG)](../09_Retrieval-Augmented_Generation_%28RAG%29_for_Developer_Workflows/README.md)

---

## ✅ Completion Checklist

* [ ] I understand how LLMs hallucinate, especially in code
* [ ] I’ve reviewed known hallucination patterns
* [ ] I’ve tested my model with a labeled prompt set
* [ ] I’ve scored outputs and visualized the results
* [ ] I feel confident building safer prompts or training data
