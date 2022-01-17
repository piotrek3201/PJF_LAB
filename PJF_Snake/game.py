import pygame

def text(text, x, y, color, font, screen):
    text_surface = font.render(text, False, color)
    screen.blit(text_surface, (x, y))

def draw_grid(surf):
    for i in range(10, 790, 15):
        pygame.draw.line(surface=surf, color=(220, 220, 220), start_pos=(i, 10), end_pos=(i, 610), width=1)
    for i in range(10, 610, 15):
        pygame.draw.line(surface=surf, color=(220, 220, 220), start_pos=(10, i), end_pos=(790, i), width=1)

def draw_level(scr, bckgrnd):
    # clear background
    scr.blit(bckgrnd, (0, 0))
    bckgrnd.fill((250, 250, 250))
    # draw grid
    draw_grid(bckgrnd)
    pygame.draw.lines(bckgrnd, (0, 0, 0), True, [(10, 10), (790, 10), (790, 610), (10, 610)], 1)

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

