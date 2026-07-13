@echo off
title DigiBridge Setup Wizard
color 0B

echo ===============================================================
echo.
echo                DigiBridge Setup Wizard v1.0
echo.
echo        Bridge Digital Twin Installation Utility
echo.
echo ===============================================================
echo.

:: ------------------------------------------------------------
:: Check Python
:: ------------------------------------------------------------

echo [1/5] Checking Python installation...
python --version >nul 2>&1

if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed or not added to PATH.
    echo.
    echo Install Python 3.12 or newer and enable:
    echo "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

python --version

echo.
echo Python detected successfully.
echo.

:: ------------------------------------------------------------
:: Upgrade pip
:: ------------------------------------------------------------

echo [2/5] Upgrading pip...
python -m pip install --upgrade pip

echo.

:: ------------------------------------------------------------
:: Install packages
:: ------------------------------------------------------------

echo [3/5] Installing required packages...

python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Package installation failed.
    pause
    exit /b 1
)

echo.
echo All packages installed successfully.
echo.

:: ------------------------------------------------------------
:: Verify installation
:: ------------------------------------------------------------

echo [4/5] Verifying installed packages...

python -c "import numpy"
python -c "import pandas"
python -c "import sklearn"
python -c "import joblib"
python -c "import serial"
python -c "import matplotlib"

if errorlevel 1 (
    echo.
    echo Verification failed.
    pause
    exit /b 1
)

echo.
echo All dependencies verified successfully.
echo.

:: ------------------------------------------------------------
:: Create project folders
:: ------------------------------------------------------------

echo [5/5] Creating project folders...

if not exist logs mkdir logs

if not exist exports mkdir exports

if not exist reports mkdir reports

echo.

echo ===============================================================
echo.
echo              DigiBridge is ready to use.
echo.
echo Next Step:
echo     Double-click launch.bat
echo.
echo ===============================================================

pause