"""
app/diagnostics.py
------------------

Runs complete DigiBridge diagnostics.

Responsibilities
----------------
- Verify Python installation
- Verify required packages
- Detect Arduino
- Verify AI model
- Verify bridge JSON
- Verify dataset
- Check project folders
- Display diagnostic report

Does NOT
--------
- Launch application
- Modify configuration
- Read sensors continuously
"""

from __future__ import annotations

import importlib.util
import shutil
import sys
from pathlib import Path

from serial.tools import list_ports

from app.config_manager import ConfigManager


class Diagnostics:

    def __init__(self):

        self.config = ConfigManager()

    # ---------------------------------------------------------

    @staticmethod
    def _result(ok: bool) -> str:

        return "[PASS]" if ok else "[FAIL]"

    # ---------------------------------------------------------

    def python(self):

        print(
            f"{self._result(True):8}"
            f" Python {sys.version.split()[0]}"
        )

    # ---------------------------------------------------------

    def packages(self):

        packages = [

            "numpy",
            "pandas",
            "joblib",
            "serial",
            "sklearn"

        ]

        missing = []

        for package in packages:

            if importlib.util.find_spec(package) is None:

                missing.append(package)

        if missing:

            print(
                f"{self._result(False):8}"
                f" Missing Packages : {', '.join(missing)}"
            )

        else:

            print(
                f"{self._result(True):8}"
                f" Required Packages Installed"
            )

    # ---------------------------------------------------------

    def arduino(self):

        ports = list_ports.comports()

        for port in ports:

            description = port.description.lower()

            if (

                "arduino" in description

                or "ch340" in description

                or "usb serial" in description

                or "cp210" in description

            ):

                print(

                    f"{self._result(True):8}"

                    f" Arduino Detected ({port.device})"

                )

                return

        print(

            f"{self._result(False):8}"

            " Arduino Not Detected"

        )

    # ---------------------------------------------------------

    def bridge(self):

        bridge = Path(

            self.config.get_bridge()

        )

        print(

            f"{self._result(bridge.exists()):8}"

            f" Bridge : {bridge.name}"

        )

    # ---------------------------------------------------------

    def model(self):

        model = Path(

            self.config.get_model()

        )

        print(

            f"{self._result(model.exists()):8}"

            f" AI Model : {model.name}"

        )

    # ---------------------------------------------------------

    def dataset(self):

        dataset = Path(

            "data/datasets/bridge_dataset.csv"

        )

        print(

            f"{self._result(dataset.exists()):8}"

            " Training Dataset"

        )

    # ---------------------------------------------------------

    def folders(self):

        folders = [

            "bridge",

            "hardware",

            "prediction",

            "digital_twin",

            "simulation",

            "models",

            "data"

        ]

        ok = True

        for folder in folders:

            if not Path(folder).exists():

                ok = False

        print(

            f"{self._result(ok):8}"

            " Project Structure"

        )

    # ---------------------------------------------------------

    def disk(self):

        usage = shutil.disk_usage(".")

        free = usage.free / (1024 ** 3)

        ok = free > 1

        print(

            f"{self._result(ok):8}"

            f" Free Disk : {free:.2f} GB"

        )

    # ---------------------------------------------------------

    def run(self):

        print()

        print("=" * 78)
        print("DIGIBRIDGE SYSTEM DIAGNOSTICS")
        print("=" * 78)
        print()

        self.python()

        self.packages()

        self.arduino()

        self.bridge()

        self.model()

        self.dataset()

        self.folders()

        self.disk()

        print()

        print("=" * 78)

        input("\nPress ENTER...")