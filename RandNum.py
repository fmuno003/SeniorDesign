from random import *

lat = open("Coordinates.txt","a")
lat.write('--------------------' +' \n')
lat.write('Lat: ' + '0 ')
lat.write('Long: ' + '0\n')
lat.close


for i in range(1,5):
    lat = open("Coordinates.txt", "a")
    lat.write('Lat: ' + str(randint(0,12)) + ' ')
    lat.write('Long: ' + str(randint(0,26)) + '\n')
    lat.close()

lat = open("Coordinates.txt","a")
lat.write('--------------------' + '\n')
lat.write('\n')
lat.close()
