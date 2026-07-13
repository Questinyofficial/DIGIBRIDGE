"""
app/bridge_selector.py
----------------------

Bridge selection utility.

Responsibilities
----------------
- Discover all bridge JSON files
- Display available bridges
- Allow the user to select one
- Update config.json

Does NOT
--------
- Load the bridge
- Validate bridge contents
- Start the application
"""

from __future__ import annotations

from pathlib import Path

from app.config_manager import ConfigManager


class BridgeSelector:
    """
    Handles bridge selection.
    """

    def __init__(self):

        self.config = ConfigManager()

        self.bridge_directory = Path("data/bridges")

    # ---------------------------------------------------------

    def _find_bridges(self):
        """
        Return all bridge JSON files.
        """

        if not self.bridge_directory.exists():

            return []

        return sorted(self.bridge_directory.glob("*.json"))

    # ---------------------------------------------------------

    @staticmethod
    def _display_name(path: Path) -> str:
        """
        Convert filename into a readable bridge name.
        """

        return (
            path.stem
            .replace("_", " ")
            .title()
        )

    # ---------------------------------------------------------

    def run(self):

        bridges = self._find_bridges()

        print("\n")
        print("=" * 75)
        print("AVAILABLE BRIDGE MODELS")
        print("=" * 75)
        print()

        if not bridges:

            print("No bridge files were found.")
            input("\nPress ENTER...")
            return

        current_bridge = Path(
            self.config.get_bridge()
        ).name

        for index, bridge in enumerate(bridges, start=1):

            marker = ""

            if bridge.name == current_bridge:
                marker = "   <-- Current"

            print(
                f"[{index}] "
                f"{self._display_name(bridge)}"
                f"{marker}"
            )

        print()
        print("[0] Cancel")
        print()

        # -----------------------------------------------------

        choice = input(
            "Select Bridge : "
        ).strip()

        if choice == "0":

            return

        if not choice.isdigit():

            print("\nInvalid selection.")
            input("\nPress ENTER...")
            return

        choice = int(choice)

        if choice < 1 or choice > len(bridges):

            print("\nInvalid selection.")
            input("\nPress ENTER...")
            return

        selected_bridge = bridges[choice - 1]

        self.config.set_bridge(
            str(selected_bridge)
        )

        self.config.save()

        print()
        print(
            f"Bridge changed to:"
        )

        print(
            f"{self._display_name(selected_bridge)}"
        )

        input("\nPress ENTER...")