# ───────────────
# 🐉 Train Your Dragon - Justfile
# ───────────────

# Set Python env if needed
set dotenv-load := true

default:
    just --summary


# 🛠 Setup
setup:
    python3 -m venv .venv
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
