import random, time

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

# x  = Latitude
# y = longitude
# SouthWest Latitude < x < SouthEast Latitude
# SouthWest Lognitude < y < NorthWest Longitude
# NW Longitude = SW Longitude
# SE Latitude = SW Latitude
# NE Latitude = SE Latitude 
# NE Longitude = NW Longitude

lat.write(coordinates[2] + ',' + coordinates[3] + '\n')
for i in range(0,int(coordinates[8])):
    latitude = random.uniform(float(coordinates[2]),float(coordinates[0]))
    longitude = random.uniform(float(coordinates[1]),float(coordinates[5]))
    lat.write(str(latitude) + ',' + str(longitude) + '\n')

lat.write(coordinates[2] + ',' + coordinates[3] + '\n')
lat.close()
randomInput.close()
