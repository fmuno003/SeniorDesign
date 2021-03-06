import RPi.GPIO as GPIO
import time
import math

counter = 0
def stepCoordinates():
    
    #coordinates = open("/home/pi/Desktop/Coordinates.txt", "r") # opens file with name of "Coordinates.txt"\
    #firstLine = coordinates.readline()
    #splitCoor = firstLine.split(",")
    #intCoor = [int(e) for e in splitCoor]
    #xCoor, yCoor = intCoor

    #print xCoor, yCoor
    #radTan = yCoor / xCoor
    #degreeTan = math.degrees(math.tan(radTan))
    #print degreeTan

    angles = open("/home/pi/Desktop/build/Platform/angles.txt","r")
    steps = angles.readline()
    steps = int(steps)
    return steps

delay = 0.01
steps = stepCoordinates()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Platform Stepper Motor

# IN1 = 36
# IN2 = 35
# IN3 = 38
# IN4 = 40

A1pin = 36
A2pin = 35
B1pin = 38
B2pin = 40

GPIO.setup(A1pin, GPIO.OUT)
GPIO.setup(A2pin, GPIO.OUT)
GPIO.setup(B1pin, GPIO.OUT)
GPIO.setup(B2pin, GPIO.OUT)

def setStep(w1, w2, w3, w4):
    GPIO.output(A1pin, w1)
    GPIO.output(A2pin, w2)
    GPIO.output(B1pin, w3)
    GPIO.output(B2pin, w4)

for i in range(0, int(steps)):
    setStep(1,0,1,0)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(1,0,0,1)
    time.sleep(delay)
