"""
Bridge Digital Twin Dataset Generator
=====================================

A modular synthetic dataset generator for bridge digital twin
applications.

Package Structure
-----------------
- config.py
- materials.py
- bridge_generator.py
- environment_generator.py
- traffic_generator.py
- deterioration_generator.py
- hazard_generator.py
- feature_generator.py
- risk_model.py
- probability_model.py
- csv_writer.py
- utils.py
- generate_dataset.py
"""

__version__ = "1.0.0"
__author__ = "Questiny"


# Public API
from .generate_dataset import generate_dataset

__all__ = [
    "generate_dataset",
]