# AEGISCAN — Battery Fundamentals Note

## 1. Introduction

Batteries are essential components of electric vehicles (EVs), battery energy storage systems, and many aerospace and unmanned aerial vehicle (UAV) applications. A battery stores chemical energy and converts it into electrical energy when required.

The Battery Management System (BMS) monitors important battery parameters and helps maintain operation within specified limits.

## 2. Cell, Module and Pack

- **Cell:** The basic electrochemical unit of a battery.
- **Module:** A group of connected cells assembled into a unit.
- **Pack:** A complete battery assembly containing cells or modules and supporting components such as monitoring electronics, wiring, cooling and protection systems.

Cells connected in series increase pack voltage. Parallel connections increase available capacity and current capability, depending on the cell and pack design.

## 3. Important Electrical Parameters

### Voltage

Voltage is the electrical potential difference between two points. Battery voltage changes with charge level, current, temperature and cell characteristics.

### Current

Current is the rate of electric charge flow, measured in amperes (A). During discharge, the battery supplies current to the load.

### Capacity

Battery capacity is commonly expressed in ampere-hours (Ah). It describes the amount of charge a battery can deliver under specified test conditions.

### Energy

Energy is commonly expressed in watt-hours (Wh) or kilowatt-hours (kWh). A useful approximation is:

Energy (Wh) = Voltage (V) × Capacity (Ah)

This is an estimate when using nominal voltage and rated capacity.

## 4. Battery State Parameters

### State of Charge (SOC)

SOC indicates the estimated remaining charge as a percentage. An SOC of 100% represents a fully charged battery under the relevant estimation convention; 0% represents the defined empty limit.

### State of Health (SOH)

SOH describes the battery's condition relative to its original or reference condition. Capacity loss and increased internal resistance can indicate degradation. Exact SOH definitions depend on the estimation method.

### State of Power (SOP)

SOP estimates the power that a battery can safely deliver or accept under current operating conditions. It depends on factors such as SOC, temperature, voltage limits and battery condition.

## 5. Charging and Discharging

During charging, electrical energy is stored chemically and SOC generally increases. During discharging, the battery supplies electrical energy to a load and SOC generally decreases.

Current, temperature, voltage limits and battery chemistry affect safe operating conditions.

## 6. Battery Safety

Important battery safety considerations include:

- Avoid overcharging and excessive discharge.
- Monitor voltage, current and temperature.
- Prevent short circuits.
- Use appropriate protection and thermal management.
- Follow manufacturer specifications and applicable safety procedures.

The software simulator developed for this project does not provide physical battery protection.

## 7. Week 2 Simulator

The AEGISCAN Week 2 simulator generates illustrative battery readings over a 30-minute period. It models voltage, current, SOC and temperature using simplified equations.

The program saves its output to:

- `data/battery_data.csv`
- `data/battery_plots.png`

The plots demonstrate how the simulated parameters change with time. They are intended for learning and visualization, not for predicting the behavior or safety of a real EV battery.

## 8. Relevance to AEGISCAN

Understanding battery parameters provides a foundation for monitoring battery-related signals in EV and Battery Management System applications.

In future stages, AEGISCAN may explore identifying unusual signal patterns and detecting anomalies in simulated or recorded data. Such detection will require separate implementation and testing.

## 9. Conclusion

This week's work introduces battery fundamentals and demonstrates a basic Python simulator that generates a sample dataset and plots. The work establishes a foundation for future battery monitoring and cybersecurity experiments within AEGISCAN.