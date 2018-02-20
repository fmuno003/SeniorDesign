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
        if x[0] == "$GPGGA" or x[0] == "$GPRMC":
            location = pynmea2.parse(data)
    ser.close()
    return location.latitude, location.longitude

latit, longi = GPSdata()
ORIGIN_LATITUDE = latit # Global constants for the origin
ORIGIN_LONGITUDE = longi # Will not change and comparison using turret function

def TurretRotation(lat, lon):
    x = lat - ORIGIN_LATITUDE
    y = lon - ORIGIN_LONGITUDE
    angle = math.degrees(math.atan2(y,x)) + 270
    txtfile = open("home/pi/Desktop/build/Platform/angles.txt","w")
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

#inputs for Forward() and Backward() are (timeSleep,dutyCycle,freq)
f = open('/home/pi/Desktop/angles.txt','r')
g = open('/home/pi/Desktop/Coordinates.txt', 'r')
points = g.readline()
latitude, longitude = stripString(points)
flag = 0
while True:
    message = f.readline()
    points = g.readline()
    if message == '' or points == '':
        break
    currentLine = float(message)
    desLat, desLong = stripString(points)
    if currentLine > 0.0:
        motorSelfTest.RightTurn(1.5)
        flag = 1
    elif currentLine < 0.0:
        motorSelfTest.LeftTurn(1.5)
        flag = 2
    motorSelfTest.Stop(0.25)
    lat, lon = GPSdata()
    distance = distanceFormula(lat, lon, desLat, desLong)
    while (distance >= 0.05):
        motorSelfTest.Forward(1,100,100)
        lat, lon = GPSdata()
        distance = distanceFormula(lat, lon, desLat,desLong)
        print distance
    motorSelfTest.Stop(0.25)
    if flag == 1:
        pass
        motorSelfTest.LeftTurn(1.5)
    elif flag == 2:
        pass
        motorSelfTest.RightTurn(1.5)
    flag = 0
    TurretRotation(lat, lon)
    os.system('python /home/pi/Desktop/build/Platform/platformCCW.py')
    os.system('python /home/pi/Desktop/build/Platform/armUp.py')
    start_time = time.time()
    while time.time() - start_time <= 4:
        os.system('python /home/pi/Desktop/build/Platform/vibration.py')
        vibration = open("/home/pi/Desktop/build/Platform/vibration.txt","r")
        data = vibration.readline()
        data = int(data)
        if data == 1:
            print "Hit"
            break

    os.python('python /home/pi/Desktop/build/Platform/armDown.py')
    os.system('python /home/pi/Desktop/build/Platform/platformCW.py')

f.close()
g.close()
