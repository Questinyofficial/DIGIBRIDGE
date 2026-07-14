"""
Bridge Digital Twin Test Runner

Author: Aarush
"""

import csv
import importlib
import inspect
import os
import sys
import time
import traceback
from datetime import datetime

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

REPORT_FOLDER = os.path.join(PROJECT_ROOT, "test_reports")
REPORT_FILE = os.path.join(REPORT_FOLDER, "test_report.csv")

os.makedirs(REPORT_FOLDER, exist_ok=True)


results = []


def write_result(module, test_name, status, runtime, message):
    results.append([
        datetime.now().strftime("%Y-%m-%d"),
        datetime.now().strftime("%H:%M:%S"),
        module,
        test_name,
        status,
        f"{runtime:.4f}",
        message
    ])


def discover_modules():

    modules = []

    for root, _, files in os.walk(PROJECT_ROOT):

        if "venv" in root.lower():
            continue

        if "__pycache__" in root:
            continue

        for file in files:

            if not file.endswith(".py"):
                continue

            if file == "runtest.py":
                continue

            path = os.path.join(root, file)

            relative = os.path.relpath(path, PROJECT_ROOT)

            module = relative[:-3].replace(os.sep, ".")

            modules.append(module)

    return sorted(modules)


def run():

    passed = 0
    failed = 0
    imported = 0

    print("=" * 70)
    print("BRIDGE DIGITAL TWIN TEST RUNNER")
    print("=" * 70)

    start_total = time.perf_counter()

    modules = discover_modules()

    print(f"\nModules Found : {len(modules)}\n")

    for module_name in modules:

        print(f"Loading {module_name}...")

        try:

            module = importlib.import_module(module_name)

            imported += 1

        except Exception:

            failed += 1

            write_result(
                module_name,
                "IMPORT",
                "FAILED",
                0,
                traceback.format_exc()
            )

            print("   IMPORT FAILED")

            continue

        functions = inspect.getmembers(module, inspect.isfunction)

        tests = [
            func for name, func in functions
            if name.startswith("test_")
        ]

        if len(tests) == 0:

            write_result(
                module_name,
                "-",
                "NO TESTS",
                0,
                ""
            )

            continue

        for func in tests:

            name = func.__name__

            print(f"   Running {name}")

            start = time.perf_counter()

            try:

                func()

                runtime = time.perf_counter() - start

                passed += 1

                write_result(
                    module_name,
                    name,
                    "PASS",
                    runtime,
                    ""
                )

                print(f"      PASS ({runtime:.4f}s)")

            except Exception:

                runtime = time.perf_counter() - start

                failed += 1

                write_result(
                    module_name,
                    name,
                    "FAIL",
                    runtime,
                    traceback.format_exc()
                )

                print(f"      FAIL ({runtime:.4f}s)")

    total_runtime = time.perf_counter() - start_total

    with open(REPORT_FILE, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Date",
            "Time",
            "Module",
            "Test",
            "Status",
            "Runtime",
            "Message"
        ])

        writer.writerows(results)

    print("\n")
    print("=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)

    print(f"Modules Imported : {imported}")
    print(f"Tests Passed     : {passed}")
    print(f"Tests Failed     : {failed}")
    print(f"Execution Time   : {total_runtime:.2f} seconds")
    print(f"CSV Report       : {REPORT_FILE}")

    print("=" * 70)


if __name__ == "__main__":
    run()