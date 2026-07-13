"""
hazard_generator.py
-------------------

Generates natural hazard conditions affecting a bridge.

Current Features
----------------
- Wind Speed (km/h)
- Rainfall (mm/day)
- River Water Level (m)
- Earthquake Factor

Correlation
-----------
Rainfall
    ↓
Higher River Water Level

Wind and earthquake activity are generated independently to
represent different environmental hazards.

The generated values are intended for synthetic dataset creation
and are not site-specific.
"""

import random


# ------------------------------------------------------------------
# Engineering Limits
# ------------------------------------------------------------------

MIN_WIND_SPEED = 0.0          # km/h
MAX_WIND_SPEED = 180.0        # km/h

MIN_RAINFALL = 0.0            # mm/day
MAX_RAINFALL = 300.0          # mm/day

MIN_RIVER_LEVEL = 1.0         # m
MAX_RIVER_LEVEL = 12.0        # m

MIN_EARTHQUAKE = 0.0          # Hazard factor
MAX_EARTHQUAKE = 1.0


# ------------------------------------------------------------------
# Hazard Generator
# ------------------------------------------------------------------

def generate_hazards():
    """
    Generates environmental hazard conditions.

    Returns
    -------
    dict

    Example
    -------
    {
        "wind_speed": 72.14,
        "rainfall": 84.25,
        "river_water_level": 4.61,
        "earthquake_factor": 0.32
    }
    """

    # --------------------------------------------------------------
    # Wind Speed
    # --------------------------------------------------------------

    wind_speed = random.uniform(
        MIN_WIND_SPEED,
        MAX_WIND_SPEED
    )

    # --------------------------------------------------------------
    # Rainfall
    # --------------------------------------------------------------

    rainfall = random.uniform(
        MIN_RAINFALL,
        MAX_RAINFALL
    )

    # --------------------------------------------------------------
    # River Water Level
    #
    # Higher rainfall generally raises river levels.
    # --------------------------------------------------------------

    rainfall_ratio = rainfall / MAX_RAINFALL

    river_level = (
        MIN_RIVER_LEVEL
        + rainfall_ratio * (MAX_RIVER_LEVEL - MIN_RIVER_LEVEL)
        + random.uniform(-0.5, 0.5)
    )

    river_level = max(
        MIN_RIVER_LEVEL,
        min(MAX_RIVER_LEVEL, river_level)
    )

    # --------------------------------------------------------------
    # Earthquake Factor
    #
    # Represents normalized seismic hazard:
    #
    # 0.0 -> No seismic activity
    # 1.0 -> Severe seismic activity
    # --------------------------------------------------------------

    earthquake_factor = random.uniform(
        MIN_EARTHQUAKE,
        MAX_EARTHQUAKE
    )

    return {
        "wind_speed": round(wind_speed, 2),
        "rainfall": round(rainfall, 2),
        "river_water_level": round(river_level, 2),
        "earthquake_factor": round(earthquake_factor, 3)
    }


# ------------------------------------------------------------------
# Standalone Testing
# ------------------------------------------------------------------

if __name__ == "__main__":

    for _ in range(10):
        print(generate_hazards())