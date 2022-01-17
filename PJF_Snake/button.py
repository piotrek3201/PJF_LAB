import pygame
from game import text

class Button:
    def __init__(self, text, x, y, width, height, button_color, button_color_hover, font_color, font, screen, gap, max_state):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_color = button_color
        self.button_color_hover = button_color_hover
        self.font_color = font_color
        self.font = font
        self.screen = screen
        self.screen_size = screen.get_size()
        self.on_click = False
        self.gap = gap
        self.hover = False
        self.state = 0
        self.max_state = max_state
        self.time = pygame.time.Clock().tick(1000)

    def draw(self):
        if self.state > self.max_state:
            self.state = 0

        self.time += pygame.time.Clock().tick(1000)
        mouse = pygame.mouse.get_pos()

        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height:
            pygame.draw.rect(self.screen, self.button_color_hover, [self.x, self.y, self.width, self.height])
            self.hover = True
        else:
            pygame.draw.rect(self.screen, self.button_color, [self.x, self.y, self.width, self.height])
            self.hover = False

        text(self.text, self.x + (self.font.size(self.text)[0]/self.gap), self.y + (self.font.get_height()/2.5), self.font_color, self.font, self.screen)


        if pygame.mouse.get_pressed()[0] and self.hover:
            if self.time / 1000.0 > 0.01:
                self.time = 0
                self.on_click = True
                self.state += 1
        else:
            self.on_click = False