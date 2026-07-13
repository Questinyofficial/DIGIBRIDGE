"""
prediction/feature_builder.py
-----------------------------

Builds the machine learning feature vector from the current
BridgeModel and SimulationParameters.

IMPORTANT:
The feature order MUST exactly match the order used when
training random_forest.pkl.
"""

from __future__ import annotations

from typing import List

from bridge.bridge_model import BridgeModel
from simulation.simulation_parameters import SimulationParameters


class FeatureBuilder:
    """
    Converts the current bridge state into the feature vector
    expected by the Random Forest model.
    """

    @staticmethod
    def build_features(
        bridge: BridgeModel,
        simulation: SimulationParameters
    ) -> List[float]:
        """
        Build the feature vector.

        Parameters
        ----------
        bridge : BridgeModel

        simulation : SimulationParameters

        Returns
        -------
        list[float]
            Ordered feature vector.
        """

        members = bridge.get_all_members()

        if not members:
            raise ValueError("Bridge contains no members.")

        # ----------------------------------------------------------
        # Aggregate bridge properties
        # ----------------------------------------------------------

        total_area = sum(member.area for member in members)

        average_area = total_area / len(members)

        average_age = (
            sum(member.age for member in members)
            / len(members)
        )

        average_corrosion = (
            sum(member.corrosion for member in members)
            / len(members)
        )

        average_crack_width = (
            sum(member.crack_width for member in members)
            / len(members)
        )

        average_density = (
            sum(member.material.density for member in members)
            / len(members)
        )

        average_youngs_modulus = (
            sum(member.material.youngs_modulus for member in members)
            / len(members)
        )

        average_yield_strength = (
            sum(member.material.yield_strength for member in members)
            / len(members)
        )

        # ----------------------------------------------------------
        # Feature vector
        # IMPORTANT:
        # This order MUST match the training dataset.
        # ----------------------------------------------------------

        return [

            # Bridge Properties
            total_area,
            average_area,
            average_age,
            average_corrosion,
            average_crack_width,
            average_density,
            average_youngs_modulus,
            average_yield_strength,

            # Simulation Parameters
            simulation.temperature,
            simulation.humidity,
            simulation.vehicle_load,
            simulation.pedestrian_load,
            simulation.wind_speed,
            simulation.rainfall,
            simulation.river_water_level,
            simulation.earthquake_factor,
            simulation.dynamic_load_factor,
            simulation.safety_factor,
        ]

    @staticmethod
    def feature_names() -> List[str]:
        """
        Returns the feature names in the exact order expected
        by the trained model.
        """

        return [

            "total_area",
            "average_area",
            "average_age",
            "average_corrosion",
            "average_crack_width",
            "average_density",
            "average_youngs_modulus",
            "average_yield_strength",

            "temperature",
            "humidity",
            "vehicle_load",
            "pedestrian_load",
            "wind_speed",
            "rainfall",
            "river_water_level",
            "earthquake_factor",
            "dynamic_load_factor",
            "safety_factor",
        ]