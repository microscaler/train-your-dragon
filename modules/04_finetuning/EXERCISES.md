# 🧪 Module 04 – Practice Exercises: Fine-Tuning with Unsloth

These self-paced exercises help reinforce key skills in configuring and executing fine-tuning workflows.

---

## ✅ Exercise 1: Train on 1 Example (Debug Run)

* Create a `.jsonl` file with a single, known-good example
* Run `train_model.ipynb` using `num_train_epochs = 1`
* Confirm the model memorizes the output exactly

🎯 **Goal:** Understand overfitting as a way to debug training pipeline

---

## ✅ Exercise 2: Try a Different Base Model

* Replace Zephyr with another LoRA-compatible model (e.g., TinyLlama or DeepSeek)
* Modify `model_name` in the notebook or script
* Note any VRAM or performance differences

🎯 **Goal:** Learn how model choice affects memory and speed

---

## ✅ Exercise 3: Modify Training Parameters

* Change `per_device_train_batch_size`, `num_train_epochs`, and `learning_rate`
* Observe effects on training time and final loss

🎯 **Goal:** Develop intuition for hyperparameter tuning

---

## ✅ Exercise 4: Add `wandb` Logging

* Install with `pip install wandb`
* Add `report_to="wandb"` in `TrainingArguments`
* Watch metrics in real-time at [wandb.ai](https://wandb.ai)

🎯 **Goal:** Learn to monitor training with external tools

---

## ✅ Exercise 5: Reload and Test Model from Checkpoint

* Use `from_pretrained()` to load your saved model
* Generate completions from test prompts in `evaluate_model.ipynb`

🎯 **Goal:** Verify you can recover, reuse, and share trained models
