"""
generate_dataset.py
-------------------

Main entry point for the Bridge Digital Twin Dataset Generator.

Workflow
--------
Load Config
      ↓
Generate Bridge Features
      ↓
Calculate Structural Risk
      ↓
Calculate Failure Probability
      ↓
Repeat for NUM_SAMPLES
      ↓
Write Dataset to CSV
"""
print("hello world")
from config import NUM_SAMPLES, OUTPUT_CSV

from feature_generator import generate_feature_sample
from risk_model import calculate_structural_risk
from probability_model import calculate_failure_probability
from csv_writer import write_dataset


# ------------------------------------------------------------------
# Dataset Generator
# ------------------------------------------------------------------

def generate_dataset():
    """
    Generates the complete Bridge Digital Twin dataset.

    Returns
    -------
    pandas.DataFrame
        Generated dataset.
    """

    samples = []

    print("=" * 60)
    print("Bridge Digital Twin Dataset Generator")
    print("=" * 60)
    print(f"Generating {NUM_SAMPLES:,} bridge samples...\n")

    for i in range(NUM_SAMPLES):

        # ----------------------------------------------------------
        # Generate bridge features
        # ----------------------------------------------------------

        sample = generate_feature_sample()

        # ----------------------------------------------------------
        # Calculate structural risk
        # ----------------------------------------------------------

        sample = calculate_structural_risk(sample)

        # ----------------------------------------------------------
        # Calculate failure probability
        # ----------------------------------------------------------

        sample = calculate_failure_probability(sample)

        samples.append(sample)

        # ----------------------------------------------------------
        # Progress update every 10,000 samples
        # ----------------------------------------------------------

        if (i + 1) % 10000 == 0:
            print(f"Generated {i + 1:,} samples...")

    print("\nWriting dataset to CSV...\n")

    dataset = write_dataset(
        samples=samples,
        output_path=OUTPUT_CSV
    )

    print("\nDataset generation completed successfully.")
    print(f"Total Samples : {len(dataset):,}")
    print(f"Total Features: {len(dataset.columns)}")

    return dataset


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

if __name__ == "__main__":

    generate_dataset()