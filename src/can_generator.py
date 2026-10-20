
"""
AEGISCAN Week 4: Simulated CAN message generator.

This educational program encodes simulated BMS readings into
classic CAN-style identifiers and 8-byte payloads.
It does not transmit messages onto physical CAN hardware.
"""

def encode_bms_values(voltage_v, current_a, soc_percent, temperature_c):
    """Encode four BMS signals into an 8-byte payload.

    Scaling:
    voltage:     0.1 V per bit
    current:     0.1 A per bit, signed
    SOC:         1% per bit
    temperature: 0.1 °C per bit, signed

    Layout:
    bytes 0-1: voltage, unsigned, big-endian
    bytes 2-3: current, signed, big-endian
    byte 4:    SOC
    bytes 5-6: temperature, signed, big-endian
    byte 7:    reserved, zero
    """

    if not 0 <= soc_percent <= 100:
        raise ValueError("SOC must be between 0 and 100 percent.")

    voltage_raw = round(voltage_v * 10)
    current_raw = round(current_a * 10)
    soc_raw = round(soc_percent)
    temperature_raw = round(temperature_c * 10)

    if not 0 <= voltage_raw <= 65535:
        raise ValueError("Voltage is outside the encoding range.")
    if not -32768 <= current_raw <= 32767:
        raise ValueError("Current is outside the encoding range.")
    if not -32768 <= temperature_raw <= 32767:
        raise ValueError("Temperature is outside the encoding range.")

    payload = bytearray(8)

    payload[0:2] = voltage_raw.to_bytes(2, "big", signed=False)
    payload[2:4] = current_raw.to_bytes(2, "big", signed=True)
    payload[4] = soc_raw
    payload[5:7] = temperature_raw.to_bytes(2, "big", signed=True)
    payload[7] = 0

    return bytes(payload)


def decode_bms_values(payload):
    """Decode an 8-byte payload back into readable BMS values."""

    if len(payload) != 8:
        raise ValueError("Classic CAN payload must contain 8 bytes.")

    voltage_raw = int.from_bytes(payload[0:2], "big", signed=False)
    current_raw = int.from_bytes(payload[2:4], "big", signed=True)
    soc_raw = payload[4]
    temperature_raw = int.from_bytes(payload[5:7], "big", signed=True)

    return {
        "voltage_V": voltage_raw / 10,
        "current_A": current_raw / 10,
        "SOC_percent": soc_raw,
        "temperature_C": temperature_raw / 10,
    }


def main():
    can_id = 0x100

    # Example values from a simulated BMS.
    readings = {
        "voltage_v": 47.5,
        "current_a": 5.0,
        "soc_percent": 95,
        "temperature_c": 29.0,
    }

    payload = encode_bms_values(**readings)

    print("AEGISCAN - CAN MESSAGE GENERATOR")
    print(f"CAN ID: 0x{can_id:03X}")
    print("DLC: 8 bytes")
    print("Payload:", " ".join(f"{byte:02X}" for byte in payload))

    print("\nDecoded BMS values:")
    for name, value in decode_bms_values(payload).items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()
