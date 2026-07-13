"""
utils/json_utils.py
------------------

Utility functions for reading and writing JSON files.

These functions provide a consistent interface for
loading and saving JSON data throughout the application.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_json(file_path: str | Path) -> dict:
    """
    Load a JSON file.

    Parameters
    ----------
    file_path : str | Path

    Returns
    -------
    dict
        Parsed JSON object.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.

    json.JSONDecodeError
        If the file contains invalid JSON.
    """

    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(
    data: Any,
    file_path: str | Path,
    indent: int = 4,
) -> None:
    """
    Save data to a JSON file.

    Parameters
    ----------
    data : Any

    file_path : str | Path

    indent : int
        JSON indentation.
    """

    path = Path(file_path)

    # Create parent directories if needed
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=indent,
            ensure_ascii=False,
        )


def file_exists(file_path: str | Path) -> bool:
    """
    Returns True if the JSON file exists.
    """

    return Path(file_path).exists()


def pretty_print(data: Any) -> str:
    """
    Convert an object into a formatted JSON string.

    Useful for debugging.
    """

    return json.dumps(
        data,
        indent=4,
        ensure_ascii=False,
    )