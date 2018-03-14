import RPi.GPIO as GPIO
import time

#GPIO Setup
pinSensor = 37 # Have to update this since not sure which pin we will use
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinSensor, GPIO.IN)

def callback(pinSensor):
    vibration = open("/home/pi/Desktop/build/Platform/vibration.txt", "w")
    if GPIO.input(pinSensor):
        vibration.write(str(1))
    else:
        vibration.write(str(0))
    vibration.close()

GPIO.add_event_detect(pinSensor, GPIO.RISING, bouncetime=550)
#GPIO.add_event_callback(pinSensor, callback)

callback(37)
time.sleep(1)

