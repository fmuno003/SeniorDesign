import RPi.GPIO as GPIO
import time
import serial
import turningFunctions

angleArray = [100.00,150.00,200.00,45.00]

mode = GPIO.getmode()

motor_1_Forward = 18
motor_2_Forward = 11
motor_3_Forward = 21
motor_4_Forward = 22
motor_1_Backward = 12
motor_2_Backward = 13
motor_3_Backward = 23
motor_4_Backward = 24
EnableM1 = 16
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


#Generates Arrays

# > Coordinates.txt
# > angles.txt
# cd GUI
# python gui.py
# cd ..
# python RandNum.py
# python angles.py


#Self Test
''''
turningFunctions.Forward(1,100,75)
turningFunctions.Stop(0.5)
turningFunctions.Backward(1,100,75)
turningFunctions.Stop(0.5)
turningFunctions.RightTurn(1.5)
turningFunctions.Stop(0.5)
turningFunctions.LeftTurn(1.5)
turningFunctions.Stop(0.5)
#   Main
'''''
#i is our array position, once we hit 3, we break
i=0
transitionFlag = 0
j=0
while (i<3):
    #if we reach the end of the array, break
    if i == 3:
        break

    #Turning
    ser = serial.Serial("/dev/ttyACM0", 9600)
    currentIMU = ser.readline()
    print currentIMU
    print angleArray[0]
    if (float(angleArray[0]) > float(currentIMU)):
        print("Less Than")
    elif (float(angleArray[0]) < float(currentIMU)):
        print("Greater Than")
    else:
        "Equal"
    #While the current angle =/= desired angle, call turning function
    #-----NEEDS TO BE TESTED-----------#
