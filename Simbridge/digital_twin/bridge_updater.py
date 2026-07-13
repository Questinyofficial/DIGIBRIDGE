"""
digital_twin/bridge_updater.py
------------------------------

Updates the structural condition of the bridge
to simulate long-term deterioration.

Responsibilities
----------------
- Increase corrosion gradually
- Increase crack width gradually
- Update member age

Does NOT
---------
- Read Arduino
- Predict failure
- Modify loads
"""

from __future__ import annotations

import random

from bridge.bridge_model import BridgeModel


class BridgeUpdater:
    """
    Simulates bridge deterioration.
    """

    def __init__(self):

        self.time_step = 0

    # ----------------------------------------------------------

    def update(
        self,
        bridge: BridgeModel
    ) -> BridgeModel:
        """
        Update every bridge member.

        Parameters
        ----------
        bridge : BridgeModel

        Returns
        -------
        BridgeModel
        """

        self.time_step += 1

        for member in bridge.get_all_members():

            self._update_member(member)

        return bridge

    # ----------------------------------------------------------

    def _update_member(self, member):
        """
        Update one bridge member.
        """

        # ------------------------------------------------------
        # Age
        #
        # Exhibition:
        # Increase every 1000 updates
        # ------------------------------------------------------

        if self.time_step % 1000 == 0:

            member.age += 1

        # ------------------------------------------------------
        # Corrosion
        # ------------------------------------------------------

        member.corrosion += random.uniform(
            0.0000,
            0.0005
        )

        member.corrosion = min(
            member.corrosion,
            1.0
        )

        # ------------------------------------------------------
        # Crack Width
        # ------------------------------------------------------

        member.crack_width += random.uniform(
            0.000,
            0.003
        )

        member.crack_width = min(
            member.crack_width,
            5.0
        )