import random
from brick_info import *
bricks = []


def initial_game(field):
    for y in range(len(field)):
        for x in range(0,30):
            field[0 + x][y] = 'b'
            field[len(field) - 1 - x][y] = 'b'
    return field


def brick_fallen(field):
    global bricks
    k=0
    while k < 10:
        if random.randint(1, 10) == 1:
            x = random.randint(31, 769)
            brick = Brick(x, 0)
            bricks.append(brick)
            k+=1
    for brick in bricks:
        field[brick.pos.x][brick.pos.y] = ' '
        brick.pos.y += 20
        field[brick.pos.x][brick.pos.y] = 'b'
        if brick.pos.y >= 779:
            field[brick.pos.x][brick.pos.y] = ' '
            brick.pos.x = random.randint(31, 769)
            brick.pos.y = 0
            field[brick.pos.x][brick.pos.y] = 'b'
    return field

