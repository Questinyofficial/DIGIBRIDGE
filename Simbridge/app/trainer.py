"""
app/trainer.py
--------------

Launches the AI model training process.

Responsibilities
----------------
- Verify training script exists
- Launch model training
- Display execution status
- Report success or failure

Does NOT
--------
- Implement machine learning
- Generate datasets
- Load trained models
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path


class Trainer:
    """
    Launches the model training script.
    """

    def __init__(self):

        self.training_script = Path("models/train_model.py")

    # ---------------------------------------------------------

    def run(self):

        print()
        print("=" * 78)
        print("AI MODEL TRAINING")
        print("=" * 78)
        print()

        # -----------------------------------------------------
        # Verify script exists
        # -----------------------------------------------------

        if not self.training_script.exists():

            print("ERROR")
            print()
            print("Training script not found.")
            print(self.training_script)

            input("\nPress ENTER...")
            return

        print("Training Script")
        print(f"    {self.training_script}")

        print()
        print("Starting training...")
        print()

        start = time.perf_counter()

        try:

            result = subprocess.run(

                [sys.executable, str(self.training_script)],

                check=True

            )

        except subprocess.CalledProcessError:

            print()
            print("=" * 78)
            print("TRAINING FAILED")
            print("=" * 78)

            input("\nPress ENTER...")
            return

        elapsed = time.perf_counter() - start

        print()
        print("=" * 78)
        print("TRAINING COMPLETED SUCCESSFULLY")
        print("=" * 78)

        print()

        print(f"Execution Time : {elapsed:.2f} seconds")

        print()

        print("The trained model has been saved.")

        input("\nPress ENTER...")