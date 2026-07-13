"""
materials.py
------------

Generates realistic material properties for bridge components.

Supported Materials
-------------------
- Steel
- Reinforced Concrete
- Aluminium
- Composite

Each generated sample contains:

- Material Type
- Density (kg/m³)
- Young's Modulus (GPa)
- Yield Strength (MPa)

These values are randomly generated within realistic engineering ranges
to create diverse but physically reasonable bridge datasets.
"""

import random


# ------------------------------------------------------------------
# Material Property Ranges
# ------------------------------------------------------------------

MATERIAL_DATABASE = {
    "Steel": {
        "density": (7700, 8050),          # kg/m³
        "youngs_modulus": (195, 210),     # GPa
        "yield_strength": (250, 550)      # MPa
    },

    "Reinforced Concrete": {
        "density": (2300, 2500),
        "youngs_modulus": (25, 40),
        "yield_strength": (30, 60)
    },

    "Aluminium": {
        "density": (2650, 2800),
        "youngs_modulus": (68, 72),
        "yield_strength": (150, 350)
    },

    "Composite": {
        "density": (1500, 2200),
        "youngs_modulus": (50, 160),
        "yield_strength": (400, 1200)
    }
}


# ------------------------------------------------------------------
# Material Generator
# ------------------------------------------------------------------

def generate_material():
    """
    Randomly generates realistic material properties.

    Returns
    -------
    dict

    Example
    -------
    {
        "material": "Steel",
        "average_density": 7850.23,
        "average_youngs_modulus": 201.45,
        "average_yield_strength": 412.87
    }
    """

    material_name = random.choice(list(MATERIAL_DATABASE.keys()))
    properties = MATERIAL_DATABASE[material_name]

    density = round(
        random.uniform(*properties["density"]),
        2
    )

    youngs_modulus = round(
        random.uniform(*properties["youngs_modulus"]),
        2
    )

    yield_strength = round(
        random.uniform(*properties["yield_strength"]),
        2
    )

    return {
        "material": material_name,
        "average_density": density,
        "average_youngs_modulus": youngs_modulus,
        "average_yield_strength": yield_strength
    }


# ------------------------------------------------------------------
# Standalone Testing
# ------------------------------------------------------------------

if __name__ == "__main__":

    for _ in range(5):
        print(generate_material())