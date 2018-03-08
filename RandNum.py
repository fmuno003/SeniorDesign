import random
import time

random.seed(time.time())

randomInput = open("/home/pi/Desktop/GUI/examples.txt", "r")
lat = open("/home/pi/Desktop/Coordinates.txt", "w")
coordinates = []

while True:
    data = randomInput.readline()
    if data == '':
        break
    else:
        data = data.strip('\n')
        coordinates.append(data)

lat.write(coordinates[2] + ',' + coordinates[3] + '\n')
for i in range(0,int(coordinates[8])):
    x = random.uniform(float(coordinates[2]),float(coordinates[6]))
    y = random.uniform(float(coordinates[3]),float(coordinates[1]))
    lat.write(str(x) + ',' + str(y) + '\n')

lat.write(coordinates[2] + ',' + coordinates[3] + '\n')
lat.close()
randomInput.close()
