"""
prediction/predictor.py
-----------------------

Runs the trained Random Forest model to predict
bridge failure probability.

Responsibilities
----------------
- Load trained model
- Build feature vector
- Predict failure probability
- Return PredictionResult

No GUI code.
No simulation logic.
"""

from __future__ import annotations
import pandas as pd
import time
from pathlib import Path

import joblib
import numpy as np

from bridge.bridge_model import BridgeModel
from prediction.feature_builder import FeatureBuilder
from prediction.prediction_result import PredictionResult
from simulation.simulation_parameters import SimulationParameters

print("Predictor loaded from:")
print(__file__)
class Predictor:
    """
    Random Forest prediction engine.
    """

    def __init__(self, model_path: str | Path):

        self.model_path = Path(model_path)

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model not found: {self.model_path}"
            )

        loaded = joblib.load(self.model_path)

        # ---------------------------------------------------------
        # Support both:
        #
        # joblib.dump(model)
        #
        # and
        #
        # joblib.dump({
        #     "model": model,
        #     "feature_names": [...]
        # })
        # ---------------------------------------------------------

        if isinstance(loaded, dict):
            self.model = loaded["model"]
            self.feature_names = loaded.get("feature_names")
        else:
            self.model = loaded
            self.feature_names = None

    # -------------------------------------------------------------
    # Prediction
    # -------------------------------------------------------------

    def predict(
        self,
        bridge: BridgeModel,
        simulation: SimulationParameters,
    ) -> PredictionResult:
        """
        Predict bridge failure probability.

        Parameters
        ----------
        bridge : BridgeModel

        simulation : SimulationParameters

        Returns
        -------
        PredictionResult
        """

        start = time.perf_counter()

        features = FeatureBuilder.build_features(
            bridge,
            simulation,
        )
        print("\nFEATURE VECTOR")
        print("-" * 60)

        for name, value in zip(
            FeatureBuilder.feature_names(),
            features):
            print(f"{name:30} {value}")

        # ---------------------------------------------------------
        # Validate feature count
        # ---------------------------------------------------------

        if (
            self.feature_names is not None
            and len(features) != len(self.feature_names)
        ):
            raise ValueError(
                "Feature count does not match the trained model.\n"
                f"Expected {len(self.feature_names)} features.\n"
                f"Received {len(features)}."
            )

        feature_names = FeatureBuilder.feature_names()

        X = pd.DataFrame(
            [features],
            columns=feature_names
        )

        probability = float(
            self.model.predict(X)[0]
        )

        # Clamp prediction to [0, 1]
        probability = max(0.0, min(1.0, probability))

        prediction_time = time.perf_counter() - start

        confidence = self._calculate_confidence(probability)

        risk = self._risk_level(probability)

        return PredictionResult(
            failure_probability=probability,
            risk_level=risk,
            confidence=confidence,
            prediction_time=prediction_time,
        )

    # -------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------

    @staticmethod
    def _risk_level(probability: float) -> str:
        """
        Convert probability into a risk category.
        """

        if probability < 0.20:
            return "LOW"

        if probability < 0.50:
            return "MODERATE"

        if probability < 0.75:
            return "HIGH"

        return "CRITICAL"

    @staticmethod
    def _calculate_confidence(probability: float) -> float:
        """
        Approximate prediction confidence.

        NOTE
        ----
        RandomForestRegressor does not directly provide
        confidence scores.

        This method returns a heuristic confidence.

        Later, confidence can be computed from the
        variance of all decision trees.
        """

        distance = abs(probability - 0.5)

        confidence = 0.60 + (distance * 0.80)

        return min(confidence, 0.99)