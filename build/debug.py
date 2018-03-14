import RPi.GPIO as GPIO
from random import*
import motorSelfTest
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
        return a

def motorTesting():
    motorSelfTest.Forward(1,100,75)
    motorSelfTest.Stop(0.1)
    motorSelfTest.Backward(1,100,75)
    motorSelfTest.Stop(0.1)
    motorSelfTest.RightTurn(1.5)
    motorSelfTest.Stop(0.1)
    motorSelfTest.LeftTurn(1.5)
    motorSelfTest.Stop(0.1)

def GPSdata():
    ser = serial.Serial("/dev/ttyUSB0", 4800, timeout=1)
    if  not(ser.isOpen()):
        ser.open()
    start_time = time.time()
    while(time.time() - start_time < 1.5 ):
        data = ser.readline()
        x = data.split(',')
        if x[0] == "$GPRMC":
            location = pynmea2.parse(data)
    ser.close()
    return location.latitude, location.longitude

#latit, longi = GPSdata()
#ORIGIN_LATITUDE = latit # Global constants for the origin
#ORIGIN_LONGITUDE = longi # Will not change and comparison using turret function

def TurretRotation(lat, lon):
    x = lat - ORIGIN_LATITUDE
    y = lon - ORIGIN_LONGITUDE
    angle = math.degrees(math.atan2(y,x)) + 270
    txtfile = open("/home/pi/Desktop/build/Platform/angles.txt","w")
    txtfile.write(str(angle))
    txtfile.close()
    # write to text file for platform rotation 

def distanceFormula(moveLatitude, moveLongitude, latitude, longitude):
    latDis = ((moveLatitude - latitude)**2) * LATITUDE_CONST
    longDis = ((longitude - moveLongitude)**2) * LONGITUDE_CONST
    distance = math.sqrt(latDis + longDis)
    return distance #returns distance in meters

def stripString(string):
    tempData = string.strip(',')
    latitude = float(tempData[0])
    longitude = float(tempData[1])
    return latitude, longitude

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

#Parameter: Flag
def Turning(flag, Offset, a):
    CurrentAngle = IMU(Offset)
    calcAngle = CurrentAngle + a
    if flag == 1:
        while IMU(Offset) < calcAngle:
            print(IMU(Offset))
            motorSelfTest.RightTurn(1.5)
    elif flag == 2:
        while IMU(Offset) > calcAngle:
            print(IMU(Offset))
            motorSelfTest.LeftTurn(1.5)
    motorSelfTest.Stop(0.25)
    
#Parameter: Flag
def returnTurn(flag, Offset):
    if flag == 1:
        while (IMU(Offset) > 0) or (IMU(Offset) < 360):
            motorSelfTest.LeftTurn(1.5)
    elif flag == 2:
        while (IMU(Offset) > 0) or (IMU(Offset) < 360):
            motorSelfTest.RightTurn(1.5)
    motorSelfTest.Stop(0.25)

