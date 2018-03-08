import serial

ser = serial.Serial('/dev/ttyACM0',9600)
imu = open('/home/pi/Desktop/build/imu.txt','w')
read_serial = ser.readline()
read_2 = ser.readline()
print (read_serial)
print (read_2)
if read_2 == ' ':
    read_2 = ser.readline()
if read_serial == ' ':
    read_serial = ser.readline()

if (read_serial) != (read_2):
    print(read_2)
    imu.write(read_2)
else:
    imu.write(read_2)
