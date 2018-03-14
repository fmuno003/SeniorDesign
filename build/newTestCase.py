import time, os, variableSpeed
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
mode = GPIO.getmode()

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
pinSensor = 37

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
GPIO.setup(pinSensor, GPIO.IN)

def motorTesting():
    variableSpeed.Forward(1,100,75)
    variableSpeed.Stop(0.5)
    variableSpeed.Backward(1,100,75)
    variableSpeed.Stop(0.5)

def callback(pinSensor):
    if GPIO.input(pinSensor):
        return 1
    else:
        return 0

GPIO.add_event_detect(pinSensor, GPIO.RISING, bouncetime=550)
#GPIO.add_event_callback(pinSensor, callback)
#motorTesting()
array = [25,19,12]
i = 0
hit = 0
while i < 3:
    #Forward 3 Sec and Turret
    variableSpeed.Forward(3,100,100)
    variableSpeed.Stop(0.5)
    print("stop")
    angles = open("/home/pi/Desktop/build/Platform/angles.txt","w")
    angles.write(str(array[i]) + '\n')
    angles.close()
    if i == 0:
        os.system(' python /home/pi/Desktop/build/Platform/platformCCW.py')
        os.system(' python /home/pi/Desktop/build/Platform/armUp.py')
        start_time = time.time()
        while time.time() - start_time < 3:
            data = callback(37)
            if data == 1:
                hit += 1
            data = 0
        os.system(' python /home/pi/Desktop/build/Platform/armDown.py')
        os.system(' python /home/pi/Desktop/build/Platform/platformCW.py')
    else:
        os.system(' python /home/pi/Desktop/build/Platform/platformCW.py')
        os.system(' python /home/pi/Desktop/build/Platform/armUp.py')
        start_time = time.time()
        while time.time() - start_time < 3:
            data = callback(37)
            if data == 1:
                hit += 1
            data = 0
        os.system(' python /home/pi/Desktop/build/Platform/armDown.py')
        os.system(' python /home/pi/Desktop/build/Platform/platformCCW.py')

    print("Step")
    
    #90deg Turn
    print("Right Turn")
    variableSpeed.RightTurn(2.3)
    variableSpeed.Stop(0.5)
    #Left to orient "North" and Turret
    #variableSpeed.LeftTurn(turnTime)
    #variableSpeed.Stop(0.5)
 
    #Reverse to next point and turret
    #variableSpeed.Backward(moveTime,100,100)
    #variableSpeed.Stop(0.5)  

    #Left turn and move to next point, no turret.
    #variableSpeed.LeftTurn(turnTime)
    #variableSpeed.Stop(0.5)

    print ("Hits: " + str(hit))
    i += 1
    hit = 0
