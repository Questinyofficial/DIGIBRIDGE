"""
live_prediction.py

Legacy entry point.

The launcher starts this file.
"""

from app.application import Application


def main():

    app = Application()

    app.run()


if __name__ == "__main__":
    main()