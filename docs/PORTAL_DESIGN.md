# 📘 Final Exam Architecture for "Train Your Dragon"

This document outlines the full design for the Final Exam system used to assess learners' retention and performance at the end of the "Train Your Dragon" LLM training course.

---

## 🎯 Purpose

To deliver a secure, scalable, and verifiable 90-question final exam containing *entirely new* questions not seen during the module quizzes. The exam results will be used for certification issuance and audit.

---

## 🧱 System Components

### Frontend (Local)

* **Platform**: Streamlit tab embedded in the local course app
* **Location**: Runs on learner's local machine (same as notebooks)
* **Features**:

  * One question at a time
  * Answer locking (no back navigation)
  * Auto-save of responses (locally and remotely)
  * Final score + certificate request trigger

### Backend (Cloud)

* **Platform**: FastAPI + gRPC
* **Hosting**: Google Cloud App Engine
* **Database**: Supabase
* **Auth**: Supabase Auth (magic link or OAuth)
* **Endpoints**:

  * `GetQuestion(user_id, index) → Question`
  * `SubmitAnswer(user_id, index, answer) → Ack`
  * `GetResult(user_id) → Score + Pass/Fail`

---

## 🔐 Authentication Flow

1. Learner logs in via Supabase (email + magic link)
2. Receives session token or JWT
3. Frontend stores token in session and sends with all requests
4. Supabase RLS policies enforce per-user data isolation

---

## 🗃 Data Model

### `questions`

* `id` UUID
* `text` string
* `options` array
* `correct_answer` string (hidden from client)
* `module_tag` optional

### `responses`

* `user_id`
* `question_id`
* `answer`
* `submitted_at`

### `users`

* Managed via Supabase Auth

### `scores`

* `user_id`
* `total_score`
* `passed` boolean
* `cert_generated_at`

---

## 🧪 Exam Logic

* 90 random questions served from backend
* Questions tracked with index and ID
* Each answer submitted immediately
* No ability to skip or go back
* Timer optional (e.g. 90m total)
* Pass threshold: 75% (67/90)

---

## 🎓 Certificate Generation

* If passed:

  * Trigger backend certificate record
  * Return a downloadable PDF or email link
* Include:

  * Learner name
  * Serial number
  * Date
  * Score breakdown

---

## 🧰 Deployment

* **Backend**: GCP App Engine with HTTPS
* **Frontend**: Local Streamlit app
* **DB**: Supabase Postgres with RLS enabled
* **Exam Entry Point**: New tab in `streamlit_main.py`

---

## 🧭 Next Steps

1. Generate `.proto` file for gRPC backend
2. Scaffold `exam_backend.py` with FastAPI + grpcio
3. Add Supabase schema and API key integration
4. Build frontend exam runner in Streamlit
5. Integrate certificate PDF generation
