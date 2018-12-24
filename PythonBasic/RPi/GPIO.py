pins = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

def setup(IntPin,outMode):
    pass

def setwarnings(boolValue):
    pass

def setmode(intValue):
    pass

def output(IntPin,boolValue):
    if boolValue == 0:
        pins[IntPin]=0
    else:
        pins[IntPin]=1
    print(pins)

def input(IntPin):
    return pins[IntPin]

def BCM(int):
    pass

def OUT(int):
    pass