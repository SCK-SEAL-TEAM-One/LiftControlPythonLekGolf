import time
limit_weight = 1000.00
current_floor = 1

def isWeightOver (current_weight,limit_weight):
    
    return float(current_weight) > float(limit_weight)

def controlLift (current_floor,goto_floor):
    while True:
        if current_floor == goto_floor:
            print("Lift stop")
            break
        if current_floor < goto_floor:
            current_floor = current_floor + 1
            print("current_floor UP :" ,current_floor)
            time.sleep(3)
        elif current_floor > goto_floor:
            current_floor = current_floor - 1
            print("current_floor Down :" ,current_floor)
            time.sleep(3)


current_weight = input('input weight :');

if isWeightOver( current_weight, limit_weight) :
    print("stop")
else:
    goto_floor = int(input('input goto :'));
    controlLift(current_floor,goto_floor)
