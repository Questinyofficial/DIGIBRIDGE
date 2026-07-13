"""
bridge/material.py
------------------

Defines the Material class used by bridge members.

This module contains only engineering data and does not perform
any GUI operations, AI prediction, or simulation logic.
"""

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Material:
    """
    Represents the material assigned to a bridge member.

    Attributes
    ----------
    name : str
        Name of the material (e.g., Steel, Concrete).

    density : float
        Density of the material (kg/mcube).

    youngs_modulus : float
        Young's Modulus (Pa).

    poisson_ratio : float
        Poisson's Ratio.

    yield_strength : float
        Yield Strength (Pa).

    ultimate_strength : float
        Ultimate Tensile Strength (Pa).

    thermal_expansion : float
        Coefficient of thermal expansion (1 C).

    corrosion_resistance : float
        Relative corrosion resistance (0-1).

    cost_per_kg : float
        Material cost per kilogram.
    """

    name: str

    density: float
    youngs_modulus: float
    poisson_ratio: float

    yield_strength: float
    ultimate_strength: float

    thermal_expansion: float

    corrosion_resistance: float

    cost_per_kg: float

    metadata: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the material into a dictionary.

        Returns
        -------
        dict
        """

        return {
            "name": self.name,
            "density": self.density,
            "youngs_modulus": self.youngs_modulus,
            "poisson_ratio": self.poisson_ratio,
            "yield_strength": self.yield_strength,
            "ultimate_strength": self.ultimate_strength,
            "thermal_expansion": self.thermal_expansion,
            "corrosion_resistance": self.corrosion_resistance,
            "cost_per_kg": self.cost_per_kg,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Material":
        """
        Create a Material object from a dictionary.
        """

        return cls(
            name=data["name"],
            density=data["density"],
            youngs_modulus=data["youngs_modulus"],
            poisson_ratio=data["poisson_ratio"],
            yield_strength=data["yield_strength"],
            ultimate_strength=data["ultimate_strength"],
            thermal_expansion=data["thermal_expansion"],
            corrosion_resistance=data["corrosion_resistance"],
            cost_per_kg=data["cost_per_kg"],
            metadata=data.get("metadata", {}),
        )

    # ------------------------------------------------------------------
    # Utility Methods
    # ------------------------------------------------------------------

    def copy(self) -> "Material":
        """
        Returns a deep copy of the material.
        """

        return Material.from_dict(self.to_dict())

    def __str__(self) -> str:
        return (
            f"Material("
            f"name={self.name}, "
            f"density={self.density}, "
            f"E={self.youngs_modulus}, "
            f"yield={self.yield_strength})"
        )

    def __repr__(self) -> str:
        return self.__str__()