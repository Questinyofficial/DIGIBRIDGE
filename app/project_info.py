"""
app/project_info.py
-------------------

Displays information about the DigiBridge project.

Responsibilities
----------------
- Display project overview
- Display software architecture
- Display AI model information
- Display hardware information
- Display project directory structure

Does NOT
--------
- Run diagnostics
- Launch the application
- Train AI models
"""

from __future__ import annotations


class ProjectInfo:
    """
    Displays DigiBridge project information.
    """

    @staticmethod
    def show():

        print()
        print("=" * 78)
        print("DIGIBRIDGE PROJECT INFORMATION")
        print("=" * 78)

        print()
        print("PROJECT")
        print("-" * 78)
        print("Name              : DigiBridge")
        print("Version           : 1.0.0")
        print("Type              : AI-Based Bridge Digital Twin")
        print("Platform          : Desktop Application")
        print("Language          : Python")
        print("Author            : Rohan J Philip")

        print()
        print("DESCRIPTION")
        print("-" * 78)
        print(
            "DigiBridge is an AI-powered bridge digital twin that combines\n"
            "live sensor data from a physical bridge model with a trained\n"
            "Random Forest model to estimate the probability of structural\n"
            "failure in real time."
        )

        print()
        print("FEATURES")
        print("-" * 78)
        print("✓ Live Arduino Sensor Integration")
        print("✓ Temperature Monitoring")
        print("✓ Humidity Monitoring")
        print("✓ Load Monitoring")
        print("✓ Digital Twin Simulation")
        print("✓ AI Failure Prediction")
        print("✓ Multiple Bridge Models")
        print("✓ Automatic Arduino Detection")
        print("✓ Hardware Diagnostics")
        print("✓ Dataset Generation")
        print("✓ AI Model Training")

        print()
        print("HARDWARE")
        print("-" * 78)
        print("• Arduino UNO")
        print("• DHT11 Temperature & Humidity Sensor")
        print("• HX711 Load Cell Amplifier")
        print("• Load Cell")
        print("• Forex Sheet Bridge Model")

        print()
        print("SOFTWARE")
        print("-" * 78)
        print("• Python")
        print("• Scikit-Learn")
        print("• Pandas")
        print("• NumPy")
        print("• Joblib")
        print("• PySerial")

        print()
        print("AI MODEL")
        print("-" * 78)
        print("Algorithm         : Random Forest Regressor")
        print("Prediction Target : Bridge Failure Probability")
        print("Training Dataset  : Synthetic Bridge Dataset")
        print("Output            : Failure Probability")
        print("Risk Levels       : LOW / MODERATE / HIGH / CRITICAL")

        print()
        print("APPLICATION MODULES")
        print("-" * 78)
        print("• Bridge Model")
        print("• Digital Twin")
        print("• Prediction Engine")
        print("• Hardware Interface")
        print("• Live Simulation")
        print("• Terminal Dashboard")
        print("• Diagnostics")
        print("• Dataset Generator")
        print("• AI Trainer")

        print()
        print("=" * 78)
        print("DigiBridge © 2026")
        print("=" * 78)

        input("\nPress ENTER to continue...")