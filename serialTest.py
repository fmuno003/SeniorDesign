import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600)
start_time = time.time()
imu = open("IMU.txt","w")

while time.time() - start_time <= 1:
    ser.readline()

while time.time() - start_time <= 8:
    read_ser=ser.readline()
    if float(read_ser) == 0.00:
        pass
    else:
        read = read_ser.strip('\n')
        imu.write(read)
        imu.write('\n')

imu.close()
