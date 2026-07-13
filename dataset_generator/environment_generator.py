"""
environment_generator.py
------------------------

Generates realistic environmental conditions affecting bridge
performance.

Current Features
----------------
- Temperature (°C)
- Relative Humidity (%)

The generated values are mildly correlated so that:
Higher temperature generally leads to slightly lower humidity,
while cooler conditions tend to have higher humidity.

This creates a more realistic synthetic dataset than choosing
both values completely independently.
"""

import random


# ------------------------------------------------------------------
# Environmental Limits
# ------------------------------------------------------------------

MIN_TEMPERATURE = -10.0      # °C
MAX_TEMPERATURE = 50.0       # °C

MIN_HUMIDITY = 20.0          # %
MAX_HUMIDITY = 100.0         # %


# ------------------------------------------------------------------
# Environment Generator
# ------------------------------------------------------------------

def generate_environment():
    """
    Generates realistic environmental conditions.

    Returns
    -------
    dict

    Example
    -------
    {
        "temperature": 31.8,
        "humidity": 58.4
    }
    """

    # Random ambient temperature
    temperature = random.uniform(
        MIN_TEMPERATURE,
        MAX_TEMPERATURE
    )

    # Normalize temperature to 0–1
    normalized_temp = (
        temperature - MIN_TEMPERATURE
    ) / (
        MAX_TEMPERATURE - MIN_TEMPERATURE
    )

    # Hotter weather generally lowers humidity
    base_humidity = (
        MAX_HUMIDITY -
        normalized_temp * 60
    )

    # Add natural variation
    humidity = base_humidity + random.uniform(-10, 10)

    # Clamp within engineering limits
    humidity = max(
        MIN_HUMIDITY,
        min(MAX_HUMIDITY, humidity)
    )

    return {
        "temperature": round(temperature, 2),
        "humidity": round(humidity, 2)
    }


# ------------------------------------------------------------------
# Standalone Testing
# ------------------------------------------------------------------

if __name__ == "__main__":

    for _ in range(10):
        print(generate_environment())