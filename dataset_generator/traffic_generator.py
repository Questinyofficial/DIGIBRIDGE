"""
traffic_generator.py
--------------------

Generates realistic traffic loading conditions for bridge structures.

Current Features
----------------
- Vehicle Load (kN)
- Pedestrian Load (kN)
- Dynamic Load Factor

The Dynamic Load Factor (DLF) is correlated with the traffic loading.

Higher vehicle traffic generally produces higher bridge vibrations,
resulting in an increased dynamic load factor.
"""

import random


# ------------------------------------------------------------------
# Engineering Limits
# ------------------------------------------------------------------

MIN_VEHICLE_LOAD = 100.0      # kN
MAX_VEHICLE_LOAD = 3000.0     # kN

MIN_PEDESTRIAN_LOAD = 5.0     # kN
MAX_PEDESTRIAN_LOAD = 300.0   # kN

MIN_DLF = 1.00
MAX_DLF = 2.00


# ------------------------------------------------------------------
# Traffic Generator
# ------------------------------------------------------------------

def generate_traffic():
    """
    Generates realistic bridge traffic conditions.

    Returns
    -------
    dict

    Example
    -------
    {
        "vehicle_load": 1854.62,
        "pedestrian_load": 142.37,
        "dynamic_load_factor": 1.48
    }
    """

    # Generate traffic loads
    vehicle_load = random.uniform(
        MIN_VEHICLE_LOAD,
        MAX_VEHICLE_LOAD
    )

    pedestrian_load = random.uniform(
        MIN_PEDESTRIAN_LOAD,
        MAX_PEDESTRIAN_LOAD
    )

    # Normalize values
    vehicle_ratio = (
        (vehicle_load - MIN_VEHICLE_LOAD)
        /
        (MAX_VEHICLE_LOAD - MIN_VEHICLE_LOAD)
    )

    pedestrian_ratio = (
        (pedestrian_load - MIN_PEDESTRIAN_LOAD)
        /
        (MAX_PEDESTRIAN_LOAD - MIN_PEDESTRIAN_LOAD)
    )

    # Vehicle traffic has the largest influence
    dynamic_load_factor = (
        1.0
        + 0.75 * vehicle_ratio
        + 0.15 * pedestrian_ratio
        + random.uniform(-0.05, 0.05)
    )

    # Keep within engineering limits
    dynamic_load_factor = max(
        MIN_DLF,
        min(MAX_DLF, dynamic_load_factor)
    )

    return {
        "vehicle_load": round(vehicle_load, 2),
        "pedestrian_load": round(pedestrian_load, 2),
        "dynamic_load_factor": round(dynamic_load_factor, 3)
    }


# ------------------------------------------------------------------
# Standalone Testing
# ------------------------------------------------------------------

if __name__ == "__main__":

    for _ in range(10):
        print(generate_traffic())