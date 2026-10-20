
# AEGISCAN — BMS Fault State Definitions

## 1. Purpose

This document defines the operating states used by the simplified
Battery Management System (BMS) model developed for Week 3 of AEGISCAN.

The model checks simulated battery voltage, current, state of charge
(SOC), and temperature against example limits.

These definitions are for educational simulation only. They are not
validated battery protection thresholds and must not be used to control
real battery hardware.

## 2. Defined States

### NORMAL

**Description:** All monitored parameters remain within the example
limits configured in the software.

**Expected behavior:**
- Report the battery status as NORMAL.
- Return an empty list of detected faults.

### FAULT

**Description:** At least one monitored parameter exceeds an example
limit configured in the software.

**Expected behavior:**
- Report the battery status as FAULT.
- Identify the detected fault in the output.
- Allow the fault information to be recorded or displayed.

## 3. Fault Conditions

| Fault | Example detection condition | Meaning |
|---|---|---|
| OVERVOLTAGE | Voltage > 54.0 V | Voltage exceeds the configured upper limit |
| UNDERVOLTAGE | Voltage < 40.0 V | Voltage falls below the configured lower limit |
| OVERCURRENT | Current > 10.0 A | Discharge current exceeds the configured limit |
| EXCESSIVE_CHARGING_CURRENT | Current < -10.0 A | Negative current exceeds the example charging-current limit |
| SOC_TOO_HIGH | SOC > 100% | SOC is above the valid percentage range |
| SOC_TOO_LOW | SOC < 10% | SOC is below the configured example limit |
| OVERTEMPERATURE | Temperature > 45.0 °C | Temperature exceeds the configured upper limit |

Note: The current-sign convention assumes positive current represents
discharging and negative current represents charging.

## 4. Demonstration Scenarios

### Scenario A — Normal Operation

Input:
- Voltage: 47.5 V
- Current: 5.0 A
- SOC: 95%
- Temperature: 29 °C

Expected result:
- Status: NORMAL
- Faults: None

### Scenario B — Simulated Overtemperature

Input:
- Voltage: 47.0 V
- Current: 6.0 A
- SOC: 90%
- Temperature: 50 °C

Expected result:
- Status: FAULT
- Fault: OVERTEMPERATURE

## 5. Limitations

- The model uses simulated input values.
- The example thresholds are not validated for a real battery chemistry.
- The model does not control physical contactors or perform hardware protection.
- The model does not implement complete SOC, SOH, or SOP estimation.
- The model does not detect CAN attacks or implement a complete cybersecurity system.

## 6. Future Improvements

- Add cell-level voltage monitoring.
- Include configurable thresholds and sensor-error checks.
- Record faults with timestamps.
- Add fault severity and recovery-state handling.
- Integrate validated battery models and, later, CAN data monitoring.
