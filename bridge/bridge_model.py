"""
bridge/bridge_model.py
----------------------

Defines the BridgeModel class.

The BridgeModel is the central engineering representation of the bridge.
It stores every node, member, and available material while providing
utility methods for querying and modifying the model.

This module contains no GUI, simulation, or AI prediction logic.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from bridge.node import Node
from bridge.member import Member
from bridge.material import Material


class BridgeModel:
    """
    Represents the complete bridge.

    Attributes
    ----------
    nodes
        Dictionary of Node objects indexed by node ID.

    members
        Dictionary of Member objects indexed by member ID.

    materials
        Dictionary of available materials indexed by material name.
    """

    def __init__(self) -> None:
        self.nodes: Dict[int, Node] = {}
        self.members: Dict[int, Member] = {}
        self.materials: Dict[str, Material] = {}

    # ------------------------------------------------------------------
    # Node Management
    # ------------------------------------------------------------------

    def add_node(self, node: Node) -> None:
        """Add a node to the bridge."""

        if node.node_id in self.nodes:
            raise ValueError(f"Node {node.node_id} already exists.")

        self.nodes[node.node_id] = node

    def get_node(self, node_id: int) -> Optional[Node]:
        """Return a node by its ID."""
        return self.nodes.get(node_id)

    def remove_node(self, node_id: int) -> None:
        """
        Remove a node.

        Raises
        ------
        ValueError
            If the node is connected to any member.
        """

        if node_id not in self.nodes:
            raise KeyError(f"Node {node_id} does not exist.")

        for member in self.members.values():
            if (
                member.start_node.node_id == node_id
                or member.end_node.node_id == node_id
            ):
                raise ValueError(
                    f"Cannot remove node {node_id}; it is connected to member {member.member_id}."
                )

        del self.nodes[node_id]

    # ------------------------------------------------------------------
    # Member Management
    # ------------------------------------------------------------------

    def add_member(self, member: Member) -> None:
        """Add a member to the bridge."""

        if member.member_id in self.members:
            raise ValueError(f"Member {member.member_id} already exists.")

        self.members[member.member_id] = member

    def get_member(self, member_id: int) -> Optional[Member]:
        """Return a member by its ID."""
        return self.members.get(member_id)

    def remove_member(self, member_id: int) -> None:
        """Remove a member."""

        if member_id not in self.members:
            raise KeyError(f"Member {member_id} does not exist.")

        del self.members[member_id]

    # ------------------------------------------------------------------
    # Material Management
    # ------------------------------------------------------------------

    def add_material(self, material: Material) -> None:
        """Register an available material."""

        self.materials[material.name] = material

    def get_material(self, name: str) -> Optional[Material]:
        """Return a material by name."""
        return self.materials.get(name)

    def assign_material(self, member_id: int, material_name: str) -> None:
        """
        Assign a material to a member.
        """

        member = self.get_member(member_id)
        if member is None:
            raise KeyError(f"Member {member_id} not found.")

        material = self.get_material(material_name)
        if material is None:
            raise KeyError(f"Material '{material_name}' not found.")

        member.set_material(material)

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def get_all_nodes(self) -> List[Node]:
        """Return all nodes."""
        return list(self.nodes.values())

    def get_all_members(self) -> List[Member]:
        """Return all members."""
        return list(self.members.values())

    def get_all_materials(self) -> List[Material]:
        """Return all registered materials."""
        return list(self.materials.values())

    def member_count(self) -> int:
        """Return number of members."""
        return len(self.members)

    def node_count(self) -> int:
        """Return number of nodes."""
        return len(self.nodes)

    def total_length(self) -> float:
        """Return total member length."""
        return sum(member.length for member in self.members.values())

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        """
        Convert the bridge into a serializable dictionary.
        """

        return {
            "nodes": [
                node.to_dict()
                for node in self.nodes.values()
            ],
            "materials": [
                material.to_dict()
                for material in self.materials.values()
            ],
            "members": [
                member.to_dict()
                for member in self.members.values()
            ],
        }

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    def clear(self) -> None:
        """Remove every node, member, and material."""

        self.nodes.clear()
        self.members.clear()
        self.materials.clear()

    def __str__(self) -> str:
        return (
            f"BridgeModel("
            f"nodes={self.node_count()}, "
            f"members={self.member_count()}, "
            f"materials={len(self.materials)})"
        )

    def __repr__(self) -> str:
        return self.__str__()