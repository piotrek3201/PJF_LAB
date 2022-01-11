import pygame
from pygame.locals import *
import snake
import game
import level

def main():
    #window initialization
    pygame.init()
    size_x = 900
    size_y = 720
    screen = pygame.display.set_mode((size_x, size_y))
    pygame.display.set_caption('Snake')

    #variables initialization
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(name="Calibri", size=20 , bold=True, italic=False)

    fruit = snake.Fruit()

    players = []
    for i in range(4):
        players.append(snake.Player())
    players[0].active = True

    fields = []

    for i in range(52):
        for j in range(40):
            fields.append(level.Field(i, j, players, fruit))



    #screen initialization
    backgroung = pygame.Surface(screen.get_size())
    backgroung = backgroung.convert()
    backgroung.fill((250, 250, 250))

    screen.blit(backgroung, (0, 0))
    pygame.display.flip()

    #pygame.draw.circle(backgroung, (255, 0, 0), (50, 50), 20)
    pygame.draw.lines(backgroung, (0, 0, 0), True, [(10, 10),(790, 10), (790, 590), (10, 590)], 1)


    while running:    #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        #update variables

        #draw level
        game.draw_level(screen,backgroung)
        game.text(text="Długość: " + str(players[0].lenght), x=800, y=10, color=(0, 0, 0), font=font, screen=screen)

        if players[0].lost:
            game.text(text="Porażka!", x=50, y=630, color=(255, 0, 0), font=font, screen=screen)
            players[0].lenght = 1

        #draw player
        #pygame.draw.rect(backgroung, (50, 255, 255), (players[0].x, players[0].y, 15, 15))
        players[0].update()

        for i in range(len(fields)):
            fields[i].update()
            if fields[i].fruit_is_here:
                pygame.draw.rect(backgroung, (255, 255, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
            if fields[i].tail_is_here:
                pygame.draw.rect(backgroung, (200, 0, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
            if fields[i].player_is_here:
                pygame.draw.rect(backgroung, (255, 0, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))




        pygame.display.flip()
        pygame.event.pump()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__': main()