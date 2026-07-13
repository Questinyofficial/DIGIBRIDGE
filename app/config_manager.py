"""
app/config_manager.py
---------------------

Reads and writes DigiBridge configuration.
"""

from __future__ import annotations

import json
from pathlib import Path


class ConfigManager:

    CONFIG_FILE = Path("config.json")

    DEFAULT_CONFIG = {

        "bridge": "data/bridges/default_bridge.json",

        "model": "models/random_forest.pkl",

        "update_interval": 2,

        "baud_rate": 9600,

        "auto_detect_arduino": True

    }

    # ---------------------------------------------------------

    def __init__(self):

        if not self.CONFIG_FILE.exists():

            self.config = self.DEFAULT_CONFIG.copy()

            self.save()

        else:

            with open(self.CONFIG_FILE, "r") as f:

                self.config = json.load(f)

    # ---------------------------------------------------------

    def save(self):

        with open(self.CONFIG_FILE, "w") as f:

            json.dump(

                self.config,

                f,

                indent=4

            )

    # ---------------------------------------------------------

    def get_bridge(self):

        return self.config["bridge"]

    def set_bridge(self, bridge):

        self.config["bridge"] = bridge

    # ---------------------------------------------------------

    def get_model(self):

        return self.config["model"]

    def set_model(self, model):

        self.config["model"] = model

    # ---------------------------------------------------------

    def get_update_interval(self):

        return self.config["update_interval"]

    def set_update_interval(self, interval):

        self.config["update_interval"] = interval

    # ---------------------------------------------------------

    def get_baud_rate(self):

        return self.config["baud_rate"]

    def set_baud_rate(self, baud):

        self.config["baud_rate"] = baud

    # ---------------------------------------------------------

    def get_auto_detect(self):

        return self.config["auto_detect_arduino"]

    def set_auto_detect(self, value):

        self.config["auto_detect_arduino"] = value