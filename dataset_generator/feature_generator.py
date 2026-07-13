"""
feature_generator.py
--------------------

Combines all feature generators into a single bridge sample.

Workflow
--------
Materials
      ↓
Bridge Geometry
      ↓
Environment
      ↓
Traffic
      ↓
Hazards
      ↓
Deterioration
      ↓
Combined Feature Dictionary

This module does NOT calculate structural risk or failure
probability. Those responsibilities belong to:

- risk_model.py
- probability_model.py
"""

from materials import generate_material
from bridge_generator import generate_bridge
from environment_generator import generate_environment
from traffic_generator import generate_traffic
from deterioration_generator import generate_deterioration
from hazard_generator import generate_hazards


# ------------------------------------------------------------------
# Feature Generator
# ------------------------------------------------------------------

def generate_feature_sample():
    """
    Generates one complete bridge feature sample.

    Returns
    -------
    dict

    Example
    -------
    {
        total_area: ...,
        average_area: ...,
        average_age: ...,
        average_corrosion: ...,
        ...
    }
    """

    # --------------------------------------------------------------
    # Generate individual feature groups
    # --------------------------------------------------------------

    material = generate_material()

    bridge = generate_bridge()

    environment = generate_environment()

    traffic = generate_traffic()

    hazards = generate_hazards()

    deterioration = generate_deterioration()

    # --------------------------------------------------------------
    # Combine everything
    # --------------------------------------------------------------

    sample = {}

    sample.update(bridge)

    sample.update(deterioration)

    sample.update(material)

    sample.update(environment)

    sample.update(traffic)

    sample.update(hazards)

    return sample


# ------------------------------------------------------------------
# Standalone Testing
# ------------------------------------------------------------------

if __name__ == "__main__":

    sample = generate_feature_sample()

    print("\nGenerated Bridge Feature Sample\n")

    for key, value in sample.items():
        print(f"{key:25} : {value}")