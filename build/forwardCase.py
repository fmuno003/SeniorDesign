import RPi.GPIO as GPIO
import random, motorSelfTest, time, serial, pynmea2, math, os, sys

random.seed(time.time())
GPIO.setwarnings(False)
mode = GPIO.getmode()

LATITUDE_CONST = 0.0000063265 # Latitude distance for 1 meter
LONGITUDE_CONST = 0.000010488 # Longitude Distance for 1 meter

motor_1_Forward = 10
motor_2_Forward = 11
motor_3_Forward = 21
motor_4_Forward = 22
motor_1_Backward = 12
motor_2_Backward = 13
motor_3_Backward = 23
motor_4_Backward = 24
EnableM1 = 8
EnableM2 = 15
EnableM3 = 19
EnableM4 = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_1_Forward, GPIO.OUT)
GPIO.setup(motor_2_Forward, GPIO.OUT)
GPIO.setup(motor_3_Forward, GPIO.OUT)
GPIO.setup(motor_4_Forward, GPIO.OUT)
GPIO.setup(motor_1_Backward, GPIO.OUT)
GPIO.setup(motor_2_Backward, GPIO.OUT)
GPIO.setup(motor_3_Backward, GPIO.OUT)
GPIO.setup(motor_4_Backward, GPIO.OUT)
GPIO.setup(EnableM1, GPIO.OUT)
GPIO.setup(EnableM2, GPIO.OUT)
GPIO.setup(EnableM3, GPIO.OUT)
GPIO.setup(EnableM4, GPIO.OUT)

def TurnAngles():
    turning = open("/home/pi/Desktop/angles.txt","r")
    a = []
    data = turning.readline()
    while data != "":
        a.append(float(data))
        data = turning.readline()
        print(a)
    return a

def motorTesting():
    motorSelfTest.Forward(100,75)
    motorSelfTest.Stop()
    motorSelfTest.Backward(100,75)
    motorSelfTest.Stop()

def GPSdata():
    ser = serial.Serial("/dev/ttyUSB0", 4800, timeout=1)
    if not(ser.isOpen()):
        ser.open()
    start_time = time.time()
    while(time.time() - start_time < 1):
        data = ser.readline()
        x = data.split(',')
        if x[0] == "$GPGGA":
            location = pynmea2.parse(data)
    ser.close()
    return location.latitude, location.longitude

latit, longi = GPSdata()
ORIGIN_LATITUDE = latit # Global constants for the origin
ORIGIN_LONGITUDE = longi # Will not change and comparison using turret function

def TurretRotation(lat, lon):
    x = lat - ORIGIN_LATITUDE
    y = lon - ORIGIN_LONGITUDE
    angle = math.degrees(math.atan2(y,x)) + 270
    txtfile = open("/home/pi/Desktop/build/Platform/angles.txt","w")
    txtfile.write(str(angle))
    txtfile.close()
    # write to text file for platform rotation 

def distanceFormula(moveLatitude, moveLongitude, latitude, longitude):
    latDis = ((moveLatitude - latitude)**2) * LATITUDE_CONST
    longDis = ((longitude - moveLongitude)**2) * LONGITUDE_CONST
    distance = math.sqrt(latDis + longDis)
    return distance #returns distance in meters

def stripString(string):
    tempData = string.strip(',')
    latitude = float(tempData[0])
    longitude = float(tempData[1])
    return latitude, longitude

# Sets inital for IMU
def CalibrateIMU(readValue):
    #os.system("python /home/pi/Desktop/build/imu.py")
    #readValue = open("/home/pi/Desktop/build/imu.txt","r")
    #read_ser = readValue.readline()
    #while read_ser == None  or read_ser == ' ':
    read_ser = readValue.readline()
    
    Offset = 0.0 - float(read_ser)
    print("Offset" + str(Offset))
    return Offset

def IMU(Offset,readValue):
#    os.system("python /home/pi/Desktop/build/imu.py")
#    readValue = open("/home/pi/Desktop/build/imu.txt","r")
    read_ser = readValue.readline()
    read_ser = float(read_ser) + float(Offset)
    print(read_ser)
    if read_ser < 0.0: 
        read_ser += 360.0
    elif read_ser > 360.0:
        read_ser -= 360.0
    return read_ser

def Turning(flag, Offset, a, readValue):
    calcAngle = a

    if calcAngle < 0.0: 
        calcAngle += 360.0
    elif calcAngle > 360.0:
        calcAngle -= 360.0

    print("Turning now:")
    print("Target Angle" + str(calcAngle))
    

    if flag == 1:
        motorSelfTest.RightTurn()
        while IMU(Offset,readValue) < calcAngle:
            print("Current angle " + str(IMU(Offset,readValue)))
            #Loops until angle is achieved
        motorSelfTest.Stop()
        
    elif flag == 2:
        motorSelfTest.LeftTurn()
        while IMU(Offset) > calcAngle:
            print("Current angle " + IMU(Offset,readValue))
            #Loops until angle is achieved
        motorSelfTest.Stop()
    motorSelfTest.Stop()

#Parameter: Flag
def returnTurn(flag, Offset):
    if flag == 1:
        while (IMU(Offset) > 10) or (IMU(Offset) < 350):
            motorSelfTest.LeftTurn()
    elif flag == 2:
        while (IMU(Offset) > 10) or (IMU(Offset) < 350):
            motorSelfTest.RightTurn()
    motorSelfTest.Stop()
    
def calculateBounds():
    fp = open("/home/pi/Desktop/GUI/examples.txt","r")
    for i, line in enumerate(fp):
        if i == 6:
            rightLat = float(line)
            print rightLat
        if i == 1:
            upLong = float(line)
            print upLong
        if i == 2:
            lowLong = float(line)
            print lowLong
        if i == 3:
            leftLat = float(line)
            print leftLat
    return leftLat, rightLat, upLong, lowLong

def checkBounds(lat,lon, leftLat, rightLat, upLong, lowLong):
    if lat < leftLat or lat > rightLat:
        return 1
    if lon > upLong or lon < lowLong:
        return 1
    return 0
#===== Main =====
LEFT_LAT, RIGHT_LAT, UP_LONG, LOW_LONG = calculateBounds()

#GUI CODE
os.system('python /home/pi/Desktop/GUI/gui.py')
os.system('python /home/pi/Desktop/RandNum.py')
os.system('python /home/pi/Desktop/angles.py')

readValue = serial.Serial('/dev/ttyACM0', baudrate=9600)

#Flushes Serial Ports
i=0
while i<15:
    test = readValue.readline()
    i=i+1
print("Flushed IMU")
motorTesting()

#inputs for Forward() and Backward() are (timeSleep,dutyCycle,freq)
f = open('/home/pi/Desktop/angles.txt','r')
g = open('/home/pi/Desktop/Coordinates.txt', 'r')
points = g.readline()
latitude, longitude = stripString(points)
flag = 0
anglesArray = []
i = 0
#===== Loop =====
while True:

    #== Reads in locations ==
    message = f.readline()
    points = g.readline()
    if message == '' or points == '':
        break
    currentLine = float(message)
    
    desLat, desLong = stripString(points)
    if currentLine > 0.0:
        flag = 1
    elif currentLine < 0.0:
        flag = 2
    
    print("flag: " + str(flag))

    Offset = CalibrateIMU(readValue)
    #==== Angles =====
    anglesArray = TurnAngles()
    #==== Turning ====
    print(anglesArray[i])
    #Turning(flag, Offset, anglesArray[i], readValue)
    #==== Forward Movement ====
    lat, lon = GPSdata()
    distance = distanceFormula(lat, ORIGIN_LONGITUDE, desLat, ORIGIN_LONGITUDE)
    
    #Motor Activates for 10 Seconds
    if (desLat < lat):
        motorSelfTest.Backward(random.randint(25,100),100)
    if (lat > desLat):
        motorSelfTest.Forward(random.randint(25,100),100)
    while (distance >= 0.05):
        lat, lon = GPSdata()
        boundary = checkBounds(lat, lon, LEFT_LAT, RIGHT_LAT, UP_LONG, LOW_LONG)
        distance = distanceFormula(lat, ORIGIN_LONGITUDE, desLat, ORIGIN_LONGITUDE)
        print distance
    motorSelfTest.Stop()
    #===== Turret Code ===== 
    TurretRotation(lat, lon)
    os.system('python /home/pi/Desktop/build/Platform/platformCCW.py')
    # Arm Up works fine, no need to touch it
    os.system('python /home/pi/Desktop/build/Platform/armUp.py')
    start_time = time.time()
    while time.time() - start_time <= 4:
        os.system('python /home/pi/Desktop/build/Platform/vibration.py')
        vibration = open("/home/pi/Desktop/build/Platform/vibration.txt","r")
        data = vibration.readline()
        data = int(data)
        if data == 1:
            print "Hit"
            break
    # Arm Down works fine, no need to touch it
    os.system('python /home/pi/Desktop/build/Platform/armDown.py')
    os.system('python /home/pi/Desktop/build/Platform/platformCW.py')
    
    #===== Turning ======
    #returnTurning(flag, Offset)
    flag = 0
    Offset = 0
    i = i + 1

f.close()
g.close()
