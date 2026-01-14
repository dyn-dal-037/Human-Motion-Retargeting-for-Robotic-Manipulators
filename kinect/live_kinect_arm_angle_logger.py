import csv
import math
import datetime
from pykinect2 import PyKinectV2, PyKinectRuntime

def get_angle(p1, p2, p3):
    try:
        a = [p1.x - p2.x, p1.y - p2.y, p1.z - p2.z]
        b = [p3.x - p2.x, p3.y - p2.y, p3.z - p2.z]
        dot = sum(a[i] * b[i] for i in range(3))
        na = math.sqrt(sum(a[i] ** 2 for i in range(3)))
        nb = math.sqrt(sum(b[i] ** 2 for i in range(3)))
        return math.degrees(math.acos(dot / (na * nb)))
    except:
        return 0.0

# Initialize Kinect Camera
kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Body)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
csv_filename = f"arm_joint_angles_{timestamp}.csv"

csv_file = open(csv_filename, "w", newline="")
writer = csv.writer(csv_file)

writer.writerow([
    "Timestamp",
    "Shoulder_Angle",
    "Elbow_Angle",
    "Wrist_Angle"
])

print(f"[INFO] Recording arm joint angles → {csv_filename}")
print("[INFO] Tracking RIGHT ARM. Press Ctrl+C to stop.")

try:
    while True:
        if kinect.has_new_body_frame():
            bodies = kinect.get_last_body_frame()
            if bodies is None:
                continue

            for body in bodies.bodies:
                if not body.is_tracked:
                    continue

                j = body.joints

                spine = j[PyKinectV2.JointType_SpineShoulder].Position
                shoulder = j[PyKinectV2.JointType_ShoulderRight].Position
                elbow = j[PyKinectV2.JointType_ElbowRight].Position
                wrist = j[PyKinectV2.JointType_WristRight].Position
                hand = j[PyKinectV2.JointType_HandRight].Position

                shoulder_angle = get_angle(spine, shoulder, elbow)
                elbow_angle = get_angle(shoulder, elbow, wrist)
                wrist_angle = get_angle(elbow, wrist, hand)

                ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                writer.writerow([
                    ts,
                    round(shoulder_angle, 2),
                    round(elbow_angle, 2),
                    round(wrist_angle, 2)
                ])

except KeyboardInterrupt:
    print("\n[INFO] Stopped by user.")

finally:
    csv_file.close()
    kinect.close()
    print("[INFO] CSV file saved successfully.")
