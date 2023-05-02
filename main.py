import pygame
import gameplay
from car_info import *


def render_pygame(field, screen):
    scale = 10
    for x in range(0,len(field)):
        for y in range(0,len(field)):
            if field[x][y] == 'b':
                pygame.draw.rect(screen,(255,0,0),(x,y,1,1))
            if field[x][y] == 'car':
                pygame.draw.rect(screen,(0,255,0),(x,y,scale,scale))


def main():

    field = [[' '] * 800 for i in range(800)]
    field = gameplay.initial_game(field)
    x = 400
    y = 750
    car = Car(x,y)
    field[car.pos.x][y] = car.sprite
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("brick_track")
    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if field[car.pos.x-25][y] != 'b':
                        field[car.pos.x][y] = ' '
                        car.pos.x -= 25
                        field[car.pos.x][y] = car.sprite
                if event.key == pygame.K_RIGHT:
                    if field[car.pos.x+25][y] != 'b':
                        field[car.pos.x][y] = ' '
                        car.pos.x += 25
                        field[car.pos.x][y] = car.sprite


        screen.fill((0, 0, 0))
        render_pygame(field, screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
