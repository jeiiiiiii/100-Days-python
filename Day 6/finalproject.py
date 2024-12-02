def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
while not at_goal():
    if right_is_clear():
        turn_right()
        if wall_in_front():
            turn_left()
        else:
            move()
    else:
        if wall_in_front():
            turn_left()
        else:
            move()
