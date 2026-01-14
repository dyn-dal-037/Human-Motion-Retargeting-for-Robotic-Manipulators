import csv
import serial
import time

# Replace 'COM3' with the appropriate serial port for your ESP32
SERIAL_PORT = 'COM7'
BAUD_RATE = 115200

# Open the serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Wait for the ESP32 to initialize
time.sleep(2)

# Open the CSV file and read the angle values
with open('/mnt/data/angles_gradual_increase.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip header if there is one
    next(csvreader)
    
    for row in csvreader:
        # Each row contains angle values for three servos
        angles = ','.join(row)
        print(f"Sending angles: {angles}")
        ser.write(f"{angles}\n".encode('utf-8'))
        time.sleep(1)  # Wait before sending the next set of angles

# Close the serial connection
ser.close()
