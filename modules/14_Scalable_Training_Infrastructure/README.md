# ⚙️ Module 14: Scalable Training Infrastructure

This module shows how to prepare and run training jobs at scale: from single-GPU laptops to multi-GPU servers or clusters. You'll learn how to optimize memory, distribute data, and recover from interruptions.

---

## 🎯 Objectives

By the end of this module, you will:

* Understand distributed training strategies (DDP, FSDP, Deepspeed)
* Apply memory-saving techniques to train larger models
* Configure a training run for a multi-GPU or multi-node setup
* Track and resume jobs across hardware or cloud runs

---

## ✅ Skills Gained

* Launching distributed training jobs with `torchrun`
* Using gradient checkpointing and mixed precision
* Memory profiling and optimizer strategies
* Checkpointing and fault recovery

---

## 🗂️ Activities

### 1. Compare Training Modes

| Strategy  | Use Case                    | Pros                    | Cons                    |
| --------- | --------------------------- | ----------------------- | ----------------------- |
| DDP       | Most standard multi-GPU     | Easy to configure       | Memory duplication      |
| FSDP      | Sharded model parallelism   | Efficient memory use    | Slower startup, complex |
| Deepspeed | Optimized sharded + offload | Train very large models | Requires config tuning  |

---

### 2. Optimize Memory Footprint

* Enable:

  * `bf16` or `fp16` mixed precision
  * Gradient checkpointing
  * CPU offload (FSDP, Deepspeed)
* Log RAM, VRAM, and throughput

---

### 3. Setup Distributed Runs

* Use `torchrun` or `accelerate launch`
* Pass:

  * `--nproc_per_node`, `--rdzv_backend=static`, etc.
* Enable process\_group init and DDP wrappers

---

### 4. Checkpointing & Fault Tolerance

* Save `state_dict()` every N steps
* Write `.ckpt` and `.json` with:

  * epoch, step, loss, metrics
  * hostname / hardware
* Resume on crash or reboot with `--resume_from_checkpoint`

---

## 🧪 Lab: Multi-GPU Sim Demo

1. Create a config: `configs/fsdp_2gpu.yaml`
2. Train a small model with FSDP and checkpointing
3. Simulate crash with `KeyboardInterrupt`
4. Resume and verify integrity

Bonus:

* Add Weights & Biases logging
* Try training with ZeRO3 or Megatron core

---

## 🔗 Linked Modules

* [Module 04: Fine-tuning LLMs](../04_Finetuning_LLMs_%28from_scratch_and_adapters%29/README.md)
* [Module 14: Infrastructure](../14_Scalable_Training_Infrastructure/README.md)
* [Module 18: LLMOps](../18_LLMOps_&_Model_Lifecycle_Management/README.md)

---

## ✅ Completion Checklist

* [ ] I configured and launched a multi-GPU training job
* [ ] I enabled memory-saving strategies (e.g. fp16, checkpointing)
* [ ] I logged key metrics like RAM, time, and step losses
* [ ] I implemented basic checkpoint + resume logic
* [ ] I understand which training mode suits my use case
