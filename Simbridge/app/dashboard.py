"""
app/dashboard.py
----------------

Displays the DigiBridge terminal dashboard.
"""

from __future__ import annotations

import os


class Dashboard:

    def update(

        self,

        bridge,

        simulation,

        sensor_data,

        prediction,

    ):

        os.system("cls" if os.name == "nt" else "clear")

        print("=" * 75)
        print("=" * 75)
        print(r"""
        ██████╗ ██╗ ██████╗ ██╗██████╗ ██████╗ ██╗██████╗  ██████╗ ███████╗
        ██╔══██╗██║██╔════╝ ██║██╔══██╗██╔══██╗██║██╔══██╗██╔════╝ ██╔════╝
        ██║  ██║██║██║  ███╗██║██████╔╝██████╔╝██║██║  ██║██║  ███╗█████╗
        ██║  ██║██║██║   ██║██║██╔══██╗██╔══██╗██║██║  ██║██║   ██║██╔══╝
        ██████╔╝██║╚██████╔╝██║██████╔╝██║  ██║██║██████╔╝╚██████╔╝███████╗
        ╚═════╝ ╚═╝ ╚═════╝ ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝ ╚══════╝
        """)
        print("=" * 75)
        print("=" * 75)
        print()

        print("LIVE SENSOR DATA")
        print("-" * 50)

        print(f"Temperature       : {sensor_data['temperature']:.1f} °C")
        print(f"Humidity          : {sensor_data['humidity']:.1f} %")
        print(f"Vehicle Load      : {sensor_data['load']:.2f} kg")

        print()

        print("SIMULATION PARAMETERS")
        print("-" * 50)

        print(f"Pedestrian Load   : {simulation.pedestrian_load:.2f}")
        print(f"Wind Speed        : {simulation.wind_speed:.2f} m/s")
        print(f"Rainfall          : {simulation.rainfall:.2f} mm")
        print(f"River Level       : {simulation.river_water_level:.2f} m")
        print(f"Safety Factor     : {simulation.safety_factor:.2f}")

        print()

        print("AI PREDICTION")
        print("-" * 50)

        print(
            f"Failure Probability : "
            f"{prediction.failure_probability*100:.2f}%"
        )

        print(
            f"Risk Level          : "
            f"{prediction.risk_level}"
        )

        print(
            f"Confidence          : "
            f"{prediction.confidence*100:.2f}%"
        )

        print(
            f"Prediction Time     : "
            f"{prediction.prediction_time:.4f} sec"
        )

        print()

        print("=" * 80)