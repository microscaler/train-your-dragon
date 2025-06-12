# 📌 Backlog: Post-Course Enhancements

This document tracks future improvements and features to implement once all modules and quizzes are complete.

---

## ✅ Quiz System Enhancements

### 1. Secure Answer Handling

* Parse and extract answers from `QUIZ.md` into a runtime `answers.json` file
* Hide answers from learners by not storing them in clear text within the markdown
* Optional: Encrypt `answers.json` or use obfuscation

### 2. Quiz Result Storage

* Store scores in `logs/quiz_scores.csv`
* Track date, module, user ID (optional), and score
* Aggregate performance across modules

### 3. Certification or Completion Export

* If learner passes 80% of modules, generate certificate of completion
* PDF export with name and completion date

---

## 🔜 Future Streamlit/Gradio Enhancements

* Add chat memory and user profile session to RAG assistant
* Enable SLIDES.md browser presentation mode
* Interactive walkthroughs for EXERCISES.md

---

## 💼 Monetization & Certification Portal

### 4. SolidJS Brochure Website

* Build a public-facing marketing site using SolidJS
* Include:

  * Overview of the course and outcomes
  * Executive summary for hiring managers / recruiters
  * Certificate verification lookup by serial number
  * Candidate profile page if opted-in
  * Secure server-side certificate validation endpoint

### 5. Certificate Generation Flow

* Generate certificate PDF upon course completion with unique serial ID
* Embed learner name, date, module completion stats
* Validate via QR or public lookup tool

---

### 🧪 Unified Streamlit App Launcher

### Multi-Notebook Launcher App

- Build a single Streamlit interface in ./scripts directory
- Allow user to select and launch any lab notebook via dropdown
- Optionally track module usage analytics or quiz linkage

---
## ✍️ Notes

* All backlog items are paused until core course content is complete
* Tag backlog issues with `type::enhancement` in GitHub for prioritization
