from car_info import *

def initial_game(field):
    for y in range(len(field)):
        for x in range(0,30):
            field[0 + x][y] = 'b'
            field[770 + x][y] = 'b'
    return field

