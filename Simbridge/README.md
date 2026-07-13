# 🌉 DigiBridge – AI-Based Bridge Digital Twin

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Arduino](https://img.shields.io/badge/Arduino-Uno-green)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## Overview

**DigiBridge** is an AI-powered Bridge Digital Twin that combines real-time sensor measurements, structural simulation, and machine learning to estimate the probability of bridge failure.

The system receives live data from an Arduino-based hardware model, generates realistic environmental parameters, updates a virtual bridge model, and predicts structural risk using a trained Random Forest model.

The project demonstrates the integration of:

* Structural Engineering
* Artificial Intelligence
* Internet of Things (IoT)
* Digital Twin Technology
* Embedded Systems

---

# Features

* Real-time Arduino communication
* Automatic Arduino COM port detection
* Live temperature and humidity monitoring
* Live bridge load monitoring
* Bridge deterioration simulation
* Environmental parameter generation
* AI-based bridge failure prediction
* Risk level classification
* Prediction confidence estimation
* Terminal dashboard
* Modular software architecture
* Automatic dependency installation
* One-click application launcher

---

# Project Architecture

```
                   +--------------------+
                   |    Arduino Uno     |
                   +--------------------+
                              |
                              |
                    Temperature
                     Humidity
                    Vehicle Load
                              |
                              v
                   +--------------------+
                   |   Serial Reader    |
                   +--------------------+
                              |
                              v
                   +--------------------+
                   | Live Simulation    |
                   +--------------------+
                              |
                              |
            Generates Environmental Parameters
                              |
                              v
                   +--------------------+
                   |  Bridge Updater    |
                   +--------------------+
                              |
                              v
                   +--------------------+
                   | Feature Builder    |
                   +--------------------+
                              |
                              v
                   +--------------------+
                   | Random Forest AI   |
                   +--------------------+
                              |
                              v
                   Failure Probability
```

---

# Hardware Components

| Component                            | Quantity |
| ------------------------------------ | -------: |
| Arduino Uno                          |        1 |
| DHT11 Temperature & Humidity Sensor  |        1 |
| HX711 Load Cell Amplifier *(Future)* |        1 |
| Load Cell *(Future)*                 |        1 |
| Forex Sheet Bridge Model             |        1 |
| Breadboard                           |        1 |
| Jumper Wires                         |  Several |
| USB Cable                            |        1 |

---

# Software Requirements

* Python 3.12 or newer
* Arduino IDE
* Windows 10 / Windows 11

---

# Python Dependencies

The project automatically installs:

* NumPy
* Pandas
* Scikit-learn
* Joblib
* PySerial
* Matplotlib
* OpenPyXL

---

# Folder Structure

```
DigiBridge/

├── assets/
├── bridge/
├── data/
├── dataset_generator/
├── digital_twin/
├── hardware/
├── models/
├── prediction/
├── simulation/
├── tests/
├── utils/
│
├── logs/
├── exports/
├── reports/
│
├── requirements.txt
├── setup.bat
├── launch.bat
├── run_tests.py
├── live_prediction.py
├── README.md
└── test_bridge.py
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd DigiBridge
```

Run the setup wizard:

```text
setup.bat
```

The setup script will:

* Verify Python installation
* Upgrade pip
* Install all required packages
* Verify installed dependencies
* Create required folders

---

# Running the Project

Launch the application:

```text
launch.bat
```

Choose:

```
1. Launch DigiBridge
```

The application will automatically:

* Detect the Arduino
* Connect to the serial port
* Read live sensor values
* Generate environmental parameters
* Update the bridge model
* Predict bridge failure probability

---

# Arduino Connections

## DHT11

| DHT11 | Arduino Uno   |
| ----- | ------------- |
| VCC   | 5V            |
| GND   | GND           |
| DATA  | Digital Pin 7 |

---

# Live Sensor Data

Current sensors:

* Temperature
* Humidity
* Vehicle Load *(Placeholder until HX711 integration)*

Example serial output:

```
27.4,72.0,0.0
```

---

# Machine Learning Model

Algorithm:

**Random Forest Regressor**

Model Input Features:

* Total Area
* Average Area
* Average Age
* Average Corrosion
* Average Crack Width
* Average Density
* Young's Modulus
* Yield Strength
* Temperature
* Humidity
* Vehicle Load
* Pedestrian Load
* Wind Speed
* Rainfall
* River Water Level
* Earthquake Factor
* Dynamic Load Factor
* Safety Factor

Model Output:

* Failure Probability

---

# Risk Classification

| Failure Probability | Risk Level |
| ------------------: | ---------- |
|             0 – 20% | LOW        |
|            20 – 50% | MODERATE   |
|            50 – 75% | HIGH       |
|           Above 75% | CRITICAL   |

---

# Testing

Run all project tests:

```text
python run_tests.py
```

or

```
Launch.bat

↓

Run System Tests
```

---

# Future Improvements

* HX711 Load Cell Integration
* ESP32 Wi-Fi Connectivity
* PyQt Desktop Interface
* Live Charts
* Data Logging
* PDF Report Generation
* Crack Detection using Computer Vision
* Cloud-Based Monitoring
* MQTT Communication
* Real-Time Alert System

---

# Educational Objectives

This project demonstrates:

* Structural Health Monitoring
* Bridge Digital Twin Technology
* Machine Learning in Civil Engineering
* Embedded Systems Programming
* Object-Oriented Python
* Arduino–Python Serial Communication
* Predictive Maintenance
* Software Architecture Design



# License

This project is intended for educational and research purposes.
