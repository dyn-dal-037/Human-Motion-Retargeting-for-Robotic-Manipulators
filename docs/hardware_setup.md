# Hardware Setup

This document describes the hardware components and physical setup used in the project.

---

## Components Used

### 1. Motion Capture
- **Kinect Xbox 360 Sensor**
- Used for real-time skeletal tracking and joint position estimation.
- Connected to a Windows PC via USB and power adapter.

### 2. Processing Unit
- **Laptop / PC (Windows)**
- Runs Python scripts for:
  - Kinect data acquisition
  - Joint angle computation
  - Motion retargeting
  - WiFi communication

### 3. Robot Controller
- **ESP32 Development Board**
- Hosts a lightweight HTTP web server.
- Receives joint angle commands over WiFi.

### 4. Actuation
- **3 × High-Torque Serial Bus Servos**
- Driven using a **Waveshare General Motor Driver for Robots**.
- Configured as a 3-DOF manipulator (shoulder–elbow–wrist).

---

## Physical Assembly

- The servos are mechanically connected to form a serial kinematic chain.
- Each servo corresponds to one human arm joint:
  - Servo 1 → Shoulder
  - Servo 2 → Elbow
  - Servo 3 → Wrist (proxy)
- Power supply for servos is isolated from ESP32 logic power.

---

## Safety Considerations

- Servo angle limits are enforced in both Python and ESP32 code.
- Motion commands are rate-limited to avoid sudden movements.
- Initial testing is performed using static test payloads.

---

## Notes

This hardware configuration was chosen to balance **simplicity, robustness, and reproducibility**, making it suitable for rapid experimentation and demonstration.
