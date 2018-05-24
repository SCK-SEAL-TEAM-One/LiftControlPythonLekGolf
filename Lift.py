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
            print("Lift is",lift_state,"at floor",current_floor)
            break
        if current_floor < goto_floor:
            current_floor = current_floor + sendSignal()
            lift_state = "up"
            print("˄",current_floor)
            #print("Lift is ",lift_state,"to floor",current_floor)
        elif current_floor > goto_floor:
            current_floor = current_floor - sendSignal()
            lift_state = "down"
            print("˅",current_floor)
            #print("Lift is",lift_state,"to floor",current_floor)

while True:
    print("======= Welcome ======")
    print("Lift is now at floor",current_floor)
    current_weight = input('Input weight :');
    if isWeightOver( current_weight, limit_weight) :
        lift_state = "stop"
        print("Lift is",lift_state,"at floor",current_floor)
    else:
        goto_floor = int(input('Input destination floor :'));
        controlLift(goto_floor)
