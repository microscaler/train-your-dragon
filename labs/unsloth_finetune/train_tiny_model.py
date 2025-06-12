# train_tiny_model.py
"""
Train a small LLM using Unsloth for low-memory environments.
Perfect for coroutine-first or prompt pattern datasets.
"""

from unsloth import FastLanguageModel
from transformers import TrainingArguments
from datasets import load_dataset
import torch

# Load a small model like TinyLlama or Zephyr 1.3B
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/zephyr-1.3b-bnb-4bit", # Or TinyLlama
    max_seq_length = 2048,
    dtype = torch.float16,
    load_in_4bit = True
)

FastLanguageModel.for_inference(model)  # Setup for fast generation

# Load your dataset (JSONL-style)
dataset = load_dataset("json", data_files="coroutine_training_data.jsonl")["train"]

# Format prompt → output as expected by Unsloth
def format_example(example):
    return {
        "prompt": example["instruction"],
        "completion": example["output"]
    }

dataset = dataset.map(format_example)

# Training parameters
args = TrainingArguments(
    output_dir = "./checkpoints/coroutine-llm",
    per_device_train_batch_size = 2,
    gradient_accumulation_steps = 2,
    num_train_epochs = 3,
    warmup_steps = 10,
    logging_steps = 10,
    learning_rate = 2e-5,
    bf16 = False,
    fp16 = True,
    save_total_limit = 2,
    save_strategy = "epoch",
    report_to = "none"
)

# Launch training
model.train_model(
    dataset = dataset,
    args = args,
)
