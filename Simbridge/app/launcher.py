"""
app/launcher.py
---------------

Main launcher for DigiBridge.

Responsibilities
----------------
- Display startup banner
- Display system status
- Display main menu
- Dispatch user actions

Does NOT:
- Run the Digital Twin directly
- Perform AI prediction
- Read serial ports
- Train models
"""

from __future__ import annotations

import os

from app.startup import show_banner
from app.status import Status

from app.application import Application
from app.bridge_selector import BridgeSelector
from app.model_selector import ModelSelector

from app.trainer import Trainer
from app.dataset_generator import DatasetGenerator

from app.diagnostics import Diagnostics
from app.project_info import ProjectInfo
from app.cleaner import Cleaner


class Launcher:
    """
    DigiBridge launcher.
    """

    def __init__(self):

        self.running = True

    # ---------------------------------------------------------

    @staticmethod
    def clear():

        os.system("cls" if os.name == "nt" else "clear")

    # ---------------------------------------------------------

    def display(self):

        self.clear()

        show_banner()

        Status.show()

        print("=" * 78)
        print("MAIN MENU")
        print("=" * 78)
        print()

        print("[1] Launch Live Digital Twin")
        print("[2] Select Bridge Model")
        print("[3] Select AI Model")
        print("[4] Train AI Model")
        print("[5] Generate Training Dataset")
        print("[6] Hardware Diagnostics")
        print("[7] Run System Tests")
        print("[8] Project Information")
        print("[9] Clean Generated Files")
        print("[10] Exit")

        print()

    # ---------------------------------------------------------

    def run(self):

        while self.running:

            self.display()

            choice = input("Enter Choice : ").strip()

            if choice == "1":

                self.launch_application()

            elif choice == "2":

                BridgeSelector().run()

            elif choice == "3":

                ModelSelector().run()

            elif choice == "4":

                Trainer().run()

            elif choice == "5":

                DatasetGenerator().run()

            elif choice == "6":

                Diagnostics().run()

            elif choice == "7":

                self.run_tests()

            elif choice == "8":

                ProjectInfo.show()

            elif choice == "9":

                Cleaner().run()

            elif choice == "10":

                self.exit()

            else:

                print()

                print("Invalid selection.")

                input("\nPress ENTER...")

    # ---------------------------------------------------------

    @staticmethod
    def launch_application():

        Application().run()

    # ---------------------------------------------------------

    @staticmethod
    def run_tests():

        os.system("python run_tests.py")

        input("\nPress ENTER...")

    # ---------------------------------------------------------

    def exit(self):

        print()

        print("Thank you for using DigiBridge.")

        self.running = False


# =============================================================
# Entry Point
# =============================================================

if __name__ == "__main__":

    Launcher().run()