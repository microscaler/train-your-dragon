# 🎓 Slide Deck: Module 11 – Data Governance, Licensing & Ethical AI Use

---

## Slide 1: Welcome to Module 10

**Title:** Governing the Data that Governs the Model

> Note: This module shifts focus from model mechanics to the legal and ethical rules that guide dataset use.

---

## Slide 2: Why Governance Matters

* Most LLM risks come from poor dataset choices
* Legal, ethical, and reputational damage is preventable
* Good governance == safer, more sustainable systems

---

## Slide 3: Know Your Licenses

| License      | Use in Training? | Risk Level      |
| ------------ | ---------------- | --------------- |
| MIT / Apache | ✅ Allowed        | Low             |
| GPL          | ⚠️ Risky         | High (copyleft) |
| CC-BY        | ⚠️ Must credit   | Medium          |
| Proprietary  | ❌ Never use      | High            |

---

## Slide 4: Dataset Intake Policy

**Define What You Allow:**

* ✅ Open datasets (MIT, public domain)
* ⚠️ Attribution datasets (CC-BY)
* ❌ Private data, logs, user content

**Document It:**

* Store as `DATA_POLICY.md`
* Add commit history for audits

---

## Slide 5: PII and Secrets Detection

Look for:

* Emails, passwords, phone numbers
* SSH keys, tokens, access URLs

Tools:

* Regex filters
* Microsoft Presidio
* Cleanlab, Tranco list

---

## Slide 6: Redaction Pipeline

* Input → Scanner → Logger → Filtered Output
* Keep `violations.csv` for review
* Add SHA-256 hash to registry

---

## Slide 7: Provenance Logging

Track:

* Dataset name
* Source (URL, Git repo)
* License
* Hash / checksum

Store in:

* `data/registry.jsonl`
* Optional signed registry for audit

---

## Slide 8: Lab Preview – Validator Script

* Scan `.jsonl` or `.md` files
* Flag:

  * PII
  * Invalid license mentions
* Output:

  * `clean.jsonl`
  * `violations.csv`
  * `registry.jsonl`

---

## Slide 9: Model Ethics in Practice

* If it trains on toxic/biased/private data…
* It will repeat or reinforce those patterns
* Filter in → filter out

> Governance = reproducibility + responsibility

---

## Slide 10: Coming Up Next…

**Module 11: Tokenizer Engineering & Vocabulary Optimization**

* Custom vocab for code, domain terms, and multilingual tasks
