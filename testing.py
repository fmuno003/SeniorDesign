import math

f = open('Coordinates.txt','r')
previousX = 0
previousY = 0
while True:
    message = f.readline()
    if message == '':
        break
    currentLine = message.split(",")
    x = int(currentLine[0]) #reading in the x coordinate
    y = int(currentLine[1]) # reading in the y coordinate
    if previousX == x: #if previous x coordinate and current x coordinate equal each other it does not move in the x axis
        print('Stationary')
    elif previousX < x: #if the previous coordinate is greater than the current coordinate, it has to move forwards 
        for i in range(previousX, x):
            print('Moving Forward on X axis')
    else: #if the previousX is less than the current coordinate, it has to move backwards
        for i in range(x, previousX):
            print('Moving Backwards on X axis')
    if previousY == y: # if the previous y coordinate is equal to the current y coordinate, it does not move in the y axis
        print('Stationary')
    elif previousY < y: # if the previous y coordinate is greater than the current y coordinate, move forward
        for i in range(previousY, y):
            print('Moving Forward on Y axis')
    else: # if the previous coorindate is less than the current coordinate, move backwards
        for i in range(y, previousY):
            print('Moving Backward on Y axis')
    previousX = x
    previousY = y
    print('\n')
f.close()
