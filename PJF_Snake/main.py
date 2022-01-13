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

    players = [snake.Player(1, 30, 20, 0), snake.Player(2, 30, 21, 2)]
    players[0].active = True
    players[1].active = True

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
        players[0].update()
        players[1].update()

        #draw level
        game.draw_level(screen,backgroung)
        game.text(text="Długość: " + str(players[0].lenght), x=800, y=10, color=(0, 0, 0), font=font, screen=screen)
        game.text(text="Długość: " + str(players[1].lenght), x=800, y=30, color=(0, 0, 0), font=font, screen=screen)

        if players[0].lost:
            game.text(text="Porażka gracza 1!", x=50, y=630, color=(255, 0, 0), font=font, screen=screen)
        if players[1].lost:
            game.text(text="Porażka gracza 2!", x=50, y=650, color=(255, 0, 0), font=font, screen=screen)

        #draw player


        for i in range(len(fields)):
            fields[i].update()
            if fields[i].fruit_is_here:
                pygame.draw.rect(backgroung, (255, 255, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
            for j in range(2):
                if fields[i].tail_is_here[j]:
                    if j == 0:
                        pygame.draw.rect(backgroung, (200, 0, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
                    if j == 1:
                        pygame.draw.rect(backgroung, (0, 0, 200), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
                if fields[i].player_is_here[j]:
                    if j == 0:
                        pygame.draw.rect(backgroung, (255, 0, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
                    if j == 1:
                        pygame.draw.rect(backgroung, (0, 0, 255), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))



        pygame.display.flip()
        pygame.event.pump()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__': main()