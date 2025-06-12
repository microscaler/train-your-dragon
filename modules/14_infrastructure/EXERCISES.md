# 🧪 Module 12 – Practice Exercises: Scalable Training Infrastructure

Use these exercises to practice launching, monitoring, and recovering training jobs in real or simulated multi-GPU environments.

---

## ✅ Exercise 1: Training Mode Comparison

* Create a markdown table listing:

  * DDP, FSDP, Deepspeed
  * Their pros and cons
  * When you'd use each

🎯 Goal: Choose the right strategy for your use case

---

## ✅ Exercise 2: Launch a Dummy FSDP Job

* Use `torchrun` on a minimal script
* Wrap a tiny model in `FSDP`
* Log batch time, GPU usage, and memory footprint

🎯 Goal: Validate distributed launch mechanics

---

## ✅ Exercise 3: Enable Checkpointing

* Add checkpoint saving to a `Trainer` loop
* Save every N steps and include:

  * Step, loss, timestamp, GPU ID
* Resume from a checkpoint and verify result

🎯 Goal: Ensure your job is restart-safe

---

## ✅ Exercise 4: Measure Memory Usage

* Run with and without:

  * Mixed precision (fp16)
  * Gradient checkpointing
* Record:

  * VRAM used
  * Step/sec
  * Final loss

🎯 Goal: Understand scaling tradeoffs

---

## ✅ Exercise 5: Log Run to Weights & Biases

* Set up `wandb.init()`
* Log:

  * Model size
  * Params/sec
  * Step loss
  * Checkpoint time

🎯 Goal: Learn to track experiments across machines
