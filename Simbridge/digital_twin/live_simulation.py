"""
digital_twin/live_simulation.py
-------------------------------

Creates live simulation parameters from
real sensor measurements.

Responsibilities
----------------
- Receive Arduino sensor values
- Update SimulationParameters
- Generate missing environmental parameters

Does NOT:
- Read serial data
- Run the AI model
- Display GUI
"""

from __future__ import annotations

import random

from simulation.simulation_parameters import SimulationParameters


class LiveSimulation:
    """
    Updates SimulationParameters using
    live Arduino sensor readings.
    """

    def __init__(self):

        # Fixed values for the exhibition
        self.bridge_age = 20

        # Slowly varying values
        self.corrosion = 0.12
        self.crack_width = 0.35
        self.wind_speed = random.uniform(3.0, 6.0)
        self.rainfall = 0.0
        self.pedestrian_load = 60

    # ---------------------------------------------------------

    def update(
        self,
        simulation: SimulationParameters,
        sensor_data: dict,
    ) -> SimulationParameters:
        """
        Update simulation parameters using
        live sensor readings.

        Parameters
        ----------
        simulation : SimulationParameters

        sensor_data : dict

        Returns
        -------
        SimulationParameters
        """

        # ------------------------------
        # Real sensor values
        # ------------------------------

        simulation.temperature = sensor_data["temperature"]

        simulation.humidity = sensor_data["humidity"]

        simulation.vehicle_load = sensor_data["load"]

        # ------------------------------
        # Estimated values
        # ------------------------------

        self.pedestrian_load += random.randint(-3, 3)
        self.pedestrian_load = max(0, min(120, self.pedestrian_load))

        simulation.pedestrian_load = self.pedestrian_load
        self.wind_speed += random.uniform(-0.2, 0.2)
        self.wind_speed = max(0.0, min(20.0, self.wind_speed))

        simulation.wind_speed = self.wind_speed

        if random.random() < 0.02:
            self.rainfall = random.uniform(5,15)
        else:
            self.rainfall *= 0.95

        simulation.river_water_level = min(
        5.0,
        1.5 + self.rainfall * 0.08
        )

        simulation.earthquake_factor = 0.0

        simulation.dynamic_load_factor = 1.0 + (
        simulation.vehicle_load / 100.0
        )

        simulation.safety_factor = max(
        1.5,
        min(3.0, simulation.safety_factor)
        )
        return simulation