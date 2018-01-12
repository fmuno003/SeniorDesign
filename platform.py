import RPi.GPIO as GPIO
import time
import sys

# Pins 29, 31, 32, 33
# Pin 34 Ground

GPIO.setmode(GPIO.BCM)

StepPins = [29, 31, 32, 33]

for pin in StepPins:
    print "Setup Pins"
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

StepCount = len(Seq)
StepDir = 1

if len(sys.argv)>1:
    WaitTime = int(sys.argv[1])/float(1000)
else:
    WaitTime = 10/float(1000)

StepCounter = 0

while True:
    print StepCounter

    for pin in range(0,4):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin] != 0:
            print "Enable GPIO %i" %(xpin)
            GPIO.output(xpin, True)
        else:
            GPIO.output(xpin, False)

    StepCounter += StepDir
    if (StepCounter >= StepCount):
        StepCounter = 0
    if (StepCounter < 0):
        StepCounter = StepCounter + StepDir

    time.sleep(WaitTime)
