import math

calculate = open("Coordinates.txt", "r")
number = open("/home/pi/Desktop/GUI/examples.txt", "r")
angles = open("angles.txt","a")

coordinates = []
message = calculate.readline()
currentLine = message.split(",")
previousX = float(currentLine[0])
previousY = float(currentLine[1])
while True:
    google = number.readline()
    if google == '':
        break
    else:
        coordinates.append(google)
        pass


for i in range(0, int(coordinates[8])+1):
    message = calculate.readline()
    if message == '':
        break
    currentLine = message.split("i,")
    x = float(currentLine[0])
    y = float(currentLine[1])
    tempX = x - previousX
    tempY = y - previousY
    if(previousY == y):
        if(previousX < x):
            angle = 90
        else:
            angle = -90
    else:
        angle = math.degrees(math.atan2(tempY,tempX))
    angles.write(str(angle) + '\n')
    previousX = x
    previousY = y

number.close()
calculate.close()
angles.close()