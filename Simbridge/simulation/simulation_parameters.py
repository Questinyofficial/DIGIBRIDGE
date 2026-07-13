"""
simulation/simulation_parameters.py
-----------------------------------

Defines the SimulationParameters class.

This class stores all environmental and loading conditions used
during bridge simulation and AI prediction.

It contains no simulation logic or machine learning code.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class SimulationParameters:
    """
    Represents the environmental and loading conditions
    for a bridge simulation.

    Units
    -----
    temperature           : °C
    humidity              : %
    vehicle_load          : tons
    pedestrian_load       : persons
    wind_speed            : m/s
    rainfall              : mm/hr
    river_water_level     : m
    earthquake_factor     : 0.0 - 1.0
    dynamic_load_factor   : dimensionless
    safety_factor         : dimensionless
    """

    temperature: float = 25.0
    humidity: float = 50.0

    vehicle_load: float = 10.0
    pedestrian_load: float = 100.0

    wind_speed: float = 5.0
    rainfall: float = 0.0

    river_water_level: float = 1.0

    earthquake_factor: float = 0.0

    dynamic_load_factor: float = 1.0

    safety_factor: float = 2.0

    # -------------------------------------------------------------
    # Serialization
    # -------------------------------------------------------------

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the simulation parameters to a dictionary.
        """

        return {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "vehicle_load": self.vehicle_load,
            "pedestrian_load": self.pedestrian_load,
            "wind_speed": self.wind_speed,
            "rainfall": self.rainfall,
            "river_water_level": self.river_water_level,
            "earthquake_factor": self.earthquake_factor,
            "dynamic_load_factor": self.dynamic_load_factor,
            "safety_factor": self.safety_factor,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SimulationParameters":
        """
        Create SimulationParameters from a dictionary.
        """

        return cls(
            temperature=data.get("temperature", 25.0),
            humidity=data.get("humidity", 50.0),
            vehicle_load=data.get("vehicle_load", 10.0),
            pedestrian_load=data.get("pedestrian_load", 100.0),
            wind_speed=data.get("wind_speed", 5.0),
            rainfall=data.get("rainfall", 0.0),
            river_water_level=data.get("river_water_level", 1.0),
            earthquake_factor=data.get("earthquake_factor", 0.0),
            dynamic_load_factor=data.get("dynamic_load_factor", 1.0),
            safety_factor=data.get("safety_factor", 2.0),
        )

    # -------------------------------------------------------------
    # Utility
    # -------------------------------------------------------------

    def copy(self) -> "SimulationParameters":
        """
        Return a copy of the current simulation parameters.
        """

        return SimulationParameters.from_dict(self.to_dict())

    def __str__(self) -> str:
        return (
            "SimulationParameters("
            f"temperature={self.temperature} °C, "
            f"humidity={self.humidity} %, "
            f"vehicle_load={self.vehicle_load} tons, "
            f"pedestrian_load={self.pedestrian_load}, "
            f"wind_speed={self.wind_speed} m/s, "
            f"rainfall={self.rainfall} mm/hr, "
            f"river_water_level={self.river_water_level} m, "
            f"earthquake_factor={self.earthquake_factor}, "
            f"dynamic_load_factor={self.dynamic_load_factor}, "
            f"safety_factor={self.safety_factor})"
        )

    def __repr__(self) -> str:
        return self.__str__()