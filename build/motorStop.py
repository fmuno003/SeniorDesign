import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)

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

# Stop
def Stop():
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

Stop()
