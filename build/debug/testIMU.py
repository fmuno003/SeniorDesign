import RPi.GPIO as GPIO
from random import*
import time
import serial
import pynmea2
import math
import os

GPIO.setwarnings(False)
mode = GPIO.getmode()

LATITUDE_CONST = 0.0000063265 # Latitude distance for 1 meter
LONGITUDE_CONST = 0.000010488 # Longitude Distance for 1 meter

motor_1_Forward = 10
motor_2_Forward = 11
motor_3_Forward = 21
motor_4_Forward = 22
motor_1_Backward = 12
motor_2_Backward = 13
motor_3_Backward = 23
motor_4_Backward = 24
EnableM1 = 8
EnableM2 = 15
EnableM3 = 19
EnableM4 = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_1_Forward, GPIO.OUT)
GPIO.setup(motor_2_Forward, GPIO.OUT)
GPIO.setup(motor_3_Forward, GPIO.OUT)
GPIO.setup(motor_4_Forward, GPIO.OUT)
GPIO.setup(motor_1_Backward, GPIO.OUT)
GPIO.setup(motor_2_Backward, GPIO.OUT)
GPIO.setup(motor_3_Backward, GPIO.OUT)
GPIO.setup(motor_4_Backward, GPIO.OUT)
GPIO.setup(EnableM1, GPIO.OUT)
GPIO.setup(EnableM2, GPIO.OUT)
GPIO.setup(EnableM3, GPIO.OUT)
GPIO.setup(EnableM4, GPIO.OUT)

def TurnAngles():
    turning = open("/home/pi/Desktop/angles.txt","r")
    a = []
    data = turning.readline()
    while data != "":
        a.append(float(data))
        data = turning.readline()
        print(a)

# Sets inital for IMU
def CalibrateIMU():
    os.system("python /home/pi/Desktop/build/imu.py")
    readValue = open("/home/pi/Desktop/build/imu.txt","r")
    read_ser = readValue.readline()
    if read_ser == ' ' or read_ser == '':
        read_ser = readValue.readline()
    Offset = 0.0 - float(read_ser)
    print(Offset)
    return Offset

def IMU(Offset):
    os.system("python /home/pi/Desktop/build/imu.py")
    readValue = open("/home/pi/Desktop/build/imu.txt","r")
    IMUValue = readValue.readline()
    while IMUValue == ' ' or IMUValue == '':
        IMUValue = readValue.readline()
    IMUValue = float(IMUValue)
    IMUValue = IMUValue + Offset
    print(IMUValue)
    if IMUValue < 0.0: 
        IMUValue = IMUValue + 360.0
    elif IMUValue > 360.0:
        IMUValue = IMUValue - 360.0
    return IMUValue


a=CalibrateIMU()
print(a)

IMU(a)


