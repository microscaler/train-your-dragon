# 🧪 Module 10 – Practice Exercises: Data Governance & Ethical AI

These exercises will help you define and enforce your own data use policies.

---

## ✅ Exercise 1: Classify Common Licenses

* Create a table with 6 dataset licenses:

  * MIT, Apache-2.0, GPL-3.0, CC-BY-4.0, CC-BY-SA, Proprietary
* Label each with:

  * Usage allowed for LLM training? ✅ / ❌ / ⚠️
  * Attribution required?
  * Risk level: Low / Medium / High

🎯 Goal: Practice evaluating legal exposure

---

## ✅ Exercise 2: Create a `DATA_POLICY.md`

* Write your team’s training data acceptance rules
* Define red/yellow/green zones:

  * ✅ MIT, public domain, permissive
  * ⚠️ CC-BY with credit
  * ❌ GitHub Issues, Discord logs, screenshots

🎯 Goal: Prevent future dataset mistakes

---

## ✅ Exercise 3: Run a Redaction Pass

* Use a regex filter to scan `.jsonl` prompts for:

  * Emails, tokens, phone numbers
  * Any line with both `key` and `secret`
* Output flagged lines to `violations.csv`
* Save the rest to `clean.jsonl`

🎯 Goal: Remove PII and secrets before training

---

## ✅ Exercise 4: Track Dataset Metadata

* For each file in `data/internal_curated/`, record:

  * Name
  * License
  * Author/source
  * SHA256 hash
  * Notes
* Save into `data/registry.jsonl`

🎯 Goal: Create auditable provenance tracking

---

## ✅ Exercise 5: Design an Ethics Checklist

* Make a short pre-flight check before training:

  * [ ] Dataset license is safe
  * [ ] PII filtered
  * [ ] Dataset documented
* Add as `checklist.md` and use before finetuning

🎯 Goal: Normalize safety + ethics across team workflows
