# 🎓 Slide Deck: Module 12 – Scalable Training Infrastructure

---

## Slide 1: Welcome to Module 12

**Title:** Training Models Beyond a Single GPU

> Note: You’ve learned how to fine-tune. Now learn how to do it at scale.

---

## Slide 2: Why Multi-GPU and Multi-Node Matter

* Modern models exceed 16–32GB easily
* Faster training = more iteration = better models
* Efficient scaling saves 💰 and time

---

## Slide 3: Distributed Training Strategies

| Strategy  | Description            | Memory Efficiency | Setup Difficulty |
| --------- | ---------------------- | ----------------- | ---------------- |
| DDP       | Full model on each GPU | ❌                 | ✅                |
| FSDP      | Sharded model state    | ✅✅                | ⚠️               |
| Deepspeed | Hybrid + CPU/Offload   | ✅✅✅               | ⚠️⚠️             |

---

## Slide 4: Training Optimization Techniques

* Mixed precision (fp16 / bf16)
* Gradient checkpointing
* CPU Offload / Sharded State
* Small batch accumulation + logging

---

## Slide 5: Launching Distributed Jobs

* Use `torchrun` or `accelerate`
* Pass `--nproc_per_node=N`
* Initialize `process_group` in script
* Wrap model with DDP/FSDP as needed

---

## Slide 6: Memory & Throughput Profiling

* Use `nvidia-smi`, `torch.cuda.memory_allocated()`
* Log with:

  * Weights & Biases
  * CSV / JSON logs
* Monitor steps/sec and VRAM usage

---

## Slide 7: Checkpointing Best Practices

* Save `.ckpt` every N steps
* Log:

  * Epoch, loss, batch size
  * Hardware / device ID
  * Timestamp + hostname
* Resume with `--resume_from_checkpoint`

---

## Slide 8: Lab – Simulated Multi-GPU Run

1. Train on FSDP with 2 GPUs (real or fake)
2. Interrupt (e.g. KeyboardInterrupt)
3. Resume from latest `.ckpt`
4. Check metrics integrity

---

## Slide 9: Tools to Explore

* HuggingFace Accelerate
* Lightning Trainer
* Deepspeed CLI launcher
* Weights & Biases, Comet.ml

---

## Slide 10: Coming Up Next…

**Module 13: Adversarial Testing & Robustness**

* How your model behaves under pressure
* Red-teaming LLMs with edge-case prompts
