import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)

# H-Bridge Pinout

# Motor 1
# enA - Pin 16
# IN1 - Pin 18
# IN2 - Pin 12

# Motor 2
# IN3 - Pin 11
# IN4 - Pin 13
# enB - Pin 15

# Motor 3
# enA - Pin 19
# IN1 - Pin 21
# IN2 - Pin 23

# Motor 4
# IN3 - Pin 22
# IN4 - Pin 24
# enB - Pin 26

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


# Move Forward
def Forward(timeSleep,dutyCycle,freq):
    GPIO.output(EnableM1, GPIO.HIGH)
    GPIO.output(EnableM2, GPIO.HIGH)
    GPIO.output(EnableM3, GPIO.HIGH)
    GPIO.output(EnableM4, GPIO.HIGH)
    GPIO.output(motor_1_Forward, GPIO.HIGH)
    GPIO.output(motor_2_Forward, GPIO.HIGH)
    GPIO.output(motor_3_Forward, GPIO.HIGH)
    GPIO.output(motor_4_Forward, GPIO.HIGH)
    pwm_forwardM1 = GPIO.PWM(motor_1_Forward, freq)
    pwm_forwardM2 = GPIO.PWM(motor_2_Forward, freq)
    pwm_forwardM3 = GPIO.PWM(motor_3_Forward, freq)
    pwm_forwardM4 = GPIO.PWM(motor_4_Forward, freq)
    pwm_forwardM1.start(dutyCycle)
    pwm_forwardM2.start(dutyCycle)
    pwm_forwardM3.start(dutyCycle)
    pwm_forwardM4.start(dutyCycle)
    #print "Moving Forward"
    time.sleep(timeSleep)

# Move Backward
def Backward(timeSleep,dutyCycle,freq):
    GPIO.output(EnableM1, GPIO.HIGH)
    GPIO.output(EnableM2, GPIO.HIGH)
    GPIO.output(EnableM3, GPIO.HIGH)
    GPIO.output(EnableM4, GPIO.HIGH)
    GPIO.output(motor_1_Backward, GPIO.HIGH)
    GPIO.output(motor_2_Backward, GPIO.HIGH)
    GPIO.output(motor_3_Backward, GPIO.HIGH)
    GPIO.output(motor_4_Backward, GPIO.HIGH)
    pwm_backwardM1 = GPIO.PWM(motor_1_Backward, freq)
    pwm_backwardM2 = GPIO.PWM(motor_2_Backward, freq)
    pwm_backwardM3 = GPIO.PWM(motor_3_Backward, freq)
    pwm_backwardM4 = GPIO.PWM(motor_4_Backward, freq)
    pwm_backwardM1.start(dutyCycle)
    pwm_backwardM2.start(dutyCycle)
    pwm_backwardM3.start(dutyCycle)
    pwm_backwardM4.start(dutyCycle)
    #print "Moving Backward"
    time.sleep(timeSleep)

# Right Turn
def RightTurn(timeSleep):
    GPIO.output(EnableM1, GPIO.HIGH)
    GPIO.output(EnableM2, GPIO.HIGH)
    GPIO.output(EnableM3, GPIO.HIGH)
    GPIO.output(EnableM4, GPIO.HIGH)
    GPIO.output(motor_1_Backward, GPIO.HIGH) #inner motor
    GPIO.output(motor_2_Forward, GPIO.HIGH) #outer motor
    GPIO.output(motor_3_Forward, GPIO.HIGH) #outer motor
    GPIO.output(motor_4_Backward, GPIO.HIGH) #inner motor
    '''pwm_forwardM1 = GPIO.PWM(motor_1_Forward, 75)
    pwm_forwardM2 = GPIO.PWM(motor_2_Forward, 75)
    pwm_forwardM3 = GPIO.PWM(motor_3_Forward, 75)
    pwm_forwardM4 = GPIO.PWM(motor_4_Forward, 75)
    pwm_forwardM1.start(50)
    pwm_forwardM2.start(100)
    pwm_forwardM3.start(100)
    pwm_forwardM4.start(50)'''
    #print "Turning Right"
    time.sleep(timeSleep)

# Left Turn
def LeftTurn(timeSleep):
    GPIO.output(EnableM1, GPIO.HIGH)
    GPIO.output(EnableM2, GPIO.HIGH)
    GPIO.output(EnableM3, GPIO.HIGH)
    GPIO.output(EnableM4, GPIO.HIGH)
    GPIO.output(motor_1_Forward, GPIO.HIGH) #outer motor
    GPIO.output(motor_2_Backward, GPIO.HIGH) #inner motor
    GPIO.output(motor_3_Backward, GPIO.HIGH) #inner motor
    GPIO.output(motor_4_Forward, GPIO.HIGH) #outer motor
    '''pwm_forwardM1 = GPIO.PWM(motor_1_Forward, 75)
    pwm_forwardM2 = GPIO.PWM(motor_2_Forward, 75)
    pwm_forwardM3 = GPIO.PWM(motor_3_Forward, 75)
    pwm_forwardM4 = GPIO.PWM(motor_4_Forward, 75)
    pwm_forwardM1.start(100)
    pwm_forwardM2.start(50)
    pwm_forwardM3.start(50)
    pwm_forwardM4.start(100)'''  
    #print "Turning Left"
    time.sleep(timeSleep)

# Stop
def Stop(timeSleep):
    GPIO.output(EnableM1, GPIO.LOW)
    GPIO.output(EnableM2, GPIO.LOW)
    GPIO.output(EnableM3, GPIO.LOW)
    GPIO.output(EnableM4, GPIO.LOW)
    GPIO.output(motor_1_Forward, GPIO.LOW)
    GPIO.output(motor_2_Forward, GPIO.LOW)
    GPIO.output(motor_3_Forward, GPIO.LOW)
    GPIO.output(motor_4_Forward, GPIO.LOW)
    GPIO.output(motor_1_Backward, GPIO.LOW)
    GPIO.output(motor_2_Backward, GPIO.LOW)
    GPIO.output(motor_3_Backward, GPIO.LOW)
    GPIO.output(motor_4_Backward, GPIO.LOW)
    time.sleep(timeSleep)

RightTurn(1.5)
Stop(0.5)
LeftTurn(1.5)
Stop(0.5)
