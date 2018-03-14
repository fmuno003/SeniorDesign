import serial
from time import sleep

print ("starting")
ser = serial.Serial('/dev/ttyACM0', baudrate=9600)
ser.flush()
read_serial = ser.readline()
read_2 = ser.readline()

print ("start reading")
if read_serial == None:
    read_serial = ser.readline()
if read_2 == None:
    read_2 = ser.readline()

print (read_serial)
print (read_2)

imu = open('/home/pi/Desktop/build/imu.txt','w')
if (read_serial) != (read_2):
    print("sending this: " + str(read_2))
    imu.write(str(read_2))
else:
    print("sending this: " + str(read_serial))
    imu.write(str(read_serial))
imu.close()

ser.close()
