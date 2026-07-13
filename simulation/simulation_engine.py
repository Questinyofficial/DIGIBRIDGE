"""
simulation/simulation_engine.py
-------------------------------

Coordinates the complete bridge simulation workflow.

Workflow
--------
BridgeModel
      ↓
SimulationParameters
      ↓
SimulationValidator
      ↓
FeatureBuilder
      ↓
Random Forest Predictor
      ↓
PredictionResult

This module contains no GUI code.
"""

from __future__ import annotations

from pathlib import Path

from bridge.bridge_model import BridgeModel
from prediction.predictor import Predictor
from prediction.prediction_result import PredictionResult
from simulation.simulation_parameters import SimulationParameters
from simulation.validator import SimulationValidator


class SimulationEngine:
    """
    Coordinates bridge simulation and AI prediction.
    """

    def __init__(self, model_path: str | Path):
        """
        Initialize the simulation engine.

        Parameters
        ----------
        model_path : str | Path
            Path to the trained Random Forest model.
        """

        self.predictor = Predictor(model_path)

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def run(
        self,
        bridge: BridgeModel,
        simulation: SimulationParameters,
    ) -> PredictionResult:
        """
        Run a complete bridge simulation.

        Parameters
        ----------
        bridge : BridgeModel

        simulation : SimulationParameters

        Returns
        -------
        PredictionResult
        """

        # Step 1: Validate user input
        SimulationValidator.validate(simulation)

        # Step 2: Perform prediction
        result = self.predictor.predict(
            bridge,
            simulation,
        )

        return result

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    @property
    def model_loaded(self) -> bool:
        """
        Returns True if the predictor has loaded a model.
        """

        return self.predictor is not None