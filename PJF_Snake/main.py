#Piotr Kałuziński WCY19IJ1S1
import pygame
from pygame.locals import *
import snake
from game import Game
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
    font = pygame.font.SysFont(name="Calibri", size=20 , bold=True, italic=False)

    fruit = snake.Fruit()

    players = [snake.Player(1, 30, 20, 0, fruit), snake.Player(2, 30, 21, 2, fruit)]

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

    button_mode = Button("Ostatni żywy", 810, 320, 150, 30, (200, 200, 200), (255, 255, 200), (0, 0, 0), font, screen, 5, 2)
    button_increase = Button("+", 880, 355, 30, 30, (200, 200, 200), (255, 255, 200), (0, 0, 0), font, screen, 0.85, 0)
    button_decrease = Button("-", 840, 355, 30, 30, (200, 200, 200), (255, 255, 200), (0, 0, 0), font, screen, 0.45, 0)

    #screen initialization
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    game = Game(players, fields, fruit, background, screen, button_restart, button_pause, button_player1, button_player2, button_mode, button_increase, button_decrease,font)

    while running:    #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        game.update()

        pygame.display.flip()
        pygame.event.pump()

    pygame.quit()

if __name__ == '__main__': main()