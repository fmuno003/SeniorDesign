import time

def ControlFunction():
    print "Cycle Start"
while True:
    ControlFunction()
    print "Rotate CW"
    try:
        execfile('platformCW.py')
    except:
        print "Now raise arm"
    
    time.sleep(1)

    print "Target Up"
    try:
        execfile('armUp.py')
    except:
        print "Now lower arm"
   
    time.sleep(1)

    print "Target Down"
    try:
        execfile('armDown.py')
    except:
        print "Now rotate CCW"

    time.sleep(1)

    print "Rotate CCW"
    try:
        execfile('platformCCW.py')
    except:
        print "Cycle Done"

    time.sleep(1)
    
