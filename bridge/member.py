"""
bridge/member.py
----------------

Defines the Member class used in the bridge model.

A Member represents a structural element connecting two nodes in the
bridge truss. It stores its assigned material, geometric properties,
condition data, and engineering attributes.

This module contains only engineering data structures.
No GUI, AI prediction, or simulation logic belongs here.
"""

from dataclasses import dataclass, field
from math import sqrt
from typing import Dict, Any, Optional

from bridge.material import Material
from bridge.node import Node


@dataclass
class Member:
    """
    Represents a bridge member (edge).

    Attributes
    ----------
    member_id : int
        Unique identifier.

    start_node : Node
        Starting node.

    end_node : Node
        Ending node.

    material : Material
        Assigned material.

    area : float
        Cross-sectional area (m square).

    age : float
        Age of the member (years).

    corrosion : float
        Corrosion percentage (0-100).

    crack_width : float
        Crack width (mm).

    metadata : dict
        Optional user-defined information.
    """

    member_id: int

    start_node: Node
    end_node: Node

    material: Material

    area: float

    age: float = 0.0
    corrosion: float = 0.0
    crack_width: float = 0.0

    metadata: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Geometry
    # ------------------------------------------------------------------

    @property
    def length(self) -> float:
        """
        Returns the member length in meters.
        """
        dx = self.end_node.x - self.start_node.x
        dy = self.end_node.y - self.start_node.y
        return sqrt(dx * dx + dy * dy)

    @property
    def angle(self) -> float:
        """
        Returns the angle of the member in radians.
        """
        from math import atan2

        dx = self.end_node.x - self.start_node.x
        dy = self.end_node.y - self.start_node.y
        return atan2(dy, dx)

    # ------------------------------------------------------------------
    # Material
    # ------------------------------------------------------------------

    def set_material(self, material: Material) -> None:
        """
        Assign a new material to the member.
        """
        self.material = material

    # ------------------------------------------------------------------
    # Condition
    # ------------------------------------------------------------------

    def set_condition(
        self,
        *,
        age: Optional[float] = None,
        corrosion: Optional[float] = None,
        crack_width: Optional[float] = None,
    ) -> None:
        """
        Update condition-related properties.
        """

        if age is not None:
            self.age = age

        if corrosion is not None:
            self.corrosion = corrosion

        if crack_width is not None:
            self.crack_width = crack_width

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert member into a dictionary.
        """

        return {
            "member_id": self.member_id,
            "start_node": self.start_node.node_id,
            "end_node": self.end_node.node_id,
            "material": self.material.name,
            "area": self.area,
            "age": self.age,
            "corrosion": self.corrosion,
            "crack_width": self.crack_width,
            "metadata": self.metadata,
        }

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    def copy(
        self,
        start_node: Node,
        end_node: Node,
        material: Material,
    ) -> "Member":
        """
        Create a copy of this member using supplied node/material objects.
        """

        return Member(
            member_id=self.member_id,
            start_node=start_node,
            end_node=end_node,
            material=material,
            area=self.area,
            age=self.age,
            corrosion=self.corrosion,
            crack_width=self.crack_width,
            metadata=self.metadata.copy(),
        )

    def __str__(self) -> str:
        return (
            f"Member("
            f"id={self.member_id}, "
            f"{self.start_node.node_id}->{self.end_node.node_id}, "
            f"material={self.material.name}, "
            f"length={self.length:.3f} m)"
        )

    def __repr__(self) -> str:
        return self.__str__()