#Piotr Kałuziński WCY19IJ1S1
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

