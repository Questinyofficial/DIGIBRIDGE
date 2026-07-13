"""
app/application.py
------------------

Main DigiBridge application controller.

Responsibilities
----------------
- Load the selected bridge
- Load the trained AI model
- Connect to Arduino
- Update the Digital Twin
- Run AI predictions
- Update the terminal dashboard

Does NOT
--------
- Display launcher menus
- Train AI models
- Generate datasets
- Select bridge/model
"""

from __future__ import annotations

import time

from app.config_manager import ConfigManager
from app.dashboard import Dashboard

from bridge.bridge_loader import BridgeLoader

from hardware.serial_reader import SerialReader

from digital_twin.bridge_updater import BridgeUpdater
from digital_twin.live_simulation import LiveSimulation

from prediction.predictor import Predictor

from simulation.simulation_parameters import SimulationParameters


class Application:
    """
    Main DigiBridge runtime controller.
    """

    # ---------------------------------------------------------

    def __init__(self):

        self.config = ConfigManager()

        self.bridge = None

        self.predictor = None

        self.reader = None

        self.dashboard = Dashboard()

        self.bridge_updater = BridgeUpdater()

        self.live_simulation = LiveSimulation()

        self.simulation = SimulationParameters()

    # ---------------------------------------------------------

    def initialize(self):
        """
        Initialize DigiBridge.
        """

        print("\nInitializing DigiBridge...\n")

        # -----------------------------
        # Load bridge
        # -----------------------------

        bridge_file = self.config.get_bridge()

        self.bridge = BridgeLoader.load(
            bridge_file
        )

        print(f"Bridge Loaded : {bridge_file}")

        # -----------------------------
        # Load AI model
        # -----------------------------

        model_file = self.config.get_model()

        self.predictor = Predictor(
            model_file
        )

        print(f"AI Model      : {model_file}")

        # -----------------------------
        # Connect Arduino
        # -----------------------------

        self.reader = SerialReader()

        print("\nSearching for Arduino...")

        if not self.reader.connect():

            raise RuntimeError(
                "Arduino could not be found."
            )

        print("Arduino Connected.")

        print("\nInitialization Complete.")

        time.sleep(2)

    # ---------------------------------------------------------

    def run(self):
        """
        Run DigiBridge.
        """

        self.initialize()

        update_interval = (
            self.config.get_update_interval()
        )

        while True:

            sensor_data = self.reader.read_sensor_data()

            if sensor_data is None:

                time.sleep(0.2)

                continue

            # --------------------------------------------
            # Update deterioration model
            # --------------------------------------------

            self.bridge = self.bridge_updater.update(
                self.bridge
            )

            # --------------------------------------------
            # Update simulation
            # --------------------------------------------

            self.simulation = (
                self.live_simulation.update(
                    self.simulation,
                    sensor_data
                )
            )


            # --------------------------------------------
            # AI Prediction
            # --------------------------------------------

            result = self.predictor.predict(

                self.bridge,

                self.simulation
            )

            # --------------------------------------------
            # Update dashboard
            # --------------------------------------------

            self.dashboard.update(

                bridge=self.bridge,

                simulation=self.simulation,

                sensor_data=sensor_data,

                prediction=result

            )

            time.sleep(update_interval)