"""
deterioration_generator.py
--------------------------

Generates deterioration-related properties of a bridge.

Current Features
----------------
- Average Age (years)
- Average Corrosion (%)
- Average Crack Width (mm)

Correlation
-----------
Older Bridge
        ↓
Higher Corrosion
        ↓
Larger Crack Width

This creates a much more realistic synthetic dataset than
choosing each feature independently.
"""

import random


# ------------------------------------------------------------------
# Engineering Limits
# ------------------------------------------------------------------

MIN_AGE = 0
MAX_AGE = 80

MIN_CORROSION = 0.0       # %
MAX_CORROSION = 100.0     # %

MIN_CRACK_WIDTH = 0.00    # mm
MAX_CRACK_WIDTH = 10.00   # mm


# ------------------------------------------------------------------
# Deterioration Generator
# ------------------------------------------------------------------

def generate_deterioration():
    """
    Generates correlated deterioration properties.

    Returns
    -------
    dict

    Example
    -------
    {
        "average_age": 42,
        "average_corrosion": 48.63,
        "average_crack_width": 2.41
    }
    """

    # Bridge age
    age = random.randint(
        MIN_AGE,
        MAX_AGE
    )

    # --------------------------------------------------------------
    # Corrosion increases with age
    # --------------------------------------------------------------

    age_ratio = age / MAX_AGE

    corrosion = (
        age_ratio * 85
        + random.uniform(-8, 8)
    )

    corrosion = max(
        MIN_CORROSION,
        min(MAX_CORROSION, corrosion)
    )

    # --------------------------------------------------------------
    # Crack width increases with corrosion
    # --------------------------------------------------------------

    corrosion_ratio = corrosion / MAX_CORROSION

    crack_width = (
        corrosion_ratio * 8
        + random.uniform(0, 1.5)
    )

    crack_width = max(
        MIN_CRACK_WIDTH,
        min(MAX_CRACK_WIDTH, crack_width)
    )

    return {
        "average_age": age,
        "average_corrosion": round(corrosion, 2),
        "average_crack_width": round(crack_width, 2)
    }


# ------------------------------------------------------------------
# Standalone Testing
# ------------------------------------------------------------------

if __name__ == "__main__":

    for _ in range(10):
        print(generate_deterioration())