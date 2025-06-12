# 🛠️ Module 01: Environment Setup & Tooling

This module ensures you have all tools, libraries, and environment configurations ready to support the entire LLM training workflow—locally or in the cloud.

---

## 🎯 Objectives

By the end of this module, you will:

* Set up Python (via Miniconda) and virtual environments
* Install foundational libraries for training, evaluation, and experimentation
* Validate that your environment supports Jupyter, Unsloth, and Transformers
* Run a test generation from a pre-trained LLM

---

## ✅ Skills Gained

* Environment isolation with `conda`
* Installing GPU-optional Python ML stacks
* Verifying GPU support (if available)
* Running and troubleshooting a simple LLM inference pipeline

---

## 🗂️ Activities

### 1. Choose Your Platform

Choose the operating system you are using and follow the steps below to configure your environment.

#### macOS M1/M2 (Apple Silicon)

```bash
# Install Homebrew if needed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Miniconda
brew install --cask miniconda

# Add Conda to your shell
conda init zsh  # or bash/fish depending on your shell

# Create environment
conda create -n train-your-dragon python=3.10
conda activate train-your-dragon

# Install Python packages
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install transformers accelerate unsloth datasets jupyter peft
```

#### Linux (Ubuntu/Debian/Fedora)

```bash
# Download and install Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Create and activate environment
conda create -n train-your-dragon python=3.10
conda activate train-your-dragon

# Optional: install NVIDIA GPU support
sudo apt install nvidia-cuda-toolkit

# Install required packages
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers accelerate unsloth datasets jupyter peft
```

#### Windows 11 (WSL2 Recommended)

```bash
# Open WSL2 terminal and install Miniconda manually or via script
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Restart terminal then:
conda create -n train-your-dragon python=3.10
conda activate train-your-dragon

# Install required packages
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install transformers accelerate unsloth datasets jupyter peft
```

🧪 **Validation Test**

```python
from transformers import pipeline
pipe = pipeline("text-generation")
print(pipe("The future of coding is")[0]['generated_text'])
```

### 2. Create Conda Environment

```bash
conda create -n train-your-dragon python=3.10
conda activate train-your-dragon
```

### 3. Install Requirements

```bash
pip install -r ../../requirements.txt
```

### 4. Test LLM Inference

```python
from transformers import pipeline
pipe = pipeline("text-generation", model="tiiuae/falcon-rw-1b")
print(pipe("Once upon a time,")[0]['generated_text'])
```

### 5. Open Jupyter or VS Code Notebooks

```bash
jupyter notebook
```

Or use VS Code’s built-in notebook UI.

---

## 🧪 Lab: Inference Test Harness

Write a Python script called `test_inference.py` that:

* Accepts a prompt as CLI argument
* Loads a model from HuggingFace
* Outputs the generated result

Example:

```bash
python test_inference.py "Why use coroutine-based concurrency?"
```

---

## 🧰 Tools Installed

* `transformers`, `accelerate`, `unsloth`
* `torch` (with or without GPU)
* `datasets`, `jupyter`, `peft`
* `wandb` (optional)

---

## 🔗 Linked Modules

* [Module 00: Orientation](../00_orientation/README.md)
* [Module 04: Fine-Tuning](../04_Finetuning_LLMs_%28from_scratch_and_adapters%29/README.md)
* [labs/unsloth\_finetune](../../labs/unsloth_finetune/README.md)

---

## ✅ Completion Checklist

* [ ] Python environment is installed and working
* [ ] Jupyter runs locally
* [ ] I tested model inference successfully
* [ ] I created `test_inference.py` and tested output
* [ ] I understand how to launch notebooks for future modules
