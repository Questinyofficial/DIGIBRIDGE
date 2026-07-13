"""
bridge/bridge_loader.py
-----------------------

Loads a bridge model from a JSON file.

Responsibilities
----------------
- Load nodes
- Load materials
- Load members
- Construct a complete BridgeModel

This module performs no GUI operations, simulation,
or AI prediction.
"""

from __future__ import annotations

import json
from pathlib import Path

from bridge.bridge_model import BridgeModel
from bridge.node import Node
from bridge.member import Member
from bridge.material import Material


class BridgeLoader:
    """
    Utility class responsible for loading bridge models
    from JSON files.
    """

    @staticmethod
    def load(json_file: str | Path) -> BridgeModel:
        """
        Load a bridge model from a JSON file.

        Parameters
        ----------
        json_file : str | Path
            Path to bridge JSON.

        Returns
        -------
        BridgeModel
        """

        json_file = Path(json_file)

        if not json_file.exists():
            raise FileNotFoundError(f"Bridge file not found: {json_file}")

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        bridge = BridgeModel()

        # ---------------------------------------------------------
        # Load Materials
        # ---------------------------------------------------------

        for material_data in data.get("materials", []):
            material = Material.from_dict(material_data)
            bridge.add_material(material)

        # ---------------------------------------------------------
        # Load Nodes
        # ---------------------------------------------------------

        for node_data in data.get("nodes", []):
            node = Node.from_dict(node_data)
            bridge.add_node(node)

        # ---------------------------------------------------------
        # Load Members
        # ---------------------------------------------------------

        for member_data in data.get("members", []):

            start_node = bridge.get_node(member_data["start_node"])
            end_node = bridge.get_node(member_data["end_node"])

            if start_node is None:
                raise ValueError(
                    f"Member {member_data['member_id']} references "
                    f"missing start node {member_data['start_node']}."
                )

            if end_node is None:
                raise ValueError(
                    f"Member {member_data['member_id']} references "
                    f"missing end node {member_data['end_node']}."
                )

            material = bridge.get_material(member_data["material"])

            if material is None:
                raise ValueError(
                    f"Member {member_data['member_id']} references "
                    f"unknown material '{member_data['material']}'."
                )

            member = Member(
                member_id=member_data["member_id"],
                start_node=start_node,
                end_node=end_node,
                material=material,
                area=member_data["area"],
                age=member_data.get("age", 0.0),
                corrosion=member_data.get("corrosion", 0.0),
                crack_width=member_data.get("crack_width", 0.0),
                metadata=member_data.get("metadata", {}),
            )

            bridge.add_member(member)

        return bridge

    @staticmethod
    def save(bridge: BridgeModel, json_file: str | Path) -> None:
        """
        Save a BridgeModel to a JSON file.

        Parameters
        ----------
        bridge : BridgeModel

        json_file : str |Path
        """

        json_file = Path(json_file)

        json_file.parent.mkdir(parents=True, exist_ok=True)

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(
                bridge.to_dict(),
                f,
                indent=4,
            )