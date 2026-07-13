"""
hardware/serial_reader.py
-------------------------

Automatically finds an Arduino and reads
CSV sensor data.

Expected Arduino Output
-----------------------
temperature,humidity,load

Example
-------
31.4,65.2,12.8
"""

from __future__ import annotations

import time
import serial
import serial.tools.list_ports


class SerialReader:

    def __init__(self, baudrate=9600, timeout=2):

        self.baudrate = baudrate
        self.timeout = timeout

        self.serial_connection = None
        self.port = None

    # ---------------------------------------------------------

    def _find_arduino(self):
        """
        Search all serial ports for an Arduino.
        """

        ports = serial.tools.list_ports.comports()

        if not ports:
            return None

        for port in ports:

            description = port.description.lower()
            manufacturer = (
                port.manufacturer.lower()
                if port.manufacturer
                else ""
            )

            if (
                "arduino" in description
                or "ch340" in description
                or "usb serial" in description
                or "wch" in manufacturer
            ):
                return port.device

        # Fallback:
        # if only one serial device exists, use it.

        if len(ports) == 1:
            return ports[0].device

        return None

    # ---------------------------------------------------------

    def connect(self):

        self.port = self._find_arduino()

        if self.port is None:

            print("[ERROR] Arduino not found.")

            return False

        try:

            self.serial_connection = serial.Serial(
                self.port,
                self.baudrate,
                timeout=self.timeout
            )

            time.sleep(2)

            print(f"[INFO] Connected on {self.port}")

            return True

        except Exception as e:

            print(e)

            return False

    # ---------------------------------------------------------

    def disconnect(self):

        if (
            self.serial_connection
            and self.serial_connection.is_open
        ):
            self.serial_connection.close()

    # ---------------------------------------------------------

    def is_connected(self):

        return (
            self.serial_connection
            is not None
            and
            self.serial_connection.is_open
        )

    # ---------------------------------------------------------

    def read_sensor_data(self):

        if not self.is_connected():
            return None

        try:

            line = (
                self.serial_connection
                .readline()
                .decode("utf-8", errors="ignore")
                .strip()
            )

            if not line:
                return None

            if line == "ERROR":
                return None

            print("RAW:", line)

            values = line.split(",")

            if len(values) != 3:

                print("[WARNING] Invalid CSV:", line)

                return None

            return {

                "temperature": float(values[0]),
                "humidity": float(values[1]),
                "load": float(values[2])

            }

        except Exception as e:

            print(e)

            return None