"""
prediction/prediction_result.py
-------------------------------

Defines the PredictionResult class.

This module represents the output of the AI prediction engine.

It contains no machine learning logic or GUI code.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class PredictionResult:
    """
    Represents the output of the bridge failure prediction.

    Attributes
    ----------
    failure_probability : float
        Probability of bridge failure (0.0 - 1.0).

    risk_level : str
        Risk category (LOW, MODERATE, HIGH, CRITICAL).

    confidence : float
        Confidence of the prediction (0.0 - 1.0).

    prediction_time : float
        Time taken to perform the prediction (seconds).

    timestamp : datetime
        Time when the prediction was generated.

    metadata : dict
        Optional additional information.
    """

    failure_probability: float
    risk_level: str
    confidence: float
    prediction_time: float

    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Convenience Properties
    # ------------------------------------------------------------------

    @property
    def failure_percentage(self) -> float:
        """
        Returns the failure probability as a percentage.
        """
        return self.failure_probability * 100.0

    @property
    def confidence_percentage(self) -> float:
        """
        Returns the confidence as a percentage.
        """
        return self.confidence * 100.0

    @property
    def is_safe(self) -> bool:
        """
        Indicates whether the bridge is considered safe.
        """
        return self.failure_probability < 0.30

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the prediction result to a dictionary.
        """

        return {
            "failure_probability": self.failure_probability,
            "failure_percentage": self.failure_percentage,
            "risk_level": self.risk_level,
            "confidence": self.confidence,
            "confidence_percentage": self.confidence_percentage,
            "prediction_time": self.prediction_time,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PredictionResult":
        """
        Create a PredictionResult from a dictionary.
        """

        return cls(
            failure_probability=data["failure_probability"],
            risk_level=data["risk_level"],
            confidence=data["confidence"],
            prediction_time=data["prediction_time"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            metadata=data.get("metadata", {}),
        )

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        return (
            f"PredictionResult("
            f"Failure={self.failure_percentage:.2f}%, "
            f"Risk={self.risk_level}, "
            f"Confidence={self.confidence_percentage:.2f}%, "
            f"Time={self.prediction_time:.4f}s)"
        )

    def __repr__(self) -> str:
        return self.__str__()