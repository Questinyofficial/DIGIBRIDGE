"""
bridge/node.py
--------------

Defines the Node class used in the bridge model.

A Node represents a joint (vertex) in the bridge truss. Nodes are
connected by members and may contain supports, external loads, and
optional sensor information.

This module contains only engineering data structures.
No GUI, AI, or simulation logic belongs here.
"""

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Node:
    """
    Represents a single node (joint) in the bridge.

    Attributes
    ----------
    node_id : int
        Unique identifier.

    x : float
        X coordinate (meters).

    y : float
        Y coordinate (meters).

    support_type : str
        Support condition.
        Allowed examples:
            - "NONE"
            - "PINNED"
            - "ROLLER"
            - "FIXED"

    load_x : float
        Horizontal applied load (kN).

    load_y : float
        Vertical applied load (kN).

    sensor_installed : bool
        Whether a monitoring sensor is installed.

    metadata : dict
        Optional custom data.
    """

    node_id: int

    x: float
    y: float

    support_type: str = "NONE"

    load_x: float = 0.0
    load_y: float = 0.0

    sensor_installed: bool = False

    metadata: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Geometry
    # ------------------------------------------------------------------

    @property
    def position(self) -> tuple[float, float]:
        """
        Returns the node coordinates.
        """
        return self.x, self.y

    def set_position(self, x: float, y: float) -> None:
        """
        Updates node coordinates.
        """
        self.x = x
        self.y = y

    # ------------------------------------------------------------------
    # Loads
    # ------------------------------------------------------------------

    def set_load(self, load_x: float, load_y: float) -> None:
        """
        Assign external loads.
        """
        self.load_x = load_x
        self.load_y = load_y

    def clear_load(self) -> None:
        """
        Removes all applied loads.
        """
        self.load_x = 0.0
        self.load_y = 0.0

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert node to dictionary.
        """
        return {
            "node_id": self.node_id,
            "x": self.x,
            "y": self.y,
            "support_type": self.support_type,
            "load_x": self.load_x,
            "load_y": self.load_y,
            "sensor_installed": self.sensor_installed,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Node":
        """
        Create a Node from a dictionary.
        """
        return cls(
            node_id=data["node_id"],
            x=data["x"],
            y=data["y"],
            support_type=data.get("support_type", "NONE"),
            load_x=data.get("load_x", 0.0),
            load_y=data.get("load_y", 0.0),
            sensor_installed=data.get("sensor_installed", False),
            metadata=data.get("metadata", {}),
        )

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    def copy(self) -> "Node":
        """
        Returns a copy of this node.
        """
        return Node.from_dict(self.to_dict())

    def __str__(self) -> str:
        return (
            f"Node("
            f"id={self.node_id}, "
            f"position=({self.x}, {self.y}), "
            f"support={self.support_type})"
        )

    def __repr__(self) -> str:
        return self.__str__()