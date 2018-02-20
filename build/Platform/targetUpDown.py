import time

def ControlFunction():

while True:
    ControlFunction()
    print "Target Up"
    try:
        execfile('armUp.py')
    except:
        print "Continue"
    
    time.sleep(2)

    print "Target Down"
    try:
        execfile("armDown.py")
    except:
        print "Done"

    time.sleep(2)
    
