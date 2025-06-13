# Dataset Preparation Checklist

This document lists the datasets and output files referenced by the module notebooks. Use it as a guide when creating placeholder data so the Jupyter labs run without errors.

| Module | Notebook Path | Expected Files & Directories |
|-------|---------------|------------------------------|
|03 Datasets|modules/03_datasets/labs/jupyter_lab.ipynb|`data/custom_training.jsonl`|
|04 Finetuning|modules/04_finetuning/labs/jupyter_lab.ipynb|`data/custom_training.jsonl`, `checkpoints/my_model/`|
|05 Hallucination Control|modules/05_hallucination_control/labs/jupyter_lab.ipynb|`data/hallucination_cases.jsonl`, `checkpoints/my_model/`, `logs/hallucination_eval_results.json` (output)|
|06 Continual Training|modules/06_continual_training/labs/jupyter_lab.ipynb|`logs/hallucination_eval_results.json`, `data/hallucination_corrections.jsonl`, `checkpoints/model_v1.1/`|
|07 Evaluation|modules/07_evaluation/labs/jupyter_lab.ipynb|`data/eval_cases.jsonl`, `checkpoints/model_v1.0/`, `checkpoints/model_v1.1/`|
|08 Deployment|modules/08_deployment/labs/jupyter_lab.ipynb|`data/corpus/` (directory of docs), `checkpoints/my_model/`|
|09 RAG|modules/09_rag/labs/jupyter_lab.ipynb|`data/internal_curated/prompts.jsonl`|
|10 Scaling|modules/10_scaling/labs/jupyter_lab.ipynb|`data/prompt_feedback_log.csv`|
|11 Governance|modules/11_governance/labs/jupyter_lab.ipynb|`data/internal_curated/sample.jsonl`, outputs `data/internal_curated/clean.jsonl`, `data/internal_curated/violations.csv`, `data/registry.jsonl`|
|12 Tokenizer|modules/12_tokenizer/labs/jupyter_lab.ipynb|`data/internal_curated/clean.jsonl`|
|13 Instruction Tuning|modules/13_instruction_tuning/labs/jupyter_lab.ipynb|`data/chat_dataset.jsonl`|
|14 Infrastructure|modules/14_infrastructure/labs/jupyter_lab.ipynb|`checkpoints/sim.ckpt`, `checkpoints/log.json`|
|15 Adversarial|modules/15_adversarial/labs/jupyter_lab.ipynb|`data/redteam_results.jsonl`, `data/redteam_labeled.jsonl`, `checkpoints/my_model/`|
|16 Multiagent|modules/16_multiagent/labs/jupyter_lab.ipynb|`data/internal_curated/clean.jsonl`, helper script also uses `data/hallucination_cases.jsonl`|
|17 Benchmarks|modules/17_benchmarks/labs/jupyter_lab.ipynb|`data/leaderboard.csv`|
|18 LLMOps|modules/18_llmops/labs/jupyter_lab.ipynb|`models/model_v1.0/eval.json`, `models/model_v1.1/eval.json`, writes `models/model_v1.1/metadata.json`|

## Suggested Steps

1. **Create Minimal Examples** – For each path above, add small placeholder files (e.g., a few JSON lines) so notebooks can load data without failing.
2. **Version Control** – Keep generated datasets under `data/`, `logs/`, or `checkpoints/` as shown. Do not commit large or proprietary data.
3. **Iterate After Each Lab** – Many notebooks produce new files (e.g., evaluation logs or cleaned datasets). Ensure these output paths exist to avoid runtime errors.
4. **Organize by Module** – Optionally create subfolders within `data/` to group training, evaluation, and governance examples.
5. **Update This Checklist** – When new modules are added or paths change, update the table so future contributors know which data files are required.

