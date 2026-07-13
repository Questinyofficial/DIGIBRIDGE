"""
config.py
---------

Central configuration file for the Bridge Digital Twin
Dataset Generator.

This module contains ONLY configuration constants.
No calculations or business logic should be placed here.
"""

# ==============================================================
# DATASET CONFIGURATION
# ==============================================================

# Number of bridge samples to generate
NUM_SAMPLES = 100000

# Output CSV location
OUTPUT_CSV = "data/bridge_digital_twin_dataset.csv"


# ==============================================================
# BRIDGE GEOMETRY
# ==============================================================

# Number of structural members
MIN_MEMBERS = 40
MAX_MEMBERS = 350

# Cross-sectional area (m²)
MIN_AREA = 0.10
MAX_AREA = 0.70


# ==============================================================
# MATERIAL PROPERTIES
# ==============================================================

# Density (kg/m³)

STEEL_DENSITY = (7700, 8050)
CONCRETE_DENSITY = (2300, 2500)
ALUMINIUM_DENSITY = (2650, 2800)
COMPOSITE_DENSITY = (1500, 2200)

# Young's Modulus (GPa)

STEEL_YOUNGS = (195, 210)
CONCRETE_YOUNGS = (25, 40)
ALUMINIUM_YOUNGS = (68, 72)
COMPOSITE_YOUNGS = (50, 160)

# Yield Strength (MPa)

STEEL_YIELD = (250, 550)
CONCRETE_YIELD = (30, 60)
ALUMINIUM_YIELD = (150, 350)
COMPOSITE_YIELD = (400, 1200)


# ==============================================================
# DETERIORATION
# ==============================================================

# Bridge age (years)

MIN_AGE = 0
MAX_AGE = 30

# Corrosion (%)

MIN_CORROSION = 0
MAX_CORROSION = 50

# Crack width (mm)

MIN_CRACK_WIDTH = 0.0
MAX_CRACK_WIDTH = 5.0


# ==============================================================
# ENVIRONMENT
# ==============================================================

# Temperature (°C)

MIN_TEMPERATURE = -10.0
MAX_TEMPERATURE = 50.0

# Relative Humidity (%)

MIN_HUMIDITY = 20.0
MAX_HUMIDITY = 100.0


# ==============================================================
# TRAFFIC
# ==============================================================

# Vehicle Load (kN)

MIN_VEHICLE_LOAD = 100.0
MAX_VEHICLE_LOAD = 300.0

# Pedestrian Load (kN)

MIN_PEDESTRIAN_LOAD = 5.0
MAX_PEDESTRIAN_LOAD = 300.0

# Dynamic Load Factor

MIN_DYNAMIC_LOAD_FACTOR = 1.0
MAX_DYNAMIC_LOAD_FACTOR = 2.0


# ==============================================================
# NATURAL HAZARDS
# ==============================================================

# Wind Speed (km/h)

MIN_WIND_SPEED = 0.0
MAX_WIND_SPEED = 180.0

# Rainfall (mm/day)

MIN_RAINFALL = 0.0
MAX_RAINFALL = 300.0

# River Water Level (m)

MIN_RIVER_LEVEL = 1.0
MAX_RIVER_LEVEL = 12.0

# Earthquake Factor (Normalized)

MIN_EARTHQUAKE_FACTOR = 0.0
MAX_EARTHQUAKE_FACTOR = 1.0


# ==============================================================
# RISK MODEL
# ==============================================================

# Safety Factor Limits

MIN_SAFETY_FACTOR = 1.0
MAX_SAFETY_FACTOR = 3.5

# Structural Risk Index

MIN_STRUCTURAL_RISK = 0.0
MAX_STRUCTURAL_RISK = 100.0


# ==============================================================
# FAILURE PROBABILITY
# ==============================================================

MIN_FAILURE_PROBABILITY = 0.0
MAX_FAILURE_PROBABILITY = 1.0


# ==============================================================
# FINAL DATASET COLUMNS
# ==============================================================

FINAL_COLUMNS = [

    "total_area",
    "average_area",

    "average_age",
    "average_corrosion",
    "average_crack_width",

    "average_density",
    "average_youngs_modulus",
    "average_yield_strength",

    "temperature",
    "humidity",

    "vehicle_load",
    "pedestrian_load",

    "wind_speed",
    "rainfall",
    "river_water_level",
    "earthquake_factor",

    "dynamic_load_factor",

    "safety_factor",

    "failure_probability"
]