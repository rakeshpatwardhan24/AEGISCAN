
# AEGISCAN — Week 4 CAN Fundamentals Learning Note

## 1. Introduction

Controller Area Network (CAN) is a communication protocol that allows
electronic control units (ECUs) to exchange information over a shared
communication bus. It is widely used in automotive and embedded systems.

## 2. CAN Bus, Controller, and Transceiver

- CAN bus: The shared communication network connecting CAN nodes.
- CAN controller: Handles CAN protocol operations, including frame
  formatting, arbitration, and error handling.
- CAN transceiver: Converts logic-level signals into electrical signals
  suitable for the physical CAN bus and converts received signals back.
- CAN node: A device connected to the CAN network.

## 3. CAN Arbitration

When multiple nodes begin transmitting together, CAN arbitration determines
which message continues based on the transmitted identifier. For standard
CAN identifiers, a lower numerical identifier generally has higher priority
when comparing identifiers in the same arbitration context.

## 4. CAN Identifier, DLC, Frame, and Payload

- CAN ID: Identifies a message and helps determine its priority.
- Frame: The complete protocol unit transmitted over the CAN bus.
- Payload: The data bytes carried in a data frame.
- DLC: Data Length Code, which indicates the payload length according
  to the CAN frame format.
- Classic CAN: Supports up to 8 payload bytes.
- CAN FD: Supports payloads of up to 64 bytes and can use a faster
  data phase when supported by the network.

## 5. Message Frequency

Message frequency describes how often a CAN message is transmitted.
For example, a 10 Hz message is transmitted 10 times per second, or
once every 100 milliseconds.

The current AEGISCAN generator creates a single simulated payload.
Periodic transmission has not yet been implemented.

## 6. DBC Concept

A DBC file describes CAN messages and their signals, including identifiers,
signal positions, lengths, byte order, scaling, offsets, and units.

AEGISCAN currently uses Markdown documents to record its message map and
signal definitions. It does not yet generate or use an actual DBC file.

## 7. AEGISCAN CAN Message Example

The project defines an educational message named BMS_Status:

- CAN ID: 0x100
- Identifier format: Standard 11-bit
- DLC: 8 bytes
- Voltage: 16-bit unsigned, scale 0.1 V per bit
- Current: 16-bit signed, scale 0.1 A per bit
- SOC: 8-bit unsigned, scale 1% per bit
- Temperature: 16-bit signed, scale 0.1 °C per bit
- Reserved byte: 1 byte

Example payload:

`01 DB 00 32 5F 01 22 00`

These are project-defined example signals, not an official vehicle CAN
database or a validated vehicle communication specification.

## 8. Limitations and Future Work

The current program encodes and decodes CAN-style payload bytes in software.
It does not transmit actual CAN frames or model physical arbitration.

Future work may include periodic message generation, DBC file creation,
CAN FD concepts, and integration with a CAN interface in a controlled lab.

## 9. Conclusion

This week introduces CAN communication concepts and demonstrates how
simulated BMS readings can be encoded into a defined 8-byte payload.
This forms a foundation for later AEGISCAN work on CAN monitoring
and cybersecurity.
