"""
utils/validators.py
-------------------

Generic validation helper functions used throughout
the Bridge Digital Twin application.

These functions are intentionally independent of any
specific class or module.
"""

from __future__ import annotations


def is_number(value) -> bool:
    """
    Returns True if the value can be converted to a float.
    """
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


def is_positive(value) -> bool:
    """
    Returns True if the value is greater than zero.
    """
    return is_number(value) and float(value) > 0


def is_non_negative(value) -> bool:
    """
    Returns True if the value is greater than or equal to zero.
    """
    return is_number(value) and float(value) >= 0


def is_percentage(value) -> bool:
    """
    Returns True if the value is between 0 and 100.
    """
    return is_number(value) and 0.0 <= float(value) <= 100.0


def is_probability(value) -> bool:
    """
    Returns True if the value is between 0.0 and 1.0.
    """
    return is_number(value) and 0.0 <= float(value) <= 1.0


def in_range(value, minimum, maximum) -> bool:
    """
    Returns True if value lies within the specified range.
    """
    return (
        is_number(value)
        and float(minimum) <= float(value) <= float(maximum)
    )


def clamp(value, minimum, maximum):
    """
    Restrict a value to the specified range.
    """
    value = float(value)

    if value < minimum:
        return minimum

    if value > maximum:
        return maximum

    return value