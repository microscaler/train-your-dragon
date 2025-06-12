import json
from pathlib import Path
from transformers import pipeline

# Load test cases
with open("data/hallucination_cases.jsonl") as f:
    cases = json.load(f)["cases"]

# Load model (adjust path or model_id as needed)
generator = pipeline("text-generation", model="./checkpoints/my_model")

results = []

for case in cases:
    prompt = case["instruction"]
    expected = case["expected"]
    model_output = generator(prompt, max_new_tokens=128)[0]["generated_text"]

    hallucinated = case["expected"] not in model_output

    results.append({
        "instruction": prompt,
        "expected": expected,
        "output": model_output,
        "hallucinated": hallucinated,
        "reason": case["reason"] if hallucinated else ""
    })

# Save to results file
Path("logs").mkdir(exist_ok=True)
with open("logs/hallucination_check_results.json", "w") as out:
    json.dump(results, out, indent=2)

print(f"✅ Checked {len(results)} cases. See logs/hallucination_check_results.json")
