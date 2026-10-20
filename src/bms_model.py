
def check_bms_status(voltage, current, soc, temperature):
    """
    Simplified educational BMS monitoring model.
    Checks simulated battery readings against example limits.
    These limits are illustrative, not validated for real batteries.
    """

    faults = []

    if voltage > 54.0:
        faults.append("OVERVOLTAGE")
    elif voltage < 40.0:
        faults.append("UNDERVOLTAGE")

    if current > 10.0:
        faults.append("OVERCURRENT")
    elif current < -10.0:
        faults.append("EXCESSIVE_CHARGING_CURRENT")

    if soc > 100.0:
        faults.append("SOC_TOO_HIGH")
    elif soc < 10.0:
        faults.append("SOC_TOO_LOW")

    if temperature > 45.0:
        faults.append("OVERTEMPERATURE")

    if faults:
        status = "FAULT"
    else:
        status = "NORMAL"

    return {
        "status": status,
        "faults": faults
    }


if __name__ == "__main__":
    # Example 1: Normal battery readings
    normal = check_bms_status(
        voltage=47.5,
        current=5.0,
        soc=95.0,
        temperature=29.0
    )

    print("NORMAL OPERATION")
    print(normal)

    # Example 2: Simulated overtemperature fault
    fault = check_bms_status(
        voltage=47.0,
        current=6.0,
        soc=90.0,
        temperature=50.0
    )

    print("\nSIMULATED BATTERY FAULT")
    print(fault)
