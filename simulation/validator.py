"""
simulation/validator.py
-----------------------

Validates simulation parameters before running a prediction.

Responsibilities
----------------
- Validate user input
- Report validation errors

No GUI code.
No AI code.
No simulation logic.
"""

from __future__ import annotations

from simulation.simulation_parameters import SimulationParameters


class ValidationError(Exception):
    """Raised when simulation parameters are invalid."""
    pass


class SimulationValidator:
    """
    Validates SimulationParameters.
    """

    @staticmethod
    def validate(params: SimulationParameters) -> None:
        """
        Validate all simulation parameters.

        Raises
        ------
        ValidationError
            If any parameter is outside its allowed range.
        """

        # Temperature (°C)
        if not (-40.0 <= params.temperature <= 80.0):
            raise ValidationError(
                "Temperature must be between -40°C and 80°C."
            )

        # Humidity (%)
        if not (0.0 <= params.humidity <= 100.0):
            raise ValidationError(
                "Humidity must be between 0% and 100%."
            )

        # Vehicle load (tons)
        if params.vehicle_load < 0:
            raise ValidationError(
                "Vehicle load cannot be negative."
            )

        if params.vehicle_load > 200:
            raise ValidationError(
                "Vehicle load exceeds the supported limit (200 tons)."
            )

        # Pedestrian load
        if params.pedestrian_load < 0:
            raise ValidationError(
                "Pedestrian load cannot be negative."
            )

        if params.pedestrian_load > 5000:
            raise ValidationError(
                "Pedestrian load exceeds the supported limit."
            )

        # Wind speed (m/s)
        if not (0.0 <= params.wind_speed <= 100.0):
            raise ValidationError(
                "Wind speed must be between 0 and 100 m/s."
            )

        # Rainfall (mm/hr)
        if not (0.0 <= params.rainfall <= 500.0):
            raise ValidationError(
                "Rainfall must be between 0 and 500 mm/hr."
            )

        # River water level (m)
        if not (0.0 <= params.river_water_level <= 20.0):
            raise ValidationError(
                "River water level must be between 0 and 20 m."
            )

        # Earthquake factor
        if not (0.0 <= params.earthquake_factor <= 1.0):
            raise ValidationError(
                "Earthquake factor must be between 0.0 and 1.0."
            )

        # Dynamic load factor
        if not (0.5 <= params.dynamic_load_factor <= 5.0):
            raise ValidationError(
                "Dynamic load factor must be between 0.5 and 5.0."
            )

        # Safety factor
        if not (0.5 <= params.safety_factor <= 10.0):
            raise ValidationError(
                "Safety factor must be between 0.5 and 10.0."
            )

    @staticmethod
    def is_valid(params: SimulationParameters) -> bool:
        """
        Returns True if the parameters are valid.
        """

        try:
            SimulationValidator.validate(params)
            return True
        except ValidationError:
            return False