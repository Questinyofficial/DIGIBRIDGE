"""
probability_model.py
--------------------

Converts Structural Risk into Failure Probability.

Workflow
--------
Structural Risk
        ↓
Sigmoid Function
        ↓
Failure Probability (0 - 1)

The sigmoid function provides a smooth transition between
low-risk and high-risk bridges while ensuring the probability
always remains between 0 and 1.

A small amount of random noise is added to improve the realism
of the synthetic dataset.
"""

import math
import random


# ------------------------------------------------------------------
# Probability Calculator
# ------------------------------------------------------------------

def calculate_failure_probability(sample):
    """
    Calculates the probability of bridge failure.

    Parameters
    ----------
    sample : dict
        Bridge sample after structural risk has been calculated.

    Returns
    -------
    dict
        Updated sample containing:

        failure_probability
    """

    structural_risk = sample["structural_risk"]

    # --------------------------------------------------------------
    # Logistic (Sigmoid) Transformation
    #
    # Risk = 50 is approximately the midpoint where the probability
    # begins increasing more rapidly.
    # --------------------------------------------------------------

    probability = 1 / (
        2 + math.exp(-(structural_risk - 50) / 10)
    )

    # --------------------------------------------------------------
    # Add small random variation
    # --------------------------------------------------------------

    probability += random.uniform(-0.02, 0.02)

    # Clamp to valid probability range
    probability = max(
        0.0,
        min(1.0, probability)
    )

    sample["failure_probability"] = round(probability, 4)

    return sample


# ------------------------------------------------------------------
# Standalone Testing
# ------------------------------------------------------------------

if __name__ == "__main__":

    from feature_generator import generate_feature_sample
    from risk_model import calculate_structural_risk

    bridge = generate_feature_sample()

    bridge = calculate_structural_risk(bridge)

    bridge = calculate_failure_probability(bridge)

    print("\nBridge Failure Prediction\n")

    for key, value in bridge.items():
        print(f"{key:25} : {value}")