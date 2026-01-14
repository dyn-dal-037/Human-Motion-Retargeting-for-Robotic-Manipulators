# Kinect Setup

This document explains how to set up the Kinect Xbox 360 sensor and required software to run the motion capture component.

---

## System Requirements

- Operating System: **Windows 10 / 11**
- Python Version: **3.7 – 3.9** (recommended)
- Kinect Sensor: **Xbox 360 Kinect**

---

## Software Dependencies

1. **Microsoft Kinect SDK**
   - Required for Kinect drivers and skeletal tracking support.
   - Must be installed before running Python scripts.

2. **Python Libraries**
   - pykinect2
   - numpy

Install Python dependencies using:

```bash
pip install -r requirements.txt

```

## Sensor Setup

1. **Connect the Kinect sensor to:**
    - USB port
    - External power adapter
2. **Verify sensor functionality using Kinect SDK tools.**
3. **Ensure the sensor has a clear view of the upper body.**

## Running the Kinect Logger

From the kinect/ directory:
```bash
python live_kinect_arm_angle_logger.py
```

This will:

   - Track the right arm
   -  Compute shoulder, elbow, and wrist angles
   -  Save the data to a timestamped CSV file