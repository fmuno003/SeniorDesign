#!/bin/bash

import time
import serial
import turningFunction

#Generates Arrays

# > Coordinates.txt
# > angles.txt
# cd GUI
# python gui.py
# cd ..
# python RandNum.py
# python angles.py


#Self Test
cd build
python motorControl.py
cd ..

#   Main

#i is our array position, once we hit 3, we break
i=0
while (i<3)
    #if we reach the end of the array, break
    if i == 3
        break

    #Turning
    ser=serial.Serial("/dev/ttyACM0", 9600)
    ser.baudrate=9600

    #While the current angle =/= desired angle, call turning function
    #-----NEEDS TO BE TESTED-----------#
    while(read_ser = ser.readline() < angleArray[i])
        #Turn function goes here --------
        turningFunction.RightTurn()
