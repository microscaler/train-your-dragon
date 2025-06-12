# ───────────────
# 🐉 Train Your Dragon - Justfile
# ───────────────

# Set Python env if needed
set dotenv-load := true

default:
    just --summary


# 🛠 Setup
setup-python:
    python3 -m venv .venv

install-req:
    source .venv/bin/activate && pip install -r requirements.txt

activate:
	conda activate train-your-dragon

# ✅ Run test finetune
train-test:
    python labs/unsloth_finetune/train_tiny_model.py

# 🧪 Run eval loop
eval:
    python labs/eval_test_harness/run_eval.py

# 🧹 Clean outputs
clean:
    rm -rf checkpoints/ outputs/ logs/

venv:
	conda create -n train-your-dragon python=3.10

notebook:
	jupyter notebook labs/unsloth_finetune/

quiz MODULE:
	streamlit run scripts/quiz_web_app.py -- --module {{MODULE}}

# Start Docker Compose
start-dev:
	docker-compose -f docker-compose.yml up --build

# Stop containers
stop-dev:
	docker-compose -f docker-compose.yml down

# Seed Supabase with schema and questions
seed-db:
	docker exec -i supabase-db psql -U postgres -d postgres < scripts/grpc/schema.sql
	docker exec -i supabase-db psql -U postgres -d postgres < scripts/grpc/supabase_seed_questions.sql

# Rebuild only backend service
build-backend:
	docker-compose -f docker-compose.yml build exam-backend

# Test certificate PDF generation
build-cert:
	python3 scripts/certificate_generator.py
