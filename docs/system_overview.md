# System Overview

This project implements an end-to-end **human motion retargeting pipeline** that maps human arm motion captured using a Kinect Xbox 360 sensor to a 3-DOF robotic manipulator controlled by an ESP32 over WiFi.

The system demonstrates a complete **perception-to-action loop**, starting from vision-based sensing and ending in real-world robotic execution.

---

## High-Level Pipeline

Human arm motion is captured as 3D joint positions using Kinect. From these positions, joint angles are computed and recorded. The recorded angles are then retargeted to a robotic manipulator by mapping human joint angles to servo-safe ranges and transmitting them to an ESP32-based controller.



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

## Key Design Principles

- **Modularity**: Perception, retargeting, and control are cleanly separated.
- **Hardware Safety**: Angle limits enforced at both software and embedded levels.
- **Reproducibility**: Motion trajectories are stored as CSV files.
- **Simplicity**: Deterministic algorithms preferred over complex models.

---

## Scope of the Project

- Focuses on **arm motion imitation** (shoulder, elbow, wrist).
- Demonstrates feasibility of vision-based imitation on real hardware.
- Designed as a foundation for future work in imitation learning and humanoid robotics.
