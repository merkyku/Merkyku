import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("brick_track")
    clock = pygame.time.Clock()
    while True:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)



if __name__ == '__main__':
    main()
