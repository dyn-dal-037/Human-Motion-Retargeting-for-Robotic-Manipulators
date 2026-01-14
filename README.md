# Human Motion Retargeting for Robotic Manipulators

This repository implements an end-to-end **vision-based human arm motion retargeting system** that maps human motion captured using a Kinect Xbox 360 sensor to a physical 3-DOF robotic manipulator controlled by an ESP32 over WiFi.

The project demonstrates a complete **perception → representation → retargeting → embedded control** pipeline running on real hardware.

---

## Overview

Human arm motion is captured using Kinect skeletal tracking. From the tracked joint positions, joint angles for the shoulder, elbow, and wrist are computed and stored as time-series trajectories. These trajectories are then retargeted to a robotic arm by mapping human joint angles to servo-safe ranges and transmitting them to an ESP32-based controller via HTTP.

The system emphasizes **modularity, hardware safety, and reproducibility**, making it suitable for research demonstrations and further extensions in imitation learning and humanoid robotics.

---

## Photos

![Robotic Arm](assets/hardware_images/view.jpeg)
![Kinect_Used](assets/hardware_images/kinect.jpeg)
![Wiring and Servo Driver](assets/hardware_images/closeup.jpeg)
![Kinect_setup](assets/hardware_images/kinect_software_setup.jpeg)

## Demo Video

🎥 **System Demonstration**  
https://drive.google.com/drive/folders/1rJb3mp3yVHOqHLJPWuf4lFBBddkgHWPv?usp=sharing
---

## System Pipeline



                                                            Human Arm
                                                                ↓
                                                Kinect Xbox 360 (Vision-Based Sensing)
                                                                ↓
                                                  Joint Angle Computation (Python)
                                                                ↓
                                                    CSV Trajectory Representation
                                                                ↓
                                                   Motion Retargeting + Smoothing
                                                                ↓
                                                    WiFi Transmission (HTTP)
                                                                ↓
                                                        ESP32 WebServer
                                                                ↓
                                                       Serial Bus Servos
                                                                ↓
                                                   3-DOF Robotic Manipulator

---

## Hardware Setup

- **Kinect Xbox 360** for skeletal tracking  
- **Windows PC** for motion capture and retargeting  
- **ESP32** running a WiFi web server  
- **Waveshare General Motor Driver for Robots**  
- **3 High-Torque Serial Bus Servos** configured as a 3-DOF arm  

Servo-to-joint mapping:
- Servo 1 → Shoulder  
- Servo 2 → Elbow  
- Servo 3 → Wrist (proxy angle)

Servo limits and rate constraints are enforced at both the Python and ESP32 levels for safety.

---

## Kinect Setup

### Requirements
- OS: Windows 10 / 11  
- Python: 3.7 – 3.9 (recommended)  
- Kinect Xbox 360 with power adapter  
- Microsoft Kinect SDK installed  

### Install Python Dependencies

```bash
pip install -r kinect/requirements.txt
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

## Output CSV Format

```bash
Timestamp,Shoulder_Angle,Elbow_Angle,Wrist_Angle
```

## Motion Retargeting and Control

Recorded joint angles are mapped to servo-safe ranges and sent to the ESP32 via HTTP.

Smoothed Retargeting (Recommended):
```bash
python retargeting/kinect_csv_to_esp32_wifi_smoothed.py
```

## ESP32 Control Interface

The ESP32 hosts an HTTP endpoint::
```bash
POST /sendData
Payload: angle1,angle2,angle3
```

## Utility Scripts
```bash
scripts/csv_visualizer.py
```
Visualizes recorded joint angle trajectories.
```bash
scripts/test_payload_sender.py
```
Sends test angle commands to the ESP32 without using Kinect.

## Results

The system successfully demonstrates:

   - Vision-based human arm motion capture

   - Joint angle extraction and logging

   - Safe and smooth retargeting

   - Real-time robotic execution over WiFi

A demo video link is provided in docs/demo_video_link.md.

## Limitations and Future Work
- Wrist angle is approximated due to Kinect sensing constraints.

- Current pipeline uses recorded CSV trajectories.

- Future extensions include:

    - Live Kinect-to-robot streaming

    - ROS/ROS2 integration

    - Learning-based retargeting and imitation learning
