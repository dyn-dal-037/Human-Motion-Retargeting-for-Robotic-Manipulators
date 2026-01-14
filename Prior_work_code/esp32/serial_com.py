import serial
import csv
import time

ser=serial.Serial('COM7',115200,timeout=1)

time.sleep(2)

file=open('angles_gradual_increase.csv','r')
csvreader=csv.reader(file)
next(csvreader)
for row in csvreader:
    angles=','.join(row)
    print(f'Sending angles:{angles}')
    ser.write(f"{angles}\n".encode('utf-8'))
    time.sleep(1)




