import Lift as lift
while True:
    print("======= Welcome ======")
    print("Lift is now at floor")
    current_weight = input('Input weight :');
    if lift.isWeightOver( current_weight) :
        lift_state = "stop"
        print("Lift is",lift_state,"at floor",lift.current_floor)
    else:
        goto_floor = int(input('Input destination floor :'));
        lift.controlLift(goto_floor)
