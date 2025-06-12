# 🧪 Module 12 Quiz: Scalable Training Infrastructure

Test your understanding of distributed training and infrastructure choices.

---

### ✅ Instructions

Choose the best answer per question. Reflect in your notes for scenario-based questions.

---

### 1. Which training strategy is most memory-efficient?

A. DDP
B. DataLoader Parallel
C. FSDP
D. Single-GPU only

**Correct Answer:** C

---

### 2. What does `torchrun` help you do?

A. Visualize loss graphs
B. Launch multi-process training jobs
C. Tune hyperparameters
D. Create checkpoints

**Correct Answer:** B

---

### 3. What should be included in a `.ckpt` file?

A. Only model weights
B. Model weights, step info, metrics, and environment info
C. Your `.env` secrets
D. Gradients and temporary RAM state

**Correct Answer:** B

---

### 4. What technique helps reduce GPU memory use during training?

A. Lower learning rate
B. Increase epoch count
C. Gradient checkpointing
D. Disable dropout

**Correct Answer:** C

---

### 5. Reflection:

> Which setup do you expect to use in practice: local single-GPU, multi-GPU workstation, or cloud-based node cluster? Why?
