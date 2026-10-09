
import pandas as pd
import matplotlib.pyplot as plt

# AEGISCAN - Week 2: Battery Fundamentals Simulator

# Initial battery parameters
battery_capacity_ah = 50.0
soc = 100.0
temperature = 28.0

# Simulation settings
time_step_minutes = 1
total_minutes = 30

# Store simulated readings
readings = []

for minute in range(total_minutes + 1):

    # Simulated current drawn by the load (amperes)
    if minute < 10:
        current = 5.0
    elif minute < 20:
        current = 8.0
    else:
        current = 6.0

    # Simple illustrative voltage model
    voltage = 48.0 - (100.0 - soc) * 0.08 - current * 0.05

    # Record readings
    readings.append({
        "time_min": minute,
        "voltage_V": round(voltage, 2),
        "current_A": current,
        "SOC_percent": round(soc, 2),
        "temperature_C": round(temperature, 2)
    })

    # Update SOC for the next time step
    soc = max(
        0.0,
        soc - (current * time_step_minutes / 60)
        / battery_capacity_ah * 100
    )

    # Simple illustrative temperature change
    temperature += (current / 100) * time_step_minutes

# Create a DataFrame and save the dataset
df = pd.DataFrame(readings)
df.to_csv("data/battery_data.csv", index=False)

# Plot the simulated battery readings
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

plots = [
    ("voltage_V", "Voltage (V)"),
    ("current_A", "Current (A)"),
    ("SOC_percent", "State of Charge (%)"),
    ("temperature_C", "Temperature (°C)")
]

for ax, (column, label) in zip(axes.flat, plots):
    ax.plot(df["time_min"], df[column])
    ax.set_title(label)
    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel(label)
    ax.grid(True)

plt.tight_layout()
plt.savefig("data/battery_plots.png", dpi=150)
plt.show()

print("Battery simulation completed successfully!")
print("Dataset saved to data/battery_data.csv")
print("Plots saved to data/battery_plots.png")
print(df.head())
