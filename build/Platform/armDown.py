import RPi.GPIO as GPIO
import time
import sys
import os

# Pin 33, 29, 31, 32

GPIO.setmode(GPIO.BOARD)

StepPins = [33, 29, 31, 32]

total = 0
for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

Seq = [ [0,1,1,0],
        [0,0,1,0],
        [1,0,1,0],
        [1,0,0,0],
        [1,0,0,1],
        [0,0,0,1],
        [0,1,0,1],
        [0,1,0,0]]

Reverse = [ [0,1,0,0],
            [0,1,0,1],
            [0,0,0,1],
            [1,0,0,1],
            [1,0,0,0],
            [1,0,1,0],
            [0,0,1,0],
            [0,1,1,0]]

StepCount = len(Seq)
StepDir = 1

if len(sys.argv)>1:
    WaitTime = int(sys.argv[1])/float(1000)
else:
    WaitTime = 10/float(1000)

StepCounter = 0

while True:

    for pin in range(0,4):
        xpin = StepPins[pin]
        if (Seq[StepCounter][pin] != 0):
            GPIO.output(xpin, True)
            total = total + 1
        else:
            GPIO.output(xpin, False)

    StepCounter += StepDir
    if (StepCounter >= StepCount):
        StepCounter = 0
    if(StepCounter < 0):
        StepCounter = StepCounter + StepDir
    
    if total == 150:
        break
    else:
        time.sleep(WaitTime)

