import csv
import math
import datetime
import pygame
from pykinect2 import PyKinectV2, PyKinectRuntime

# Calculate angle between three points
def get_angle(p1, p2, p3):
    try:
        a = [p1.x - p2.x, p1.y - p2.y, p1.z - p2.z]
        b = [p3.x - p2.x, p3.y - p2.y, p3.z - p2.z]
        dot_product = sum(a[i]*b[i] for i in range(3))
        norm_a = math.sqrt(sum(a[i]**2 for i in range(3)))
        norm_b = math.sqrt(sum(b[i]**2 for i in range(3)))
        angle_rad = math.acos(dot_product / (norm_a * norm_b))
        return math.degrees(angle_rad)
    except:
        return 0.0

# Init Kinect
kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Body)

# Output CSV
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
csv_file = open(f'joint_angles_{timestamp}.csv', mode='w', newline='')
writer = csv.writer(csv_file)

# ✅ Add Timestamp column in header
writer.writerow(["Timestamp", "Gender", "Age", "Height", "Weight", 
                 "L_Foot_Angle", "R_Foot_Angle", 
                 "L_Knee_Angle", "R_Knee_Angle", 
                 "L_Hip_Angle", "R_Hip_Angle"])

# === Enter User Info
gender = input("Enter Gender (Male/Female): ")
age = input("Enter Age: ")
height = input("Enter Height (cm): ")
weight = input("Enter Weight (kg): ")

print("Tracking started... Press Ctrl+C to stop.")

try:
    while True:
        if kinect.has_new_body_frame():
            bodies = kinect.get_last_body_frame()
            if bodies is not None:
                for i in range(0, kinect.max_body_count):
                    body = bodies.bodies[i]
                    if not body.is_tracked:
                        continue

                    joints = body.joints

                    # Extract joints
                    hip_left = joints[PyKinectV2.JointType_HipLeft].Position
                    knee_left = joints[PyKinectV2.JointType_KneeLeft].Position
                    ankle_left = joints[PyKinectV2.JointType_AnkleLeft].Position
                    foot_left = joints[PyKinectV2.JointType_FootLeft].Position

                    hip_right = joints[PyKinectV2.JointType_HipRight].Position
                    knee_right = joints[PyKinectV2.JointType_KneeRight].Position
                    ankle_right = joints[PyKinectV2.JointType_AnkleRight].Position
                    foot_right = joints[PyKinectV2.JointType_FootRight].Position

                    # Calculate angles
                    l_knee_angle = get_angle(hip_left, knee_left, ankle_left)
                    r_knee_angle = get_angle(hip_right, knee_right, ankle_right)
                    l_hip_angle = get_angle(knee_left, hip_left, joints[PyKinectV2.JointType_SpineBase].Position)
                    r_hip_angle = get_angle(knee_right, hip_right, joints[PyKinectV2.JointType_SpineBase].Position)
                    l_foot_angle = get_angle(knee_left, ankle_left, foot_left)
                    r_foot_angle = get_angle(knee_right, ankle_right, foot_right)

                    # ✅ Timestamp with date + hour:minute:second
                    row_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Write to CSV
                    writer.writerow([row_time, gender, age, height, weight,
                                     round(l_foot_angle, 2), round(r_foot_angle, 2),
                                     round(l_knee_angle, 2), round(r_knee_angle, 2),
                                     round(l_hip_angle, 2), round(r_hip_angle, 2)])
except KeyboardInterrupt:
    print("Stopped.")
finally:
    csv_file.close()
    kinect.close()
