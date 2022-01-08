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

    players = []
    for i in range(4):
        players.append(snake.Player())
    players[0].active = True

    fields = []

    for i in range(52):
        for j in range(40):
            fields.append(level.Field(i, j, players))

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


        #clear background
        screen.blit(backgroung, (0, 0))
        backgroung.fill((250, 250, 250))

        #draw grid
        for i in range(10, 790, 15):
            pygame.draw.line(surface=backgroung, color=(220, 220, 220), start_pos=(i,10), end_pos=(i,610), width=1)
        for i in range(10, 610, 15):
            pygame.draw.line(surface=backgroung, color=(220, 220, 220), start_pos=(10,i), end_pos=(790,i), width=1)

        # draw level boundaries
        pygame.draw.lines(backgroung, (0, 0, 0), True, [(10, 10), (790, 10), (790, 610), (10, 610)], 1)

        game.text(text="Długość: " + str(players[0].lenght), x=800, y=10, color=(0, 0, 0), font=font, screen=screen)

        if players[0].lost:
            game.text(text="Porażka!", x=50, y=630, color=(255, 0, 0), font=font, screen=screen)

        #draw player
        #pygame.draw.rect(backgroung, (50, 255, 255), (players[0].x, players[0].y, 15, 15))
        players[0].update()

        for i in range(len(fields)):
            fields[i].update()
            if fields[i].used:
                pygame.draw.rect(backgroung, (255, 0, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))



        pygame.display.flip()
        pygame.event.pump()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__': main()