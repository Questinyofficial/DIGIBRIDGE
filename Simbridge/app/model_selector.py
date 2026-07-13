"""
app/model_selector.py
---------------------

AI Model Selection Utility.

Responsibilities
----------------
- Discover all trained AI models
- Display available models
- Allow user to select a model
- Update config.json

Does NOT
--------
- Train models
- Load models
- Run predictions
"""

from __future__ import annotations

from pathlib import Path

from app.config_manager import ConfigManager


class ModelSelector:
    """
    Allows the user to choose the active AI model.
    """

    def __init__(self):

        self.config = ConfigManager()

        self.model_directory = Path("models")

    # ---------------------------------------------------------

    def _find_models(self):
        """
        Return every .pkl model inside the models folder.
        """

        if not self.model_directory.exists():
            return []

        models = []

        for file in self.model_directory.glob("*.pkl"):

            # Ignore helper files
            if file.name == "feature_columns.pkl":
                continue

            models.append(file)

        return sorted(models)

    # ---------------------------------------------------------

    @staticmethod
    def _display_name(path: Path) -> str:
        """
        Convert filename into a readable model name.
        """

        return (
            path.stem
            .replace("_", " ")
            .title()
        )

    # ---------------------------------------------------------

    def run(self):

        models = self._find_models()

        print()
        print("=" * 75)
        print("AVAILABLE AI MODELS")
        print("=" * 75)
        print()

        if not models:

            print("No trained AI models were found.")

            input("\nPress ENTER...")

            return

        current_model = Path(
            self.config.get_model()
        ).name

        for index, model in enumerate(models, start=1):

            marker = ""

            if model.name == current_model:
                marker = "   <-- Current"

            print(
                f"[{index}] "
                f"{self._display_name(model)}"
                f"{marker}"
            )

        print()
        print("[0] Cancel")
        print()

        choice = input("Select Model : ").strip()

        if choice == "0":
            return

        if not choice.isdigit():

            print("\nInvalid selection.")

            input("\nPress ENTER...")

            return

        choice = int(choice)

        if choice < 1 or choice > len(models):

            print("\nInvalid selection.")

            input("\nPress ENTER...")

            return

        selected_model = models[choice - 1]

        self.config.set_model(str(selected_model))

        self.config.save()

        print()

        print(
            f"Active AI Model : "
            f"{self._display_name(selected_model)}"
        )

        input("\nPress ENTER...")