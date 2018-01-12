import time

def ControlFunction():
    print "Main script running"

while True:
    print "Hello"
    ControlFunction()
    try:
        execfile('targetUp.py')
    except:
        print "Continue"
    print "Target Up"
    
    time.sleep(3)

    try:
        execfile("targetDown.py")
    except:
        print "Done"
    print "Target Down"

    time.sleep(3)
    
