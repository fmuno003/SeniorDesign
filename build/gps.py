import serial
import time

start_time = time.time()
def getdata(port):
# open the serial port
    port.open()
# check that the port is open
    if port.isOpen():
# read 16 lines
        line = []
        #print 'receiving data from device\n'
        for i in range(1,40):
            line.append(port.readline())
# close the serial port
    port.close()
# discard the first line (sometimes it contains rubbish, so just always discard it)
    del line[0]
# return the list of lines
    return line
 
def outputdata(data):
    #print '= Satellites in view ='
    #print 'Number of satellites in view: ' + data[0][3]
    for i in range(0,int(data[0][1])):
        processGPGSV(data[i])
    #print ''
# look for the newest fix
    #print '= Fix data ='
    fixfound = False
    for i in range(0,len(data)):
        if fixfound == False and data[i][0] == '$GPGGA':
            fixfound = True
            processGPGGA(data[i])
    #print ''
    #print '= End ='
 
def initialise():
# initialise serial port settings
    Port = serial.Serial()
    Port.baudrate = 4800
    Port.port = '/dev/ttyUSB0'
    Port.xonxoff = 1
# return the port as an object we can use
    return Port
 
def trimdata(trimdata):
# first split the data. as NMEA sentence checksums follow straight on from the previous
# piece of data with a *, we will first replace the * with a , then split the string
# using , as the separator
#
# if you were going to use the data for navigation it would probably be a good idea to
# actually do something with the checksum, like using it to verify the data, but i'm
# not really too concerned for what i'm doing.
    splitdata = []
    for i in range(0,len(rawdata)):
        splitdata.append(rawdata[i].replace('*',',').split(',',-1))
# now we can access/reference the first part of a sentence easily (i.e. [i][0]
# find the three GPGSV sentences in a row and trim dataset accordingly to one 'cycle'
    foundstart = False
    start = 0
    for i in range(0,len(splitdata)):
        if foundstart == False and splitdata[i][0]  == '$GPGSV' and splitdata[i + 1][0] == '$GPGSV' and splitdata[i + 2][0] == '$GPGSV':
            foundstart = True
            start = i
    if foundstart:
        trimmeddata = []
        for i in range(start,start+18):
            trimmeddata.append(splitdata[i])
        return trimmeddata
    else:
        print 'could not isolate cycle'
 
def processGPGSV(snippet):
# list satellite information
    #if not snippet[4] == '':
        #print '*** Satellite PRN ' + snippet[4] + '. SNR ' + snippet[7].rjust(2, '0') + '. Elev ' + snippet[5] + '. Azi ' + snippet [6] + '. ***'
    #if not snippet[8] == '':
        #print '*** Satellite PRN ' + snippet[8] + '. SNR ' + snippet[11].rjust(2, '0') + '. Elev ' + snippet[9] + '. Azi ' + snippet [10] + '. ***'
    #if not snippet[12] == '':
        #print '*** Satellite PRN ' + snippet[12] + '. SNR ' + snippet[15].rjust(2, '0') + '. Elev ' + snippet[13] + '. Azi ' + snippet [14] + '. ***'
    '''if not snippet[16] == '':
        print '*** Satellite PRN ' + snippet[16] + '. SNR ' + snippet[19].rjust(2, '0') + '. Elev ' + snippet[17] + '. Azi ' + snippet [18] + '. ***'
 '''
def processGPGGA(snippet):
# list fix information
    '''print 'Time of Fix                          : ' + snippet[1][0:2] + ':' + snippet[1][2:4] + ':' + snippet[1][4:6] + ' UTC'
    print 'Latitude                             : ' + snippet[2][0:2] + ' Degrees ' + snippet[2][2:len(snippet[2])] + '\' ' + snippet[3]
    print 'Longitude                            : ' + snippet[4][0:3] + ' Degrees ' + snippet[4][3:len(snippet[4])] + '\' ' + snippet[5]'''
    
# this is lazy as it treats anything other than a GPS fix as bad
    if snippet[6] == '1':
        #print 'Fix Quality                          : GOOD'
        dummy = 5
    else:
        #print 'Fix Quality                          : BAD'
        dummy = 6
    ''' print 'Number of satellites being tracked   : ' + snippet[7]
    print 'Horizontal DOP, lower = better       : ' + snippet[8]
    print 'Altitude above mean sea level        : ' + snippet[9] + ' meters'
    print 'Height of geoid above WGS84 ellips.  : ' + snippet[11] + ' meters'''
    lat = float(snippet[2][0:2]) + float(snippet[2][2:len(snippet[2])]) / 60.0
    lng = float(snippet[4][0:3]) + float(snippet[4][3:len(snippet[4])]) / 60.0
    if snippet[3] == 'S':
        lat *= -1
    if snippet[5] == 'W':
        lng *= -1
    #print 'http://maps.google.com?q=' + str(lat) + ',' + str(lng)
    print 'Lat: ' + str(lat)
    print 'Lng: ' + str(lng)
    
    '''f = open("Coordinates.txt","a")
    f.write(str(lat) + ' ')
    f.write(str(lng) + '\n')
    f.close()'''

# main program starts here
sPort = initialise()
while True:
    start_time = time.time()
    rawdata = getdata(sPort)
    trim = trimdata(rawdata)
    outputdata(trim)
    print (time.time() - start_time)
    print
# end
