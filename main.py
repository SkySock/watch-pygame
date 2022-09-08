import sys

import pygame
import datetime
import math
from watch import Watch

WINDOW_SIZE = (551, 551)
CENTER = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
RADIUS = 255


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    watch = Watch(RADIUS)
    clock = pygame.time.Clock()

    running = True
    while(running):
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                sys.exit()
        watch.update()
        pygame.Surface.blit(screen, watch.image, (CENTER[0] - RADIUS, CENTER[1] - RADIUS))
        pygame.display.update()
        pygame.display.set_caption(datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S"))
        
        clock.tick(60)


if __name__ == '__main__':
    main()
