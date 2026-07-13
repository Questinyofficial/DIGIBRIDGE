"""
risk_model.py
-------------

Calculates the Structural Risk Index and Safety Factor.

Workflow
--------
Bridge Features
        ↓
Weighted Engineering Risk Model
        ↓
Structural Risk Index
        ↓
Safety Factor

The Structural Risk Index is a normalized engineering score
between 0 and 100.

A higher Structural Risk Index indicates a more vulnerable bridge.

The Safety Factor is inversely proportional to the calculated risk.

This module does NOT calculate failure probability.
"""

# ------------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------------

def normalize(value, minimum, maximum):
    """
    Normalize a value to the range [0, 1].
    """

    if maximum == minimum:
        return 0.0

    value = max(minimum, min(maximum, value))
    return (value - minimum) / (maximum - minimum)


# ------------------------------------------------------------------
# Risk Calculator
# ------------------------------------------------------------------

def calculate_structural_risk(sample):
    """
    Calculates structural risk and safety factor.

    Parameters
    ----------
    sample : dict

    Returns
    -------
    dict
        Updated sample containing:

        structural_risk
        safety_factor
    """

    # --------------------------------------------------------------
    # Normalize deterioration features
    # --------------------------------------------------------------

    age = normalize(sample["average_age"], 0, 80)

    corrosion = normalize(sample["average_corrosion"], 0, 100)

    cracks = normalize(sample["average_crack_width"], 0, 10)

    # --------------------------------------------------------------
    # Normalize environmental hazards
    # --------------------------------------------------------------

    wind = normalize(sample["wind_speed"], 0, 180)

    rainfall = normalize(sample["rainfall"], 0, 300)

    river = normalize(sample["river_water_level"], 1, 12)

    earthquake = sample["earthquake_factor"]

    # --------------------------------------------------------------
    # Normalize traffic
    # --------------------------------------------------------------

    vehicle = normalize(sample["vehicle_load"], 100, 3000)

    pedestrian = normalize(sample["pedestrian_load"], 5, 300)

    dynamic = normalize(sample["dynamic_load_factor"], 1.0, 2.0)

    # --------------------------------------------------------------
    # Material resistance
    # Stronger materials reduce structural risk.
    # --------------------------------------------------------------

    yield_strength = normalize(
        sample["average_yield_strength"],
        30,
        1200
    )

    youngs_modulus = normalize(
        sample["average_youngs_modulus"],
        25,
        210
    )

    # --------------------------------------------------------------
    # Weighted Engineering Risk Model
    # --------------------------------------------------------------

    deterioration_score = (
        0.30 * age +
        0.35 * corrosion +
        0.35 * cracks
    )

    traffic_score = (
        0.45 * vehicle +
        0.15 * pedestrian +
        0.40 * dynamic
    )

    hazard_score = (
        0.30 * wind +
        0.20 * rainfall +
        0.25 * river +
        0.25 * earthquake
    )

    material_score = (
        0.60 * yield_strength +
        0.40 * youngs_modulus
    )

    # Overall Structural Risk
    risk = (
        0.45 * deterioration_score +
        0.25 * traffic_score +
        0.20 * hazard_score -
        0.20 * material_score
    )

    # Convert to 0–100 scale
    structural_risk = max(
        0,
        min(100, risk * 100)
    )

    # --------------------------------------------------------------
    # Safety Factor
    # Higher risk -> Lower safety factor
    # --------------------------------------------------------------

    safety_factor = 3.5 - (structural_risk / 100) * 2.5

    safety_factor = max(
        1.0,
        min(3.5, safety_factor)
    )

    sample["structural_risk"] = round(structural_risk, 2)

    sample["safety_factor"] = round(safety_factor, 2)

    return sample


# ------------------------------------------------------------------
# Standalone Testing
# ------------------------------------------------------------------

if __name__ == "__main__":

    from feature_generator import generate_feature_sample

    bridge = generate_feature_sample()

    bridge = calculate_structural_risk(bridge)

    print("\nBridge Structural Assessment\n")

    for key, value in bridge.items():
        print(f"{key:25} : {value}")