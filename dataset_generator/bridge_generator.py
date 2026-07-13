"""
bridge_generator.py
-------------------

Generates realistic bridge geometry statistics.

Current Features
----------------
- Total Cross-Sectional Area (m²)
- Average Member Cross-Sectional Area (m²)

Future Expansion
----------------
This module is intentionally designed so additional bridge geometry
properties can be added later without changing the dataset pipeline.

Possible future additions:
- Bridge Type
- Total Span
- Deck Width
- Number of Members
- Number of Nodes
- Deck Thickness
- Pier Height
"""

import random


# ------------------------------------------------------------------
# Engineering Limits
# ------------------------------------------------------------------

MIN_MEMBERS = 40
MAX_MEMBERS = 350

MIN_MEMBER_AREA = 0.01      # m²
MAX_MEMBER_AREA = 0.08      # m²


# ------------------------------------------------------------------
# Bridge Geometry Generator
# ------------------------------------------------------------------

def generate_bridge():
    """
    Generates bridge geometry statistics.

    Returns
    -------
    dict

    Example
    -------
    {
        "total_area": 8.42,
        "average_area": 0.042
    }
    """

    number_of_members = random.randint(
        MIN_MEMBERS,
        MAX_MEMBERS
    )

    member_areas = [
        random.uniform(
            MIN_MEMBER_AREA,
            MAX_MEMBER_AREA
        )
        for _ in range(number_of_members)
    ]

    total_area = round(sum(member_areas), 3)

    average_area = round(
        total_area / number_of_members,
        4
    )

    return {
        "total_area": total_area,
        "average_area": average_area
    }


# ------------------------------------------------------------------
# Standalone Testing
# ------------------------------------------------------------------

if __name__ == "__main__":

    for _ in range(5):
        print(generate_bridge())