#!/usr/bin/python
import RPi.GPIO as GPIO
import time


#GPIO Setup
pinSensor = 26 # Have to update this since not sure which pin we will use
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinSensor, GPIO.IN)

vibration = open("vibration.txt.","w")
def callback(pinSensor):
    if GPIO.input(pinSensor):
        vibration.write('1')
        print "Movement Detected!"


GPIO.add_event_detect(pinSensor, GPIO.RISING, bouncetime=550)
GPIO.add_event_callback(pinSensor, callback)

while True:
    time.sleep(1)
