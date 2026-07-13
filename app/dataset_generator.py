"""
app/dataset_generator.py
------------------------

Launches the Bridge Dataset Generator.

Responsibilities
----------------
- Verify dataset generation script exists
- Launch dataset generation
- Display execution status
- Report success or failure

Does NOT
--------
- Generate datasets itself
- Train AI models
- Perform predictions
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path


class DatasetGenerator:
    """
    Launches the dataset generation script.
    """

    def __init__(self):

        self.generator_script = Path(
            "dataset_generator/generate_dataset.py"
        )

    # ---------------------------------------------------------

    def run(self):

        print()
        print("=" * 78)
        print("BRIDGE DATASET GENERATOR")
        print("=" * 78)
        print()

        # -----------------------------------------------------
        # Verify script exists
        # -----------------------------------------------------

        if not self.generator_script.exists():

            print("ERROR")
            print()
            print("Dataset generator script not found.")
            print(self.generator_script)

            input("\nPress ENTER...")
            return

        print("Dataset Generator")
        print(f"    {self.generator_script}")

        print()
        print("Generating training dataset...")
        print("This may take several seconds.")
        print()

        start = time.perf_counter()

        try:

            subprocess.run(

                [sys.executable, str(self.generator_script)],

                check=True

            )

        except subprocess.CalledProcessError:

            print()
            print("=" * 78)
            print("DATASET GENERATION FAILED")
            print("=" * 78)

            input("\nPress ENTER...")
            return

        elapsed = time.perf_counter() - start

        print()
        print("=" * 78)
        print("DATASET GENERATED SUCCESSFULLY")
        print("=" * 78)
        print()

        print(f"Execution Time : {elapsed:.2f} seconds")
        print()
        print("Dataset generation completed successfully.")
        print("You can now train a new AI model using the")
        print("'Train AI Model' option from the launcher.")

        input("\nPress ENTER...")