import random
from brick_info import *
from car_info import *
bricks = []

delta_time = 0
cooldown = 20

def initial_game(field):
    for y in range(len(field)):
            field[0][y] = 'b'
            field[19][y] = 'b'
    return field


def brick_fallen(field, car):
    global bricks, delta_time, cooldown
    k=0
    dead_list = []
    if delta_time > cooldown:
        while k < 4:
            if random.randint(1, 20) == 1:
                x = random.randint(1, len(field)-2)
                brick = Brick(x, -1)
                bricks.append(brick)
                k += 1
        for brick in bricks:
            field[brick.pos.x][brick.pos.y] = ' '
            if brick.pos.y >= len(field)-1:
                bricks.remove(brick)
            elif field[brick.pos.x][brick.pos.y+1] == 'car':
                bricks.remove(brick)
                car.take_damage(10)
            else:
                brick.pos.y += 1
                field[brick.pos.x][brick.pos.y] = 'b'
        delta_time = 0
    else:
        delta_time += 1

    return field

