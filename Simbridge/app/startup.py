"""
app/startup.py
--------------

Displays the DigiBridge startup banner.

Responsibilities
----------------
- Clear the screen
- Display DigiBridge logo
- Display version information

Does NOT:
- Check hardware
- Load configuration
- Launch the application
"""

from __future__ import annotations

import os
from datetime import datetime

# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "DigiBridge"
VERSION = "1.0.0"
AUTHOR = "ROHAN J PHILIP"
COPYRIGHT = "© 2026 DigiBridge Project"


# ==========================================================
# Utilities
# ==========================================================

def clear_screen() -> None:
    """
    Clear the terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


# ==========================================================
# Banner
# ==========================================================

def show_banner() -> None:
    """
    Display the DigiBridge startup banner.
    """

    clear_screen()

    print("=" * 78)
    print()

    print("=" * 75)
    print("=" * 75)
    print(r"""
    ██████╗ ██╗ ██████╗ ██╗██████╗ ██████╗ ██╗██████╗  ██████╗ ███████╗
    ██╔══██╗██║██╔════╝ ██║██╔══██╗██╔══██╗██║██╔══██╗██╔════╝ ██╔════╝
    ██║  ██║██║██║  ███╗██║██████╔╝██████╔╝██║██║  ██║██║  ███╗█████╗
    ██║  ██║██║██║   ██║██║██╔══██╗██╔══██╗██║██║  ██║██║   ██║██╔══╝
    ██████╔╝██║╚██████╔╝██║██████╔╝██║  ██║██║██████╔╝╚██████╔╝███████╗
    ╚═════╝ ╚═╝ ╚═════╝ ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝ ╚══════╝
    """)
    print("=" * 75)
    print("=" * 75)
    print()

    print("=" * 78)

    print(f" Application : {APP_NAME}")
    print(f" Version     : {VERSION}")
    print(f" Author      : {AUTHOR}")
    print(f" Date        : {datetime.now().strftime('%d-%m-%Y')}")
    print(f" Time        : {datetime.now().strftime('%H:%M:%S')}")
    print(f" {COPYRIGHT}")

    print("=" * 78)
    print()