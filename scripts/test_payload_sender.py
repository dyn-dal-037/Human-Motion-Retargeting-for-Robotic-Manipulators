import time
import requests

ESP32_IP = "http://192.168.8.214"
ENDPOINT = "/sendData"

TEST_PAYLOADS = [
    "90,90,90",
    "110,90,70",
    "70,110,110",
    "90,90,90"
]

SEND_INTERVAL = 2  # in seconds

print("[INFO] Testing ESP32 payload reception...")

for payload in TEST_PAYLOADS:
    try:
        print(f"[SEND] {payload}")
        response = requests.post(
            ESP32_IP + ENDPOINT,
            data=payload,
            timeout=3
        )
        print(f"[RESP] {response.text}")
        time.sleep(SEND_INTERVAL)

    except Exception as e:
        print("[ERROR]", e)

print("[INFO] Test completed.")
