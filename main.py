import pygame
import gameplay
from car_info import *


def render_pygame(field, screen):
    scale = 40
    for x in range(0,len(field)):
        for y in range(0,len(field)):
            if field[x][y] == 'b':
                pygame.draw.rect(screen, (34, 177, 77), (x*scale+19, y*scale+1, 4, 4))
                pygame.draw.rect(screen, (34, 177, 77), (x * scale+15, y * scale+5, 4*3, 4))
                pygame.draw.rect(screen, (34, 177, 77), (x * scale + 11, y * scale + 9, 4*5, 4))
                pygame.draw.rect(screen, (34, 177, 77), (x * scale + 7, y * scale + 13, 4*7, 4))
                pygame.draw.rect(screen, (34, 177, 77), (x * scale + 3, y * scale + 17, 4*9, 4))
                pygame.draw.rect(screen, (34, 177, 77), (x * scale, y * scale + 21, 4*10, 4))
                pygame.draw.rect(screen, (120, 63, 23), (x * scale + 17, y * scale + 25, 7, 15))

            if field[x][y] == 'car':
                pygame.draw.rect(screen, (47, 54, 153), (x*scale+10, y*scale+6,4,8))
                pygame.draw.rect(screen, (47, 54, 153), (x * scale + 27, y * scale + 6, 4, 8))
                pygame.draw.rect(screen, (47, 54, 153), (x * scale + 16, y * scale + 9, 8, 2))
                pygame.draw.rect(screen, (47, 54, 153), (x * scale + 15, y * scale + 11, 10, 3))
                pygame.draw.rect(screen, (47, 54, 153), (x * scale + 15, y * scale + 14, 10, 20))
                pygame.draw.rect(screen, (47, 54, 153), (x * scale + 10, y * scale + 30, 4, 8))
                pygame.draw.rect(screen, (47, 54, 153), (x * scale + 27, y * scale +30, 4, 8))
                pygame.draw.rect(screen, (255, 255, 255), (x * scale + 18, y * scale + 15, 4, 13))



def main():
    field = [[' '] * 20 for i in range(20)]
    field = gameplay.initial_game(field)
    x = 10
    y = 18
    car = Car(x, y)
    field[x][y] = car.sprite

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("brick_track")
    clock = pygame.time.Clock()
    is_running = True
    main_font = pygame.font.Font(None, 24)
    while is_running:
        field = gameplay.brick_fallen(field, car)
        text1 = main_font.render(f'ваше здоровье {car.health}%', True, (255, 255, 255))
        if not car.is_alive:
            is_running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    if field[car.pos.x-1][y] != 'b':
                        field[car.pos.x][y] = ' '
                        car.pos.x -= 1
                        field[car.pos.x][y] = car.sprite
                    else:
                        car.take_damage(10)
                if event.key == pygame.K_RIGHT:
                    if field[car.pos.x+1][y] != 'b':
                        field[car.pos.x][y] = ' '
                        car.pos.x += 1
                        field[car.pos.x][y] = car.sprite
                    else:
                        car.take_damage(10)

        screen.fill((0, 0, 0))
        screen.blit(text1, (820, 10))
        render_pygame(field, screen)
        pygame.display.flip()

        clock.tick(60)
        #pygame.time.delay(100)


if __name__ == '__main__':
    main()
