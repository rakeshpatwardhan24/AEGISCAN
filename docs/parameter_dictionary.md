# AEGISCAN — Battery Parameter Dictionary

## 1. Purpose

This document defines the battery parameters used in the Week 2 simulator. The generated readings are illustrative software data, not measurements from a physical battery.

## 2. Parameters

| Parameter | Description | Unit | Value or behavior |
|---|---|---|---|
| Battery capacity | Nominal capacity configured for the simulation | Ah | 50 Ah |
| Voltage | Simulated electrical potential difference | V | Calculated by the model |
| Current | Simulated current drawn by the load | A | 5 A, 8 A or 6 A |
| SOC | State of Charge: remaining charge percentage | % | Starts at 100% |
| Temperature | Illustrative simulated battery temperature | °C | Starts at 28°C |
| Time | Elapsed simulation time | minutes | 0–30 minutes |

## 3. Dataset Columns

The file `data/battery_data.csv` contains:

- `time_min`: Elapsed time in minutes.
- `voltage_V`: Simulated voltage in volts.
- `current_A`: Simulated current in amperes.
- `SOC_percent`: Simulated State of Charge.
- `temperature_C`: Simulated temperature in degrees Celsius.

## 4. Model Limitations

The simulator uses simplified equations to demonstrate battery parameter trends. It does not accurately model electrochemical behavior, internal resistance, real thermal dynamics, State of Health (SOH), or State of Power (SOP). Its output must not be used for real battery operation or safety decisions.

## 5. Future Scope

Future versions may incorporate validated battery models, additional battery parameters, anomaly detection, and integration with AEGISCAN's broader monitoring architecture.