import pygame
from pygame.locals import *
import snake
import game
from button import Button
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
    paused = True
    font = pygame.font.SysFont(name="Calibri", size=20 , bold=True, italic=False)

    fruit = snake.Fruit()

    players = [snake.Player(1, 30, 20, 0, fruit), snake.Player(2, 30, 21, 2, fruit)]

    game_mode = 0
    player1_result = 0
    player2_result = 0

    for i in players:
        i.other_players = players

    fields = []

    for i in range(52):
        for j in range(40):
            fields.append(level.Field(i, j, players, fruit))

    button_restart = Button("Start", 830, 540, 100, 30, (200, 200, 200), (255, 255, 200), (0, 0, 0), font, screen, 1.3, 0)
    button_pause = Button("Pauza", 830, 580, 100, 30, (200, 200, 200), (255, 255, 200), (0, 0, 0), font,screen, 1.9, 0)

    button_player1 = Button("Strzałki", 830, 120, 100, 30, (200, 200, 200), (255, 255, 200), (0, 0, 0), font, screen,3, 2)
    button_player2 = Button("CPU", 830, 180, 100, 30, (200, 200, 200), (255, 255, 200), (0, 0, 0), font, screen, 1.1, 2)

    button_mode = Button("Ostatni żywy", 810, 320, 150, 30, (200, 200, 200), (255, 255, 200), (0, 0, 0), font, screen, 5, 1)

    #screen initialization
    backgroung = pygame.Surface(screen.get_size())
    backgroung = backgroung.convert()
    backgroung.fill((250, 250, 250))

    screen.blit(backgroung, (0, 0))
    pygame.display.flip()

    pygame.draw.lines(backgroung, (0, 0, 0), True, [(10, 10),(790, 10), (790, 590), (10, 590)], 1)


    while running:    #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        #update variables
        if not paused:
            players[0].update()
            players[1].update()

        if button_restart.on_click:
            button_restart.text = "Restart"
            button_restart.gap = 2.8

            game_mode = button_mode.state

            if button_player1.state == 0:
                players[0].active = True
                players[0].cpu = False
            elif button_player1.state == 1:
                players[0].active = True
                players[0].cpu = True
            elif button_player1.state == 2:
                players[0].active = False
                players[0].cpu = False

            if button_player2.state == 0:
                players[1].active = True
                players[1].cpu = True
            elif button_player2.state == 1:
                players[1].active = True
                players[1].cpu = False
            elif button_player2.state == 2:
                players[1].active = False
                players[1].cpu = False

            for i in players:
                if i.active:
                    i.lose()
                    i.restart()

            paused = False
        if button_pause.on_click:
            if paused:
                paused = False
            else:
                paused = True

        #draw level
        game.draw_level(screen,backgroung)
        game.text(text="Długość gracza 1: " + str(players[0].lenght), x=800, y=10, color=(0, 0, 0), font=font, screen=screen)
        game.text(text="Długość gracza 2: " + str(players[1].lenght), x=800, y=30, color=(0, 0, 0), font=font, screen=screen)
        game.text(text="Gracz 1", x=850, y=100, color=(255, 0, 0), font=font, screen=screen)
        game.text(text="Gracz 2", x=850, y=160, color=(0, 0, 255), font=font, screen=screen)
        game.text(text="Tryb gry", x=850, y=300, color=(0, 0, 0), font=font, screen=screen)


        if players[0].lost:
            game.text(text="Śmierć gracza 1!", x=50, y=630, color=(255, 0, 0), font=font, screen=screen)
            if game_mode == 0:
                game.text(text="Wygrywa gracz 2!", x=400, y=630, color=(0, 255, 0), font=font, screen=screen)
                paused = True
            if game_mode == 1:
                player1_result = players[0].lenght
        if players[1].lost:
            game.text(text="Śmierć gracza 2!", x=50, y=650, color=(255, 0, 0), font=font, screen=screen)
            if game_mode == 0:
                game.text(text="Wygrywa gracz 1!", x=400, y=630, color=(0, 255, 0), font=font, screen=screen)
                paused = True
            if game_mode == 1:
                player2_result = players[1].lenght

        if game_mode == 1 and players[0].lost and players[1].lost:
            paused = True
            if player1_result > player2_result:
                game.text(text="Wygrywa gracz 1! Długość: " + str(player1_result), x=400, y=630, color=(0, 255, 0), font=font, screen=screen)
            elif player2_result > player1_result:
                game.text(text="Wygrywa gracz 2! Długość: " + str(player2_result), x=400, y=630, color=(0, 255, 0), font=font, screen=screen)
            else:
                game.text(text="Remis! Długość obydwu węży: " + str(player1_result), x=400, y=630, color=(255, 200, 0), font=font, screen=screen)

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

        button_restart.draw()
        button_pause.draw()
        button_mode.draw()

        if button_player1.state == 0:
            button_player1.text = "Strzałki"
            button_player1.gap = 3
        elif button_player1.state == 1:
            button_player1.text = "CPU"
            button_player1.gap = 1.1
        else:
            button_player1.text = "Brak"
            button_player1.gap = 1.2
        button_player1.draw()

        if button_player2.state == 0:
            button_player2.text = "CPU"
            button_player2.gap = 1.1
        elif button_player2.state == 1:
            button_player2.text = "WASD"
            button_player2.gap = 2.2
        else:
            button_player2.text = "Brak"
            button_player2.gap = 1.2
        button_player2.draw()

        if button_mode.state == 0:
            button_mode.text = "Ostatni żywy"
            button_mode.gap = 5
        elif button_mode.state == 1:
            button_mode.text = "Najdłuższy wąż"
            button_mode.gap = 10

        pygame.display.flip()
        pygame.event.pump()

    pygame.quit()

if __name__ == '__main__': main()