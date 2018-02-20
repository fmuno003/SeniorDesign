a!/usr/bin/python

import smbus
import math

# Power Management
power_mgmt1 = 0x6b
power_mgmt2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a) + (b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x,dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def get_z_rotation(x,y,z):
    radians = math.atan2(z, dist(x, y))
    return math.degrees(radians)

bus = smbus.SMBus(1)
address = 0x68

# Now we activate the 6050 
bus.write_byte_data(address, power_mgmt1, 0)

print "Gyroscope Data"
print "--------------"

gyro_xout = read_word_2c(0x43)
gyro_yout = read_word_2c(0x45)
gyro_zout = read_word_2c(0x47)

gyro_xout_scaled = gyro_xout / 131.0
gyro_yout_scaled = gyro_yout / 131.0
gyro_zout_scaled = gyro_zout / 131.0

print "gyro_xout: ", gyro_xout, "scaled: ", gyro_xout_scaled
print "gyro_yout: ", gyro_yout, "scaled: ", gyro_yout_scaled
print "gyro_zout: ", gyro_zout, "scaled: ", gyro_zout_scaled

print
print "Accelerometer Data"
print "------------------"

accel_xout = read_word_2c(0x3b)
accel_yout = read_word_2c(0x3d)
accel_zout = read_word_2c(0x3f)

accel_xout_scaled = accel_xout / 16384.0
accel_yout_scaled = accel_yout / 16384.0
accel_zout_scaled = accel_zout / 16384.0

print "accel_xout: ", accel_xout, "scaled: ", accel_xout_scaled
print "accel_yout: ", accel_yout, "scaled: ", accel_yout_scaled
print "accel_zout: ", accel_zout, "scaled: ", accel_zout_scaled

print
print "X, Y, Z Rotations"
print "-----------------"
print "x rotation: ", get_x_rotation(gyro_xout_scaled, gyro_yout_scaled, gyro_zout_scaled)
print "y rotation: ", get_y_rotation(gyro_xout_scaled, gyro_yout_scaled, gyro_zout_scaled)
print "z rotation: ", get_z_rotation(gyro_xout_scaled, gyro_yout_scaled, gyro_zout_scaled)
