import csv
import requests
import time

# ESP32 IP address and endpoint
ESP32_IP = 'http://192.168.8.214'
ENDPOINT = '/sendData'

# Open the CSV file and read the angle values
with open('angles_gradual_increase.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip header if there is one
    next(csvreader)
    
    for row in csvreader:
        # Each row contains angle values for three servos
        angles = ','.join(row)
        print(f"Sending angles: {angles}")
        try:
            response = requests.post(f"{ESP32_IP}{ENDPOINT}", data=angles, timeout=10)  # Timeout set to 10 seconds
            print(f"Response: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        time.sleep(2)  # Wait before sending the next set of angles
