import time
global current_floor
limit_weight = 1000.00
current_floor = 1

def isWeightOver (current_weight,limit_weight):
    return float(current_weight) > float(limit_weight)

def sendSignal ():
    signal = 1    
    time.sleep(3)
    return signal

def controlLift (goto_floor):
    global current_floor
    while True:
        if current_floor == goto_floor:
            print("Lift stop")
            break
        if current_floor < goto_floor:
            current_floor = current_floor + sendSignal()
            print("current_floor UP :" ,current_floor)
        elif current_floor > goto_floor:
            current_floor = current_floor - sendSignal()
            print("current_floor Down :" ,current_floor)

while True:
    current_weight = input('input weight :');
    if isWeightOver( current_weight, limit_weight) :
        print("Lift stop")
    else:
        goto_floor = int(input('input goto :'));
        controlLift(goto_floor)
