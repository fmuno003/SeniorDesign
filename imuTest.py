from time import sleep
from mpu6050 import mpu6050

sensor = mpu6050(0x68)

gyroData = sensor.get_gyro_data()

while True:
    print gyroData
    sleep(1)
