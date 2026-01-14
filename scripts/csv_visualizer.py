import csv
import matplotlib.pyplot as plt

CSV_FILE = "arm_joint_angles.csv"

timestamps = []
shoulder = []
elbow = []
wrist = []

with open(CSV_FILE, "r") as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader):
        timestamps.append(i)  # simple index-based time
        shoulder.append(float(row["Shoulder_Angle"]))
        elbow.append(float(row["Elbow_Angle"]))
        wrist.append(float(row["Wrist_Angle"]))

plt.figure(figsize=(10, 5))
plt.plot(timestamps, shoulder, label="Shoulder")
plt.plot(timestamps, elbow, label="Elbow")
plt.plot(timestamps, wrist, label="Wrist")

plt.xlabel("Frame Index")
plt.ylabel("Angle (degrees)")
plt.title("Recorded Human Arm Joint Angles (Kinect)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
