import csv
import time
import requests

from angle_mapping_utils import map_human_to_servo

ESP32_IP = "http://192.168.8.214"
ENDPOINT = "/sendData"

CSV_FILE = "arm_joint_angles.csv"
SEND_INTERVAL = 0.25  # seconds

print("[INFO] Starting Kinect → ESP32 WiFi retargeting (no smoothing)")

with open(CSV_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            shoulder = float(row["Shoulder_Angle"])
            elbow = float(row["Elbow_Angle"])
            wrist = float(row["Wrist_Angle"])

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
