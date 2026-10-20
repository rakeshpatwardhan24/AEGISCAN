
# AEGISCAN — CAN Message Map

## 1. Purpose

This document describes the simulated classic CAN message used to
represent selected Battery Management System (BMS) parameters.

The generator creates an 8-byte payload with the standard 11-bit
CAN identifier 0x100. This is a software simulation and does not
transmit messages on physical CAN hardware.

## 2. Message Definition

| Property | Definition |
|---|---|
| Message name | BMS_Status |
| CAN identifier | 0x100 (decimal 256) |
| Identifier format | Standard 11-bit CAN ID |
| Frame type | Data frame (simulated) |
| DLC | 8 bytes |
| Payload length | 8 bytes |
| Transmission frequency | Not implemented yet |
| Intended use | Educational BMS monitoring demonstration |

## 3. Payload Layout

| Byte(s) | Signal | Data type | Scaling | Unit |
|---|---|---|---|---|
| 0–1 | Battery voltage | Unsigned 16-bit, big-endian | Raw × 0.1 | V |
| 2–3 | Battery current | Signed 16-bit, big-endian | Raw × 0.1 | A |
| 4 | State of Charge (SOC) | Unsigned 8-bit | Raw × 1 | % |
| 5–6 | Battery temperature | Signed 16-bit, big-endian | Raw × 0.1 | °C |
| 7 | Reserved | Unsigned 8-bit | Not applicable | None |

## 4. Example

Input BMS values:

- Voltage: 47.5 V
- Current: 5.0 A
- SOC: 95%
- Temperature: 29.0 °C

Expected payload:

`01 DB 00 32 5F 01 22 00`

The payload can be decoded using the same scaling rules to recover
the original values.

## 5. Limitations

- This program constructs CAN-style identifiers and payload bytes only.
- It does not transmit actual CAN frames through a CAN controller or transceiver.
- The message identifier and signal layout are project-defined examples.
- Message transmission frequency and bus arbitration are not simulated.
- This message map is not a standardized vehicle communication definition.
