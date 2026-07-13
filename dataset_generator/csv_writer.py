"""
csv_writer.py
-------------

Writes the generated bridge dataset to a CSV file.

Responsibilities
----------------
- Convert generated samples into a Pandas DataFrame
- Remove internal columns not required in the final dataset
- Save the dataset as

    data/bridge_digital_twin_dataset.csv

This module performs no feature generation or calculations.
"""

import os
import pandas as pd


# ------------------------------------------------------------------
# Final Dataset Column Order
# ------------------------------------------------------------------

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


# ------------------------------------------------------------------
# CSV Writer
# ------------------------------------------------------------------

def write_dataset(
    samples,
    output_path="data/bridge_digital_twin_dataset.csv"
):
    """
    Writes bridge samples to a CSV file.

    Parameters
    ----------
    samples : list
        List of dictionaries.

    output_path : str
        Output CSV location.

    Returns
    -------
    pandas.DataFrame
    """

    # --------------------------------------------------------------
    # Create DataFrame
    # --------------------------------------------------------------

    df = pd.DataFrame(samples)

    # --------------------------------------------------------------
    # Remove internal columns
    # --------------------------------------------------------------

    internal_columns = [
        "material",
        "structural_risk"
    ]

    df = df.drop(
        columns=internal_columns,
        errors="ignore"
    )

    # --------------------------------------------------------------
    # Arrange columns in the required order
    # --------------------------------------------------------------

    df = df[FINAL_COLUMNS]

    # --------------------------------------------------------------
    # Create output directory if needed
    # --------------------------------------------------------------

    output_directory = os.path.dirname(output_path)

    if output_directory:
        os.makedirs(
            output_directory,
            exist_ok=True
        )

    # --------------------------------------------------------------
    # Save CSV
    # --------------------------------------------------------------

    df.to_csv(
        output_path,
        index=False
    )

    print(f"\nDataset saved successfully.")
    print(f"Location : {output_path}")
    print(f"Rows     : {len(df)}")
    print(f"Columns  : {len(df.columns)}")

    return df


# ------------------------------------------------------------------
# Standalone Testing
# ------------------------------------------------------------------

if __name__ == "__main__":

    from feature_generator import generate_feature_sample
    from risk_model import calculate_structural_risk
    from probability_model import calculate_failure_probability

    samples = []

    for _ in range(5):

        sample = generate_feature_sample()

        sample = calculate_structural_risk(sample)

        sample = calculate_failure_probability(sample)

        samples.append(sample)

    write_dataset(samples)