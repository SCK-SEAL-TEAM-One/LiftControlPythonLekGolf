import time
global current_floor
global lift_state
global limit_weight
limit_weight = 1000.00
current_floor = 1
top_floor = 10
lowest_floor = 1

def isWeightOver (current_weight):
    global limit_weight
    return float(current_weight) > float(limit_weight)

def isGoToFloorOverTopFloor(goto_floor):
    return goto_floor > top_floor

def isGoToFloorLowerLowestFloor(goto_floor):
    return goto_floor < lowest_floor

def sendSignal ():
    signal = 1    
    #time.sleep(3)
    return signal

def controlLift (goto_floor):
    global current_floor
    global lift_state
    while True:
        if ( current_floor == goto_floor)|(isGoToFloorOverTopFloor(goto_floor))|(isGoToFloorLowerLowestFloor(goto_floor)):
            lift_state = "stop"
            break
        if current_floor < goto_floor:
            current_floor = current_floor + sendSignal()
            lift_state = "up"
            print("˄",current_floor)
        elif current_floor > goto_floor:
            current_floor = current_floor - sendSignal()
            lift_state = "down"
            print("˅",current_floor)
    return int(current_floor)

