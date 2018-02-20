import math


def stepsCoordinates:

    coordinates = open("Coordinates.txt", "r") # opens file with name of "Coordinates.txt"\
	firstLine = coordinates.readline()
	splitCoor = firstLine.split(",")
	intCoor = [int(e) for e in splitCoor]
	xCoor, yCoor = intCoor

	print xCoor, yCoor

	degreeTan = math.degrees(math.tan(yCoor / xCoor))
	print degreeTan

	steps = degreeTan / 1.8
	steps = math.ceil(steps)
	return steps
