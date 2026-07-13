"""
utils.py
--------

Shared helper functions used throughout the dataset generator.

This module contains reusable utility functions that can be
used by any generator module without duplicating code.
"""

import random


# ------------------------------------------------------------------
# Clamp Value
# ------------------------------------------------------------------

def clamp(value, minimum, maximum):
    """
    Restricts a value to the specified range.

    Parameters
    ----------
    value : float
        Value to clamp.

    minimum : float
        Lower bound.

    maximum : float
        Upper bound.

    Returns
    -------
    float
        Clamped value.
    """

    return max(minimum, min(maximum, value))


# ------------------------------------------------------------------
# Normalize Value
# ------------------------------------------------------------------

def normalize(value, minimum, maximum):
    """
    Normalizes a value to the range [0, 1].

    Parameters
    ----------
    value : float

    minimum : float

    maximum : float

    Returns
    -------
    float
    """

    if maximum == minimum:
        return 0.0

    value = clamp(value, minimum, maximum)

    return (value - minimum) / (maximum - minimum)


# ------------------------------------------------------------------
# Random Float
# ------------------------------------------------------------------

def random_float(minimum, maximum, decimals=2):
    """
    Generates a random floating-point number.

    Parameters
    ----------
    minimum : float

    maximum : float

    decimals : int

    Returns
    -------
    float
    """

    return round(random.uniform(minimum, maximum), decimals)


# ------------------------------------------------------------------
# Random Integer
# ------------------------------------------------------------------

def random_int(minimum, maximum):
    """
    Generates a random integer.

    Parameters
    ----------
    minimum : int

    maximum : int

    Returns
    -------
    int
    """

    return random.randint(minimum, maximum)


# ------------------------------------------------------------------
# Weighted Random Choice
# ------------------------------------------------------------------

def weighted_choice(options, weights):
    """
    Selects one item based on weights.

    Parameters
    ----------
    options : list

    weights : list

    Returns
    -------
    Any
    """

    return random.choices(
        options,
        weights=weights,
        k=1
    )[0]


# ------------------------------------------------------------------
# Add Random Noise
# ------------------------------------------------------------------

def add_noise(value, noise_range):
    """
    Adds random noise to a value.

    Parameters
    ----------
    value : float

    noise_range : float

    Returns
    -------
    float
    """

    return value + random.uniform(
        -noise_range,
        noise_range
    )


# ------------------------------------------------------------------
# Round Dictionary Values
# ------------------------------------------------------------------

def round_dict(data, decimals=2):
    """
    Rounds all float values in a dictionary.

    Parameters
    ----------
    data : dict

    decimals : int

    Returns
    -------
    dict
    """

    rounded = {}

    for key, value in data.items():

        if isinstance(value, float):
            rounded[key] = round(value, decimals)
        else:
            rounded[key] = value

    return rounded


# ------------------------------------------------------------------
# Standalone Testing
# ------------------------------------------------------------------

if __name__ == "__main__":

    print("Clamp:", clamp(125, 0, 100))
    print("Normalize:", normalize(50, 0, 100))
    print("Random Float:", random_float(10, 20))
    print("Random Int:", random_int(1, 10))
    print("Weighted Choice:", weighted_choice(["Steel", "Concrete"], [70, 30]))
    print("Noise:", add_noise(100, 5))

    sample = {
        "a": 12.34567,
        "b": 8.76543,
        "c": "Bridge"
    }

    print("Rounded Dictionary:", round_dict(sample))