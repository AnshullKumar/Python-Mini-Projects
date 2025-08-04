#Welcome to this game!
##This is a simple dice game where you can play against the computer.

import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll
    
