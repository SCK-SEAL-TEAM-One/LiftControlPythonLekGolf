import time
global current_floor
global lift_state
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
    global lift_state
    while True:
        if current_floor == goto_floor:
            lift_state = "stop"
            print("Lift is",lift_state)
            break
        if current_floor < goto_floor:
            current_floor = current_floor + sendSignal()
            lift_state = "up"
            print("Lift is",lift_state)
        elif current_floor > goto_floor:
            current_floor = current_floor - sendSignal()
            lift_state = "down"
            print("Lift is",lift_state)

while True:
    current_weight = input('input weight :');
    if isWeightOver( current_weight, limit_weight) :
        lift_state = "stop"
        print("Lift is",lift_state)
    else:
        goto_floor = int(input('input goto :'));
        controlLift(goto_floor)
