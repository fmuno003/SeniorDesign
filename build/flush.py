import serial
from time import sleep

i=0

ser = serial.Serial('/dev/ttyACM0', baudrate=9600)
ser.flush()

read_serial=ser.readline()

while i<10:
    read_serial=ser.readline()
    print(read_serial)
    i=i+1

ser.close()