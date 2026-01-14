import csv
import time
import requests
from collections import deque

from angle_mapping_utils import map_human_to_servo

# ================= CONFIG =================

ESP32_IP = "http://192.168.8.214"
ENDPOINT = "/sendData"

CSV_FILE = "arm_joint_angles.csv"
SEND_INTERVAL = 0.25  # seconds

SMOOTHING_WINDOW = 5  # moving average window size

shoulder_buf = deque(maxlen=SMOOTHING_WINDOW)
elbow_buf = deque(maxlen=SMOOTHING_WINDOW)
wrist_buf = deque(maxlen=SMOOTHING_WINDOW)

print("[INFO] Starting Kinect → ESP32 WiFi retargeting (smoothed)")

with open(CSV_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            shoulder_buf.append(float(row["Shoulder_Angle"]))
            elbow_buf.append(float(row["Elbow_Angle"]))
            wrist_buf.append(float(row["Wrist_Angle"]))

            shoulder = sum(shoulder_buf) / len(shoulder_buf)
            elbow = sum(elbow_buf) / len(elbow_buf)
            wrist = sum(wrist_buf) / len(wrist_buf)

            s1 = map_human_to_servo(shoulder)
            s2 = map_human_to_servo(elbow)
            s3 = map_human_to_servo(wrist)

            payload = f"{s1},{s2},{s3}"
            print(f"[SEND] {payload}")

            response = requests.post(
                ESP32_IP + ENDPOINT,
                data=payload,
                timeout=3
            )

            if response.status_code != 200:
                print("[WARN] ESP32 returned non-200 response")

            time.sleep(SEND_INTERVAL)

        except Exception as e:
            print("[ERROR]", e)
            continue

print("[INFO] Streaming finished")
