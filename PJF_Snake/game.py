import pygame
import GUI

class Game:
    def __init__(self, players, fields, fruit, background, screen, button_restart, button_pause, button_player1, button_player2, button_mode, font):
        self.players = players
        self.fields = fields
        self.fruit = fruit
        self.running = True
        self.paused = True
        self.game_mode = 0
        self.player1_result = 0
        self.player2_result = 0
        self.background = background
        self.screen = screen
        self.button_restart = button_restart
        self.button_pause = button_pause
        self.button_player1 = button_player1
        self.button_player2 = button_player2
        self.button_mode = button_mode
        self.font = font

    def update(self):
        if not self.paused:
            self.players[0].update()
            self.players[1].update()

        if self.button_restart.on_click:
            self.button_restart.text = "Restart"
            self.button_restart.gap = 2.8

            self.game_mode = self.button_mode.state

            if self.button_player1.state == 0:
                self.players[0].active = True
                self.players[0].cpu = False
            elif self.button_player1.state == 1:
                self.players[0].active = True
                self.players[0].cpu = True
            elif self.button_player1.state == 2:
                self.players[0].active = False
                self.players[0].cpu = False

            if self.button_player2.state == 0:
                self.players[1].active = True
                self.players[1].cpu = True
            elif self.button_player2.state == 1:
                self.players[1].active = True
                self.players[1].cpu = False
            elif self.button_player2.state == 2:
                self.players[1].active = False
                self.players[1].cpu = False

            for i in self.players:
                if i.active:
                    i.lose()
                    i.restart()

            self.paused = False
        if self.button_pause.on_click:
            if self.paused:
                self.paused = False
            else:
                self.paused = True

        #draw level
        GUI.draw_level(self.screen,self.background)
        GUI.text(text="Długość gracza 1: " + str(self.players[0].lenght), x=800, y=10, color=(0, 0, 0), font=self.font, screen=self.screen)
        GUI.text(text="Długość gracza 2: " + str(self.players[1].lenght), x=800, y=30, color=(0, 0, 0), font=self.font, screen=self.screen)
        GUI.text(text="Gracz 1", x=850, y=100, color=(255, 0, 0), font=self.font, screen=self.screen)
        GUI.text(text="Gracz 2", x=850, y=160, color=(0, 0, 255), font=self.font, screen=self.screen)
        GUI.text(text="Tryb gry", x=850, y=300, color=(0, 0, 0), font=self.font, screen=self.screen)


        if self.players[0].lost:
            GUI.text(text="Śmierć gracza 1!", x=50, y=630, color=(255, 0, 0), font=self.font, screen=self.screen)
            if self.game_mode == 0:
                GUI.text(text="Wygrywa gracz 2!", x=400, y=630, color=(0, 255, 0), font=self.font, screen=self.screen)
                self.paused = True
            if self.game_mode == 1 or self.game_mode == 2:
                self.player1_result = self.players[0].lenght
        if self.players[1].lost:
            GUI.text(text="Śmierć gracza 2!", x=50, y=650, color=(255, 0, 0), font=self.font, screen=self.screen)
            if self.game_mode == 0:
                GUI.text(text="Wygrywa gracz 1!", x=400, y=630, color=(0, 255, 0), font=self.font, screen=self.screen)
                self.paused = True
            if self.game_mode == 1 or self.game_mode == 2:
                self.player2_result = self.players[1].lenght

        if self.game_mode == 1 and self.players[0].lost and self.players[1].lost:
            self.paused = True
            if self.player1_result > self.player2_result:
                GUI.text(text="Wygrywa gracz 1! Długość: " + str(self.player1_result), x=400, y=630, color=(0, 255, 0), font=self.font, screen=self.screen)
            elif self.player2_result > self.player1_result:
                GUI.text(text="Wygrywa gracz 2! Długość: " + str(self.player2_result), x=400, y=630, color=(0, 255, 0), font=self.font, screen=self.screen)
            else:
                GUI.text(text="Remis! Długość obydwu węży: " + str(self.player1_result), x=400, y=630, color=(255, 200, 0), font=self.font, screen=self.screen)

        if self.game_mode == 2 and self.players[0].lost and self.players[1].lost:
            self.paused = True
            if self.player1_result > self.player2_result:
                GUI.text(text="Gracz 1 był bliżej! Długość: " + str(self.player1_result), x=400, y=630, color=(0, 255, 0), font=self.font, screen=self.screen)
            elif self.player2_result > self.player1_result:
                GUI.text(text="Gracz 2 był bliżej! Długość: " + str(self.player2_result), x=400, y=630, color=(0, 255, 0), font=self.font, screen=self.screen)
            else:
                GUI.text(text="Remis! Długość obydwu węży: " + str(self.player1_result), x=400, y=630, color=(255, 200, 0), font=self.font, screen=self.screen)

        if self.game_mode == 2:
            if self.players[0].lenght >= 50:
                GUI.text(text="Wygrywa gracz 1! Długość: " + str(self.player1_result), x=400, y=630, color=(0, 255, 0), font=self.font, screen=self.screen)
                self.paused = True
            if self.players[1].lenght >= 50:
                GUI.text(text="Wygrywa gracz 2! Długość: " + str(self.player2_result), x=400, y=630, color=(0, 255, 0), font=self.font, screen=self.screen)
                self.paused = True

        #draw player

        for i in range(len(self.fields)):
            self.fields[i].update()
            if self.fields[i].fruit_is_here:
                pygame.draw.rect(self.background, (255, 255, 0), (self.fields[i].x * 15 + 10, self.fields[i].y * 15 + 10, 15, 15))
            for j in range(2):
                if self.fields[i].tail_is_here[j]:
                    if j == 0:
                        pygame.draw.rect(self.background, (200, 0, 0), (self.fields[i].x * 15 + 10, self.fields[i].y * 15 + 10, 15, 15))
                    if j == 1:
                        pygame.draw.rect(self.background, (0, 0, 200), (self.fields[i].x * 15 + 10, self.fields[i].y * 15 + 10, 15, 15))
                if self.fields[i].player_is_here[j]:
                    if j == 0:
                        pygame.draw.rect(self.background, (255, 0, 0), (self.fields[i].x * 15 + 10, self.fields[i].y * 15 + 10, 15, 15))
                    if j == 1:
                        pygame.draw.rect(self.background, (0, 0, 255), (self.fields[i].x * 15 + 10, self.fields[i].y * 15 + 10, 15, 15))

        self.button_restart.draw()
        self.button_pause.draw()
        self.button_mode.draw()

        if self.button_player1.state == 0:
            self.button_player1.text = "Strzałki"
            self.button_player1.gap = 3
        elif self.button_player1.state == 1:
            self.button_player1.text = "CPU"
            self.button_player1.gap = 1.1
        else:
            self.button_player1.text = "Brak"
            self.button_player1.gap = 1.2
        self.button_player1.draw()

        if self.button_player2.state == 0:
            self.button_player2.text = "CPU"
            self.button_player2.gap = 1.1
        elif self.button_player2.state == 1:
            self.button_player2.text = "WASD"
            self.button_player2.gap = 2.2
        else:
            self.button_player2.text = "Brak"
            self.button_player2.gap = 1.2
        self.button_player2.draw()

        if self.button_mode.state == 0:
            self.button_mode.text = "Ostatni żywy"
            self.button_mode.gap = 5
        elif self.button_mode.state == 1:
            self.button_mode.text = "Najdłuższy wąż"
            self.button_mode.gap = 10
        elif self.button_mode.state == 2:
            self.button_mode.text = "Pierwszy do 50"
            self.button_mode.gap = 10