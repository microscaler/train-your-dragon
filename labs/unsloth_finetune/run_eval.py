# run_eval.py
"""
Simple evaluation script for pass@k, hallucination scoring, and instruction fidelity.
Adapt as needed for your domain.
"""

import json
from transformers import pipeline

model_path = "./checkpoints/coroutine-llm"
generator = pipeline("text-generation", model=model_path)

# Load test prompts
with open("coroutine_eval_prompts.jsonl") as f:
    eval_set = [json.loads(line) for line in f]

# Output bucket
results = []

for entry in eval_set:
    prompt = entry["instruction"]
    expected = entry.get("reference_answer", "")
    result = generator(prompt, max_new_tokens=256, do_sample=False)[0]["generated_text"]

    # Basic scoring placeholder
    hallucinated = "ERROR" in result or "undefined" in result
    matched = expected.strip() in result

    results.append({
        "prompt": prompt,
        "expected": expected,
        "generated": result,
        "matched": matched,
        "hallucination": hallucinated
    })

# Save results
with open("eval_results.json", "w") as out:
    json.dump(results, out, indent=2)

print("✅ Evaluation complete.")
