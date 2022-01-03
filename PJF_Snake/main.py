import pygame
from pygame.locals import *
import time
import snake

def main():
    pygame.init()
    size_x = 800
    size_y = 600
    screen = pygame.display.set_mode((size_x, size_y))
    pygame.display.set_caption('Snake')

    backgroung = pygame.Surface(screen.get_size())
    backgroung = backgroung.convert()
    backgroung.fill((250, 250, 250))

    screen.blit(backgroung, (0, 0))
    pygame.display.flip()

    pygame.draw.circle(backgroung, (255, 0, 0), (50, 50), 20)
    pygame.draw.lines(backgroung, (0, 0, 0), True, [(10, 10),(790, 10), (790, 590), (10, 590)], 1)

    player = snake.Player()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(backgroung, (0, 0))
        pygame.display.flip()
        backgroung.fill((250, 250, 250))
        pygame.draw.lines(backgroung, (0, 0, 0), True, [(10, 10), (790, 10), (790, 590), (10, 590)], 1)
        pygame.draw.rect(backgroung, (50, 255, 255), (player.x, player.y, 15, 15))
        player.update()

        pygame.event.pump()
        time.sleep(0.01)

if __name__ == '__main__': main()