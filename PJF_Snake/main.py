import pygame
from pygame.locals import *
import snake
import game
import level

def main():
    #window initialization
    pygame.init()
    size_x = 980
    size_y = 720
    screen = pygame.display.set_mode((size_x, size_y))
    pygame.display.set_caption('Snake 4 2')

    #variables initialization
    running = True
    paused = False
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(name="Calibri", size=20 , bold=True, italic=False)

    x = font.size("Start")
    print(x)

    fruit = snake.Fruit()

    players = [snake.Player(1, 30, 20, 0, fruit), snake.Player(2, 30, 21, 2, fruit), snake.Player(3, 31, 20, 1, fruit), snake.Player(4, 29, 21, 3, fruit)]
    #players = [snake.Player(1, 30, 20, 0, fruit), snake.Player(2, 30, 21, 2, fruit)]
    players[0].active = True
    players[1].active = True
    players[1].cpu = True
    players[2].active = True
    players[2].cpu = True
    players[3].active = True
    players[3].cpu = True

    #players[0].cpu = True

    for i in players:
        i.other_players = players

    fields = []

    for i in range(52):
        for j in range(40):
            fields.append(level.Field(i, j, players, fruit))

    button_start = game.Button("Start", 830, 500, 100, 30, (200, 200, 200), (255, 255, 200), (0, 0, 0), font, screen, 1.3)
    button_restart = game.Button("Restart", 830, 550, 100, 30, (200, 200, 200), (255, 255, 200), (0, 0, 0), font, screen, 2.8)
    button_pause = game.Button("Pauza", 830, 600, 100, 30, (200, 200, 200), (255, 255, 200), (0, 0, 0), font,screen, 1.9)

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
        if not paused:
            players[0].update()
            players[1].update()
            players[2].update()
            players[3].update()

        if button_restart.on_click:
            for i in players:
                i.lose()
                i.restart()
        if button_pause.on_click:
            if paused:
                paused = False
            else:
                paused = True

        #draw level
        game.draw_level(screen,backgroung)
        game.text(text="Długość gracza 1: " + str(players[0].lenght), x=800, y=10, color=(0, 0, 0), font=font, screen=screen)
        game.text(text="Długość gracza 2: " + str(players[1].lenght), x=800, y=30, color=(0, 0, 0), font=font, screen=screen)
        game.text(text="Długość gracza 3: " + str(players[2].lenght), x=800, y=50, color=(0, 0, 0), font=font, screen=screen)
        game.text(text="Długość gracza 4: " + str(players[3].lenght), x=800, y=70, color=(0, 0, 0), font=font, screen=screen)

        if players[0].lost:
            game.text(text="Porażka gracza 1!", x=50, y=630, color=(255, 0, 0), font=font, screen=screen)
        if players[1].lost:
            game.text(text="Porażka gracza 2!", x=50, y=650, color=(255, 0, 0), font=font, screen=screen)
        if players[2].lost:
            game.text(text="Porażka gracza 3!", x=50, y=670, color=(255, 0, 0), font=font, screen=screen)
        if players[3].lost:
            game.text(text="Porażka gracza 4!", x=50, y=690, color=(255, 0, 0), font=font, screen=screen)

        #draw player


        for i in range(len(fields)):
            fields[i].update()
            if fields[i].fruit_is_here:
                pygame.draw.rect(backgroung, (255, 255, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
            for j in range(4):
                if fields[i].tail_is_here[j]:
                    if j == 0:
                        pygame.draw.rect(backgroung, (200, 0, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
                    if j == 1:
                        pygame.draw.rect(backgroung, (0, 0, 200), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
                    if j == 2:
                        pygame.draw.rect(backgroung, (0, 200, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
                    if j == 3:
                        pygame.draw.rect(backgroung, (0, 200, 200), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
                if fields[i].player_is_here[j]:
                    if j == 0:
                        pygame.draw.rect(backgroung, (255, 0, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
                    if j == 1:
                        pygame.draw.rect(backgroung, (0, 0, 255), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
                    if j == 2:
                        pygame.draw.rect(backgroung, (0, 255, 0), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))
                    if j == 3:
                        pygame.draw.rect(backgroung, (0, 255, 255), (fields[i].x * 15 + 10, fields[i].y * 15 + 10, 15, 15))


        button_start.draw()
        button_restart.draw()
        button_pause.draw()

        pygame.display.flip()
        pygame.event.pump()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__': main()