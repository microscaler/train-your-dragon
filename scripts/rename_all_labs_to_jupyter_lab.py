#!/usr/bin/env python3
import os
from pathlib import Path
import shutil

# Base path where all modules are stored
base = Path("./modules")

# Traverse all labs folders within module directories
for module_dir in base.glob("*"):
    lab_dir = module_dir / "labs"
    if lab_dir.exists() and lab_dir.is_dir():
        ipynb_files = list(lab_dir.glob("*.ipynb"))
        if not ipynb_files:
            # Also search one level deeper (nested lab dirs)
            ipynb_files = list(lab_dir.glob("*/**/*.ipynb"))

        for old_path in ipynb_files:
            target = old_path.parent / "jupyter_lab.ipynb"
            if old_path.name != "jupyter_lab.ipynb":
                print(f"Renaming: {old_path} → {target}")
                old_path.rename(target)
