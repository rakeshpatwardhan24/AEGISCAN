
# AEGISCAN — CAN Signal and Scaling Definitions

## 1. Purpose

This document defines the encoding, byte positions, scaling,
units, and data ranges of the signals in the simulated BMS_Status
classic CAN message.

## 2. Message Information

- Message name: BMS_Status
- CAN identifier: 0x100
- Identifier format: Standard 11-bit CAN identifier
- Payload length: 8 bytes
- Byte order for multi-byte signals: Big-endian

## 3. Signal Definitions

| Signal | Start byte | Length | Signed? | Factor | Offset | Unit |
|---|---:|---:|---|---:|---:|---|
| Battery voltage | 0 | 16 bits | No | 0.1 | 0 | V |
| Battery current | 2 | 16 bits | Yes | 0.1 | 0 | A |
| SOC | 4 | 8 bits | No | 1 | 0 | % |
| Battery temperature | 5 | 16 bits | Yes | 0.1 | 0 | °C |
| Reserved | 7 | 8 bits | No | Not applicable | 0 | None |

## 4. Conversion Formula

For signals with a scale factor:

Physical value = Raw value × Factor + Offset

To encode a physical value:

Raw value = round((Physical value - Offset) / Factor)

For example, a voltage of 47.5 V becomes a raw integer of 475.
The raw value 475 is hexadecimal 0x01DB, so it occupies bytes 0x01
and 0xDB in big-endian order.

A temperature of 29.0 °C becomes a raw integer of 290, represented
as 0x0122 in big-endian order.

## 5. Example Payload

For these values:

- Voltage: 47.5 V
- Current: 5.0 A
- SOC: 95%
- Temperature: 29.0 °C

The payload is:

`01 DB 00 32 5F 01 22 00`

## 6. Validation Rules

- SOC must be between 0% and 100%.
- Voltage must fit in the unsigned 16-bit encoded range.
- Current and temperature must fit in signed 16-bit encoded ranges.
- Multi-byte values use big-endian byte order.
- The payload must contain exactly 8 bytes.

## 7. Limitations

These signal definitions are educational, project-specific choices.
They are not an official automotive CAN database and have not been
validated for use in a real vehicle.
