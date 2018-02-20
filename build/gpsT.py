import serial
import string
import pynmea2
import time

ser = serial.Serial("/dev/ttyUSB0", 4800)
ser.close()
ser.open()
start_time = time.time()
while (time.time() - start_time < 5):
    data = ser.readline()
    x = data.split(',')
    if x[0] == "$GPGGA" or x[0] == "$GPRMC":
        data = pynmea2.parse(data)
        print data.latitude
        print data.longitude
