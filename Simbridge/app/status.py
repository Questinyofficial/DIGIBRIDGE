"""
app/status.py
-------------

Displays the current DigiBridge system status.

Responsibilities
----------------
- Detect Python installation
- Detect Arduino connection
- Check AI model
- Check selected bridge
- Check required dependencies

Does NOT
--------
- Modify configuration
- Launch the application
- Read sensor data
"""

from __future__ import annotations

import sys
import importlib.util
from pathlib import Path

from serial.tools import list_ports

from app.config_manager import ConfigManager


class Status:
    """
    Displays the current system status.
    """

    # ---------------------------------------------------------

    @staticmethod
    def _check_python() -> str:

        version = sys.version_info

        return f"✓ Python {version.major}.{version.minor}.{version.micro}"

    # ---------------------------------------------------------

    @staticmethod
    def _check_dependencies() -> str:

        packages = [
            "numpy",
            "pandas",
            "joblib",
            "sklearn",
            "serial",
        ]

        missing = []

        for package in packages:

            if importlib.util.find_spec(package) is None:
                missing.append(package)

        if missing:
            return "✗ Missing: " + ", ".join(missing)

        return "✓ Installed"

    # ---------------------------------------------------------

    @staticmethod
    def _check_arduino() -> str:

        ports = list_ports.comports()

        for port in ports:

            description = port.description.lower()

            if (
                "arduino" in description
                or "ch340" in description
                or "usb serial" in description
                or "cp210" in description
            ):
                return f"✓ Connected ({port.device})"

        return "✗ Not Connected"

    # ---------------------------------------------------------

    @staticmethod
    def _check_model() -> str:

        config = ConfigManager()

        model_path = Path(config.get_model())

        if model_path.exists():

            return f"✓ {model_path.name}"

        return "✗ Model Not Found"

    # ---------------------------------------------------------

    @staticmethod
    def _check_bridge() -> str:

        config = ConfigManager()

        bridge_path = Path(config.get_bridge())

        if bridge_path.exists():

            return f"✓ {bridge_path.name}"

        return "✗ Bridge Not Found"

    # ---------------------------------------------------------

    @classmethod
    def show(cls) -> None:

        print("SYSTEM STATUS")
        print("-" * 78)

        print(f"Python               : {cls._check_python()}")
        print(f"Arduino              : {cls._check_arduino()}")
        print(f"AI Model             : {cls._check_model()}")
        print(f"Selected Bridge      : {cls._check_bridge()}")
        print(f"Dependencies         : {cls._check_dependencies()}")

        print("-" * 78)
        print()