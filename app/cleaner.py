"""
app/cleaner.py
--------------

Cleans generated DigiBridge files.

Responsibilities
----------------
- Remove Python cache
- Remove temporary files
- Remove log files
- Remove generated reports
- Optionally remove datasets
- Optionally remove trained models

Does NOT
--------
- Delete source code
- Delete bridge models
- Delete configuration
"""

from __future__ import annotations

import shutil
from pathlib import Path


class Cleaner:

    def __init__(self):

        self.deleted = 0

    # ---------------------------------------------------------

    def _delete_file(self, path: Path):

        if path.exists():

            path.unlink()

            self.deleted += 1

            print(f"Deleted File : {path}")

    # ---------------------------------------------------------

    def _delete_directory(self, path: Path):

        if path.exists():

            shutil.rmtree(path)

            self.deleted += 1

            print(f"Deleted Folder : {path}")

    # ---------------------------------------------------------

    def clean_cache(self):

        print("\nRemoving Python cache...\n")

        for folder in Path(".").rglob("__pycache__"):

            self._delete_directory(folder)

        for file in Path(".").rglob("*.pyc"):

            self._delete_file(file)

    # ---------------------------------------------------------

    def clean_logs(self):

        print("\nRemoving log files...\n")

        for file in Path(".").rglob("*.log"):

            self._delete_file(file)

    # ---------------------------------------------------------

    def clean_reports(self):

        reports = Path("reports")

        if reports.exists():

            self._delete_directory(reports)

    # ---------------------------------------------------------

    def clean_temp(self):

        print("\nRemoving temporary files...\n")

        for extension in [

            "*.tmp",

            "*.bak",

            "*.old",

            "*.temp"

        ]:

            for file in Path(".").rglob(extension):

                self._delete_file(file)

    # ---------------------------------------------------------

    def clean_dataset(self):

        dataset = Path(
            "data/datasets/bridge_dataset.csv"
        )

        self._delete_file(dataset)

    # ---------------------------------------------------------

    def clean_models(self):

        print()

        choice = input(
            "Delete trained AI models? (y/n) : "
        ).lower()

        if choice != "y":

            return

        models = Path("models")

        if not models.exists():

            return

        for model in models.glob("*.pkl"):

            if model.name == "feature_columns.pkl":

                continue

            self._delete_file(model)

        for metadata in models.glob("*metadata.json"):

            self._delete_file(metadata)

    # ---------------------------------------------------------

    def run(self):

        print()
        print("=" * 78)
        print("DIGIBRIDGE CLEANER")
        print("=" * 78)

        print()
        print("This utility removes generated files only.")
        print("Your source code and bridge models are safe.")
        print()

        confirm = input(
            "Continue? (y/n) : "
        ).lower()

        if confirm != "y":

            return

        self.clean_cache()

        self.clean_logs()

        self.clean_reports()

        self.clean_temp()

        self.clean_dataset()

        self.clean_models()

        print()

        print("=" * 78)

        print(
            f"Cleaning completed.\n"
            f"Items removed : {self.deleted}"
        )

        print("=" * 78)

        input("\nPress ENTER...")