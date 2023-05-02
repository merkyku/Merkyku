import pygame
import gameplay
from car_info import *


def render_pygame(field, screen):
    scale = 40
    for x in range(0,len(field)):
        for y in range(0,len(field)):
            if field[x][y] == 'b':
                pygame.draw.rect(screen, (255, 0, 0), (x*scale, y*scale, scale, scale))
            if field[x][y] == 'car':
                pygame.draw.rect(screen, (0, 255, 0), (x*scale, y*scale, scale, scale))


def main():

    field = [[' '] * 20 for i in range(20)]
    field = gameplay.initial_game(field)
    x = 10
    y = 18
    car = Car(x, y)
    field[x][y] = car.sprite

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("brick_track")
    clock = pygame.time.Clock()
    is_running = True
    main_font = pygame.font.Font(None, 24)
    text1 = main_font.render('Добро пожаловать!', True, (255, 255, 255))
    while is_running:
        field = gameplay.brick_fallen(field)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                text1 = main_font.render(f'ваше здоровье {car.health}%', True, (255, 255, 255))
                if event.key == pygame.K_LEFT:
                    if field[car.pos.x-1][y] != 'b':
                        field[car.pos.x][y] = ' '
                        car.pos.x -= 1
                        field[car.pos.x][y] = car.sprite
                    else:
                        car.take_damage(10)
                        if not car.is_alive:
                            is_running = False
                if event.key == pygame.K_RIGHT:
                    if field[car.pos.x+1][y] != 'b':
                        field[car.pos.x][y] = ' '
                        car.pos.x += 1
                        field[car.pos.x][y] = car.sprite
                    else:
                        car.take_damage(10)
                        if not car.is_alive:
                            is_running = False
        screen.fill((0, 0, 0))
        screen.blit(text1, (50, 780))
        render_pygame(field, screen)
        pygame.display.flip()

        clock.tick(60)
        #pygame.time.delay(100)


if __name__ == '__main__':
    main()
